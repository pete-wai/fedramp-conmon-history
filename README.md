# FedRAMP monitoring history

Independent report on FedRAMP continuous monitoring, vulnerability scanning, deadlines and POA&Ms, from 2011 through the VDR/VER transition. Research cutoff: November 11, 2026.

- [Read the report](https://pwai.dev/fedramp-conmon-history/)
- [Download the nine-page PDF](https://pwai.dev/fedramp-conmon-history/fedramp-monitoring-history.pdf)
- [Edition inventory and gaps](research/edition-inventory.md)
- [Claim review](research/claim-notes.md)
- [Source provenance and hashes](research/source-inventory.json)
- [Retained government documents](research/primary/)

This is not official FedRAMP guidance. Public comments are testimony, drafts are proposals, and historical editions do not establish current requirements. The report does not claim every historical edition was recovered. Google access was attempted but blocked; see the inventory for retrieval limits.

## Development

Node 24.21.0 and npm 11.19.0 are pinned. Use mise; Python 3.14.7 and project dependencies use uv and the committed lockfile.

```sh
mise install
mise exec -- npm ci
mise exec -- npm run check
mise exec -- npm run build
mise exec -- npm test
uv run --locked python scripts/verify.py
mise exec -- npm run preview
```

Preview: http://127.0.0.1:4178/fedramp-conmon-history/

The report is authored in `src/lib/report.md`; its bibliography is `src/lib/sources.json`. SvelteKit/mdsvex prerenders the page with client-side JavaScript disabled. No analytics, external fonts or third-party embeds are included. Research files are retained in GitHub, outside the built site.

To regenerate the PDF after editing, first build with the existing PDF present, run `uv run --locked python scripts/pdf.py`, then build again to copy the updated PDF. The PDF generator uses the prerendered HTML, including the full bibliography. `scripts/verify.py` checks that the PDF contains the complete narrative, table and references and remains at most 15 pages. Browser print pagination may vary; the downloadable PDF is the measured edition.

GitHub Actions publishes the `build` directory to Pages. The project has no CNAME or DNS change: it inherits the owner's pwai.dev Pages domain. Existing projects are not replaced.

## Evidence preservation

Government-authored historical documents are retained in `research/primary`, including third-party and Internet Archive preservation copies, with exact SHA-256 provenance. Public discussion comments are linked and summarized, not republished. Local discovery files and extracted text are ignored. `scripts/collect.py` can capture a JSON list of `{id, url}` records; archival availability is not guaranteed.
