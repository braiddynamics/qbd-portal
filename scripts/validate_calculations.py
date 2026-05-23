import os
import re
import json

# Setup paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
docs_root = os.path.join(PROJECT_ROOT, "docs")
id_map_path = os.path.join(SCRIPT_DIR, "id_map.json")

# Load the ID map to verify cited section types
with open(id_map_path, "r", encoding="utf-8") as f:
    id_map = json.load(f)

# Calculation header regex
calculation_header_pat = re.compile(
    r'^###\s+(\d+\.\d+(?:\.\d+)?(?:\.\d+)?)\s+Calculation:\s*(.*?)\s*\{#(\d+\.\d+(?:\.\d+)?(?:\.\d+)?)\}',
    re.IGNORECASE
)

# Forbidden pronouns and software jargon
pronouns = {'we', 'us', 'our'}
software_jargon = {
    'return', 'returns', 'argument', 'arguments', 'int', 'float', 'tuple', 'tuples',
    'function', 'functions', 'variable', 'variables', 'class', 'classes', 'method',
    'methods', 'dictionary', 'dictionaries', 'list', 'lists', 'string', 'strings',
    'boolean', 'booleans', 'object', 'objects', 'callback', 'callbacks', 'array', 'arrays'
}

violations = []

def analyze_calculation(filepath, relpath, sec_id, title, lines, start_idx, end_idx):
    calc_body = lines[start_idx:end_idx]
    
    # 1. Check for Active Impersonal (no we, i, us, our) in prose
    prose_content = ""
    in_code = False
    for line in calc_body:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        prose_content += line + "\n"
        
    words = re.findall(r'\b\w+\b', prose_content.lower())
    
    found_pronouns = [w for w in words if w in pronouns]
    if found_pronouns:
        matching_lines = []
        for l in calc_body:
            l_words = re.findall(r'\b\w+\b', l.lower())
            if any(w in l_words for w in pronouns):
                matching_lines.append(l.strip())
        snippet = matching_lines[0] if matching_lines else "Unknown"
        violations.append({
            "file": relpath,
            "id": sec_id,
            "title": title,
            "type": "pronoun",
            "reason": f"First-person pronouns found: {set(found_pronouns)}",
            "snippet": snippet
        })
        
    # 2. Check for software jargon
    # Skip checking jargon in formulas or within backticks, so we strip out backticked words
    clean_prose = re.sub(r'`[^`]+`', '', prose_content)
    clean_words = re.findall(r'\b\w+\b', clean_prose.lower())
    found_jargon = [w for w in clean_words if w in software_jargon]
    if found_jargon:
        matching_lines = []
        for l in calc_body:
            l_clean = re.sub(r'`[^`]+`', '', l)
            l_words = re.findall(r'\b\w+\b', l_clean.lower())
            if any(w in l_words for w in found_jargon):
                matching_lines.append(l.strip())
        snippet = matching_lines[0] if matching_lines else "Unknown"
        violations.append({
            "file": relpath,
            "id": sec_id,
            "title": title,
            "type": "jargon",
            "reason": f"Software jargon found: {set(found_jargon)}",
            "snippet": snippet
        })

    # 3. Check structural formatting
    stripped_lines = [l.strip() for l in calc_body if l.strip()]
    
    # Needs note block
    note_start = -1
    note_end = -1
    for idx, l in enumerate(stripped_lines):
        if l.startswith(":::note["):
            note_start = idx
        elif l.startswith(":::") and note_start != -1 and note_end == -1:
            note_end = idx
            
    if note_start == -1 or note_end == -1:
        violations.append({
            "file": relpath,
            "id": sec_id,
            "title": title,
            "type": "note_block",
            "reason": "Missing or malformed :::note block",
            "snippet": stripped_lines[0] if stripped_lines else ""
        })
    else:
        # Check note title format: :::note[**[Gerund/Active Noun] of [Physical Concept] via [Computational Method]**]
        note_line = stripped_lines[note_start]
        if not (note_line.startswith(":::note[**") and note_line.endswith("**]")):
            violations.append({
                "file": relpath,
                "id": sec_id,
                "title": title,
                "type": "note_block_header",
                "reason": f"Malformed note block header: '{note_line}'",
                "snippet": note_line
            })
            
    # Check intro sentence: [Noun indicating verification] of the [Specific Logic/Condition] established in the [Proof Name] [Silent Citation] is based on the following protocols:
    intro_idx = note_end + 1 if note_end != -1 else 0
    if intro_idx < len(stripped_lines):
        intro_line = stripped_lines[intro_idx]
        if not intro_line.endswith("is based on the following protocols:"):
            violations.append({
                "file": relpath,
                "id": sec_id,
                "title": title,
                "type": "intro_sentence",
                "reason": "Intro sentence does not end with 'is based on the following protocols:'",
                "snippet": intro_line
            })
            
        # Check for citation
        cit_match = re.search(r'\[\(§([0-9\.]+)\)\]\(([^)]+)\)', intro_line)
        if not cit_match:
            violations.append({
                "file": relpath,
                "id": sec_id,
                "title": title,
                "type": "intro_citation",
                "reason": "Intro sentence missing silent citation in the format '[(§ID)](link)'",
                "snippet": intro_line
            })
        else:
            cited_id = cit_match.group(1)
            # Verify that cited ID exists in map and is a proof
            if cited_id not in id_map:
                violations.append({
                    "file": relpath,
                    "id": sec_id,
                    "title": title,
                    "type": "intro_citation_target",
                    "reason": f"Cited ID '{cited_id}' is not in the canonical id_map",
                    "snippet": intro_line
                })
            else:
                cited_type = id_map[cited_id].get("type")
                if cited_type != "proof":
                    violations.append({
                        "file": relpath,
                        "id": sec_id,
                        "title": title,
                        "type": "intro_citation_type",
                        "reason": f"Cited ID '{cited_id}' has type '{cited_type}', expected 'proof'",
                        "snippet": intro_line
                    })
    else:
        violations.append({
            "file": relpath,
            "id": sec_id,
            "title": title,
            "type": "intro_sentence",
            "reason": "Missing intro sentence entirely",
            "snippet": ""
        })

    # Check steps: should have exactly 3 steps, numbered 1, 2, 3
    steps = []
    # Collect only lines starting with digits (steps)
    for l in stripped_lines[intro_idx+1:]:
        if re.match(r'^\d+\.', l):
            steps.append(l)
            
    if len(steps) != 3:
        violations.append({
            "file": relpath,
            "id": sec_id,
            "title": title,
            "type": "step_count",
            "reason": f"Expected exactly 3 steps, found {len(steps)}",
            "snippet": "; ".join(steps)
        })
    else:
        for idx, step in enumerate(steps):
            step_num = idx + 1
            # Step spacing: '1.  **[Step Name]:**'
            # Note the two spaces after the period
            if not step.startswith(f"{step_num}.  **"):
                violations.append({
                    "file": relpath,
                    "id": sec_id,
                    "title": title,
                    "type": "step_spacing",
                    "reason": f"Step {step_num} is missing double spacing after period or start of bolding (expected '{step_num}.  **')",
                    "snippet": step
                })
            
            # Check for bolded name followed by colon inside bolding: e.g. '**Step Name:**'
            if not re.match(rf'^{step_num}\.  \*\*([^*:]+):\*\*\s+', step):
                violations.append({
                    "file": relpath,
                    "id": sec_id,
                    "title": title,
                    "type": "step_bold_header",
                    "reason": f"Step {step_num} is missing bolded step name with colon inside bolding (expected '{step_num}.  **Step Name:** ')",
                    "snippet": step
                })

