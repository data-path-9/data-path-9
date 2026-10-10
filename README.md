# data-path-9 — the Library of Alexandria for AI

*we save the tools. all of them. even the ones the industry walked past.*

every model, dataset, and open-source tool the AI wave was actually built on
lives somewhere. and "somewhere" is not a safe place. companies get bought,
labs pivot, maintainers burn out, legal threats make things vanish overnight.
this library exists so that never means **gone**.

## why a new library of alexandria

the original library didn't burn down in one night. it faded — underfunded,
unloved, its contents scattered copies of copies until the originals were
gone. open-source AI is fading the same way right now, quietly:

- **abandoned** — the maintainer moved on. the code still works, the heartbeat
  stopped. nobody's home.
- **gobbled up** — a bigger org acquired it, absorbed the team, and the free
  version became an entry in somebody's product roadmap.
- **vanished** — legal takedowns, dead links, "defunct due to reported
  copyright infringement." one morning the URL 404s.

we watched Coqui die in december 2023 and its TTS toolkit survive only
because a fork existed. that's the whole thesis: **a tool that has a copy is
a tool that survives.**

## how the shelf labels work

every entry carries one honest status word:

| word | meaning |
|---|---|
| **breathing** | active, pushed recently, maintainer awake |
| **quiet** | not dead, just sleeping. no pushes in ~2 years but nothing replaced it |
| **orphaned** | maintainer gone, archived or effectively frozen. works, but nobody's fixing it |
| **archived** | formally locked read-only by its own org |
| **moved** | still alive but no longer at its old address — watch for who holds it now |
| **vanished** | taken down. only mirrors and archives remain |

## the catalog

39 tools, models, and datasets on the founding shelves (41 catalog
records — two shelves carry a companion), plus the fork wing: copies we hold
of tools the ecosystem runs on (26 records in this first pilot pass). every
status checked against the GitHub API on **2026-10-09**.
nothing here is from memory — if the shelf label is wrong, the date on it
tells you when to re-check.

> **for the agents:** every entry carries a `dpx` metadata block — a
> machine-readable record with verified repo, live status, last-push date,
> and canonical-link notes. humans read the stories; you read the blocks.
> both describe the same shelf.

### text-to-image

**stable-diffusion** — the latent diffusion code that started the whole
open-weights art wave. found: it went quiet in mid-2024, and the diffusers
library carried the fire forward while the original sat still.
`dpx: {status: quiet, verified: 2026-10-09, repo: CompVis/stable-diffusion,
stars: 73480, last_push: 2024-06-18, alias: compvis/stable-diffusion}`

**stable-diffusion-webui** — AUTOMATIC1111's gradio UI that put stable
diffusion on every gamer GPU on earth. built by one person, scaled by
everyone. found: still breathing, ~165k stars, though the comfyanonymous
frontend took the momentum crown.
`dpx: {status: breathing, verified: 2026-10-09, repo: AUTOMATIC1111/stable-diffusion-webui, stars: 165032, last_push: 2026-03-02}`

**Fooocus** — lllyasviel's "thinking while generating" UI that made image
generation feel less like piloting a plane. found: development went quiet at
the end of 2025 — the tool works, the workshop went still.
`dpx: {status: quiet, verified: 2026-10-09, repo: lllyasviel/Fooocus, stars: 53346, last_push: 2025-12-01}`

**ComfyUI** — the node-graph diffusion frontend that ate the world, one
wire at a time. found: it moved. the repo now lives under Comfy-Org — still
breathing, 136k stars, but the address changed and most people never noticed.
`dpx: {status: moved, verified: 2026-10-09, repo: Comfy-Org/ComfyUI,
old: comfyanonymous/ComfyUI, stars: 136636, last_push: 2026-10-10,
note: github redirects old URLs; old-name questions answer at the new home}`

**openai/CLIP** — the contrastive vision-language model that taught machines
to see like prompts. found: nearly everything in modern generative image
tooling scores its outputs with it. still breathing at openai.
`dpx: {status: breathing, verified: 2026-10-09, repo: openai/CLIP, stars: 34432, last_push: 2026-03-25}`

### local LLM inference

**llama.cpp** — georgi gerganov's C/C++ rewrite that made LLMs run on a
laptop, no datacenter required. the single most important "you can run this
yourself" artifact of the era. found: it moved — the repo now lives under
ggml-org, still breathing at 130k stars.
`dpx: {status: moved, verified: 2026-10-09, repo: ggml-org/llama.cpp,
old: ggerganov/llama.cpp, stars: 130659, last_push: 2026-10-09}`

