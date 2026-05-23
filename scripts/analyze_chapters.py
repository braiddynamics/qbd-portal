import os

docs_root = r"c:\braid-dynamics\qbd-portal\docs"
stage_root = os.path.join(docs_root, "03-stage")

draft_files = [
    "11-differential-geometry.md",
    "12-discrete-field-equations.md",
    "13-continuum-limit.md",
    "14-lorentzian-reality.md",
    "15a.md",
    "16a.md",
    "17.md"
]

for filename in draft_files:
    path = os.path.join(stage_root, filename)
    if not os.path.exists(path):
        print(f"File not found: {filename}")
        continue
    
    print(f"\n=========================================")
    print(f"FILE: {filename}")
    print(f"=========================================")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.splitlines()
    in_code = False
    for idx, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
            
        if line.startswith("# ") or line.startswith("## "):
            safe_line = line.encode('ascii', 'replace').decode('ascii')
            print(f"Line {idx+1:4d}: {safe_line}")
