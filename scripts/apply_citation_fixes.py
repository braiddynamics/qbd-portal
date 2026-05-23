import os
import re
import json

# Auto-detect project paths relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
docs_root = os.path.join(PROJECT_ROOT, "docs")

# Load the ID map containing names and types of all sections
id_map_path = os.path.join(SCRIPT_DIR, "id_map.json")
with open(id_map_path, "r", encoding="utf-8") as f:
    id_map = json.load(f)

# Short names for common IDs to ensure elegant sentence flow
short_names = {
    "1.2.3": "finite information density lemma",
    "1.2.4": "thermodynamic divergence lemma",
    "1.2.5": "causal loops recurrence lemma",
    "1.2.6": "operational non-termination lemma",
    "2.1.1": "irreflexivity axiom",
    "2.2.1": "reflexive counter-model proof",
    "2.2.2": "topological identification lemma",
    "2.2.3": "thermodynamic nullity lemma",
    "2.3.1": "geometric constructibility axiom",
    "2.3.2": "directed three-cycle primitive",
    "2.3.3": "principle of unique causality axiom",
    "2.7.1": "acyclic effective causality axiom",
    "2.7.2": "local rewrite rule theorem",
    "3.5.7": "quantum error-correcting codespace",
    "5.2.2": "flux balance master equation",
    "5.2.5": "catalyzed deletion mechanism",
    "5.2.7": "catalytic flux relation",
    "5.4.1": "equilibrium fixed point",
    "6.1.2": "particle necessity theorem",
    "6.1.3": "reducibility lemma",
    "6.1.4": "catalyzed instability lemma",
    "6.1.5": "topological protection barrier lemma",
    "6.1.6": "necessity of topological protection proof",
    "6.2.3": "exclusion of unbraided clusters lemma",
    "6.2.4": "exclusion of single-ribbon lemma",
    "6.2.5": "exclusion of two-strand ribbons lemma",
    "6.2.6": "analytical exclusion lemma",
    "6.2.7": "uniqueness of three-strand braid proof",
    "6.3.4": "crossing scaling lemma",
    "6.3.5": "torsional scaling lemma",
    "6.3.6": "entropic vanishing lemma",
    "6.3.7": "mass functional synthesis proof",
    "6.4.3": "local horizon lemma",
    "6.4.4": "global unwinding barrier lemma",
    "6.4.5": "architectural stability proof",
    "7.1.1": "spin operator definition",
    "7.1.3": "twist anticommutation lemma",
    "7.1.4": "exchange equivalence lemma",
    "7.1.5": "phase inversion proof",
    "7.2.2": "binary state lemma",
    "7.2.3": "forbidden occupancy lemma",
    "7.2.4": "exclusion principle proof",
    "7.3.4": "writhe conservation lemma",
    "7.3.5": "lepton and quark spectrum lemma",
    "7.3.6": "quark spectrum lemma",
    "7.3.7": "anomaly normalization lemma",
    "7.3.8": "charge emergence proof",
    "7.4.3": "thermodynamic equivalence lemma",
    "7.4.4": "crossing scaling lemma",
    "7.4.5": "geometric sharing efficiency lemma",
    "7.4.6": "mass spectrum proof",
    "8.1.2": "braid isomorphism lemma",
    "8.1.3": "distant commutativity lemma",
    "8.1.4": "yang-baxter relations lemma",
    "8.1.5": "commutator depth lemma",
    "8.1.6": "lie algebra emergence proof",
    "8.2.3": "basis verification lemma",
    "8.2.4": "commutator generation lemma",
    "8.2.5": "algebraic closure lemma",
    "8.2.6": "closure verification lemma",
    "8.2.7": "confinement and isomorphism lemma",
    "8.2.8": "color symmetry su(3) emergence proof",
    "8.3.3": "chiral stability lemma",
    "8.3.4": "weak doublet algebra lemma",
    "8.3.5": "mirror path rejection lemma",
    "8.3.6": "path rejection lemma",
    "8.3.7": "mirror path rejection lemma",
    "8.3.8": "chiral weak current proof",
    "8.4.2": "friction ratio lemma",
    "8.4.3": "coupling correspondence lemma",
    "8.4.4": "complexity identification lemma",
    "8.4.5": "angle synthesis proof",
    "8.5.2": "probabilistic identity lemma",
    "8.5.3": "trace normalization lemma",
    "8.5.4": "geometric normalization lemma",
    "8.5.5": "entropic weighting lemma",
    "8.5.6": "combinatorial weighting lemma",
    "8.5.7": "coupling strength synthesis proof",
    "8.6.3": "boson mass prediction lemma",
    "8.6.4": "vacuum expectation value lemma",
    "8.6.5": "topological yukawa identity lemma",
    "8.6.6": "mass generation sensitivity lemma",
    "8.6.7": "mass condensation proof",
    "9.1.2": "rank conditions lemma",
    "9.1.3": "lower rank exclusion lemma",
    "9.1.4": "candidate elimination lemma",
    "9.1.5": "uniqueness verification proof",
    "9.2.3": "distant commutativity lemma",
    "9.2.4": "yang-baxter relations lemma",
    "9.2.5": "unified lie algebra lemma",
    "9.2.6": "anti-fundamental representation lemma",
    "9.2.7": "antisymmetric representation lemma",
    "9.2.8": "braid unification proof",
    "9.3.2": "complexity ordering lemma",
    "9.3.3": "topological protection lemma",
    "9.3.4": "decay tunneling lemma",
    "9.3.5": "trapping synthesis proof",
    "9.4.3": "interaction vertex lemma",
    "9.4.4": "fragmentation tunneling lemma",
    "9.4.5": "mixing demonstration proof",
    "9.5.2": "tension verification lemma",
    "9.5.3": "minimal action pathway lemma",
    "9.5.4": "action-mass proportionality lemma",
    "9.5.5": "stability synthesis proof",
    "9.6.3": "neutrality verification lemma",
    "9.6.4": "seesaw dynamics lemma",
    "9.6.5": "complexity density limits lemma",
    "9.6.6": "vacuum friction limits lemma",
    "9.6.7": "critical balance limits lemma",
    "9.6.8": "planck anchor lemma",
    "9.6.9": "neutrino mass chain proof",
    "10.1.3": "topological stability lemma",
    "10.1.4": "topological distinctness lemma",
    "10.1.5": "state controllability lemma",
    "10.1.6": "measurability lemma",
    "10.1.7": "qubit optimality proof",
    "10.2.3": "stabilizer commutations lemma",
    "10.2.4": "bit-flip error detection lemma",
    "10.2.5": "ribbon stabilizer commutations lemma",
    "10.2.6": "fraying error detection lemma",
    "10.2.7": "vertex stabilizer commutations lemma",
    "10.2.8": "phase error detection lemma",
    "10.2.9": "code consistency proof",
    "10.3.3": "syndrome response lemma",
    "10.3.4": "code distance lemma",
    "10.3.5": "thermodynamic healing theorem",
    "10.4.3": "writhe conservation lemma",
    "10.4.4": "charge conservation lemma",
    "10.4.5": "gate action proof",
    "10.5.2": "singlet transparency lemma",
    "10.5.3": "color phase holonomy lemma",
    "10.5.4": "gate action proof",
    "10.6.2": "temperature modulation lemma",
    "10.6.3": "topological degeneracy lemma",
    "10.6.4": "coherent quench proof",
    "10.7.2": "syndrome coupling lemma",
    "10.7.3": "catalytic control lemma",
    "10.7.4": "gate action proof",
    "10.8.3": "category structures lemma",
    "10.8.4": "monoidal structures lemma",
    "10.8.5": "braiding structures lemma",
    "10.8.6": "duality structures lemma",
    "10.8.7": "twisting morphism lemma",
    "10.8.8": "gate action proof",
    "10.9.2": "clifford generation lemma",
    "10.9.3": "approximation scheme proof"
}

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