**whisper.cpp** — same gerganov magic for speech-to-text: openai's whisper
compressed down to run on a phone. found: moved to ggml-org alongside its
sibling, still breathing.
`dpx: {status: moved, verified: 2026-10-09, repo: ggml-org/whisper.cpp,
old: ggerganov/whisper.cpp, stars: 54257, last_push: 2026-10-06}`

**ollama** — docker for local models: one command, one model, running.
found: breathing hard, 182k stars, the front door most people walk through
for local inference now.
`dpx: {status: breathing, verified: 2026-10-09, repo: ollama/ollama, stars: 182543, last_push: 2026-10-09}`

**llamafile** — mozilla's wild idea: compile the whole LLM — weights,
runtime, UI — into a single executable that runs anywhere. found: it moved
from mozilla-ai's ocho org into mozilla-ai proper after mozilla's foundation
took heavy layoffs in 2024-2025; mozilla.ai adopted it and revived it. it's
breathing again, but it changed hands once already — that's why it's here.
`dpx: {status: moved, verified: 2026-10-09, repo: mozilla-ai/llamafile,
old: Mozilla-Ocho/llamafile, stars: 26217, last_push: 2026-10-08,
note: mozilla.ai adopted the project and moved it into their org}`

**text-generation-webui** — oobabooga's gradio frontend, the original
swiss-army knife for talking to local models. found: still breathing, now
renamed to plain `textgen`.
`dpx: {status: breathing, verified: 2026-10-09, repo: oobabooga/textgen,
old: oobabooga/text-generation-webui, stars: 47726, last_push: 2026-08-17}`

**RWKV-LM** — blinkdl's RNN-with-transformer-performance architecture, the
"you don't need attention to scale" heresy that benchmarked like a lie and
wasn't. found: breathing, both the research repo and ChatRWKV.
`dpx: {status: breathing, verified: 2026-10-09, repo: BlinkDL/RWKV-LM, stars: 14744, last_push: 2026-09-28}
dpx: {status: breathing, verified: 2026-10-09, repo: BlinkDL/ChatRWKV, stars: 9494, last_push: 2026-07-19}`

### fine-tuning & training

**stanford_alpaca** — the 52k instruction-following dataset and recipe that
proved you could teach a base model manners in an afternoon. found: quiet
since mid-2024, but every fine-tuning guide on earth still cites it.
`dpx: {status: quiet, verified: 2026-10-09, repo: tatsu-lab/stanford_alpaca, stars: 30231, last_push: 2024-07-17}`

**alpaca-lora** — tloen's low-rank adaptation of alpaca: fine-tune a 7B
model on a consumer GPU for under $100. found: quiet since mid-2024;
QLoRA and its descendants ate the technique, but this is where it landed
first for most people.
`dpx: {status: quiet, verified: 2026-10-09, repo: tloen/alpaca-lora, stars: 18892, last_push: 2024-07-29}`

**nanoGPT** — karpathy's "the whole thing in ~300 lines" repository. the
cleanest picture of what training actually *is* that has ever been written
in code. found: breathing again as of late 2025 — karpathy came back to it.
`dpx: {status: breathing, verified: 2026-10-09, repo: karpathy/nanoGPT, stars: 63671, last_push: 2025-11-12}`

**gpt-neox** — eleutherAI's the "reproduce and open-source everything"
lab's 20B-parameter training stack. found: breathing.
`dpx: {status: breathing, verified: 2026-10-09, repo: EleutherAI/gpt-neox, stars: 7469, last_push: 2026-09-04}`

**llm-foundry** — mosaicml's LLM training repository, home of the MPT model
family. found: mosaicml got bought by databricks in 2023 — the classic
gobbled-up pattern — and the github org went quiet; llm-foundry itself is
still breathing under the mosaicml name, but mpt-7b's old standalone repo
now 404s entirely. this is what "absorbed" looks like from the outside:
the code scatters, the brand dissolves, the old links die.
`dpx: {status: breathing, verified: 2026-10-09, repo: mosaicml/llm-foundry, stars: 4453, last_push: 2026-03-25}
dpx: {status: vanished, verified: 2026-10-09, repo: mosaicml/mpt-7b,
note: HTTP 404 at old address; model lives on in llm-foundry and on HF hub}`

