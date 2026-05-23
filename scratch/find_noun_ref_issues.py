import os
import re

docs_dir = r"c:\braid-dynamics\qbd-portal\docs"
patterns = [
    r"this lemma\s*\[§",
    r"the lemma\s*\[§",
    r"this theorem\s*\[§",
    r"the theorem\s*\[§",
    r"this proof\s*\[§",
    r"the proof\s*\[§",
    r"this section\s*\[§",
    r"the section\s*\[§",
    r"in the\s+[A-Za-z0-9_'\-\s]+\s+the\s+\*\*"
]

matches = []

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            lines = content.split("\n")
            for idx, line in enumerate(lines):
                for pat in patterns:
                    if re.search(pat, line, re.IGNORECASE):
                        matches.append({
                            "file": os.path.relpath(filepath, docs_dir),
                            "line": idx + 1,
                            "content": line,
                            "pattern": pat
                        })

print(f"Found {len(matches)} potential noun/ref issues:")
for m in matches:
    print(f"File: {m['file']}:{m['line']} (Pattern: {m['pattern']})")
    print(f"  Content: {m['content']}")
    print("-" * 60)
