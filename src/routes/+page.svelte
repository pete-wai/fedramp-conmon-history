<script>
  import Report from '$lib/report.md';
  import sources from '$lib/sources.json';
  import { base } from '$app/paths';
  const contents = [
    ['the-finding', 'The finding'],
    ['20112014--a-broad-mandate-becomes-a-recurring-process', '2011–2014 · Foundations'],
    ['20152017--scanner-evidence-becomes-an-enforceable-specification', '2015–2017 · Specifications'],
    ['2018--more-consistency-with-some-room-for-scale-and-risk', '2018 · Consistency & exceptions'],
    ['20202021--containers-change-where-the-evidence-comes-from', '2020–2021 · Containers'],
    ['20222024--new-threats-and-interfaces-the-same-reporting-backbone', '2022–2024 · Expansion'],
    ['2025--commercial-objections-shape-successive-drafts', '2025 · Proposals & objections'],
    ['2026--vdr-and-ver-change-what-counts-as-the-unit-of-work', '2026 · VDR & VER'],
    ['what-persisted-and-what-actually-changed', 'Continuity & change'],
    ['about-the-evidence', 'About the evidence'],
    ['sources', 'Sources']
  ];
</script>

<svelte:head>
  <title>FedRAMP monitoring: from scanner evidence to VDR and VER</title>
  <meta name="description" content="An independent, sourced history of FedRAMP continuous monitoring, vulnerability scanning, remediation deadlines and POA&Ms, 2011–2026." />
  <link rel="canonical" href="https://pwai.dev/fedramp-conmon-history/" />
</svelte:head>