def get_section_title(sec_id):
    parts = sec_id.split('.')
    if len(parts) < 2:
        return None
    ch_num = int(parts[0])
    sec_num = f"{parts[0]}.{parts[1]}"
    
    found_dir = None
    for k, v in doc_dirs.items():
        if f"{ch_num:02d}" in k or (ch_num == 10 and "10" in k):
            found_dir = k
            break
            
    if not found_dir:
        return None
        
    filepath = os.path.join(docs_root, found_dir.replace("/", os.sep), f"{sec_num}.md")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith(f"## {sec_num} ") or line.startswith(f"## {sec_id} "):
                    title = line.replace(f"## {sec_num} ", "").replace(f"## {sec_id} ", "").strip()
                    title = re.sub(r'\{#[^}]+\}', '', title)
                    return title.strip()
                elif line.startswith("## "):
                    title = line.replace("## ", "").strip()
                    title = re.sub(r'\{#[^}]+\}', '', title)
                    title = re.sub(r'^\d+\.\d+\s*', '', title)
                    return title.strip()
    return None

def get_clean_name(sec_id):
    if sec_id in short_names:
        return short_names[sec_id]
        
    parts = sec_id.split('.')
    if len(parts) == 2:
        title = get_section_title(sec_id)
        if title:
            return f"{title.lower().strip()} section"
        return f"section {sec_id}"
        
    if sec_id in id_map:
        name = id_map[sec_id]["name"]
        stype = id_map[sec_id]["type"]
        name_lower = name.lower().strip()
        name_lower = re.sub(r'\s+', ' ', name_lower)
        if stype in name_lower:
            return name_lower
        else:
            return f"{name_lower} {stype}"
            
    return None

