import os
import re
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
docs_root = os.path.join(PROJECT_ROOT, "docs")

heading_pat = re.compile(r'^#+\s+(\d+\.\d+(?:\.\d+)?(?:\.\d+)?)\s+([^\{]+?)\s*\{#(.*?)\}', re.IGNORECASE)

id_map = {}

categorizers = [
    "Lemma", "Theorem", "Axiom", "Proof", "Definition", "Commentary", 
    "Postulate", "Section", "Implications", "Diagram", "Calculation", 
    "Corollary", "Example"
]

def parse_heading_text(text):
    text = text.strip()
    if ":" in text:
        parts = text.split(":", 1)
        type_candidate = parts[0].strip()
        name_candidate = parts[1].strip()
        for cat in categorizers:
            if cat.lower() in type_candidate.lower():
                return cat.lower(), name_candidate
        return "section", text
    else:
        for cat in categorizers:
            if text.lower().startswith(cat.lower()):
                name_candidate = text[len(cat):].strip()
                if name_candidate.lower().startswith("of "):
                    name_candidate = name_candidate[3:].strip()
                elif name_candidate.lower().startswith("the "):
                    name_candidate = name_candidate[4:].strip()
                return cat.lower(), name_candidate if name_candidate else text
        return "section", text

for root, dirs, files in os.walk(docs_root):
    for file in files:
        if not file.endswith(".md"):
            continue
        filepath = os.path.join(root, file)
        relpath = os.path.relpath(filepath, docs_root).replace("\\", "/")
        
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                m = heading_pat.match(line.strip())
                if m:
                    sec_id, heading_text, anchor = m.groups()
                    sec_type, sec_name = parse_heading_text(heading_text)
                    id_map[sec_id] = {
                        "name": sec_name.strip(),
                        "type": sec_type.strip(),
                        "file": relpath
                    }

out_path = os.path.join(SCRIPT_DIR, "id_map.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(id_map, f, indent=2)

print(f"Rebuilt id_map.json with {len(id_map)} entries.")
