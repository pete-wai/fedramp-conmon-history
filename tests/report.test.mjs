import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
const html = readFileSync('build/index.html', 'utf8');
const sources = JSON.parse(readFileSync('src/lib/sources.json', 'utf8'));
test('all contents and citation anchors resolve uniquely', () => {
  const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map(m => m[1]);
  assert.equal(ids.length, new Set(ids).size);
  for (const m of html.matchAll(/href="#([^"]+)"/g)) assert(ids.includes(m[1]), m[1]);
  for (const s of sources) assert(html.includes(`href="#source-${s.number}"`));
});
test('static report reads without scripts and contains every timeline section', () => {
  assert(!/<script\b/i.test(html));
  assert.equal((html.match(/<h1\b/g) || []).length, 1);
  for (const text of ['2011–2014', '2015–2017', '2020–2021', '2022–2024', '2025', '2026', 'About the evidence']) assert(html.includes(text));
  assert(html.includes('lang="en"'));
  assert(html.includes('aria-label="Report contents"'));
});
test('deployed asset links exist under the project base', () => {
  for (const m of html.matchAll(/(?:href|src)="([^"#]+)"/g)) {
    if (/^https?:/.test(m[1])) continue;
    const path=m[1].replace(/^\/fedramp-conmon-history\//,'').replace(/^\.\//,'');
    assert(existsSync('build/'+path), path);
  }
});
test('sources have explicit provenance and secure URLs', () => {
  assert.equal(sources.length,33);
  for (const s of sources) { assert(s.note.length>30); assert(s.links.length); for(const l of s.links) assert(l.url.startsWith('https://')); }
});