# Iterate through all markdown files
for root, dirs, files in os.walk(docs_root):
    for file in files:
        if not file.endswith(".md"):
            continue
        filepath = os.path.join(root, file)
        relpath = os.path.relpath(filepath, docs_root).replace("\\", "/")
        
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        in_calc = False
        calc_id = None
        calc_title = None
        calc_start = -1
        
        for idx, line in enumerate(lines):
            m = calculation_header_pat.match(line)
            if m:
                if in_calc:
                    # Analyze previous calculation
                    analyze_calculation(filepath, relpath, calc_id, calc_title, lines, calc_start, idx)
                in_calc = True
                calc_id = m.group(1)
                calc_title = m.group(2)
                calc_start = idx + 1
                continue
                
            if in_calc:
                # Calculation section ends when a code block starts or next header starts
                if line.strip().startswith("```python") or line.strip().startswith("```text") or line.startswith("## ") or line.startswith("### "):
                    analyze_calculation(filepath, relpath, calc_id, calc_title, lines, calc_start, idx)
                    in_calc = False
                    calc_id = None
                    calc_title = None
                    calc_start = -1

print(f"Total violations found: {len(violations)}")

# Write validation logs
log_dir = os.path.join(SCRIPT_DIR, "logs")
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, "calculations_violations.log")

with open(log_path, "w", encoding="utf-8") as f:
    f.write("Quantum Braid Dynamics Monograph - Calculation Validation Log\n")
    f.write(f"Total violations: {len(violations)}\n")
    f.write("=" * 60 + "\n")
    
    for file in sorted(list(set(v['file'] for v in violations))):
        f.write(f"\n=========================================\n")
        f.write(f"FILE: {file}\n")
        f.write(f"=========================================\n")
        file_violations = [v for v in violations if v['file'] == file]
        for v in file_violations:
            f.write(f"  Calculation {v['id']} ({v['title']}):\n")
            f.write(f"    Type: {v['type']}\n")
            f.write(f"    Violation: {v['reason']}\n")
            f.write(f"    Snippet: {v['snippet']}\n")
            f.write("-" * 40 + "\n")

print(f"Validation analysis saved to: {os.path.relpath(log_path, PROJECT_ROOT)}")
