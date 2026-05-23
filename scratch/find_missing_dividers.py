import os
import re

docs_dir = r"c:\braid-dynamics\qbd-portal\docs"
missing_dividers = []

# Matches headers of the form: ### X.Y.Z where Z is a digit or 'Z' or a letter
# E.g. ### 14.2.1 or ### 14.2.Z
# But NOT ### 14.2.1.1
three_level_header_pat = re.compile(r"^###\s+[0-9]+\.[0-9]+\.([0-9]+|[a-zA-Z]+)(?:\s|{)")

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            # Skip _category_.yml or other files
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            for idx, line in enumerate(lines):
                stripped = line.strip()
                if three_level_header_pat.match(stripped):
                    # Check the lines preceding this header
                    # We want to see if the nearest non-blank line is "---" or "-----"
                    found_divider = False
                    # Look backwards up to 5 lines
                    for back_idx in range(idx - 1, max(-1, idx - 6), -1):
                        back_line = lines[back_idx].strip()
                        if back_line == "---" or back_line == "-----":
                            found_divider = True
                            break
                        if back_line != "":
                            # Found some text before divider, so no divider right above it
                            break
                    
                    if not found_divider:
                        missing_dividers.append({
                            "file": os.path.relpath(filepath, docs_dir),
                            "line": idx + 1,
                            "header": stripped
                        })

print(f"Found {len(missing_dividers)} missing dividers:")
for m in missing_dividers:
    print(f"File: {m['file']}:{m['line']} -> {m['header']}")
