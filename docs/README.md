# docs/

the library's public face, served by github pages from this directory.
`index.html` is **generated** — don't edit it by hand.

```bash
python3 tools/build.py   # catalog.yaml -> docs/index.html
```

edit `catalog.yaml` (the single source of truth), rebuild, commit both.
assets are hand-set: fonts self-hosted (Fraunces + JetBrains Mono, variable,
latin subset), palette pulled from azalea's dp9.jpg. no framework, no build
step beyond the one script, served flat — any static host, or the repo itself.
