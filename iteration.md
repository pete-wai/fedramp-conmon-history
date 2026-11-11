# Publication record

Standalone report; no prototype parent. Nine-page PDF and static SvelteKit/mdsvex web narrative with 33 references. Source inventories, claim qualifications and retained government documents accompany the report in the repository.

Actual checks and limitations: [validation](docs/validation.md). Research coverage: [edition inventory](research/edition-inventory.md). Build output: `build/`; PDF: `static/fedramp-monitoring-history.pdf`; local rendered evidence: `output/verified-*.png` (not committed).

Preview: `mise exec -- npm run preview`, then http://127.0.0.1:4178/fedramp-conmon-history/.

Published at https://pwai.dev/fedramp-conmon-history/ from commit `cc95f2f690d086c5f57d0b1daca4efd86551d631`. GitHub Actions build and deployment succeeded: https://github.com/pete-wai/fedramp-conmon-history/actions/runs/43120830187.

Live HTTPS checks returned 200 for the report, stylesheet and PDF. Main report text matches the local static build, with no client scripts. The deployed PDF is byte-identical to the verified nine-page edition: SHA-256 `d21bc5d6dfb19221b340d60d2ca79a010ad28a0993402857718554ebc9176a0b`. The final metadata update records these checks without changing the published site. No DNS or homepage edits were required.

The final lab reference check confirmed 63,442 entries unchanged. Browser visual/interactive validation remains unavailable; PDF rendering and source-level responsive review are the completed visual checks.
