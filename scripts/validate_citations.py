import os
import re

# Directory mappings for QBD monograph chapters
doc_dirs = {
    "01-rules/01-ontology": ("rules", "ontology"),
    "01-rules/02-axioms": ("rules", "axioms"),
    "01-rules/03-architecture": ("rules", "architecture"),
    "01-rules/04-dynamics": ("rules", "dynamics"),
    "01-rules/05-equilibrium": ("rules", "equilibrium"),
    "02-players/06-fermions": ("players", "fermions"),
    "02-players/07-topology": ("players", "topology"),
    "02-players/08-braids": ("players", "braids"),
    "02-players/09-unification": ("players", "unification"),
    "02-players/10-computation": ("players", "computation"),
}

# Auto-detect project paths relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
docs_root = os.path.join(PROJECT_ROOT, "docs")

# Regular expression for extracting structured citations
citation_pattern = re.compile(r'(\[([^\]]+)\])?\s*\(\s*\[?§([0-9\.\-]+)\]?\s*\)(\([^\)]+\))?')

violations = []

def analyze_line(filepath, relpath, line_no, line, part, chapter):
    idx = 0
    while True:
        pos = line.find('§', idx)
        if pos == -1:
            break
        
        # Capture context around the reference
        start = max(0, pos - 150)
        end = min(len(line), pos + 150)
        snippet = line[start:end]
        
        # Extract the citation ID
        m_id = re.search(r'§([0-9a-zA-Z\.\-]+)', line[pos:])
        ref_id = m_id.group(1) if m_id else "unknown"
        
        # Check standard format [(§ID)](link)
        has_bracket_parenthesis = False
        target_str = f"[(§{ref_id})]"
        target_pos = line.find(target_str, max(0, pos - 5))
        
        link_url = None
        if target_pos != -1:
            has_bracket_parenthesis = True
            link_start = target_pos + len(target_str)
            if link_start < len(line) and line[link_start] == '(':
                link_end = line.find(')', link_start)
                if link_end != -1:
                    link_url = line[link_start+1:link_end]
            
        # Check rule 1: Bolding of the concept/lemma/axiom name before target_pos
        ref_pos = target_pos if target_pos != -1 else pos
        prefix = line[:ref_pos]
        
        is_bolded = False
        prefix_for_noun_check = prefix
        m_bold = re.search(r'\*\*([^*]+)\*\*\s*$', prefix)
        if m_bold:
            is_bolded = True
            concept_name = m_bold.group(1)
            prefix_for_noun_check = prefix[:m_bold.start()]
        else:
            concept_name = None
            m_bold_lax = re.search(r'\*\*([^*]+)\*\*\s*[\w\s]*$', prefix)
            if m_bold_lax:
                concept_name = m_bold_lax.group(1)
                is_bolded = True
                prefix_for_noun_check = prefix[:m_bold_lax.start()]
        
        # Check rule 2: Noun usage (citations must be syntactically silent)
        is_noun = False
        noun_reason = None
        words = re.findall(r'\b\w+\b', prefix_for_noun_check)
        if words:
            last_words = [w.lower() for w in words[-4:]]
            forbidden_nouns = {'lemma', 'theorem', 'section', 'axiom', 'definition', 'proof'}
            for w in last_words:
                if w in forbidden_nouns:
                    is_noun = True
                    noun_reason = f"Contains forbidden noun '{w}' before the citation."
                    break
            
            # Check for direct prepositions/verbs
            if not is_noun:
                prefix_lower = prefix.lower()
                if prefix_lower.strip().endswith('using') or prefix_lower.strip().endswith('by') or prefix_lower.strip().endswith('refer to'):
                    is_noun = True
                    noun_reason = "Preceded directly by a preposition/verb like 'using', 'by', 'refer to'."
        
        # Check rule 3: Grouped references
        is_grouped = False
        if '-' in ref_id or ',' in ref_id:
            is_grouped = True
            
        # Check rule 4: Canonical URL formatting
        is_url_correct = True
        url_reason = None
        if link_url:
            m_url = re.match(r'^/monograph/([^/]+)/([^/]+)/([^/]+)/#(.*)$', link_url)
            if m_url:
                u_part, u_chap, u_sec, u_id = m_url.groups()
                allowed_parts = {'rules', 'players', 'stage', 'output', 'conclusion', 'appendix'}
                if u_part not in allowed_parts:
                    is_url_correct = False
                    url_reason = f"Part '{u_part}' not in allowed parts: {allowed_parts}"
                if not re.match(r'^\d+\.\d+$', u_sec):
                    is_url_correct = False
                    url_reason = f"Section '{u_sec}' is not in two-digit format like 1.2"
                if u_id != ref_id:
                    is_url_correct = False
                    url_reason = f"Anchor ID '{u_id}' does not match ref ID '{ref_id}'"
            else:
                is_url_correct = False
                url_reason = f"URL '{link_url}' does not match format '/monograph/part/chapter/section/#ID'"
        else:
            is_url_correct = False
            url_reason = "Missing or malformed link parenthetical."

        # If any validation constraint fails, record it as a violation
        if not (has_bracket_parenthesis and is_bolded and not is_noun and not is_grouped and is_url_correct):
            violations.append({
                "file": relpath,
                "line_no": line_no,
                "ref_id": ref_id,
                "concept": concept_name,
                "snippet": snippet.strip(),
                "has_bracket_parenthesis": has_bracket_parenthesis,
                "is_bolded": is_bolded,
                "is_noun": is_noun,
                "noun_reason": noun_reason,
                "is_grouped": is_grouped,
                "is_url_correct": is_url_correct,
                "url_reason": url_reason,
                "link_url": link_url
            })
            
        idx = pos + 1

