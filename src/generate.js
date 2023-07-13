const fs = require('fs');

const jpCh1 = JSON.parse(fs.readFileSync(`${__dirname}/lang_ja_ch1.json`));
const enCh1 = JSON.parse(fs.readFileSync(`${__dirname}/lang_en_ch1.json`));

const merged = Object.entries(jpCh1)
  .filter(([a, _]) => a != 'date')
  .map(([key, jp]) => ({ key, jp, en: enCh1[key] }));

fs.writeFileSync(`${__dirname}/lines.json`, JSON.stringify(merged));