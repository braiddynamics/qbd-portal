import os
import re

docs_dir = r"c:\braid-dynamics\qbd-portal\docs"
changes = []

# Regex patterns
section_ref_pattern = re.compile(r"\[\(§([^)]+)\)\]")

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            lines = content.split("\n")
            modified = False
            new_lines = []
            
            for idx, line in enumerate(lines):
                stripped = line.strip()
                new_line = line
                
                # Check if it is a table row
                if stripped.startswith("|") and stripped.endswith("|"):
                    # 1. Replace the wavefunction |Psi> symbol
                    if "$|\\Psi\\rangle$" in new_line:
                        new_line = new_line.replace("$|\\Psi\\rangle$", "$\\vert\\Psi\\rangle$")
                        modified = True
                        print(f"Matched |Psi> in {file}:{idx+1}")
                    
                    # 2. Replace the ||psi_violation> symbol
                    if "$\\| \\psi_{violation}\\rangle$" in new_line:
                        new_line = new_line.replace("$\\| \\psi_{violation}\\rangle$", "$\\Vert \\psi_{violation}\\rangle$")
                        modified = True
                        print(f"Matched ||psi_violation> with space in {file}:{idx+1}")
                    if "$\\|\\psi_{violation}\\rangle$" in new_line:
                        new_line = new_line.replace("$\\|\\psi_{violation}\\rangle$", "$\\Vert\\psi_{violation}\\rangle$")
                        modified = True
                        print(f"Matched ||psi_violation> without space in {file}:{idx+1}")
                    
                    # 3. Replace the double-bars in Chapter 3.5 state table
                    if file == "3.5.md":
                        # We want to replace the double bars
                        # In 3.5.md:
                        # State $\|q_{12}q_{23}q_{31}\rangle$ -> State $\Vert q_{12}q_{23}q_{31}\rangle$
                        # $\|000\rangle$ -> $\Vert 000\rangle$
                        # etc.
                        if "$\\|q_{12}q_{23}q_{31}\\rangle$" in new_line:
                            new_line = new_line.replace("$\\|q_{12}q_{23}q_{31}\\rangle$", "$\\Vert q_{12}q_{23}q_{31}\\rangle$")
                            modified = True
                            print(f"Matched triplet state in 3.5.md:{idx+1}")
                        for state in ["000", "100", "010", "001", "110", "011", "101", "111"]:
                            target = f"$\\|{state}\\rangle$"
                            if target in new_line:
                                new_line = new_line.replace(target, f"$\\Vert {state}\\rangle$")
                                modified = True
                                print(f"Matched state {state} in 3.5.md:{idx+1}")
                    
                    # 4. Replace other absolute value blocks in table rows (e.g. 13.1.md)
                    if "$|B(r)| \\sim r^4$" in new_line:
                        new_line = new_line.replace("$|B(r)| \\sim r^4$", "$\\vert B(r)\\vert \\sim r^4$")
                        modified = True
                        print(f"Matched |B(r)| in {file}:{idx+1}")
                    if "$|K| \\leq 2$" in new_line:
                        new_line = new_line.replace("$|K| \\leq 2$", "$\\vert K\\vert \\leq 2$")
                        modified = True
                        print(f"Matched |K| in {file}:{idx+1}")
                    
                    # 5. Remove parentheses in section references: [(§1.1.1)] -> [§1.1.1]
                    if section_ref_pattern.search(new_line):
                        new_line = section_ref_pattern.sub(r"[§\1]", new_line)
                        modified = True
                
                new_lines.append(new_line)
            
            if modified:
                # Let's write the file!
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write("\n".join(new_lines))
                print(f"Successfully updated {file}!")
                print("=" * 40)
