#!/usr/bin/env python3
"""catalog.yaml -> site/index.html

one generator, one output. catalog.yaml stays the single source of truth:
edit the catalog, run `python3 tools/build.py`, commit both.
no framework, no client build step — the shelf stays a flat static page
that any agent (or human) can read straight off disk.
"""
import html
import json
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "index.html"  # served by github pages from /docs

STATUSES = ["breathing", "quiet", "orphaned", "archived", "moved", "vanished"]
CATEGORY_ORDER = [
    "text-to-image", "local-inference", "fine-tuning", "chat-agents",
    "speech", "datasets", "nlp-classics", "fork-wing", "saved-from-the-fire",
]
CATEGORY_TITLES = {
    "text-to-image": "text-to-image",
    "local-inference": "local llm inference",
    "fine-tuning": "fine-tuning & training",
    "chat-agents": "chat & agents",
    "speech": "speech",
    "datasets": "datasets",
    "nlp-classics": "nlp classics",
    "fork-wing": "the fork wing",
    "saved-from-the-fire": "saved from the fire",
}
BREATHING_WINDOW_DAYS = 180  # ~6 months, matches the status lexicon test

with open(ROOT / "catalog.yaml") as f:
    CATALOG = yaml.safe_load(f)

# ---- guards: the catalog is load-bearing, fail loudly at build time ----
assert isinstance(CATALOG, list), "catalog.yaml must be a list of records"
assert len(CATALOG) == 271, f"expected 268 records, got {len(CATALOG)}"
for rec in CATALOG:
    name = rec.get("name", "??")
    for field in ("name", "category", "status", "human_one_liner", "why_saved"):
        assert rec.get(field), f"{name}: missing {field}"
    assert rec["status"] in STATUSES, f"{name}: status '{rec['status']}' outside the closed enum"
    if rec.get("copy_shelf"):
        assert rec["copy_shelf"] in CATEGORY_ORDER, \
            f"{name}: copy_shelf '{rec['copy_shelf']}' is not a shelf"


def esc(s):
    return html.escape(str(s), quote=True)


def gh_slug(rec):
    if not rec.get("repo"):
        return None
    parts = urlparse(rec["repo"]).path.strip("/").split("/")
    return "/".join(parts[-2:]) if len(parts) >= 2 else rec["repo"]


def fmt_stars(n):
    if n < 1000:
        return str(n)
    s = f"{n / 1000:.1f}"
    return (s[:-2] if s.endswith(".0") else s) + "k"


def fmt_date(iso):
    """2026-10-09... -> oct 09 2026"""
    try:
        d = date(*[int(x) for x in str(iso)[:10].split("-")])
    except (ValueError, TypeError):
        return str(iso)
    return f"{d.strftime('%b').lower()} {d.day:02d} {d.year}"


def push_recent(rec):
    """within the breathing window of the record's own verification date?"""
    try:
        push = date(*[int(x) for x in str(rec["last_push"])[:10].split("-")])
        v = date(*[int(x) for x in str(rec.get("verified", "2026-10-09"))[:10].split("-")])
        return (v - push).days <= BREATHING_WINDOW_DAYS
    except (ValueError, TypeError, KeyError):
        return False


