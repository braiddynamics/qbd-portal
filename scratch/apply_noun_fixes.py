import os
import re

docs_dir = r"c:\braid-dynamics\qbd-portal\docs"
double_noun_pat = re.compile(
    r"established in the\s+(?:[A-Za-z0-9_'\-\s]+\s+)+the\s+(\*\*[^*]+\*\*)\s+(\[\(?§?[0-9.]+\)?\](?:\([^)]+\))?)",
    re.IGNORECASE
)

fixed_files = 0
total_noun_fixes = 0

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            new_content = content
            noun_fixes_in_file = 0
            
            # Find matches
            matches = list(double_noun_pat.finditer(new_content))
            if matches:
                for m in matches:
                    print(f"Match in {file}:")
                    print(f"  Old: {m.group(0)}")
                    # Form the replacement
                    # Group 1: bolded text, Group 2: link
                    replacement = f"established in the {m.group(1)} {m.group(2)}"
                    print(f"  New: {replacement}")
                    print("-" * 50)
                
                new_content, count = double_noun_pat.subn(r"established in the \1 \2", new_content)
                noun_fixes_in_file += count
                total_noun_fixes += count
            
            if noun_fixes_in_file > 0:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                fixed_files += 1

print("=" * 40)
print(f"Total files updated: {fixed_files}")
print(f"Total double-noun cleanups: {total_noun_fixes}")