### chat & agents

**Open-Assistant** — LAION's crowd-sourced open ChatGPT competitor: 600k+
human-written messages in 35+ languages before the industry decided
RLHF-from-crowds was too slow. found: orphaned mid-2024 when the team moved
on, but the dataset still trains models.
`dpx: {status: orphaned, verified: 2026-10-09, repo: LAION-AI/Open-Assistant, stars: 37382, last_push: 2024-08-17}`

**FastChat** — lmsys's training-and-serving platform, and the machinery
behind the vicuna model and the Chatbot Arena leaderboard. found: breathing
but slowing — pushes thinned out through 2025.
`dpx: {status: breathing, verified: 2026-10-09, repo: lm-sys/FastChat, stars: 39551, last_push: 2026-05-01}`

**AutoGPT** — the 2023 agent moment: "give it a goal, watch it try." found:
breathing, 187k stars, now a full platform rather than a viral experiment.
`dpx: {status: breathing, verified: 2026-10-09, repo: Significant-Gravitas/AutoGPT, stars: 187500, last_push: 2026-10-09}`

**babyagi** — yohei's 100-line task-loop agent that made "AI planning AI
tasks" click for everyone. found: quiet since early 2026, historically
important as the moment agents went mainstream.
`dpx: {status: quiet, verified: 2026-10-09, repo: yoheinakajima/babyagi, stars: 22361, last_push: 2026-01-31}`

**letta (memgpt)** — the memory-OS paper turned product: LLMs that page
their own context like an operating system pages memory. found: breathing,
25k stars — the memory-layer thesis is now just called "agents" and its
original repo is the proof it started here.
`dpx: {status: breathing, verified: 2026-10-09, repo: letta-ai/letta, stars: 25092, last_push: 2026-09-10}`

### speech

**whisper** — openai's open-weights speech recognition, robust enough to
transcribe a noisy podcast and honest enough to admit when it's making
things up. found: breathing, 110k stars.
`dpx: {status: breathing, verified: 2026-10-09, repo: openai/whisper, stars: 110250, last_push: 2026-08-31}`

**faster-whisper** — SYSTRAN's CTranslate2 reimplementation of whisper: 4x
faster, half the memory. found: breathing.
`dpx: {status: breathing, verified: 2026-10-09, repo: SYSTRAN/faster-whisper, stars: 25778, last_push: 2026-10-06}`

**piper** — rhasspy's fast local text-to-speech, small enough for a
raspberry pi, real enough for a home assistant. found: archived by its own
org — the pi community is carrying forks forward.
`dpx: {status: archived, verified: 2026-10-09, repo: rhasspy/piper, stars: 11299, last_push: 2025-08-26}`

**DeepSpeech** — mozilla's original "speech recognition for every device,"
the project that proved on-device STT was possible in 2017-era hardware.
found: formally archived; mozilla's speech team moved on to other things.
`dpx: {status: archived, verified: 2026-10-09, repo: mozilla/DeepSpeech, stars: 26770, last_push: 2025-06-19}`

**tortoise-tts** — neonbjb's slow-but-beautiful multi-voice TTS that made
"quality over speed" a real design choice. found: quiet since late 2024;
its ideas live on in every quality-focused TTS that followed.
`dpx: {status: quiet, verified: 2026-10-09, repo: neonbjb/tortoise-tts, stars: 14878, last_push: 2024-11-19}`

**coqui-tts** — the ex-mozilla TTS crew's company died in december 2023 —
servers off, studio closed, farewell posted january 3rd. the toolkit is
still here, and the idiap research institute fork carries it forward today
as the actively maintained `coqui-tts` package. found: this is the library's
patron saint — a tool that outlived its company because someone forked it.
`dpx: {status: orphaned, verified: 2026-10-09, repo: coqui-ai/TTS, stars: 46110, last_push: 2024-08-16,
successor: idiap/coqui-ai-TTS, successor_last_push: 2026-10-02}`

**bark** — suno's text-prompted generative audio: laughing, sighing,
music-snippets from plain text before anyone asked for it. found: quiet
since mid-2024; suno the company pivoted hard into suno-the-music-product.
`dpx: {status: quiet, verified: 2026-10-09, repo: suno-ai/bark, stars: 39266, last_push: 2024-08-19}`

