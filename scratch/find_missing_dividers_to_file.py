import os
import re

docs_dir = r"c:\braid-dynamics\qbd-portal\docs"
missing_dividers = []

three_level_header_pat = re.compile(r"^###\s+[0-9]+\.[0-9]+\.([0-9]+|[a-zA-Z]+)(?:\s|{)")

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            for idx, line in enumerate(lines):
                stripped = line.strip()
                if three_level_header_pat.match(stripped):
                    found_divider = False
                    # Look backwards up to 5 lines
                    for back_idx in range(idx - 1, max(-1, idx - 6), -1):
                        back_line = lines[back_idx].strip()
                        if back_line == "---" or back_line == "-----":
                            found_divider = True
                            break
                        if back_line != "":
                            break
                    
                    if not found_divider:
                        missing_dividers.append({
                            "file": os.path.relpath(filepath, docs_dir),
                            "line": idx + 1,
                            "header": stripped
                        })

with open(r"c:\braid-dynamics\qbd-portal\scratch\missing_dividers.txt", "w", encoding="utf-8") as out:
    out.write(f"Found {len(missing_dividers)} missing dividers:\n")
    for m in missing_dividers:
        out.write(f"File: {m['file']}:{m['line']} -> {m['header']}\n")

print(f"Total missing: {len(missing_dividers)}. Details written to scratch/missing_dividers.txt")
