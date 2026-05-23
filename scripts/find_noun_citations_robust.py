import os
import re
import sys

# Configure output to support UTF-8 safely
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
docs_root = os.path.join(PROJECT_ROOT, "docs")

# Regular expression to match raw, bare, or bolded citation nouns
pattern = re.compile(
    r'\b(Lemma|Theorem|Axiom|Proof|Section|Definition|Principle|Postulate)\s+(\d+\.\d+(?:\.\d+)?(?:\.\d+)?)',
    re.IGNORECASE
)

matches = []

for root, dirs, files in os.walk(docs_root):
    for file in files:
        if not file.endswith(".md"):
            continue
        filepath = os.path.join(root, file)
        relpath = os.path.relpath(filepath, docs_root).replace("\\", "/")
        
        # Skip table of contents and reference files
        if "00-table-of-contents" in relpath or "appendices" in relpath or "a-references" in relpath:
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        for i, line in enumerate(lines):
            # Skip tables
            if "|" in line:
                continue
                
            for m in pattern.finditer(line):
                cat = m.group(1)
                num = m.group(2)
                
                # Skip headings
                if line.strip().startswith("#"):
                    continue
                    
                matches.append({
                    "file": relpath,
                    "line_no": i + 1,
                    "match": m.group(0),
                    "line_content": line.strip()
                })

# Write findings to logs
log_dir = os.path.join(SCRIPT_DIR, "logs")
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, "noun_citations_analysis.log")

with open(log_path, "w", encoding="utf-8") as f:
    f.write("Quantum Braid Dynamics Monograph - Robust Noun Citations Log\n")
    f.write(f"Total occurrences found: {len(matches)}\n")
    f.write("=" * 60 + "\n")
    for m in matches:
        f.write(f"\nFILE: {m['file']} Line {m['line_no']} -> {m['match']}\n")
        f.write(f"  Content: {m['line_content']}\n")
        f.write("-" * 40 + "\n")

print(f"Total occurrences found: {len(matches)}")
print(f"Details written to: scripts/logs/noun_citations_analysis.log")
