import os
import re

docs_dir = r"c:\braid-dynamics\qbd-portal\docs"
matches = []

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            for line_idx, line in enumerate(lines):
                stripped = line.strip()
                if stripped.startswith("|") and stripped.endswith("|"):
                    # Count number of | characters
                    # But wait, we want to find if there's a | inside a math block like $...$
                    # Let's find $...$ blocks and see if they contain |
                    math_blocks = re.findall(r"\$.*?\$", stripped)
                    for block in math_blocks:
                        if "|" in block:
                            matches.append({
                                "file": os.path.relpath(filepath, docs_dir),
                                "line": line_idx + 1,
                                "content": stripped,
                                "block": block
                            })

print(f"Found {len(matches)} occurrences:")
for m in matches:
    print(f"File: {m['file']}:{m['line']}")
    print(f"  Content: {m['content']}")
    print(f"  Math Block: {m['block']}")
    print("-" * 40)
