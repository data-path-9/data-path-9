#!/usr/bin/env python3
"""dp9sync — keep the data-path-9 library verified.

one command after every `gh repo sync` pass. reads the live GitHub API and
reconciles it against catalog.yaml + README.md, then rebuilds the site so
the served page can never drift from the receipts.

what it does, in order:
  1. fork census      gh repo list --fork -> new forks become sweep records
                      (exact build-template prose, count guard bumped);
                      catalog forks missing from the account are flagged,
                      never silently deleted.
  2. copy receipts    held_fork_push refreshed on every founding-shelf copy
                      (the dates that prove our insurance is current).
  3. status refresh   (--deep, or --status NAME) re-verifies upstreams:
                      full_name / archived / pushed_at -> the six-word enum,
                      per docs/STATUS-LEXICON.md. moves record canonical_old;
                      vanishings require --vanish to write (court-filing care).
  4. numbers refresh  (--deep) stars + last_push on every record.
  5. rebuild          tools/build.py must pass its guards; catalog edits that
                      break the build are refused and rolled back.
  6. commit           one commit per pass, message carries the counts.

usage:
  python3 tools/dp9sync.py                 # census + copy receipts + build + commit
  python3 tools/dp9sync.py --deep          # + full upstream re-verification pass
  python3 tools/dp9sync.py --status llama.cpp --status Flowise
  python3 tools/dp9sync.py --no-commit     # leave changes uncommitted
  python3 tools/dp9sync.py --dry-run       # report only, write nothing

requires: gh (authenticated as data-path-9), pyyaml.
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
# copies of this script may live outside the repo (the curator keeps one in
# ~); resolve to the real library wherever catalog.yaml actually is
for _cand in (ROOT, Path.home() / "projects" / "data-path-9"):
    if (_cand / "catalog.yaml").is_file() and (_cand / "tools" / "build.py").is_file():
        ROOT = _cand
        break
CAT_PATH = ROOT / "catalog.yaml"
README_PATH = ROOT / "README.md"
BUILD = ROOT / "tools" / "build.py"

STATUSES = ["breathing", "quiet", "orphaned", "archived", "moved", "vanished"]
BREATHING_WINDOW_DAYS = 180  # matches the build + lexicon test
TODAY = date.today().isoformat()


# ---------------- gh / api helpers ----------------

def gh_json(*args):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"dp9sync: gh {' '.join(args)} failed:\n{r.stderr}")
    return json.loads(r.stdout)


def fork_census():
    """{fork short name: full_name} for every non-archived fork in the account."""
    rows = gh_json("repo", "list", "data-path-9", "--fork", "--limit", "10000",
                   "--json", "nameWithOwner,isArchived")
    out = {}
    for row in rows:
        if row["isArchived"]:
            continue
        out[row["nameWithOwner"].split("/", 1)[1]] = row["nameWithOwner"]
    return out


def repo_data(slug):
    """live repos/<slug> payload, or None if the address is gone (404)."""
    r = subprocess.run(["gh", "api", f"repos/{slug}"], capture_output=True, text=True)
    if r.returncode != 0:
        if "HTTP 404" in r.stderr:
            return None
        sys.exit(f"dp9sync: gh api repos/{slug} failed:\n{r.stderr}")
    return json.loads(r.stdout)


def classify(up):
    """six-word status from live api data. orphaned/moved/vanished need a
    curator's judgment or history, so the machine only ever writes
    breathing / quiet / archived — anything else is reported for review."""
    if up.get("archived"):
        return "archived"
    pushed = date.fromisoformat(up["pushed_at"][:10])
    age = (date.today() - pushed).days
    return "breathing" if age <= BREATHING_WINDOW_DAYS else "quiet"


# ---------------- yaml text surgery (keeps the file hand-formatted) ----------------

def yq(v):
    """yaml-safe scalar: ints bare, iso dates single-quoted (house style),
    anything with special chars json-dumped (valid yaml double-quoted)."""
    if isinstance(v, int):
        return str(v)
    s = str(v)
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
        return f"'{s}'"
    try:
        p = yaml.safe_load(f"x: {s}")
        if isinstance(p, dict) and p.get("x") == s and not s[:1] in "\"'{[&*!|>%@`":
            return s
    except yaml.YAMLError:
        pass
    return json.dumps(s)


def record_bounds(lines, name, category=None):
    """a record's line span. names can collide (a founding shelf and its
    sweep copy may share one), so pass category to disambiguate —
    (name, category) is the unique key of this catalog."""
    q = re.escape(str(name))
    pat = re.compile(rf"- name: (?:{q}|'{q}'|\"{q}\")\s*$")  # bare or yq-quoted
    start = next(i for i, l in enumerate(lines)
                 if pat.match(l)
                 and (category is None or any(
                     re.match(rf"  category: {re.escape(category)}\s*$", x)
                     for x in lines[i + 1:i + 4])))
    end = start + 1
    while end < len(lines) and not lines[end].startswith("- name:"):
        end += 1
    return start, end


def update_record_field(text, name, field, value, category=None):
    """set field on a record; insert after the record's last field if absent."""
    lines = text.splitlines(keepends=True)
    start, end = record_bounds(lines, name, category)
    pat = re.compile(r"^  " + re.escape(field) + r":(.*)$")
    for i in range(start + 1, end):
        if pat.match(lines[i].rstrip("\n")):
            lines[i] = f"  {field}: {yq(value)}\n"
            return "".join(lines)
    ins = end
    while ins > start + 1 and not re.match(r"^  [a-z_]+:", lines[ins - 1]):
        ins -= 1
    lines.insert(ins, f"  {field}: {yq(value)}\n")
    return "".join(lines)