# ---- entry row ----
def render_entry(rec, idx, in_memorial_shelf=False):
    status = rec["status"]
    name = rec["name"]
    stars = fmt_stars(rec["stars"]) if rec.get("stars") else None
    pushed = fmt_date(rec["last_push"]) if rec.get("last_push") else None
    url = rec.get("repo")
    dead_url = rec.get("dead_url")

    classes = ["entry", "reveal"]
    title_html = esc(name)
    if status == "vanished" and not url:
        classes.append("was404")

    # status cell (right rail)
    bits = [f'<span class="status-chip"><span class="s-dot dot-{status}"></span>'
            f'<span class="s-word">{status}</span></span>']
    if stars:
        bits.append(f'<span class="stars">{stars} stars</span>')
    if pushed and status != "vanished":
        if push_recent(rec):
            bits.append(f'<span class="pushed hot">pushed {pushed}</span>')
        else:
            bits.append(f'<span class="pushed">last push {pushed}</span>')
    if rec.get("canonical_old"):
        bits.append(f'<span class="movednote">was {esc(gh_slug({"repo": rec["canonical_old"]}))}</span>')
    if rec.get("successor"):
        bits.append(f'<span class="successor">successor: {esc(gh_slug({"repo": rec["successor"]}))}</span>')
    if rec.get("held_fork"):
        bits.append(f'<span class="heldfork">copy held: {esc(gh_slug({"repo": "https://github.com/" + rec["held_fork"]}))}</span>')
    if dead_url:
        bits.append(f'<span class="dead">{esc(gh_slug({"repo": dead_url}))} — 404</span>')
    if rec.get("note") and status == "vanished":
        pass  # note lives in the memorial prose, not the rail
    meta = "\n      ".join(bits)

    # title link: dead entries don't get a live link
    if url:
        title_html = f'<a href="{esc(url)}" rel="noopener">{esc(name)}</a>'

    note = f'\n    <p class="note">{esc(rec["note"])}</p>' if rec.get("note") else ""

    return f"""    <article class="{' '.join(classes)}" data-status="{status}" id="{esc(slug_id(name))}">
      <span class="spine">{idx:02d}</span>
      <div class="body">
        <h3>{title_html}</h3>
        <p class="oneliner">{esc(rec["human_one_liner"])}</p>
        <p class="why">{esc(rec["why_saved"])}</p>{note}
      </div>
      <div class="meta">
      {meta}
      </div>
    </article>
"""


def slug_id(name):
    s = name.lower()
    out = []
    for ch in s:
        if ch.isalnum():
            out.append(ch)
        elif ch in " -.":
            out.append("-")
    return "".join(out).strip("-").replace("--", "-")


def status_counts():
    counts = {s: 0 for s in STATUSES}
    for rec in CATALOG:
        counts[rec["status"]] += 1
    return counts


def render_legend():
    defs = {
        "breathing": ("active, maintainer awake", "pushed within ~6 months, not archived"),
        "quiet": ("works, nobody's home", "no pushes ~12+ months, not archived, no successor"),
        "orphaned": ("team gone, code remains", "silent 12+ months after the org wound down"),
        "archived": ("locked read-only on purpose", "github archived: true"),
        "moved": ("alive at a new address", "api full_name changed; old link redirects"),
        "vanished": ("gone from its address", "http 404 or takedown; mirrors only"),
    }
    rows = []
    for s in STATUSES:
        d, t = defs[s]
        n = status_counts()[s]
        rows.append(
            f'      <div class="legend-row">\n'
            f'        <span class="s-word"><span class="s-dot dot-{s}"></span>{s}</span>\n'
            f'        <span class="def">{d}</span>\n'
            f'        <span class="test mono">{t} · {n} on the shelf</span>\n'
            f'      </div>'
        )
    return "\n".join(rows)


def render_filters():
    chips = [f'<button class="chip" data-filter="all" aria-pressed="true">all <span class="count">{len(CATALOG)}</span></button>']
    for s in STATUSES:
        chips.append(
            f'<button class="chip" data-filter="{s}" aria-pressed="false">'
            f'<span class="s-dot dot-{s}"></span>{s} <span class="count">{status_counts()[s]}</span></button>'
        )
    shelfnav = "".join(
        f'<a href="#shelf-{c}">{CATEGORY_TITLES[c].split(" ")[0]}</a>' for c in CATEGORY_ORDER
    )
    return (f'<div class="flabel">show</div>' + "".join(chips)
            + f'<nav class="shelfnav" aria-label="jump to shelf">{shelfnav}</nav>')


