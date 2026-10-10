# dp9 status lexicon

six shelf-label words. each one means exactly one thing.

| status | meaning | test |
|---|---|---|
| `breathing` | alive, maintainer active | pushed within ~6 months, not archived |
| `quiet` | works, but nobody's home | no pushes ~12+ months, not archived, no successor |
| `orphaned` | maintainer gone, successor known or not | 12+ months silent + team moved on/company died |
| `archived` | formally locked read-only | GitHub `archived: true` |
| `moved` | alive but changed address | API `full_name` ≠ requested path |
| `vanished` | gone from its address | HTTP 404 / taken down; mirrors only |

## why six words and not five or fifty

five loses the difference between "sleeping" (quiet) and "dead team"
(orphaned) — different rescue strategies. fifty becomes a thesaurus nobody
applies consistently. agents parsing this repo can treat the enum as
closed: anything outside the six is a curation error, file an issue.

## escalation notes

- `quiet` → re-check every quarter; if still silent at 24 months and no
  forks carrying weight, consider reclassifying `orphaned`.
- `moved` → always record `canonical_old`. redirects are not guarantees;
  github has un-redirected before.
- `vanished` → record where mirrors live and under what court filing it
  disappeared, if any. never relink a vanished thing without a note about
  why it vanished.

verified: 2026-10-09 · curator: thoth (for data-path-9)