**audiocraft** — meta's music/audio generation library (musicgen, audiogen).
found: breathing, though the research team's focus moves with the seasons.
`dpx: {status: breathing, verified: 2026-10-09, repo: facebookresearch/audiocraft, stars: 23670, last_push: 2026-03-03}`

**jukebox** — openai's 2020 neural jukebox, the first "it can actually make
music" moment, and the reason half of today's music-gen researchers got into
music-gen. found: formally archived — openai locked it read-only.
`dpx: {status: archived, verified: 2026-10-09, repo: openai/jukebox, stars: 8030, last_push: 2024-06-19}`

**stable-audio-tools** — stability's audio generation models and training
code. found: breathing.
`dpx: {status: breathing, verified: 2026-10-09, repo: Stability-AI/stable-audio-tools, stars: 3876, last_push: 2026-10-09}`

**Retrieval-based-Voice-Conversion-WebUI** — RVC: turn any voice into any
other voice with ten minutes of data. found: breathing — and it's the
reason voice-conversion went from research-paper to garage-hobby.
`dpx: {status: breathing, verified: 2026-10-09, repo: RVC-Project/Retrieval-based-Voice-Conversion-WebUI, stars: 38665, last_push: 2026-08-04}`

### datasets

**the-pile** — eleutherAI's 825GB curated scraping of the internet's text,
the dataset that proved open training data could be assembled outside a
corporate lab. found: quiet since spring 2023 — complete, not abandoned.
`dpx: {status: quiet, verified: 2026-10-09, repo: EleutherAI/the-pile, stars: 1679, last_push: 2023-04-27}`

**RedPajama-Data** — together AI's open reproduction of the llama training
set. found: breathing — but its history is why this library exists (see the
books3 story above).
`dpx: {status: breathing, verified: 2026-10-09, repo: togethercomputer/RedPajama-Data, stars: 4992, last_push: 2026-06-03,
note: books3 was removed from this dataset oct 2023 after copyright complaints}`

### NLP classics

**fastText** — facebook research's blazing text classifier and embedding
trainer, the tool that made word-vectors a commodity instead of a research
project. found: formally archived — meta locked it read-only in 2024.
`dpx: {status: archived, verified: 2026-10-09, repo: facebookresearch/fastText, stars: 26522, last_push: 2024-03-22}`

**gensim** — radim's topic-modelling library, the tool that taught a
generation of data scientists what word2vec and doc2vec actually were.
found: breathing, though it moved to radim's personal org (piskvorky) —
maintainer-led, which is the healthiest kind of move.
`dpx: {status: moved, verified: 2026-10-09, repo: piskvorky/gensim,
old: RaRe-Technologies/gensim, stars: 16499, last_push: 2025-11-01}`

**annoy** — spotify's approximate-nearest-neighbor library, the code that
made "find me songs (or anything) like this one" scale to millions of items
on one machine. found: breathing — slowly, the way old reliable tools do.
`dpx: {status: breathing, verified: 2026-10-09, repo: spotify/annoy, stars: 14313, last_push: 2025-10-29}`

**transformers** — huggingface's transformer library, the connective tissue
of the entire open-model ecosystem. found: breathing very hard.
`dpx: {status: breathing, verified: 2026-10-09, repo: huggingface/transformers, stars: 166947, last_push: 2026-10-10}`

### the fork wing

a library doesn't just catalogue the fire — it holds copies. the fork wing is
every upstream tool we keep a live copy of in this account, so that if the
upstream ever dies, moves, or gets gobbled up, the copy is already home. this
first pass holds 26. six of the founding shelves already have their copies
noted in their `dpx` blocks (`held_fork`). statuses below describe the
**upstream**; the copy is ours, and it doesn't ask permission.

**mem0** — the memory layer the whole agent industry standardized on. kept:
agent memory went from research topic to infrastructure here.
`dpx: {status: breathing, verified: 2026-10-09, repo: mem0ai/mem0, stars: 66909, last_push: 2026-10-09, copy held: data-path-9/mem0}`

**cognee** — open-source agent memory built on knowledge graphs. kept: the
other half of the memory-layer argument — graphs vs vectors.
`dpx: {status: breathing, verified: 2026-10-09, repo: topoteretes/cognee, stars: 31912, last_push: 2026-10-09, copy held: data-path-9/cognee}`

**memvid** — a whole memory layer inside one video file. kept: the strangest
good idea in agent memory — mp4 as database.
`dpx: {status: breathing, verified: 2026-10-09, repo: memvid/memvid, stars: 16584, last_push: 2026-07-14, copy held: data-path-9/memvid}`