<a class="skip" href="#report">Skip to report</a>
<div class="page">
  <header class="masthead">
    <a href="https://pwai.dev">pwai.dev</a>
    <span>Independent research · November 11, 2026</span>
  </header>
  <div class="layout">
    <nav class="contents" aria-label="Report contents">
      <p>In this report</p>
      <ol>
        {#each contents as [id, title] (id)}
          <li><a href={'#' + id}>{title}</a></li>
        {/each}
      </ol>
      <a class="download" href={base + '/fedramp-monitoring-history.pdf'}>Download the PDF <span aria-hidden="true">↓</span></a>
      <a class="repository" href="https://github.com/pete-wai/fedramp-conmon-history">Research & source inventory ↗</a>
    </nav>
    <main id="report" tabindex="-1">
      <header class="report-header">
        <p class="eyebrow">Policy history · 2011–2026</p>
        <h1>FedRAMP monitoring:<br />from scanner evidence<br class="wide-break" /> to VDR and VER</h1>
        <p class="dek">How vulnerability scanners, remediation deadlines, and POA&Ms shaped the program, and where the approach changed.</p>
        <p class="scope">Independent analysis of published rules, guidance, drafts, and public comments. Not official FedRAMP guidance.</p>
      </header>
      <article class="prose">
        <Report />
        <section class="sources" aria-labelledby="sources">
          <h2 id="sources">Sources</h2>
          <p>Numbers in the text link here. Historical mirrors preserve government-authored documents; they are not current policy authorities. Locators refer to the cited edition.</p>
          <ol>
            {#each sources as source (source.number)}
              <li id={'source-' + source.number}>
                <p class="source-title">{source.title}</p>
                <p>{source.note}</p>
                <p class="source-links">
                  {#each source.links as link, i (link.url)}
                    <a href={link.url}>{source.links.length === 1 ? 'Read source' : link.label}</a>{i < source.links.length - 1 ? ' · ' : ''}
                  {/each}
                </p>
              </li>
            {/each}
          </ol>
        </section>
      </article>
      <footer>
        <p>Research cutoff: November 11, 2026. <a href="https://github.com/pete-wai/fedramp-conmon-history">Source files and research notes</a>.</p>
        <p><a href="#report">Back to the beginning ↑</a></p>
      </footer>
    </main>
  </div>
</div>

<style>
  :global(*) { box-sizing: border-box; }
  :global(html) { color: #172c3b; background: #fff; scroll-padding-top: 2rem; }
  :global(body) { margin: 0; font-family: Georgia, 'Times New Roman', serif; font-size: 19px; line-height: 1.7; }
  :global(a) { color: #00656b; text-decoration-thickness: 1px; text-underline-offset: .18em; overflow-wrap: anywhere; }
  :global(a:hover) { text-decoration-thickness: 2px; }
  :global(:focus-visible) { outline: 3px solid #00656b; outline-offset: 5px; }
  :global(h1), :global(h2), :global(h3) { line-height: 1.24; text-wrap: balance; }
  :global(h2) { font-size: 1.7rem; margin: 3.5rem 0 1.1rem; }
  :global(h3) { font-size: 1.28rem; margin: 2.3rem 0 .8rem; }
  :global(p) { margin: 0 0 1.15em; }
  .page { max-width: 1280px; margin: auto; padding: 0 40px; }
  .masthead { display: flex; justify-content: space-between; gap: 1rem; padding: 25px 0; border-bottom: 1px solid #d9dedb; font: 14px/1.5 system-ui, sans-serif; }
  .masthead > a { font-weight: 700; text-decoration: none; color: #172c3b; }
  .layout { display: grid; grid-template-columns: 230px minmax(0, 1fr); gap: 55px; padding-top: 55px; }
  .contents { align-self: start; position: sticky; top: 25px; font: 13px/1.5 system-ui, sans-serif; }
  .contents > p { font-weight: 650; margin-bottom: .7rem; }
  .contents ol { list-style: none; margin: 0 0 1.5rem; padding: 0; }
  .contents li { margin-bottom: .35rem; }
  .contents li a { display: block; padding: 5px 0; color: #3f515b; text-decoration: none; }
  .contents li a:hover { color: #00656b; text-decoration: underline; }
  .download, .repository { display: block; margin: 1rem 0; }
  main { max-width: 70ch; min-width: 0; }
  main:focus { outline: none; }
  .eyebrow { color: #00656b; font: 600 13px/1.4 system-ui, sans-serif; letter-spacing: .08em; text-transform: uppercase; margin-bottom: 1.2rem; }
  h1 { font-size: clamp(2.25rem, 3.9vw, 3.25rem); letter-spacing: -.035em; margin: 0 0 1.5rem; font-weight: 400; }
  .dek { font-size: 1.3rem; line-height: 1.5; max-width: 54ch; }
  .scope { font: 14px/1.6 system-ui, sans-serif; color: #4b5a60; padding: 1.2rem 0 1.7rem; border-bottom: 1px solid #d9dedb; }
  :global(.prose table) { border-collapse: collapse; width: 100%; font: 15px/1.6 system-ui, sans-serif; margin: 1.5rem 0; }
  :global(.prose th), :global(.prose td) { padding: .8rem .6rem; border-bottom: 1px solid #d9dedb; text-align: left; vertical-align: top; }
  :global(.prose th:first-child), :global(.prose td:first-child) { width: 32%; padding-left: 0; }
  :global(.prose a[href^='#source-']) { font: 12px/1 system-ui, sans-serif; vertical-align: super; white-space: nowrap; padding: 2px; }
  .sources { border-top: 1px solid #d9dedb; margin-top: 3rem; font: 14px/1.6 system-ui, sans-serif; }
  .sources ol { padding-left: 1.6rem; }
  .sources li { padding-left: .4rem; margin: 1.5rem 0; scroll-margin-top: 2rem; }
  .sources li p { margin: .3rem 0; }
  .source-title { font-weight: 650; }
  footer { font: 13px/1.6 system-ui, sans-serif; border-top: 1px solid #d9dedb; padding: 2rem 0; margin-top: 2rem; }
  .skip { position: absolute; left: 1rem; top: -100px; background: white; padding: 12px; z-index: 2; }
  .skip:focus { top: 1rem; }
  @media (max-width: 950px) {
    .page { padding: 0 24px; max-width: 820px; }
    .layout { display: block; padding-top: 28px; }
    .contents { position: static; margin-bottom: 2.5rem; }
    .contents ol { display: grid; grid-template-columns: 1fr 1fr; column-gap: 1rem; }
    .download, .repository { display: inline-block; margin: .3rem 1.5rem .3rem 0; }
    main { max-width: none; }
  }
  @media (max-width: 520px) {
    :global(body) { font-size: 18px; line-height: 1.65; }
    .page { padding: 0 20px; }
    .masthead { display: block; padding: 18px 0; }
    .masthead span { display: block; font-size: 12px; margin-top: .4rem; }
    .contents ol { display: block; }
    .contents li { margin: 0; }
    .contents li a { min-height: 32px; }
    .wide-break { display: none; }
    h1 { font-size: 2.2rem; }
    :global(h2) { font-size: 1.5rem; }
    :global(.prose table) { font-size: 13px; }
    :global(.prose td) { overflow-wrap: anywhere; }
  }
  @media print {
    @page { size: letter; margin: .7in; }
    :global(body) { font-size: 10.5pt; line-height: 1.45; color: #172c3b; }
    .page { padding: 0; max-width: none; }
    .layout { display: block; padding: 0; }
    .contents, .masthead, .skip, footer { display: none; }
    main { max-width: none; }
    h1 { font-size: 29pt; }
    .dek { font-size: 13pt; }
    .scope, .eyebrow { font-size: 9pt; }
    :global(h2) { font-size: 16pt; margin-top: 22pt; break-after: avoid; }
    :global(h3) { font-size: 12pt; break-after: avoid; }
    :global(p) { orphans: 3; widows: 3; }
    :global(a) { color: inherit; }
    :global(.prose table) { font-size: 9pt; }
    :global(tr) { break-inside: avoid; }
    .sources { font-size: 8.5pt; line-height: 1.4; }
    .sources li { margin: 10pt 0; break-inside: avoid; }
  }
</style>
