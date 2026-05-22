import os
import re
import json

docs_root = r"c:\braid-dynamics\qbd-portal\docs"

id_map = {}

# Patterns to match:
# ### 1.2.3 Lemma: Finite Information Density {#1.2.3}
# ### 2.1.1 Axiom: Irreflexivity of Causal Relations {#2.1.1}
# ### 6.1.4.1 Proof: Decay Rate Calculation {#6.1.4.1}
header_pat = re.compile(r'^###\s+(\d+\.\d+\.\d+(?:\.\d+)?)\s+(Lemma|Theorem|Axiom|Proof|Definition|Commentary|Postulate):\s+(.*?)\s*\{#(.*?)\}', re.IGNORECASE)

for root, dirs, files in os.walk(docs_root):
    for file in files:
        if not file.endswith(".md"):
            continue
        filepath = os.path.join(root, file)
        
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                m = header_pat.match(line.strip())
                if m:
                    sec_id, sec_type, sec_name, anchor = m.groups()
                    id_map[sec_id] = {
                        "name": sec_name.strip(),
                        "type": sec_type.strip().lower(),
                        "file": os.path.relpath(filepath, docs_root).replace("\\", "/")
                    }

with open("scratch/id_map.json", "w", encoding="utf-8") as f:
    json.dump(id_map, f, indent=2)

print(f"Extracted {len(id_map)} section IDs.")
# Print a few examples
for idx, (k, v) in enumerate(list(id_map.items())[:15]):
    print(f"{k} -> {v['type']}: {v['name']} ({v['file']})")