def get_url_path(sec_id):
    parts = sec_id.split('.')
    if len(parts) < 2:
        return None
    ch_num = int(parts[0])
    sec_num = f"{parts[0]}.{parts[1]}"
    
    if ch_num == 1:
        part, chap = "rules", "ontology"
    elif ch_num == 2:
        part, chap = "rules", "axioms"
    elif ch_num == 3:
        part, chap = "rules", "architecture"
    elif ch_num == 4:
        part, chap = "rules", "dynamics"
    elif ch_num == 5:
        part, chap = "rules", "equilibrium"
    elif ch_num == 6:
        part, chap = "players", "fermions"
    elif ch_num == 7:
        part, chap = "players", "topology"
    elif ch_num == 8:
        part, chap = "players", "braids"
    elif ch_num == 9:
        part, chap = "players", "unification"
    elif ch_num == 10:
        part, chap = "players", "computation"
    else:
        return None
        
    return f"/monograph/{part}/{chap}/{sec_num}/#{sec_id}"

stop_words = {
    'the', 'a', 'an', 'of', 'in', 'to', 'for', 'and', 'or', 'is', 'are', 'with', 
    'as', 'via', 'by', 'at', 'from', 'on', 'into', 'under', 'enforcing', 'respect',
    'satisfying', 'violating', 'mandates', 'excludes', 'implies', 'concludes',
    'enforced', 'occupying', 'denoted', 'residing', 'established', 'using'
}

