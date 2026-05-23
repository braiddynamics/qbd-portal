import os
import re

docs_root = r"c:\braid-dynamics\qbd-portal\docs"
stage_root = os.path.join(docs_root, "03-stage")

chapters_info = {
    "11-differential-geometry.md": {
        "dir": "11-discrete",
        "num": 11,
        "title": "Chapter 11: Differential Geometry (Discrete)",
        "num_sections": 4
    },
    "12-discrete-field-equations.md": {
        "dir": "12-einstein",
        "num": 12,
        "title": "Chapter 12: Field Equations (Einstein)",
        "num_sections": 4
    },
    "13-continuum-limit.md": {
        "dir": "13-convergence",
        "num": 13,
        "title": "Chapter 13: Continuum Limit",
        "num_sections": 4
    },
    "14-lorentzian-reality.md": {
        "dir": "14-time",
        "num": 14,
        "title": "Chapter 14: The Lorentzian Reality (Time & QFT)",
        "num_sections": 6
    },
    "15a.md": {
        "dir": "15-epr",
        "num": 15,
        "title": "Chapter 15: EPR Duality (ER=EPR)",
        "num_sections": 5
    },
    "16a.md": {
        "dir": "16-holography",
        "num": 16,
        "title": "Chapter 16: The Holographic Principle",
        "num_sections": 3
    },
    "17.md": {
        "dir": "17-worldsheets",
        "num": 17,
        "title": "Chapter 17: The String Limit (Worldsheets)",
        "num_sections": 5
    }
}

def strip_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].lstrip()
    return text

def extract_section_name(heading_text):
    # Remove ## X.Y or ## X.A or ## X.? or ## X.Ω at start
    text = re.sub(r'^##\s+\d+\.(?:\d+|A|\?|Ω)\s*', '', heading_text)
    # Remove Section: prefix if any
    text = re.sub(r'^Section:\s*', '', text)
    # Remove Theorem: prefix if any
    text = re.sub(r'^Theorem:\s*', '', text)
    # Remove any trailing anchor like {#...}
    text = re.sub(r'\{#.*\}$', '', text)
    return text.strip()

def split_drafts():
    for filename, info in chapters_info.items():
        filepath = os.path.join(stage_root, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filename}")
            continue
            
        print(f"\nProcessing {filename} -> {info['dir']}")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Clean up carriage returns to simplify regex matching
        content = content.replace("\r\n", "\n")
        content = strip_frontmatter(content)
        
        # Regex to match chapter section headers
        # Matches e.g. "## 11.1 Causal Curvature" or "## 11.Ω ..." at start of line
        header_pat = re.compile(rf"^## {info['num']}\.(?:[0-9]+|A|\?|Ω).*", re.MULTILINE)
        
        matches = list(header_pat.finditer(content))
        print(f"Found {len(matches)} section headers in {filename}")
        
        # Partition content into chunks
        chunks = []
        last_idx = 0
        for m in matches:
            chunks.append(content[last_idx:m.start()])
            last_idx = m.start()
        chunks.append(content[last_idx:])
        
        # Map chunks to target files
        # target_files[i] collects all chunks that belong to file i (1-indexed)
        num_sections = info["num_sections"]
        target_files = {i: [] for i in range(1, num_sections + 1)}
        
        # Chunk 0 goes to the first file
        target_files[1].append(chunks[0])
        
        # For chunk c > 0, it represents the section starting with match c-1
        for c in range(1, len(chunks)):
            match_header = matches[c-1].group(0)
            
            # Determine target file index based on header number
            # E.g. "## 11.1" -> file 1, "## 11.A" -> file 1, "## 11.2" -> file 2
            # "## 11.Ω" or "## 11.?" (the last match) -> file num_sections
            if "Ω" in match_header or "?" in match_header:
                file_idx = num_sections
            else:
                m_num = re.search(rf"^## {info['num']}\.([0-9]+|A)", match_header)
                if m_num:
                    num_part = m_num.group(1)
                    if num_part == "A":
                        file_idx = 1
                    else:
                        file_idx = int(num_part)
                else:
                    file_idx = 1
                    
            if file_idx > num_sections:
                file_idx = num_sections
            target_files[file_idx].append(chunks[c])
            
        # Extract section names to use as sidebar labels
        section_labels = {}
        for c in range(1, len(chunks)):
            match_header = matches[c-1].group(0)
            sec_name = extract_section_name(match_header)
            
            # Find which file index this match belongs to
            if "Ω" in match_header or "?" in match_header:
                file_idx = num_sections
            else:
                m_num = re.search(rf"^## {info['num']}\.([0-9]+|A)", match_header)
                if m_num:
                    num_part = m_num.group(1)
                    file_idx = 1 if num_part == "A" else int(num_part)
                else:
                    file_idx = 1
                    
            if file_idx > num_sections:
                file_idx = num_sections
                
            # If there's an 'A' section, keep the actual numbered section label (.1) for the sidebar
            if "A" in match_header:
                continue
            section_labels[file_idx] = sec_name
            
        # Write separate markdown files
        chapter_dir = os.path.join(stage_root, info["dir"])
        os.makedirs(chapter_dir, exist_ok=True)
        
        for file_idx in range(1, num_sections + 1):
            file_chunks = target_files[file_idx]
            file_content = "".join(file_chunks).strip()
            
            # If this is the synthesis section, perform final header normalization
            if file_idx == num_sections:
                # Rename the synthesis header to standard numbered header
                file_content = re.sub(
                    rf"## {info['num']}\.(?:\?|Ω) Formal Synthesis \{{#{info['num']}\.(?:\?|Ω)\}}",
                    f"## {info['num']}.{file_idx} Formal Synthesis {{#{info['num']}.{file_idx}}}",
                    file_content
                )
                section_labels[file_idx] = "Formal Synthesis"
                
            sec_name = section_labels.get(file_idx, "Overview")
            
            # Generate frontmatter
            if file_idx == 1:
                frontmatter = f"""---
title: " "
sidebar_label: "{info['num']}.1 - {sec_name}"
---

"""
            else:
                frontmatter = f"""---
title: "{info['title']}"
sidebar_label: "{info['num']}.{file_idx} - {sec_name}"
---

"""
            
            target_path = os.path.join(chapter_dir, f"{info['num']}.{file_idx}.md")
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(frontmatter + file_content + "\n")
            print(f"  Created: {target_path} ({len(frontmatter + file_content)} bytes)")

if __name__ == "__main__":
    split_drafts()
