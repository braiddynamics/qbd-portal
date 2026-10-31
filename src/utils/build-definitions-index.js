const fs = require('fs');
const path = require('path');

const srcPath = path.join(__dirname, '..', 'data', 'definitions.json');
const destPath = path.join(__dirname, '..', 'data', 'definitions-index.json');

if (fs.existsSync(srcPath)) {
  const data = JSON.parse(fs.readFileSync(srcPath, 'utf-8'));
  const index = {};
  for (const [k, v] of Object.entries(data)) {
    index[k] = {
      id: v.id || k,
      type: v.type || '',
      title: v.title || '',
      file: v.file || '',
    };
  }
  fs.writeFileSync(destPath, JSON.stringify(index));
  console.log(`[prebuild] Generated definitions-index.json (${Object.keys(index).length} entries)`);
}