def sweep_record_text(name, up):
    """a new copy record in the EXACT shape tools/build.py expects: the
    story/ledger split keys on why_saved starting with 'upstream '."""
    desc = re.sub(r"\s+", " ", (up.get("description") or "").strip())
    one_liner = yq(desc if desc else f"copy of {up['full_name']} — upstream kept the story thin")
    return (f"- name: {yq(name)}\n"
            "  category: fork-wing\n"
            f"  human_one_liner: {one_liner}\n"
            f"  why_saved: upstream {classify(up)} as of {TODAY}; the copy is insurance, not rescue\n"
            f"  status: {classify(up)}\n"
            f"  repo: https://github.com/{up['full_name']}\n"
            f"  last_push: {yq(up['pushed_at'][:10])}\n"
            f"  stars: {up.get('stargazers_count', 0)}\n"
            f"  held_fork: data-path-9/{name}\n"
            f"  verified: {yq(TODAY)}\n\n")


def bump_guard(text, new_total):
    return re.sub(r"assert len\(CATALOG\) == \d+",
                  f"assert len(CATALOG) == {new_total}", text)


def bump_readme_counts(text, fork_total):
    text = re.sub(r"the fork wing: \d+ copies", f"the fork wing: {fork_total} copies", text)
    text = re.sub(r"wing holds \d+\.", f"wing holds {fork_total}.", text)
    return text


def append_readme_appendix(text, new_names):
    """machine-synced roster lines land in a clearly-labeled appendix."""
    lines = "\n".join(f"- `{n}` — copy held, upstream verified {TODAY} (auto-sync)"
                      for n in new_names)
    return (text.rstrip("\n")
            + f"\n\n## sync appendix — machine-verified additions\n\n"
              f"added by `tools/dp9sync.py` on {TODAY}; curator pass pending.\n\n{lines}\n")


# ---------------- passes ----------------

def pass_census(records, text, readme, btext, report, dry, vanish_ok):
    account = fork_census()
    # forks join to records through held_fork (data-path-9/<fork>), not record
    # names — record names follow upstream identity, forks can be renamed
    held = {r["held_fork"].split("/", 1)[1] for r in records if r.get("held_fork")}
    new_names = sorted(set(account) - held)
    removed = sorted(held - set(account))
    if removed:
        report.append(f"!! {len(removed)} catalog copies no longer in the account "
                      f"(curator review, nothing edited): {', '.join(removed)}")
    added = []
    for name in new_names:
        fork_full = account[name]
        fork = repo_data(fork_full)
        parent = (fork or {}).get("parent", {}).get("full_name")
        up = repo_data(parent) if parent else None
        if up is None:
            report.append(f"!! {name}: upstream {parent or '???'} unreachable "
                          f"(404 or missing parent) — needs a curator, record NOT written "
                          f"{'(use --vanish to record a vanished upstream)' if not vanish_ok else ''}")
            continue
        text = text.rstrip("\n") + "\n" + sweep_record_text(name, up)
        added.append(name)
        report.append(f"+ {name} <- upstream {up['full_name']} "
                      f"({classify(up)}, {up.get('stargazers_count', 0)} stars)")
    if added:
        n = len(records) + len(added)
        btext = bump_guard(btext, n)
        wing = sum(1 for r in records
                   if r.get("held_fork") and r["category"] == "fork-wing") + len(added)
        readme = bump_readme_counts(readme, wing)
        readme = append_readme_appendix(readme, added)
        report.append(f"guard bumped to {n}; readme wing count -> {wing}")
    return text, readme, btext


def pass_copy_receipts(records, text, report, dry):
    n = 0
    for r in records:
        if not r.get("held_fork"):
            continue
        fork = repo_data(r["held_fork"])
        if fork is None:
            report.append(f"!! held copy {r['held_fork']} 404s — curator review")
            continue
        pushed = fork["pushed_at"][:10]
        if str(r.get("held_fork_push", ""))[:10] != pushed:
            if not dry:
                text = update_record_field(text, r["name"], "held_fork_push", pushed,
                                           category=r["category"])
            n += 1
            report.append(f"~ {r['name']}: copy pushed {pushed} (was {r.get('held_fork_push', 'unrecorded')})")
    if not n:
        report.append("copy receipts: all current")
    return text


