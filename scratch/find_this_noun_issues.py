import os
import re

docs_dir = r"c:\braid-dynamics\qbd-portal\docs"
matches = []

# Pattern to search for: "this [noun] [§...]" or "this [noun] [(§...)]"
pat = re.compile(r"\bthis\s+(lemma|theorem|proof|section|appendix|chapter)\s*(?:[(])?\s*\[?§[0-9.]+", re.IGNORECASE)

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            lines = content.split("\n")
            for idx, line in enumerate(lines):
                if pat.search(line):
                    matches.append({
                        "file": os.path.relpath(filepath, docs_dir),
                        "line": idx + 1,
                        "content": line
                    })

print(f"Found {len(matches)} occurrences of 'this [noun] [§...]':")
for m in matches:
    print(f"File: {m['file']}:{m['line']}")
    print(f"  Content: {m['content']}")
    print("-" * 60)