robust_bare_pat = re.compile(
    r'\b(Lemma|Theorem|Axiom|Proof|Section|Definition|Principle|Postulate)\s+(\d+\.\d+(?:\.\d+)?(?:\.\d+)?)\b',
    re.IGNORECASE
)

# Iterate through doc files
for root, dirs, files in os.walk(docs_root):
    for file in files:
        if not file.endswith(".md"):
            continue
        filepath = os.path.join(root, file)
        relpath = os.path.relpath(filepath, docs_root).replace("\\", "/")
        
        part = None
        chapter = None
        for key, val in doc_dirs.items():
            if key in relpath:
                part, chapter = val
                break
        
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        in_code_block = False
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                continue
                
            if in_code_block:
                continue
                
            # Skip TOC, references, appendices, tables, note headers, and other non-citations
            if "00-table-of-contents" in relpath or "appendices" in relpath or "a-references" in relpath:
                continue
            if "|" in line or stripped.startswith(":::") or "Overview**]" in line or stripped.startswith("#"):
                continue
                
            # First, check standard citations if there is a '§'
            if "§" in line:
                analyze_line(filepath, relpath, i + 1, line, part, chapter)
                
            # Second, check for bare citations
            bare_matches = robust_bare_pat.findall(line)
            if bare_matches:
                for cat, rid in bare_matches:
                    violations.append({
                        "file": relpath,
                        "line_no": i + 1,
                        "ref_id": rid,
                        "concept": None,
                        "snippet": line.strip(),
                        "has_bracket_parenthesis": False,
                        "is_bolded": False,
                        "is_noun": True,
                        "noun_reason": f"Bare/noun citation '{cat} {rid}' found without proper formatting.",
                        "is_grouped": False,
                        "is_url_correct": False,
                        "url_reason": "Missing bracketed citation format.",
                        "link_url": None
                    })

print(f"Total violations found: {len(violations)}")

# Write validation logs
log_dir = os.path.join(SCRIPT_DIR, "logs")
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, "violations_analysis.log")

with open(log_path, "w", encoding="utf-8") as f:
    f.write("Quantum Braid Dynamics Monograph - Citation Validation Log\n")
    f.write(f"Total violations: {len(violations)}\n")
    f.write("=" * 60 + "\n")
    
    for file in sorted(list(set(v['file'] for v in violations))):
        f.write(f"\n=========================================\n")
        f.write(f"FILE: {file}\n")
        f.write(f"=========================================\n")
        file_violations = [v for v in violations if v['file'] == file]
        for v in file_violations:
            f.write(f"  Line {v['line_no']}: ID {v['ref_id']}\n")
            f.write(f"    Snippet: {v['snippet']}\n")
            reasons = []
            if not v['has_bracket_parenthesis']:
                reasons.append("Missing standard format [(§ID)]")
            if not v['is_bolded']:
                reasons.append(f"Concept name not bolded before citation (Extracted: {v['concept']})")
            if v['is_noun']:
                reasons.append(f"Functions as noun: {v['noun_reason']}")
            if v['is_grouped']:
                reasons.append("Grouped reference")
            if not v['is_url_correct']:
                reasons.append(f"URL incorrect: {v['url_reason']}")
            f.write(f"    Reasons: {'; '.join(reasons)}\n")
            f.write("-" * 40 + "\n")

print(f"Validation analysis saved to: {os.path.relpath(log_path, PROJECT_ROOT)}")