def pass_verify(records, text, report, dry, vanish_ok, only=None):
    n = 0
    for r in records:
        if only and r["name"] not in only:
            continue
        if not r.get("repo") or r["status"] == "vanished":
            continue
        up = repo_data(r["repo"].removeprefix("https://github.com/"))
        if up is None:
            report.append(f"!! {r['name']}: {r['repo']} 404s — vanished upstream "
                          f"{'recorded' if vanish_ok and not dry else 'REPORTED ONLY'}")
            if vanish_ok and not dry:
                text = update_record_field(text, r["name"], "status", "vanished",
                                           category=r["category"])
                text = update_record_field(text, r["name"], "dead_url", r["repo"],
                                           category=r["category"])
                text = update_record_field(text, r["name"], "verified", TODAY,
                                           category=r["category"])
                n += 1
            continue
        live = up["full_name"]
        new_status = classify(up)
        changes = {}
        if live.lower() != r["repo"].rsplit("github.com/", 1)[-1].lower():
            changes["canonical_old"] = r["repo"]
            changes["repo"] = f"https://github.com/{live}"
            new_status = "moved"
        if new_status != r["status"]:
            changes["status"] = new_status
        if up.get("stargazers_count") != r.get("stars"):
            changes["stars"] = up.get("stargazers_count", 0)
        if up["pushed_at"][:10] != str(r.get("last_push", ""))[:10]:
            changes["last_push"] = up["pushed_at"][:10]
        # every record actually checked gets its verified stamp advanced,
        # not just the ones whose fields moved
        if str(r.get("verified", ""))[:10] != TODAY:
            changes["verified"] = TODAY
        if changes:
            if not dry:
                for k, v in changes.items():
                    text = update_record_field(text, r["name"], k, v,
                                               category=r["category"])
            n += 1
            detail = ", ".join(f"{k}={v if not isinstance(v, str) or len(v) < 40 else '...'}"
                               for k, v in changes.items())
            report.append(f"~ {r['name']}: {detail}")
    if not n:
        report.append(f"verify: {'all' if not only else 'target records'} current")
    return text


# ---------------- build / commit ----------------

def run_build_or_rollback(saved):
    r = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT,
                       capture_output=True, text=True)
    if r.returncode != 0:
        for path, content in saved.items():
            Path(path).write_text(content)
        sys.exit(f"dp9sync: build FAILED, edits rolled back:\n{r.stderr[-1200:]}")
    print(r.stdout.strip())


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args],
                          capture_output=True, text=True)


def commit_all(summary):
    r = git("add", "catalog.yaml", "README.md", "docs/index.html", "tools/build.py")
    if r.returncode != 0:
        sys.exit(f"dp9sync: git add failed:\n{r.stderr}")
    if not git("status", "--porcelain").stdout.strip():
        print("dp9sync: nothing to commit")
        return
    r = git("commit", "-m", summary)
    if r.returncode != 0:
        sys.exit(f"dp9sync: git commit failed:\n{r.stderr}")
    print(f"dp9sync: committed — {summary}")


# ---------------- main ----------------

def main():
    ap = argparse.ArgumentParser(description="keep the data-path-9 library verified")
    ap.add_argument("--deep", action="store_true", help="full upstream re-verification")
    ap.add_argument("--status", action="append", default=[], metavar="NAME",
                    help="re-verify one record (repeatable)")
    ap.add_argument("--vanish", action="store_true",
                    help="allow writing status: vanished (dead_url recorded)")
    ap.add_argument("--dry-run", action="store_true", help="report, write nothing")
    ap.add_argument("--no-commit", action="store_true", help="skip the commit step")
    args = ap.parse_args()
    dry = args.dry_run

    text = CAT_PATH.read_text()
    readme = README_PATH.read_text()
    btext = BUILD.read_text()
    records = yaml.safe_load(text)
    assert isinstance(records, list) and len(records) >= 268
    report = [f"dp9sync {TODAY} — census of {len(records)} records"
              + (" (DRY RUN)" if dry else "")]

    saved = {str(CAT_PATH): text, str(README_PATH): readme, str(BUILD): btext}
    new_text, new_readme, new_btext = pass_census(records, text, readme, btext,
                                                  report, dry, args.vanish)
    new_text = pass_copy_receipts(records, new_text, report, dry)
    if args.deep or args.status:
        new_text = pass_verify(records, new_text, report, dry, args.vanish,
                               only=set(args.status) or None)

    if new_text != text or new_readme != readme or new_btext != btext:
        if dry:
            report.append("dry run: changes NOT written")
        else:
            CAT_PATH.write_text(new_text)
            README_PATH.write_text(new_readme)
            if new_btext != btext:
                BUILD.write_text(new_btext)
            yaml.safe_load(CAT_PATH.read_text())  # must still parse
            run_build_or_rollback(saved)
            if not args.no_commit:
                n_records = len(yaml.safe_load(new_text))
                commit_all(f"dp9sync {TODAY}: library verified against live api "
                           f"({n_records} records)")
    else:
        report.append("catalog + readme already match the live api — nothing to do")

    print("\n".join(report))


if __name__ == "__main__":
    main()