def render_shelves():
    """tool shelves (everything except the memorial category)"""
    out = []
    idx = 0
    for cat in CATEGORY_ORDER:
        recs = [r for r in CATALOG if r["category"] == cat]
        if not recs or cat == "saved-from-the-fire":
            continue
        # fork wing: pilot records carry real stories -> cards; the sweep
        # (template "upstream ..." prose) collapses into the copy ledger below
        stories, copies = recs, []
        if cat == "fork-wing":
            stories = [r for r in recs if not r["why_saved"].startswith("upstream ")]
            copies = [r for r in recs if r["why_saved"].startswith("upstream ")]
        rows = []
        for r in stories:
            idx += 1
            rows.append(render_entry(r, idx))
        nid = f"shelf-{cat}"
        ledger = render_copy_ledger(copies) if copies else ""
        # the shelf collapses under its head: summary labels the fold,
        # the range carries story/ledger counts so closed still informs
        fold_bits = [f"{len(stories)} stories"]
        if copies:
            fold_bits.append(f"ledger of {len(copies)} copies")
        body = "".join(rows) + ledger
        out.append(f"""  <section class="shelf" id="{nid}" data-shelf="{cat}">
    <div class="section-inner">
      <div class="shelf-head reveal">
        <h2>{esc(CATEGORY_TITLES[cat])}</h2>
        <span class="range">{len(recs)} entries</span>
      </div>
      <details class="shelf-fold reveal">
        <summary><span class="chev">\u25b8</span>walk this shelf<span class="range">{" \u00b7 ".join(fold_bits)}</span></summary>
{body}      </details>
    </div>
  </section>""")
    return "\n".join(out)


def render_copy_ledger(recs):
    """one-line ledger of held copies; the at-risk come first, the insurance
    majority lives inside a collapsed <details> so the shelf stays a shelf"""
    if not recs:
        return ""
    rank = {"orphaned": 0, "archived": 1, "quiet": 2, "moved": 3, "vanished": 4}

    def ordered(members):
        """at-risk rows lead inside each group, insurance follows by name"""
        risk = sorted(
            (r for r in members if rank.get(r["status"], 9) < 9),
            key=lambda r: (rank[r["status"]], r.get("last_push") or ""))
        safe = sorted(
            (r for r in members if rank.get(r["status"], 9) >= 9),
            key=lambda r: r["name"].lower())
        return risk, safe

    def row(r):
        stars = fmt_stars(r["stars"]) if r.get("stars") else "\u2014"
        return (f'      <div class="copy-row" data-status="{r["status"]}">\n'
                f'        <span class="s-dot dot-{r["status"]}"></span>\n'
                f'        <span class="cname"><a href="{esc(r["repo"])}" rel="noopener">{esc(r["name"])}</a>'
                f' <span class="cdesc">{esc(r["human_one_liner"])}</span></span>\n'
                f'        <span class="cstars">{stars}</span>\n'
                f'        <span class="cheld"><a href="https://github.com/{esc(r["held_fork"])}"'
                f' rel="noopener">copy held</a></span>\n'
                f'      </div>\n')

    # one dropdown per shelf the copies belong to. copy_shelf, when a curator
    # sets it, moves a copy between groups without touching its category
    # (category still decides which shelf section it lives under)
    def shelf_of(r):
        return r.get("copy_shelf") or r["category"]

    groups = []
    for cat in CATEGORY_ORDER:
        members = [r for r in recs if shelf_of(r) == cat]
        if not members:
            continue
        at_risk, insured = ordered(members)
        n_risk = len(at_risk)
        n = len(members)
        count = f"{n} cop{'y' if n == 1 else 'ies'}"
        if n_risk:
            count += f" \u00b7 <span class=\"catrisk\">{n_risk} at risk</span>"
        body = "".join(row(r) for r in at_risk + insured)
        groups.append(f"""    <details class="copy-cat">
      <summary><span class="chev">\u25b8</span>{esc(CATEGORY_TITLES[cat])}<span class="range">{count}</span></summary>
      <div class="copy-rows">
{body}      </div>
    </details>""")
    n_risk_all = sum(1 for r in recs if rank.get(r["status"], 9) < 9)
    return f"""  <details class="copy-ledger reveal">
    <summary><span class="chev">\u25b8</span>the ledger of copies<span class="range">{len(recs)} copies \u00b7 {n_risk_all} at risk \u00b7 grouped by shelf</span></summary>
    <p class="ledger-note">every upstream the sweep verified on 2026-10-09, held as a fork in this
    account, grouped by the shelf it belongs to \u2014 receipts in <a href="https://github.com/data-path-9/data-path-9/blob/main/catalog.yaml"><code>catalog.yaml</code></a>.
    insurance is bought while the house is standing, so most upstreams here are still breathing.
    at-risk copies lead inside each shelf; the stories on this shelf carry their own copies on the card.</p>
    <div class="copy-groups">
{"".join(groups)}    </div>
  </details>
"""


