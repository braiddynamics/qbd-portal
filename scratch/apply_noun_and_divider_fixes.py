import os
import re

docs_dir = r"c:\braid-dynamics\qbd-portal\docs"
double_noun_pat = re.compile(
    r"established in the\s+(?:[A-Za-z0-9_'\-\s]+\s+)+the\s+(\*\*[^*]+\*\*)\s+\[§([0-9.]+)\]",
    re.IGNORECASE
)
three_level_header_pat = re.compile(r"^###\s+[0-9]+\.[0-9]+\.([0-9]+|[a-zA-Z]+)(?:\s|{)")

fixed_files = 0
total_noun_fixes = 0
total_divider_fixes = 0

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # --- 1. Fix the double noun issues ---
            # We can search and replace
            new_content = content
            noun_fixes_in_file = 0
            
            # Let's search for matches and replace them
            matches = list(double_noun_pat.finditer(new_content))
            if matches:
                # We can perform regex sub
                # We want to replace matching strings with:
                # "established in the \1 [§\2]"
                # where \1 is the bolded proof name, \2 is the section number
                new_content, count = double_noun_pat.subn(r"established in the \1 [§\2]", new_content)
                noun_fixes_in_file += count
                total_noun_fixes += count
            
            # --- 2. Fix the missing dividers ---
            lines = new_content.split("\n")
            new_lines = []
            modified_dividers = False
            divider_fixes_in_file = 0
            
            idx = 0
            while idx < len(lines):
                line = lines[idx]
                stripped = line.strip()
                
                if three_level_header_pat.match(stripped):
                    # Check if there is already a divider
                    found_divider = False
                    # Look backwards in new_lines (which has all processed lines so far)
                    # We check the last few elements of new_lines
                    non_blank_count = 0
                    for back_idx in range(len(new_lines) - 1, -1, -1):
                        back_line = new_lines[back_idx].strip()
                        if back_line == "---" or back_line == "-----":
                            found_divider = True
                            break
                        if back_line != "":
                            non_blank_count += 1
                            if non_blank_count > 0: # Nearest non-blank line is text, so no divider
                                break
                    
                    if not found_divider:
                        # Insert a divider before this line!
                        # We want to insert '---' with appropriate blank lines.
                        # Let's pop trailing empty lines from new_lines first to clean up spacing
                        while new_lines and new_lines[-1].strip() == "":
                            new_lines.pop()
                        
                        # Add a blank line if new_lines is not empty, then '---', then a blank line
                        if new_lines:
                            new_lines.append("")
                        new_lines.append("---")
                        new_lines.append("")
                        
                        modified_dividers = True
                        divider_fixes_in_file += 1
                        total_divider_fixes += 1
                
                new_lines.append(line)
                idx += 1
            
            # Join lines back
            final_content = "\n".join(new_lines)
            
            if noun_fixes_in_file > 0 or divider_fixes_in_file > 0:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(final_content)
                fixed_files += 1
                print(f"Fixed {file}: {noun_fixes_in_file} nouns, {divider_fixes_in_file} dividers.")

print("=" * 40)
print(f"Total files updated: {fixed_files}")
print(f"Total double-noun cleanups: {total_noun_fixes}")
print(f"Total dividers inserted: {total_divider_fixes}")