def clean_line_citations(line, part, chapter):
    # Handle special hardcoded exact matches
    if "Constants T, mu, lambda_cat derived in §4.4." in line:
        return line.replace(
            "Constants T, mu, lambda_cat derived in §4.4.",
            "Constants T, mu, lambda_cat derived in the **thermodynamic parameters section** [(§4.4)](/monograph/rules/dynamics/4.4/#4.4)."
        )
    if "fundamental topological qubits from §10.1." in line:
        return line.replace(
            "fundamental topological qubits from §10.1.",
            "fundamental topological qubits from the **universal topological qubits** [(§10.1)](/monograph/players/computation/10.1/#10.1)."
        )
    if "[(§10.4-10.8)]" in line:
        new_ref = (
            f"**gates** [(§10.4)](/monograph/players/computation/10.4/#10.4) "
            f"[(§10.5)](/monograph/players/computation/10.5/#10.5) "
            f"[(§10.6)](/monograph/players/computation/10.6/#10.6) "
            f"[(§10.7)](/monograph/players/computation/10.7/#10.7) "
            f"[(§10.8)](/monograph/players/computation/10.8/#10.8)"
        )
        line = line.replace("gates [(§10.4-10.8)](/monograph/players/computation/10.4/#10.4)", new_ref)
        line = line.replace("gates [(§10.4-10.8)]", new_ref)

    # Proof outline commentaries
    outline_re = re.compile(
        r'^(\s*\d+\.\s+)\*\*(.*?)\s*\((?:Lemma|Theorem|Proof|Axiom|Definition|Principle|Commentary|Postulate)\s+\[?§([0-9\.\-,]+)\]?(?:\(([^)]+)\))?\)(:)?\*\*',
        re.IGNORECASE
    )
    m_outline = outline_re.match(line)
    if m_outline:
        indent = m_outline.group(1)
        concept = m_outline.group(2).strip()
        rid = m_outline.group(3)
        colon = m_outline.group(5) or ""
        url = get_url_path(rid)
        trailing = line[m_outline.end():]
        line = f"{indent}**{concept}** [({chr(167)}{rid})]({url}){colon}{trailing}"

    # Standardize citations
    citation_re = re.compile(r'(?:\[\(§([0-9a-zA-Z\.\-]+)\)\]|\[§([0-9a-zA-Z\.\-]+)\]|\(§([0-9a-zA-Z\.\-]+)\)|§([0-9a-zA-Z\.\-]+))(?:\([^\)]+\))?')
    bare_categorizer_re = re.compile(
        r'\b(the\s+)?(Lemma|Theorem|Axiom|Proof|Definition|Section|Principle|Postulate)\s*(?:[0-9\.\-]+)?(?:\s*\([^)]+\))?\s*(?:in|of|for|to|on|at|a|an|the)?\s*(?:in|of|for|to|on|at|a|an|the)?\s*$',
        re.IGNORECASE
    )
    
    idx = 0
    while True:
        m = citation_re.search(line, idx)
        if not m:
            break
            
        full_match = m.group(0)
        rid = m.group(1) or m.group(2) or m.group(3) or m.group(4)
        rid_clean = rid.rstrip('.')
        
        if not re.match(r'^\d+\.\d+(\.\d+)?(\.\d+)?$', rid_clean):
            idx = m.end()
            continue
            
        match_start = m.start()
        match_end = m.end()
        
        prefix = line[:match_start]
        suffix = line[match_end:]
        
        url = get_url_path(rid_clean)
        
        if "|" in line:
            replacement = f"[({chr(167)}{rid_clean})]({url})"
            line = prefix + replacement + suffix
            idx = len(prefix) + len(replacement)
            continue
            
        is_bolded = False
        m_bold = re.search(r'\*\*([^*]+)\*\*\s*$', prefix)
        if m_bold:
            is_bolded = True
            
        if is_bolded:
            sub_prefix = prefix[:m_bold.start()]
            concept_name = m_bold.group(1)
            
            m_bare_before = bare_categorizer_re.search(sub_prefix)
            if m_bare_before:
                new_sub_prefix = sub_prefix[:m_bare_before.start()]
                concept_display = concept_name
                if new_sub_prefix.strip() == "":
                    concept_display = concept_name[0].upper() + concept_name[1:] if concept_name else concept_name
                prefix = new_sub_prefix + f"**{concept_display}**" + prefix[len(prefix.rstrip()):]
                
            replacement = f"[({chr(167)}{rid_clean})]({url})"
            spacing = prefix[len(prefix.rstrip()):]
            prefix_clean = prefix.rstrip()
            line = prefix_clean + spacing + replacement + suffix
            idx = len(prefix_clean) + len(spacing) + len(replacement)
            continue
            
        m_bare = bare_categorizer_re.search(prefix)
        
        cap_phrase_re = re.compile(
            r'\b(?:[A-Z][a-zA-Z0-9_\-]*\s+(?:of|and|the|in|for|to|on|at)\s+)*[A-Z][a-zA-Z0-9_\-]*(?:\s+[A-Z0-9][a-zA-Z0-9_\-]*)*\s*$',
            re.ASCII
        )
        m_cap = cap_phrase_re.search(prefix)
        
        if m_bare:
            prefix_stripped = prefix[:m_bare.start()]
            clean_name = get_clean_name(rid_clean)
            if not clean_name:
                clean_name = f"{m_bare.group(2).lower()} {rid_clean}"
                
            replacement = f"the **{clean_name}** [({chr(167)}{rid_clean})]({url})"
            line = prefix_stripped + replacement + suffix
            idx = len(prefix_stripped) + len(replacement)
            
        elif m_cap:
            concept_phrase = m_cap.group(0).strip()
            non_concept_prefix = prefix[:m_cap.start()]
            trailing_spaces = m_cap.group(0)[len(concept_phrase):]
            
            m_bare_before = bare_categorizer_re.search(non_concept_prefix)
            if m_bare_before:
                non_concept_prefix = non_concept_prefix[:m_bare_before.start()]
                concept_display = concept_phrase
                if non_concept_prefix.strip() == "":
                    concept_display = concept_phrase[0].upper() + concept_phrase[1:] if concept_phrase else concept_phrase
                replacement = f"**{concept_display}**{trailing_spaces}[({chr(167)}{rid_clean})]({url})"
            else:
                replacement = f"**{concept_phrase}**{trailing_spaces}[({chr(167)}{rid_clean})]({url})"
                
            line = non_concept_prefix + replacement + suffix
            idx = len(non_concept_prefix) + len(replacement)
            
        else:
            words = re.split(r'(\s+)', prefix)
            concept_words = []
            non_stop_count = 0
            word_idx = len(words) - 1
            
            while word_idx >= 0:
                word_str = words[word_idx]
                if not word_str.strip():
                    concept_words.append(word_str)
                    word_idx -= 1
                    continue
                    
                if re.search(r'[#\*\[\]\(\)_<>\.,;:!\?\-\+=/\\\|\$~`\n\r]', word_str):
                    break
                    
                word_lower = word_str.lower().strip()
                if word_lower in stop_words:
                    break
                    
                concept_words.append(word_str)
                non_stop_count += 1
                if non_stop_count >= 3:
                    break
                word_idx -= 1
                
            if non_stop_count > 0:
                concept_words.reverse()
                non_concept_prefix_spaces = ""
                while concept_words and not concept_words[0].strip():
                    non_concept_prefix_spaces += concept_words.pop(0)
                    
                trailing_spaces = ""
                while concept_words and not concept_words[-1].strip():
                    trailing_spaces = concept_words.pop() + trailing_spaces
                    
                concept_phrase = "".join(concept_words).strip()
                
                last_index_kept = word_idx + 1
                non_concept_prefix = "".join(words[:last_index_kept]) + non_concept_prefix_spaces
                
                m_bare_before = bare_categorizer_re.search(non_concept_prefix)
                if m_bare_before:
                    non_concept_prefix = non_concept_prefix[:m_bare_before.start()]
                    concept_display = concept_phrase
                    if non_concept_prefix.strip() == "":
                        concept_display = concept_phrase[0].upper() + concept_phrase[1:] if concept_phrase else concept_phrase
                    replacement = f"**{concept_display}**{trailing_spaces}[({chr(167)}{rid_clean})]({url})"
                else:
                    replacement = f"**{concept_phrase}**{trailing_spaces}[({chr(167)}{rid_clean})]({url})"
                    
                line = non_concept_prefix + replacement + suffix
                idx = len(non_concept_prefix) + len(replacement)
            else:
                clean_name = get_clean_name(rid_clean)
                if clean_name:
                    replacement = f"**{clean_name}** [({chr(167)}{rid_clean})]({url})"
                    line = prefix + replacement + suffix
                    idx = len(prefix) + len(replacement)
                else:
                    replacement = f"[({chr(167)}{rid_clean})]({url})"
                    line = prefix + replacement + suffix
                    idx = len(prefix) + len(replacement)
                    
    return line