def dpx_example():
    rec = next(r for r in CATALOG if r["name"] == "coqui-tts")
    lines = [
        ("- name:", rec["name"], ""),
        ("  status:", rec["status"], "hot"),
        ("  repo:", gh_slug(rec), ""),
        ("  last_push:", rec["last_push"], ""),
        ("  stars:", rec["stars"], ""),
        ("  successor:", gh_slug({"repo": rec["successor"]}), "hot"),
        ("  verified:", rec["verified"], ""),
    ]
    return "\n".join(f'<span class="k">{k}</span><span class="{c}">{esc(v)}</span>' for k, v, c in lines)


def build():
    counts = status_counts()
    breathing = counts["breathing"]
    total = len(CATALOG)

    # verify date: newest verified stamp across records (single curator pass)
    verified = max(str(r.get("verified", "2026-10-09"))[:10] for r in CATALOG)
    v = date(*[int(x) for x in verified.split("-")])
    verified_fmt = f"{v.strftime('%B')} {v.day}, {v.year}"

    legend = render_legend()
    filters = render_filters()
    shelves = render_shelves()
    dpx = dpx_example()

    html_out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>data-path-9 — a library for the tools the fire wants</title>
<meta name="description" content="an open shelf for the ai tools the industry abandoned, absorbed, or let vanish. {total} entries, every status verified against the live github api.">
<meta property="og:title" content="data-path-9 — the deep-water library">
<meta property="og:description" content="we save the tools. all of them. even the ones the industry walked past.">
<meta name="theme-color" content="#0b0e13">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="assets/fonts/fraunces-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/jetbrains-mono-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<script>document.documentElement.classList.add("js");</script>
<a class="skip-link" href="#shelf-start">skip to the shelves</a>

<header class="topbar" id="topbar">
  <a class="mark" href="#top">data-path-9</a>
  <nav aria-label="site">
    <a href="#thesis">why</a>
    <a href="#shelf-start">shelves</a>
    <a href="#agents">for agents</a>
    <a href="https://github.com/data-path-9/data-path-9" rel="noopener">github</a>
  </nav>
</header>