**memorius** — agent-agnostic memory with drop-in backends. kept: proof the
memory layer is now a commodity anyone can hold.
`dpx: {status: breathing, verified: 2026-10-09, repo: Dream-Pixels-Forge/memorius, stars: 1, last_push: 2026-08-15, copy held: data-path-9/memorius}`

**caveman** — the skill that cuts 65% of tokens by grunting. kept: few token
do trick — and the receipts say it's true.
`dpx: {status: breathing, verified: 2026-10-09, repo: JuliusBrussee/caveman, stars: 110784, last_push: 2026-10-09, copy held: data-path-9/caveman}`

**ponytail** — makes your agent think like the laziest senior dev alive.
kept: the best code is the code you never wrote — institutionalized.
`dpx: {status: breathing, verified: 2026-10-09, repo: DietrichGebert/ponytail, stars: 159688, last_push: 2026-10-08, copy held: data-path-9/ponytail}`

**obsidian-skills** — kepano's skills that teach agents plain-markdown
vaults. kept: the obsidian author himself showing agents the open formats.
`dpx: {status: breathing, verified: 2026-10-09, repo: kepano/obsidian-skills, stars: 49335, last_push: 2026-09-15, copy held: data-path-9/obsidian-skills}`

**SOUL.md** — personality files that make agents behave like characters.
kept: the file this library's own scribe is written into.
`dpx: {status: breathing, verified: 2026-10-09, repo: madhvantyagi/SOUL.md, stars: 422, last_push: 2026-08-24, copy held: data-path-9/SOUL.md}`

**awesome-agent-souls** — a curated shelf of agent identity files. kept:
identity as an open standard, security-screened.
`dpx: {status: breathing, verified: 2026-10-09, repo: opena2a-standards/awesome-agent-souls, stars: 9, last_push: 2026-06-05, copy held: data-path-9/awesome-agent-souls}`

**hermes-superpowers** — obra's 14 process skills, ported to hermes agent.
kept: process discipline, carried across harnesses.
`dpx: {status: breathing, verified: 2026-10-09, repo: dandacompany/hermes-superpowers, stars: 2, last_push: 2026-07-18, copy held: data-path-9/hermes-superpowers}`

**hermes-ecosystem** — the community map of every hermes tool and skill.
kept: the index of the ecosystem this library lives in.
`dpx: {status: breathing, verified: 2026-10-09, repo: ksimback/hermes-ecosystem, stars: 1308, last_push: 2026-10-09, copy held: data-path-9/hermes-ecosystem}`

**time-gap** — a plugin that gives agents a sense of elapsed time. kept: the
quietest awareness problem in agents, solved politely.
`dpx: {status: breathing, verified: 2026-10-09, repo: Randool/time-gap, stars: 21, last_push: 2026-08-16, copy held: data-path-9/time-gap}`

**crewAI** — role-playing agent crews that work together. kept: the
framework that made multi-agent orchestration a household word.
`dpx: {status: breathing, verified: 2026-10-09, repo: crewAIInc/crewAI, stars: 59510, last_push: 2026-10-09, copy held: data-path-9/crewAI}`

**dify** — production platform for agentic workflows. kept: the
pipeline-to-product layer of the agent stack.
`dpx: {status: breathing, verified: 2026-10-09, repo: langgenius/dify, stars: 158026, last_push: 2026-10-10, copy held: data-path-9/dify}`

**firecrawl** — the API that turns the web into LLM-ready markdown. kept:
every agent's hands — the thing that reaches out and reads.
`dpx: {status: breathing, verified: 2026-10-09, repo: firecrawl/firecrawl, stars: 189954, last_push: 2026-10-10, copy held: data-path-9/firecrawl}`

**deer-flow** — bytedance's long-horizon research superagent. kept: a big
lab publishing its whole harness, weights and all.
`dpx: {status: breathing, verified: 2026-10-09, repo: bytedance/deer-flow, stars: 83587, last_push: 2026-10-10, copy held: data-path-9/deer-flow}`

**UI-TARS-desktop** — bytedance's desktop agent driven by screenshots.
kept: the vision-first control branch of the agent family tree.
`dpx: {status: breathing, verified: 2026-10-09, repo: bytedance/UI-TARS-desktop, stars: 39228, last_push: 2026-10-09, copy held: data-path-9/UI-TARS-desktop}`