bare_citation_re = re.compile(
    r'(?:\*\*\s*)?\b(?:the\s+)?(Lemma|Theorem|Axiom|Proof|Section|Definition|Principle|Postulate)\s+(\d+\.\d+(?:\.\d+)?(?:\.\d+)?)\b(?:\s*\*\*)?'
    r'(?:\s*\[\s*\(\s*§\s*\2\s*\)\s*\]\s*\([^\)]+\)|'
    r'\s*\[\s*§\s*\2\s*\]|'
    r'\s*\(\s*§\s*\2\s*\))?',
    re.IGNORECASE
)

def fix_bare_citations_in_line(line):
    idx = 0
    new_line = line
    while True:
        m = bare_citation_re.search(new_line, idx)
        if not m:
            break
        
        cat = m.group(1)
        rid = m.group(2)
        
        # Get replacement
        clean_name = get_clean_name(rid)
        if not clean_name:
            clean_name = f"{cat.lower()} {rid}"
            
        url = get_url_path(rid)
        if not url:
            idx = m.end()
            continue
            
        # Capitalize if at start of string or sentence
        prefix = new_line[:m.start()]
        is_start = False
        if prefix.strip() == "" or prefix.strip()[-1] in ".!?#":
            is_start = True
            
        concept_display = clean_name
        if is_start and concept_display:
            concept_display = concept_display[0].upper() + concept_display[1:]
            
        replacement = f"the **{concept_display}** [({chr(167)}{rid})]({url})"
        if is_start:
            replacement = f"The **{concept_display}** [({chr(167)}{rid})]({url})"
            
        new_line = new_line[:m.start()] + replacement + new_line[m.end():]
        idx = m.start() + len(replacement)
        
    return new_line

