import os
import re
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
docs_root = os.path.join(PROJECT_ROOT, "docs")
id_map_path = os.path.join(SCRIPT_DIR, "id_map.json")

with open(id_map_path, "r", encoding="utf-8") as f:
    id_map = json.load(f)

# Helper to build canonical Docusaurus URL from relpath
def get_canonical_url(relpath, anchor=None):
    # E.g. '01-rules/02-axioms/2.4.md' -> ['01-rules', '02-axioms', '2.4.md']
    parts = relpath.replace("\\", "/").split("/")
    cleaned_parts = []
    for part in parts[:-1]:
        # Strip leading digits and hyphen, e.g. '01-rules' -> 'rules'
        cleaned = re.sub(r'^\d+-', '', part)
        cleaned_parts.append(cleaned)
    # Strip .md from filename, e.g. '2.4.md' -> '2.4'
    file_part = re.sub(r'\.md$', '', parts[-1])
    cleaned_parts.append(file_part)
    
    url = "/monograph/" + "/".join(cleaned_parts) + "/"
    if anchor:
        url += f"#{anchor}"
    return url

# Special mapping for non-standard anchors
special_anchors = {
    "H5": "3.3"
}

# Mapping of chapter numbers to their Docusaurus URL segments
chap_url_parts = {
    1: "rules/ontology",
    2: "rules/axioms",
    3: "rules/architecture",
    4: "rules/dynamics",
    5: "rules/equilibrium",
    6: "players/fermions",
    7: "players/topology",
    8: "players/braids",
    9: "players/unification",
    10: "players/computation",
    11: "stage/discrete",
    12: "stage/einstein",
    13: "stage/convergence",
    14: "stage/time",
    15: "stage/epr",
    16: "stage/holography",
    17: "stage/worldsheets"
}

def resolve_link(url):
    # Check if there is an anchor
    anchor = None
    url_base = url
    if "#" in url:
        parts = url.split("#", 1)
        url_base = parts[0]
        anchor = parts[1]
        
    if anchor in special_anchors:
        anchor = special_anchors[anchor]
        
    if anchor:
        # Check if the anchor is a key in id_map
        if anchor in id_map:
            entry = id_map[anchor]
            return get_canonical_url(entry["file"], anchor)
            
        # Try finding if the anchor is a substring or close match in keys
        clean_anchor = anchor.strip()
        if clean_anchor in id_map:
            entry = id_map[clean_anchor]
            return get_canonical_url(entry["file"], clean_anchor)
            
        # Fallback for standard section anchors (e.g., "12.3" or "14.2")
        m_sec = re.match(r'^(\d+)\.(\d+)$', clean_anchor)
        if m_sec:
            chap = int(m_sec.group(1))
            sec = int(m_sec.group(2))
            if chap in chap_url_parts:
                return f"/monograph/{chap_url_parts[chap]}/{chap}.{sec}/#{chap}.{sec}"
            
    # If no anchor but looks like chapterX, we can try to find X.1
    m_chap = re.match(r'^chapter(\d+)$', url_base.lower())
    if m_chap:
        chap_num = m_chap.group(1)
        first_sec = f"{chap_num}.1"
        if first_sec in id_map:
            entry = id_map[first_sec]
            return get_canonical_url(entry["file"], anchor)
            
    return None

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Find all markdown links [text](url)
    link_pat = re.compile(r'\[([^\]]*?)\]\(([^)]+?)\)')
    
    def replacer(match):
        text = match.group(1)
        url = match.group(2)
        
        # Don't modify external links
        if url.startswith("http://") or url.startswith("https://") or url.startswith("mailto:"):
            return match.group(0)
            
        resolved = resolve_link(url)
        if resolved:
            # print(f"Resolved: {url} -> {resolved}")
            return f"[{text}]({resolved})"
            
        return match.group(0)
        
    new_content, count = link_pat.subn(replacer, content)
    if count > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed {count} links in {os.path.relpath(filepath, docs_root)}")

for root, dirs, files in os.walk(docs_root):
    for file in files:
        if file.endswith(".md"):
            process_file(os.path.join(root, file))
