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
                    
                    # 2. Replace the ||psi_violation> symbol
                    if "$\\| \\psi_{violation}\\rangle$" in new_line:
                        new_line = new_line.replace("$\\| \\psi_{violation}\\rangle$", "$\\Vert \\psi_{violation}\\rangle$")
                        modified = True
                    if "$\\|\\psi_{violation}\\rangle$" in new_line:
                        new_line = new_line.replace("$\\|\\psi_{violation}\\rangle$", "$\\Vert\\psi_{violation}\\rangle$")
                        modified = True
                    
                    # 3. Replace the double-bars in Chapter 3.5 state table
                    # Wait, let's be careful about these. Let's see:
                    # 'State $\|q_{12}q_{23}q_{31}\rangle$' -> 'State $\Vert q_{12}q_{23}q_{31}\rangle$'
                    # '$\|000\rangle$' -> '$\Vert 000\rangle$'
                    # '$\|100\rangle$' -> '$\Vert 100\rangle$'
                    # '$\|010\rangle$' -> '$\Vert 010\rangle$'
                    # '$\|001\rangle$' -> '$\Vert 001\rangle$'
                    # '$\|110\rangle$' -> '$\Vert 110\rangle$'
                    # '$\|011\rangle$' -> '$\Vert 011\rangle$'
                    # '$\|101\rangle$' -> '$\Vert 101\rangle$'
                    # '$\|111\rangle$' -> '$\Vert 111\rangle$'
                    for num_str in ["q_{12}q_{23}q_{31}", "000", "100", "010", "001", "110", "011", "101", "111"]:
                        target_str = f"$\\|{num_str}\\rangle$"
                        if target_str in new_line:
                            new_line = new_line.replace(target_str, f"$\\Vert {num_str}\\rangle$")
                            modified = True
                        
                        target_str_no_space = f"$\\|{num_str}\\rangle$"
                        # Wait, let's check for spaces like '$\\| ' vs '$\\|'
                        # In the find_table_pipe_collisions output, it printed:
                        # State $\|q_{12}q_{23}q_{31}\rangle$ (one backslash, wait: state $\|q_{12}... )
                        # Let's check both ways
                    
                    # Specifically let's replace double-bar structures in 3.5.md
                    if file == "3.5.md":
                        # Let's replace the $\| with $\Vert
                        # We can use regex or straight replace
                        if "$\\|q_{12}q_{23}q_{31}\\rangle$" in new_line:
                            new_line = new_line.replace("$\\|q_{12}q_{23}q_{31}\\rangle$", "$\\Vert q_{12}q_{23}q_{31}\\rangle$")
                            modified = True
                        for state in ["000", "100", "010", "001", "110", "011", "101", "111"]:
                            if f"$\\|{state}\\rangle$" in new_line:
                                new_line = new_line.replace(f"$\\|{state}\\rangle$", f"$\\Vert {state}\\rangle$")
                                modified = True
                    
                    # 4. Replace other absolute value blocks in table rows (e.g. 13.1.md)
                    if "$|B(r)| \\sim r^4$" in new_line:
                        new_line = new_line.replace("$|B(r)| \\sim r^4$", "$\\vert B(r)\\vert \\sim r^4$")
                        modified = True
                    if "$|K| \\leq 2$" in new_line:
                        new_line = new_line.replace("$|K| \\leq 2$", "$\\vert K\\vert \\leq 2$")
                        modified = True
                    
                    # 5. Remove parentheses in section references: [(§1.1.1)] -> [§1.1.1]
                    if section_ref_pattern.search(new_line):
                        new_line = section_ref_pattern.sub(r"[§\1]", new_line)
                        modified = True
                
                if new_line != line:
                    changes.append({
                        "file": os.path.relpath(filepath, docs_dir),
                        "line": idx + 1,
                        "old": line,
                        "new": new_line
                    })
                new_lines.append(new_line)
            
            if modified:
                # We won't write yet in this dry-run script, but we will print
                pass

print(f"Total proposed changes: {len(changes)}")
for c in changes[:20]:
    print(f"File: {c['file']}:{c['line']}")
    print(f"  - {c['old']}")
    print(f"  + {c['new']}")
    print("-" * 60)
if len(changes) > 20:
    print(f"... and {len(changes) - 20} more changes.")