def fix_all_files():
    count_files = 0
    for root, dirs, files in os.walk(docs_root):
        for file in files:
            if not file.endswith(".md"):
                continue
            filepath = os.path.join(root, file)
            relpath = os.path.relpath(filepath, docs_root).replace("\\", "/")
            
            if "00-table-of-contents" in relpath or "appendices" in relpath or "a-references" in relpath:
                continue
                
            part = None
            chapter = None
            for key, val in doc_dirs.items():
                if key in relpath:
                    part, chapter = val
                    break
                    
            if not part or not chapter:
                continue
                
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
                
            new_lines = []
            modified = False
            in_code_block = False
            for i, line in enumerate(lines):
                stripped = line.strip()
                if stripped.startswith("```"):
                    in_code_block = not in_code_block
                    new_lines.append(line)
                    continue
                    
                if in_code_block:
                    new_lines.append(line)
                    continue
                    
                # Skip tables, note headers, and other non-citations
                if "|" in line or stripped.startswith(":::") or "Overview**]" in line:
                    new_lines.append(line)
                    continue
                
                fixed_line = line
                # Pass 1: Standard citation formatting (for lines with section symbol)
                if "§" in fixed_line:
                    fixed_line = clean_line_citations(fixed_line, part, chapter)
                
                # Pass 2: Bare/noun citation formatting
                fixed_line = fix_bare_citations_in_line(fixed_line)
                
                if fixed_line != line:
                    new_lines.append(fixed_line)
                    modified = True
                else:
                    new_lines.append(line)
                    
            if modified:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)
                print(f"Repaired citations in: {relpath}")
                count_files += 1
                
    print(f"\nDone! Automatically repaired citations in {count_files} files.")

if __name__ == "__main__":
    fix_all_files()
