import os
import re

docs_root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "03-stage")

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Match level-2 headings of standard sections, e.g. "## 12.3 Geometric Conservation"
    # We want to catch the ones without " {#12.3}" at the end.
    # Group 1: section number, e.g. "12.3"
    # Group 2: section title, e.g. "Geometric Conservation"
    pattern = re.compile(r'^##\s+(\d+\.\d+)\s+([^{\n]+?)\s*$', re.MULTILINE)
    
    def repl(match):
        sec_num = match.group(1)
        sec_title = match.group(2).strip()
        # If it already ends with the anchor, don't change
        if sec_title.endswith(f"{{#{sec_num}}}"):
            return match.group(0)
        print(f"File {os.path.basename(filepath)}: Adding anchor to H2 '## {sec_num} {sec_title}' -> '## {sec_num} {sec_title} {{#{sec_num}}}'")
        return f"## {sec_num} {sec_title} {{#{sec_num}}}"
        
    new_content = pattern.sub(repl, content)
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

for root, dirs, files in os.walk(docs_root):
    for file in files:
        if file.endswith(".md"):
            process_file(os.path.join(root, file))