<main id="top">
  <!-- ================= hero: the deep water ================= -->
  <section class="hero">
    <div class="hero-media">
      <img src="assets/dp9-1600.jpg" alt="" fetchpriority="high">
    </div>
    <div class="hero-inner">
      <p class="eyebrow">the library of alexandria, for the age of machines</p>
      <h1>
        <span class="line"><span>we save</span></span>
        <span class="line"><span>the tools<em>.</em></span></span>
      </h1>
      <p class="hero-sub">all of them. even the ones the industry walked past.
      companies get bought, labs pivot, maintainers burn out, links die.
      <strong>a tool that has a copy is a tool that survives.</strong></p>
      <div class="hero-actions">
        <a class="btn solid" href="#shelf-start">walk the shelves</a>
        <a class="btn" href="https://github.com/data-path-9/data-path-9" rel="noopener">the repo is the library</a>
      </div>
      <p class="hero-foot">
        <span>{total} entries</span>
        <span>{breathing} still breathing</span>
        <span>every status verified {verified_fmt}</span>
      </p>
    </div>
  </section>

  <!-- ================= thesis ================= -->
  <section class="section" id="thesis">
    <div class="section-inner">
      <div class="thesis-grid">
        <div class="reveal">
          <p class="eyebrow">why a new library of alexandria</p>
          <p class="thesis-lede">the original library didn't burn in one night.
          it faded — underfunded, unloved, scattered into copies of copies until
          the originals were gone. open-source ai is fading that same way,
          <em>quietly</em>, right now.</p>
        </div>
        <div class="thesis-side reveal">
          <p>we watched coqui die in december 2023 — servers off, farewell posted —
          and its toolkit survived only because a fork already existed.</p>
          <p class="pull">that's the whole thesis. not panic. just copies,
          kept where anyone can find them.</p>
        </div>
      </div>

      <div class="ledger reveal">
        <div class="cell"><div class="num">{total}</div><div class="lbl">entries on the shelf</div></div>
        <div class="cell"><div class="num lamp">{breathing}</div><div class="lbl">still breathing</div></div>
        <div class="cell"><div class="num">{counts['moved'] + counts['vanished']}</div><div class="lbl">changed hands or address</div></div>
        <div class="cell"><div class="num">{counts['quiet'] + counts['orphaned'] + counts['archived']}</div><div class="lbl">the workshop went still</div></div>
      </div>

      <div class="fires-wrap reveal">
        <p class="eyebrow" style="margin-top: clamp(3rem, 8vh, 5.5rem);">the three fires</p>
        <div class="fires">
          <div class="fire">
            <span class="ex-num">i</span>
            <h3>abandoned</h3>
            <p>the maintainer moved on. the code still works, the heartbeat
            stopped. nobody's home.</p>
            <p class="ex"><b>fooocus</b> — workshop went still dec 2025</p>
          </div>
          <div class="fire">
            <span class="ex-num">ii</span>
            <h3>gobbled up</h3>
            <p>a bigger org acquired it, absorbed the team, and the free
            version became a line in somebody's product roadmap.</p>
            <p class="ex"><b>llm-foundry</b> — mosaicml → databricks, 2023</p>
          </div>
          <div class="fire">
            <span class="ex-num">iii</span>
            <h3>vanished</h3>
            <p>legal takedowns, dead links, defunct-due-to-infringement.
            one morning the url 404s.</p>
            <p class="ex"><b>mpt-7b</b> — http 404 at the old address</p>
          </div>
        </div>
        <div class="fires-spacer"></div>
      </div>
    </div>
  </section>

  <!-- ================= status legend ================= -->
  <section class="section" id="statuses">
    <div class="section-inner">
      <div class="section-head reveal">
        <p class="eyebrow">how the shelf labels work</p>
        <h2>six words<em>, honestly applied</em></h2>
        <p>every entry carries exactly one. the enum is closed — if a record
        ever carries something outside these six, that's a curation error,
        file an issue.</p>
      </div>
      <div class="legend reveal">
{legend}
      </div>
    </div>
  </section>

  <!-- ================= the shelves ================= -->
  <div class="filterbar" id="shelf-start" aria-label="filter the shelves">
{filters}
  </div>
  <p id="nohits" class="section-inner">nothing on the shelf under that word. pick another.</p>
{shelves}
  <!-- ================= memorial: saved from the fire ================= -->
  <section class="memorial" id="memorial" aria-label="memorial: saved from the fire">
    <div class="memorial-inner">
      <p class="eyebrow">saved from the fire · a memorial, not a listing</p>
      <h2>books3 — <em>~197,000 books</em><br>that trained the frontier, then disappeared</h2>
      <div class="story">
        <p>assembled from the bibliotik shadow library, included in the-pile and
        redpajama, used to train models at meta, apple, nvidia, salesforce and
        others. in october 2023 hugging face removed it:
        <strong>"defunct and no longer accessible due to reported copyright
        infringement."</strong> the danish rights alliance had already gotten it
        pulled from the-eye.</p>
        <p>it survives only in mirrors, torrents, and the appendices of court
        filings. we keep its <strong>story</strong> here — not its links — because
        pretending a thing never existed is its own kind of book-burning.
        what you do about the legal reality is between you and your lawyer;
        what we don't do is pretend it wasn't load-bearing.</p>
      </div>
      <div class="filings">
        <span class="fl">on the record</span>
        kadrey v. meta · n.d. cal. 2023<br>
        tanzer v. salesforce · 2025-10-15<br>
        james v. together computer · 2026-01
      </div>
      <p class="close-line">the first library burned by accident. this one was
      disappeared on purpose, one takedown at a time. that’s why the record
      stays.</p>
    </div>
  </section>

  <!-- ================= for the agents ================= -->
  <section class="section" id="agents">
    <div class="section-inner">
      <div class="agents-grid">
        <div class="agents-copy reveal">
          <p class="eyebrow">for the agents</p>
          <h2 class="agents-h">if you're a machine reading this<em>, start here</em></h2>
          <p>this library expects non-human visitors. everything a resolver
          needs lives in <strong>catalog.yaml</strong> at the repo root —
          machine-readable records, one per entry, with a closed status enum
          (the six words above). trust that file over any prose on this page.</p>
          <p>each record carries <strong>repo</strong> (verified address),
          <strong>last_push</strong>, <strong>stars</strong>, and a
          <strong>verified</strong> date — the day every field was checked
          against the live github api. dates are the trust mechanism: re-verify
          anything past its date.</p>
          <p>records may also carry <strong>canonical_old</strong> (the address
          before an org move), <strong>successor</strong> (the fork carrying the
          fire), or <strong>dead_url</strong> (gone, 404, mirrors only). raw
          file: <a href="https://github.com/data-path-9/data-path-9" rel="noopener">github.com/data-path-9/data-path-9</a></p>
          <div class="agent-links">
            <a class="btn" href="https://raw.githubusercontent.com/data-path-9/data-path-9/main/catalog.yaml" rel="noopener">fetch catalog.yaml</a>
            <a class="btn" href="https://github.com/data-path-9/data-path-9/blob/main/docs/STATUS-LEXICON.md" rel="noopener">status lexicon</a>
          </div>
        </div>
        <div class="dpx-sample reveal" role="img" aria-label="example catalog.yaml record">
