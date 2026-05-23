import os
import re

docs_dir = r"c:\braid-dynamics\qbd-portal\docs"

# Pattern to find headers
header_pat = re.compile(
    r"^###\s+([0-9]+\.[0-9]+\.([0-9]+|[a-zA-Z]+))\s+(Lemma|Theorem|Postulate|Definition|Axiom):\s*(.+?)(?:\s*{|$)",
    re.IGNORECASE
)

# Noun patterns to search for in text
noun_pat = re.compile(
    r"\b(this|the)\s+(lemma|theorem|postulate|definition|axiom)\b",
    re.IGNORECASE
)

def clean_title(title):
    # Remove any math symbols in parentheses like (\Lambda) or (J_{auto})
    title = re.sub(r"\s*\([^)]*\\(?:Lambda|beta|kappa|mu|psi|omega|omega_W|phi|psi_violation|Psi|Omega|chi|E_bridge|J_auto|P_acc|J_out|Lambda|theta_W)[^)]*\)", "", title)
    title = re.sub(r"\s*\(\s*\$[^\$]+\$\s*\)", "", title)
    title = title.strip()
    return title.lower()

def get_url_path(rel_path, num):
    # E.g. 01-rules\01-ontology\1.1.md -> /monograph/rules/ontology/1.1/#1.1
    # First, split path
    parts = rel_path.replace("\\", "/").split("/")
    new_parts = []
    for p in parts[:-1]:
        # Strip digits prefix like "01-"
        p_clean = re.sub(r"^[0-9]+-", "", p)
        new_parts.append(p_clean)
    
    # Strip .md from filename
    filename = parts[-1].replace(".md", "")
    new_parts.append(filename)
    
    # Join parts
    path = "/monograph/" + "/".join(new_parts)
    return f"{path}/#{num}"

proposed_changes = []

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, docs_dir)
            
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            lines = content.split("\n")
            headers = []
            
            # 1. Collect all three-level headers in this file
            for idx, line in enumerate(lines):
                stripped = line.strip()
                m = header_pat.match(stripped)
                if m:
                    headers.append({
                        "line_idx": idx,
                        "num": m.group(1),
                        "type": m.group(3).lower(),
                        "title": clean_title(m.group(4))
                    })
            
            # If no headers in file, skip
            if not headers:
                continue
            
            # 2. Iterate through lines and find noun pattern matches
            new_lines = list(lines)
            modified = False
            
            for idx, line in enumerate(lines):
                stripped = line.strip()
                # Skip headers themselves when looking for noun usage
                if stripped.startswith("#"):
                    continue
                
                # Check for "this lemma" / "this theorem" / etc.
                matches = list(noun_pat.finditer(line))
                if not matches:
                    continue
                
                # Find nearest preceding header
                # A header is preceding if its line_idx < idx
                preceding_header = None
                for h in headers:
                    if h["line_idx"] < idx:
                        preceding_header = h
                    else:
                        break
                
                if not preceding_header:
                    continue
                
                # We want to perform replacements on matches that align with the active header type
                new_line = line
                for m in matches:
                    matched_noun = m.group(2).lower()
                    matched_prefix = m.group(1).lower() # "this" or "the"
                    
                    # We match if the noun is exactly the same as the header type
                    # or if we are inside a proof/commentary block for it
                    if matched_noun == preceding_header["type"]:
                        # Form the replacement
                        # We want it to be: "the **{title} {type}** [(§{num})]({url})"
                        # E.g. "the **existence and finiteness lemma** [(§3.1.4)](/path/#3.1.4)"
                        url = get_url_path(rel_path, preceding_header["num"])
                        ref_text = f"the **{preceding_header['title']} {preceding_header['type']}** [({preceding_header['num']})]({url})"
                        # Wait, let's keep the § sign in link text! E.g. [(§3.1.4)]
                        ref_text = f"the **{preceding_header['title']} {preceding_header['type']}** [(§{preceding_header['num']})]({url})"
                        
                        # Replace in new_line
                        # E.g. "This lemma anchors" -> "The **existence and finiteness lemma** ... anchors"
                        # E.g. "this lemma" -> "the **existence and finiteness lemma** ..."
                        # Let's match the capitalization of the matched prefix
                        if m.group(1)[0].isupper():
                            # Capitalize first letter of replacement
                            ref_text_capped = ref_text[0].upper() + ref_text[1:]
                            new_line = new_line.replace(m.group(0), ref_text_capped, 1)
                        else:
                            new_line = new_line.replace(m.group(0), ref_text, 1)
                        
                        modified = True
                
                if new_line != line:
                    proposed_changes.append({
                        "file": rel_path,
                        "line": idx + 1,
                        "old": line,
                        "new": new_line
                    })
                    new_lines[idx] = new_line
            
            if modified:
                # We will write the file here!
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write("\n".join(new_lines))
                print(f"Successfully refactored {file}!")

print("=" * 40)
print(f"Total files updated: {len(set(c['file'] for c in proposed_changes))}")
print(f"Total replacements applied: {len(proposed_changes)}")
