const fs = require('fs');
const path = require('path');

const mdPath = path.join(__dirname, '..', '..', 'docs', '06-appendices', 'a-references.md');
const srcJsonPath = path.join(__dirname, '..', 'data', 'references.json');
const staticJsonPath = path.join(__dirname, '..', '..', 'static', 'data', 'references.json');

if (!fs.existsSync(mdPath)) {
  console.warn(`[build-references] a-references.md not found at ${mdPath}`);
  process.exit(0);
}

const content = fs.readFileSync(mdPath, 'utf-8');
const sections = content.split(/\n---\r?\n/);

const hPat = /^###\s+\d+\.\s+\*\*(.*?)\*\*\s+\{#(A\.\d+)\}/m;
const titlePat = /^\*\*["“](.*?)["”]\*\*/m;
const pubPat = /^\s*-\s+\*(.*?)\*/m;
const linkPat = /^\s*\*\s+\*\*Link:\*\*\s+\[?(https?:\/\/[^\s\]\)]+)/m;
const overviewPat = /\*\*Overview:\*\*\s*\r?\n([\s\S]*?)(?=\r?\n\s*\*\*Relevance|$)/;
const relevancePat = /\*\*Relevance to QBD:\*\*\s*\r?\n([\s\S]*)$/;

const references = {};

for (const section of sections) {
  const mh = hPat.exec(section);
  if (!mh) continue;

  const author = mh[1].trim();
  const refId = mh[2].trim();

  const mt = titlePat.exec(section);
  const title = mt ? mt[1].trim() : '';

  const mp = pubPat.exec(section);
  const publication = mp ? mp[1].trim() : undefined;

  const ml = linkPat.exec(section);
  const url = ml ? ml[1].trim() : '';

  const mo = overviewPat.exec(section);
  const overview = mo ? mo[1].replace(/\s+/g, ' ').trim() : '';

  const mr = relevancePat.exec(section);
  const relevance = mr ? mr[1].replace(/\s+/g, ' ').trim() : '';

  references[refId] = {
    author,
    title,
    ...(publication ? { publication } : {}),
    url,
    overview,
    relevance,
  };
}

const count = Object.keys(references).length;
if (count > 0) {
  const jsonContent = JSON.stringify(references, null, 2);
  fs.writeFileSync(srcJsonPath, jsonContent, 'utf-8');
  if (fs.existsSync(path.dirname(staticJsonPath))) {
    fs.writeFileSync(staticJsonPath, jsonContent, 'utf-8');
  }
  console.log(`[build-references] Compiled references.json (${count} entries: A.1 - A.${count})`);
} else {
  console.error('[build-references] Error: Parsed 0 references from a-references.md');
  process.exit(1);
}
