import os
import re

docs_dir = r"c:\braid-dynamics\qbd-portal\docs"
double_the_pat = re.compile(r"\b(The|the)\s+\*\*(The|the)\s+", re.IGNORECASE)

fixed_files = 0
total_fixes = 0

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            new_content = content
            # Replace
            matches = list(double_the_pat.finditer(new_content))
            if matches:
                for m in matches:
                    print(f"Match in {file}:")
                    print(f"  Old: {m.group(0)}")
                    # Form the replacement: keep the casing of the first "the"
                    replacement = f"{m.group(1)} **"
                    print(f"  New: {replacement}")
                    print("-" * 50)
                
                new_content, count = double_the_pat.subn(r"\1 **", new_content)
                total_fixes += count
                fixed_files += 1
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)

print("=" * 40)
print(f"Total files updated: {fixed_files}")
print(f"Total double-the cleanups: {total_fixes}")