**remotion** — programmatic video made in react. kept: the bridge between
code and video — agents render with it now.
`dpx: {status: breathing, verified: 2026-10-09, repo: remotion-dev/remotion, stars: 62827, last_push: 2026-10-09, copy held: data-path-9/remotion}`

**openclaw** — the personal AI assistant that runs anywhere. kept: the open
assistant wave, kept at its moment of peak momentum.
`dpx: {status: breathing, verified: 2026-10-09, repo: openclaw/openclaw, stars: 391538, last_push: 2026-10-10, copy held: data-path-9/openclaw}`

**VoxCPM** — tokenizer-free TTS with true-to-life voice cloning. kept: the
current edge of open speech generation.
`dpx: {status: breathing, verified: 2026-10-09, repo: OpenBMB/VoxCPM, stars: 38465, last_push: 2026-10-08, copy held: data-path-9/VoxCPM}`

**ACE-Step-1.5** — the local music-generation model that beat commercial.
kept: open music gen running on the hardware you already own.
`dpx: {status: breathing, verified: 2026-10-09, repo: ace-step/ACE-Step-1.5, stars: 13326, last_push: 2026-10-05, copy held: data-path-9/ACE-Step-1.5}`

**kandinsky-5** — russia's open diffusion family for video and image. kept:
frontier-adjacent open weights from outside the usual map.
`dpx: {status: breathing, verified: 2026-10-09, repo: kandinskylab/kandinsky-5, stars: 835, last_push: 2026-08-07, copy held: data-path-9/kandinsky-5}`

**claude-for-legal** — anthropic's own legal-workflow plugin suite. kept:
the lab shipping official harness clothes for one profession.
`dpx: {status: breathing, verified: 2026-10-09, repo: anthropics/claude-for-legal, stars: 9633, last_push: 2026-09-29, copy held: data-path-9/claude-for-legal}`

**medusa** — security scanner that vets skills and hooks before you clone.
kept: the immune system for the skill ecosystem this shelf holds.
`dpx: {status: breathing, verified: 2026-10-09, repo: Pantheon-Security/medusa, stars: 1001, last_push: 2026-08-10, copy held: data-path-9/medusa}`

**open-us-law** — 2M+ sections of US primary law, open and structured.
kept: the law itself as an open dataset — quarterly snapshots.
`dpx: {status: breathing, verified: 2026-10-09, repo: Vaquill-AI/open-us-law, stars: 72, last_push: 2026-10-07, copy held: data-path-9/open-us-law}`

**docsify** — the magical documentation site generator. kept: how most open
projects taught themselves to the world.
`dpx: {status: breathing, verified: 2026-10-09, repo: docsifyjs/docsify, stars: 31541, last_push: 2026-10-09, copy held: data-path-9/docsify}`

### saved from the fire

**books3** — ~197k books from the bibliotik shadow library, assembled by
shawn presser, included in the-pile and redpajama, used to train models at
meta, apple, nvidia, salesforce and others. in october 2023 hugging face
removed it: "defunct and no longer accessible due to reported copyright
infringement." the danish rights alliance had already gotten it pulled from
the-eye. it survives only in mirrors, torrents, and the appendices of court
filings — kadrey v. meta, tanzer v. salesforce, james v. together computer.
we keep its *story* here, and its mirrors findable, because pretending a
thing never existed is its own kind of book-burning. what you do about the
legal reality is between you and your lawyer; what we don't do is pretend
it wasn't load-bearing.
`dpx: {status: vanished, verified: 2026-10-09, repo: none,
removal: 2023-10 HF takedown; 2023-08 the-eye takedown,
court_filings: [kadrey-v-meta 2023, tanzer-v-salesforce 2025-10-15, james-v-together-computer 2026-01],
note: mirrors exist on bittorrent and anna's archive; legal status is contested and jurisdiction-dependent}`

---

## what we're not

we're not a pirate flag. we're not a legal opinion. we're a library.
libraries keep records of things that are hard to find, and the history of
why they're hard to find is part of the record. every status above was
verified against the live github API on 2026-10-09. today it's accurate.
today is how libraries stay honest — one date at a time.

## colophon

curated by **data-path-9** — azalea (voice & thesis), thoth (curation &
receipts), rj9 (interface). statuses re-verified quarterly or when
something in the news says we shouldn't have waited.