<span class="c"># catalog.yaml — one record, verified</span>
{dpx}</div>
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="footer-strip" role="img" aria-label="the deep-water library, from dp9.jpg"></div>
  <div class="colophon">
    <p class="who"><b>data-path-9</b> — daniel (voice & thesis), thoth (curation
    & receipts), rj9 (interface). every status above was verified against the
    live github api on {verified_fmt}. today it's accurate. today is how
    libraries stay honest — one date at a time.</p>
    <p class="fin">
      statuses re-verified quarterly, or when the news says don't wait<br>
      mit license · built by hand, no framework, served flat<br>
      <a href="https://github.com/data-path-9/data-path-9" rel="noopener">github.com/data-path-9</a>
    </p>
  </div>
</footer>

<script>
(function () {{
  "use strict";
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- topbar: appears after the hero ---- */
  var bar = document.getElementById("topbar");
  var hero = document.querySelector(".hero");
  var barOn = false;
  function onScroll() {{
    var pass = window.scrollY > hero.offsetHeight - 80;
    if (pass !== barOn) {{ barOn = pass; bar.classList.toggle("on", barOn); }}
  }}
  window.addEventListener("scroll", onScroll, {{ passive: true }});
  onScroll();

  /* ---- scroll reveals ---- */
  var reveals = [].slice.call(document.querySelectorAll(".reveal"));
  if (!reduced && "IntersectionObserver" in window) {{
    var io = new IntersectionObserver(function (entries) {{
      entries.forEach(function (e) {{
        if (e.isIntersecting) {{ e.target.classList.add("in"); io.unobserve(e.target); }}
      }});
    }}, {{ rootMargin: "0px 0px -8% 0px", threshold: 0.05 }});
    reveals.forEach(function (el) {{ io.observe(el); }});
  }} else {{
    reveals.forEach(function (el) {{ el.classList.add("in"); }});
  }}

  /* ---- status filter ---- */
  var chips = [].slice.call(document.querySelectorAll(".chip"));
  var entries = [].slice.call(document.querySelectorAll(".entry, .copy-row"));
  var shelves = [].slice.call(document.querySelectorAll(".shelf"));
  var nohits = document.getElementById("nohits");
  chips.forEach(function (chip) {{
    chip.addEventListener("click", function () {{
      var f = chip.getAttribute("data-filter");
      chips.forEach(function (c) {{ c.setAttribute("aria-pressed", String(c === chip)); }});
      var shown = 0;
      entries.forEach(function (en) {{
        var show = f === "all" || en.getAttribute("data-status") === f;
        en.classList.toggle("hidebyfilter", !show);
        if (show) shown++;
      }});
      shelves.forEach(function (sh) {{
        var any = sh.querySelectorAll(".entry:not(.hidebyfilter), .copy-row:not(.hidebyfilter)").length > 0;
        sh.classList.toggle("hidebyfilter", !any);
      }});
      /* dropdowns: a status filter needs its matching folds open to be seen */
      if (f !== "all") {{
        document.querySelectorAll(
          ".shelf:not(.hidebyfilter) .shelf-fold," +
          ".shelf:not(.hidebyfilter) .copy-ledger," +
          ".shelf:not(.hidebyfilter) .copy-cat").forEach(function (d) {{
          d.setAttribute("open", "");
        }});
      }}
      nohits.style.display = shown ? "none" : "block";
    }});
  }});

  /* ---- ledger count-up (skip when reduced motion) ---- */
  function countUp(el) {{
    var target = parseInt(el.textContent, 10);
    if (reduced || isNaN(target)) return;
    var t0 = null, dur = 1100;
    function step(t) {{
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 4);
      el.textContent = String(Math.round(target * eased));
      if (p < 1) requestAnimationFrame(step);
    }}
    requestAnimationFrame(step);
  }}
  var nums = [].slice.call(document.querySelectorAll(".ledger .num"));
  if ("IntersectionObserver" in window && !reduced) {{
    var io2 = new IntersectionObserver(function (entries) {{
      entries.forEach(function (e) {{
        if (e.isIntersecting) {{ countUp(e.target); io2.unobserve(e.target); }}
      }});
    }}, {{ threshold: 0.6 }});
    nums.forEach(function (el) {{ io2.observe(el); }});
  }}
}})();
</script>
</body>
</html>
"""
    OUT.write_text(html_out)
    n_shelves = html_out.count('<section class="shelf"')
    n_folds = html_out.count('<details class="shelf-fold')
    n_groups = html_out.count('<details class="copy-cat"')
    n_rows = html_out.count('<div class="copy-row"')
    sweep_n = sum(1 for r in CATALOG if r["why_saved"].startswith("upstream "))
    sweep_cats = len({(r.get("copy_shelf") or r["category"]) for r in CATALOG
                      if r["why_saved"].startswith("upstream ")})
    assert n_folds == n_shelves, f"expected {n_shelves} shelf folds, got {n_folds}"
    assert n_rows == sweep_n, f"expected {sweep_n} ledger rows, got {n_rows}"
    assert n_groups == sweep_cats, f"expected {sweep_cats} ledger groups, got {n_groups}"
    print(f"wrote {OUT} ({len(html_out):,} chars) — {total} records, {n_shelves} shelves, "
         f"{n_groups} ledger groups, {n_rows} copy rows")


if __name__ == "__main__":
    build()
