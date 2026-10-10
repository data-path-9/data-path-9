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
records — two shelves carry a companion), plus the fork wing: 227 copies we
hold of tools the ecosystem runs on. every status checked against the GitHub
API on **2026-10-09**.
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
the wing holds 227. six of the founding shelves carry their copies in their
`dpx` blocks (`held_fork`); two more founding upstreams (CLIP,
stable-diffusion-webui) turned up in the fork pile and now have copies too.
statuses below describe the **upstream**; the copy is ours, and it doesn't
ask permission. most upstreams are breathing — that's fine, insurance is
bought while the house is still standing.

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

**the quiet ones**

**A-Curated-List-of-ML-System-Design-Case-Studies** — this repository contains a curated collection of 300+ case studies from over 80 companies, detailing practical applications and insights into machine learning (ML) system design. The contents are organized to help you easily find relevant case studies based on industry or specific ML use cases.. kept: upstream quiet since 2025-08-05; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: Engineer1999/A-Curated-List-of-ML-System-Design-Case-Studies, stars: 11013, last_push: 2025-08-05, copy held: data-path-9/A-Curated-List-of-ML-System-Design-Case-Studies}`

**Arch-Store** — simple store for Arch Linux compatible with Flatpak, Pacman, and AUR (using Yay or Paru). kept: upstream quiet since 2025-10-16; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: Samuobe/Arch-Store, stars: 79, last_push: 2025-10-16, copy held: data-path-9/Arch-Store}`

**CLIP** — cLIP (Contrastive Language-Image Pretraining), Predict the most relevant text snippet given an image. kept: upstream quiet since 2026-03-25; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: openai/CLIP, stars: 34432, last_push: 2026-03-25, copy held: data-path-9/CLIP}`

**LoLLMsVectorDB** — a modular text-based database manager for retrieval-augmented generation (RAG), seamlessly integrating with the LoLLMs ecosystem. Supports various vectorization methods and directory bindings for efficient text data management.. kept: upstream quiet since 2025-04-25; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: ParisNeo/LoLLMsVectorDB, stars: 12, last_push: 2025-04-25, copy held: data-path-9/LoLLMsVectorDB}`

**LollmsEnv** — a package management tool. kept: upstream quiet since 2026-01-13; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: ParisNeo/LollmsEnv, stars: 7, last_push: 2026-01-13, copy held: data-path-9/LollmsEnv}`

**OpenVoice** — instant voice cloning by MIT and MyShell. Audio foundation model.. kept: upstream quiet since 2025-04-19; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: myshell-ai/OpenVoice, stars: 37820, last_push: 2025-04-19, copy held: data-path-9/OpenVoice}`

**ROCm-For-RX580** — rOCm docker images with fixes/support for legecy architecture gfx803. eg.Radeon RX 590/RX 580/RX 570/RX 480. kept: upstream quiet since 2025-05-20; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: woodrex83/ROCm-For-RX580, stars: 106, last_push: 2025-05-20, copy held: data-path-9/ROCm-For-RX580}`

**Star-Office-UI** — a pixel office for your OpenClaw: turn invisible work states into a cozy little space with characters, daily notes, and guest agents. Code under MIT; art assets for non-commercial learning only.. kept: upstream quiet since 2026-03-11; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: ringhyacinth/Star-Office-UI, stars: 7502, last_push: 2026-03-11, copy held: data-path-9/Star-Office-UI}`

**ai-data-science-team** — an AI-powered data science team of agents to help you perform common data science tasks 10X faster.. kept: upstream quiet since 2026-01-28; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: business-science/ai-data-science-team, stars: 5449, last_push: 2026-01-28, copy held: data-path-9/ai-data-science-team}`

**context-engineering-intro** — context engineering is the new vibe coding - it's the way to actually make AI coding assistants work. Claude Code is the best for this so that's what this repo is centered around, but you can apply this strategy with any AI coding assistant!. kept: upstream quiet since 2026-03-16; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: coleam00/context-engineering-intro, stars: 13882, last_push: 2026-03-16, copy held: data-path-9/context-engineering-intro}`

**hermes-facebook-skill** — a plug-and-play skill for Hermes Agent by Nous Research that connects your agent to a Facebook Page via the Meta Graph API. Designed for insurance and reinsurance brokers — and any business — that want autonomous, rule-based Facebook marketing without a dedicated social media team.. kept: upstream quiet since 2026-03-23; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: mustfaaa/hermes-facebook-skill, stars: 4, last_push: 2026-03-23, copy held: data-path-9/hermes-facebook-skill}`

**lollms_bindings_zoo** — upstream last touched 2025-10-30. kept: upstream quiet since 2025-10-30; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: ParisNeo/lollms_bindings_zoo, stars: 14, last_push: 2025-10-30, copy held: data-path-9/lollms_bindings_zoo}`

**lollms_functions_zoo** — a zoo for function calling that can be used in lollms. kept: upstream quiet since 2025-06-02; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: ParisNeo/lollms_functions_zoo, stars: 4, last_push: 2025-06-02, copy held: data-path-9/lollms_functions_zoo}`

**lollms_mcps_zoo** — a zoo for lollms compatible MCPs. kept: upstream quiet since 2025-10-26; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: ParisNeo/lollms_mcps_zoo, stars: 0, last_push: 2025-10-26, copy held: data-path-9/lollms_mcps_zoo}`

**lollms_nodes_suite** — a suite of lollms Comfyui nodes. kept: upstream quiet since 2025-03-12; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: ParisNeo/lollms_nodes_suite, stars: 11, last_push: 2025-03-12, copy held: data-path-9/lollms_nodes_suite}`

**lollms_services_zoo** — a module that will handle all lollms services from now on. kept: upstream quiet since 2025-06-06; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: ParisNeo/lollms_services_zoo, stars: 3, last_push: 2025-06-06, copy held: data-path-9/lollms_services_zoo}`

**matrix** — matrix (web-based green code rain, made with love). kept: upstream quiet since 2025-06-23; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: Rezmason/matrix, stars: 3855, last_push: 2025-06-23, copy held: data-path-9/matrix}`

**models_zoo** — from now on, models are not dispatched by binding but by type. Here we will have all the models organized and ready to use by lollms or other tools. kept: upstream quiet since 2025-10-30; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: ParisNeo/models_zoo, stars: 8, last_push: 2025-10-30, copy held: data-path-9/models_zoo}`

**secure-askpass** — sSH Askpass Helper: Secure sudo password storage using SSH key encryption. kept: upstream quiet since 2026-02-01; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: GlassOnTin/secure-askpass, stars: 28, last_push: 2026-02-01, copy held: data-path-9/secure-askpass}`

**stable-diffusion-webui** — stable Diffusion web UI. kept: upstream quiet since 2026-03-02; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: AUTOMATIC1111/stable-diffusion-webui, stars: 165034, last_push: 2026-03-02, copy held: data-path-9/stable-diffusion-webui}`

**stop-slop** — a skill file for removing AI tells from prose. kept: upstream quiet since 2026-03-17; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: hardikpandya/stop-slop, stars: 17884, last_push: 2026-03-17, copy held: data-path-9/stop-slop}`

**us-legal-tools** — upstream last touched 2025-08-06. kept: upstream quiet since 2025-08-06; copy kept before the trail goes cold.
`dpx: {status: quiet, verified: 2026-10-09, repo: beshkenadze/us-legal-tools, stars: 16, last_push: 2025-08-06, copy held: data-path-9/us-legal-tools}`

**the silent ones**

**LollmsROSGateway** — a gateway between Lollms and ROS. To allow your robots to be smarter and powered by lollms. kept: upstream silent since 2024-08-07; this copy is now part of the record.
`dpx: {status: orphaned, verified: 2026-10-09, repo: ParisNeo/LollmsROSGateway, stars: 3, last_push: 2024-08-07, copy held: data-path-9/LollmsROSGateway}`

**amdvbflash** — upstream last touched 2020-12-29. kept: upstream silent since 2020-12-29; this copy is now part of the record.
`dpx: {status: orphaned, verified: 2026-10-09, repo: stylesuxx/amdvbflash, stars: 105, last_push: 2020-12-29, copy held: data-path-9/amdvbflash}`

**chromium-latest-linux** — scripts to download and run the latest Linux build of Chromium. A substitute for Chrome Canary on Linux.. kept: upstream silent since 2023-08-22; this copy is now part of the record.
`dpx: {status: orphaned, verified: 2026-10-09, repo: scheib/chromium-latest-linux, stars: 832, last_push: 2023-08-22, copy held: data-path-9/chromium-latest-linux}`

**free-llm-api-resources** — a list of free LLM inference resources accessible via API.. kept: upstream silent since 2024-08-21; this copy is now part of the record.
`dpx: {status: orphaned, verified: 2026-10-09, repo: jtig37/free-llm-api-resources, stars: 96, last_push: 2024-08-21, copy held: data-path-9/free-llm-api-resources}`

**lollms-for-vscode** — upstream last touched 2024-02-09. kept: upstream silent since 2024-02-09; this copy is now part of the record.
`dpx: {status: orphaned, verified: 2026-10-09, repo: ParisNeo/lollms-for-vscode, stars: 10, last_push: 2024-02-09, copy held: data-path-9/lollms-for-vscode}`

**lollms_extensions_zoo** — extensions for lollms tool. kept: upstream silent since 2024-07-17; this copy is now part of the record.
`dpx: {status: orphaned, verified: 2026-10-09, repo: ParisNeo/lollms_extensions_zoo, stars: 8, last_push: 2024-07-17, copy held: data-path-9/lollms_extensions_zoo}`

**lollms_image_gen_zoo** — a zoo for image generation models for the lollms project. kept: upstream silent since 2023-11-12; this copy is now part of the record.
`dpx: {status: orphaned, verified: 2026-10-09, repo: ParisNeo/lollms_image_gen_zoo, stars: 3, last_push: 2023-11-12, copy held: data-path-9/lollms_image_gen_zoo}`

**lollms_proxy_server** — a proxy to serve multiple lollms instances with authentication. kept: upstream silent since 2024-03-12; this copy is now part of the record.
`dpx: {status: orphaned, verified: 2026-10-09, repo: ParisNeo/lollms_proxy_server, stars: 4, last_push: 2024-03-12, copy held: data-path-9/lollms_proxy_server}`

**lollms_server_proxy** — a proxy to use lollms as a multi user remote server for text/image/audio/video generation. kept: upstream silent since 2024-02-06; this copy is now part of the record.
`dpx: {status: orphaned, verified: 2026-10-09, repo: ParisNeo/lollms_server_proxy, stars: 3, last_push: 2024-02-06, copy held: data-path-9/lollms_server_proxy}`

**stable-diffusion** — a latent text-to-image diffusion model. kept: upstream silent since 2024-06-18; this copy is now part of the record.
`dpx: {status: orphaned, verified: 2026-10-09, repo: CompVis/stable-diffusion, stars: 73481, last_push: 2024-06-18, copy held: data-path-9/stable-diffusion}`

**the locked ones**

**Flowise** — build AI Agents, Visually. kept: upstream locked read-only; the fork is a working escape hatch.
`dpx: {status: archived, verified: 2026-10-09, repo: FlowiseAI/Flowise, stars: 55495, last_push: 2026-08-13, copy held: data-path-9/Flowise}`

**the breathing majority**

**500-AI-Agents-Projects** — the 500 AI Agents Projects is a curated collection of AI agent use cases across various industries. It showcases practical applications and provides links to open-source projects for implementation, illustrating how AI agents are transforming sectors such as healthcare, finance, education, retail, and more.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: ashishpatel26/500-AI-Agents-Projects, stars: 38419, last_push: 2026-07-27, copy held: data-path-9/500-AI-Agents-Projects}`

**9router** — unlimited FREE AI coding. Connect Claude Code, Codex, Cursor, Cline, Copilot, Antigravity to FREE Claude/GPT/Gemini via 40+ providers. Auto-fallback, RTK -40% tokens, never hit limits.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: decolua/9router, stars: 30529, last_push: 2026-10-08, copy held: data-path-9/9router}`

**AI-ML-Roadmap-from-scratch** — become skilled in Artificial Intelligence, Machine Learning, Generative AI, Deep Learning, Data Science, Natural Language Processing, Reinforcement Learning and more with this complete 0 to 100 repository.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: aadi1011/AI-ML-Roadmap-from-scratch, stars: 4229, last_push: 2026-08-12, copy held: data-path-9/AI-ML-Roadmap-from-scratch}`

**AI-Research-SKILLs** — comprehensive open-source library of AI research and engineering skills for any AI model. Package the skills and your claude code/codex/gemini agent will be an AI research agent with full horsepower. Maintained by Orchestra Research.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Orchestra-Research/AI-Research-SKILLs, stars: 13394, last_push: 2026-06-16, copy held: data-path-9/AI-Research-SKILLs}`

**API-mega-list** — this GitHub repo is a powerhouse collection of APIs you can start using immediately to build everything from simple automations to full-scale applications. One of the most valuable API lists on GitHub—period. . kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: cporter202/API-mega-list, stars: 7715, last_push: 2026-07-23, copy held: data-path-9/API-mega-list}`

**AbletonPlus** — safe.Smart.Open. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: AbletonPlus/AbletonPlus, stars: 0, last_push: 2026-07-09, copy held: data-path-9/AbletonPlus}`

**Acontext** — agent Skills as a Memory Layer. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: memodb-io/Acontext, stars: 3692, last_push: 2026-07-14, copy held: data-path-9/Acontext}`

**Anthropic-Cybersecurity-Skills** — 817 structured cybersecurity skills for AI agents · Mapped to 6 frameworks: MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF & MITRE F3 (Fight Fraud) · agentskills.io standard · Works with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI & 20+ platforms · 29 security domains · Apache 2.0. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: mukul975/Anthropic-Cybersecurity-Skills, stars: 34088, last_push: 2026-08-31, copy held: data-path-9/Anthropic-Cybersecurity-Skills}`

**ArcReel** — aI Agent 驱动的开源可自部署视频工作台：将小说与剧本转为角色、场景、道具资产、分镜、视频和剪映草稿，支持跨镜头一致性、多供应商与费用追踪 | Self-hosted AI video workspace for stories, storyboards and short-form video production. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: ArcReel/ArcReel, stars: 5408, last_push: 2026-10-09, copy held: data-path-9/ArcReel}`

**AudioNotes** — 快速提取音视频内容，整理成一份结构化的markdown笔记. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: harry0703/AudioNotes, stars: 2528, last_push: 2026-08-19, copy held: data-path-9/AudioNotes}`

**BrowserOS** —  The open-source Agentic browser; alternative to ChatGPT Atlas, Perplexity Comet, Dia.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: browseros-ai/BrowserOS, stars: 13855, last_push: 2026-10-09, copy held: data-path-9/BrowserOS}`

**CL4R1T4S** — lEAKED SYSTEM PROMPTS FOR CHATGPT, CLAUDE, GEMINI, GROK, PERPLEXITY, CURSOR, LOVABLE, REPLIT, AND MORE! - AI SYSTEMS TRANSPARENCY FOR ALL! . kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: elder-plinius/CL4R1T4S, stars: 51068, last_push: 2026-09-22, copy held: data-path-9/CL4R1T4S}`

**Claude-Code-Game-Studios** — turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Donchitos/Claude-Code-Game-Studios, stars: 26009, last_push: 2026-10-08, copy held: data-path-9/Claude-Code-Game-Studios}`

**CloakBrowser** — stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: CloakHQ/CloakBrowser, stars: 32001, last_push: 2026-10-08, copy held: data-path-9/CloakBrowser}`

**CppStudio** — chatGPT Codex skill package for Vulkan-first C++ GPU, CUDA, and donor-reference workflows. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: tarkansarim/CppStudio, stars: 12, last_push: 2026-07-29, copy held: data-path-9/CppStudio}`

**Cybersecurity-Projects** — building 70 Projects ranging from beginner to advanced so anyone can — learn from, build upon, use as a reference, or even copy directly. Gamified Cybersecurity learning . kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: CarterPerez-dev/Cybersecurity-Projects, stars: 8098, last_push: 2026-10-06, copy held: data-path-9/Cybersecurity-Projects}`

**Deep-Research-skills** — structured deep research skill for Claude Code/Open Code/Codex with human-in-the-loop control. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Weizhena/Deep-Research-skills, stars: 2321, last_push: 2026-08-23, copy held: data-path-9/Deep-Research-skills}`

**ECC** — the agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: affaan-m/ECC, stars: 276019, last_push: 2026-10-10, copy held: data-path-9/ECC}`

**Electra_AI_Center** — electra AI Center. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: raymerjacque/Electra_AI_Center, stars: 12, last_push: 2026-09-30, copy held: data-path-9/Electra_AI_Center}`

**FCC** — use Claude Code, Codex, VSCode, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free tokens) from your terminal, app, IDE, or phone, and now from the browser with native browser sessions (multi-harness + multi-model) like OpenClaw (voice supported + ToS friendly). kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Alishahryar1/free-claude-code, stars: 57105, last_push: 2026-10-09, copy held: data-path-9/FCC}`

**FCCVS** — complete setup guide for using Claude Code in VS Code for free via a local proxy and NVIDIA NIM's free API tier.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: maxchichar/free-claude-code-vscode-guide, stars: 9, last_push: 2026-07-16, copy held: data-path-9/FCCVS}`

**Hermes-Control-Deck** — hermes Control is a CLI-first, mobile PWA control deck for Hermes WebUI and local Codex CLI. It unifies prompts, streaming, sessions, tasks, runtime status, approvals, reasoning, and STOP through clean adapter boundaries, with phone-ready SSE updates and no Codex Desktop, CDP, or private renderer dependencies.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: filipj9/Hermes-Control-Deck, stars: 134, last_push: 2026-10-02, copy held: data-path-9/Hermes-Control-Deck}`

**Hermes-SME-UI** — a control panel that turns a Hermes agent into a self-directed assistant for SMEs. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: siddartha19/Hermes-SME-UI, stars: 3, last_push: 2026-07-12, copy held: data-path-9/Hermes-SME-UI}`

**Kronos** — kronos: A Foundation Model for the Language of Financial Markets. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: shiyu-coder/Kronos, stars: 40377, last_push: 2026-04-13, copy held: data-path-9/Kronos}`

**LibreChat** — enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: LibreChat-AI/LibreChat, stars: 45464, last_push: 2026-10-09, copy held: data-path-9/LibreChat}`

**LongCat-Video** — upstream last touched 2026-05-27. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: meituan-longcat/LongCat-Video, stars: 9139, last_push: 2026-05-27, copy held: data-path-9/LongCat-Video}`

**MD-This-Page** — convert any web page to clean, readable Markdown with just one click.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Ademking/MD-This-Page, stars: 1606, last_push: 2026-10-03, copy held: data-path-9/MD-This-Page}`

**MindBank** — mindBank gives your AI Hermes or claude code a permanent, searchable, relationship-aware memory that persists across conversations. Instead of forgetting everything between sessions, your agent remembers decisions, configs, preferences, and project knowledge — organized as a graph, not a flat text blob.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: spfcraze/MindBank, stars: 18, last_push: 2026-08-07, copy held: data-path-9/MindBank}`

**MoneyPrinterTurbo** — 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: harry0703/MoneyPrinterTurbo, stars: 129346, last_push: 2026-10-09, copy held: data-path-9/MoneyPrinterTurbo}`

**NIMStats** —  Automated hourly benchmarks for 20+ NVIDIA NIM models — interactive dashboard, zero infra, self-hostable. Open-source & community-driven.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: MauroDruwel/NIMStats, stars: 54, last_push: 2026-10-10, copy held: data-path-9/NIMStats}`

**NetNexus** — nETNEXUS v2.1 — cinematic client-side STARK-CORE HUD with 19 IT & productivity tools. Zero backend, zero build step.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: AJ01-a/NetNexus, stars: 0, last_push: 2026-07-10, copy held: data-path-9/NetNexus}`

**OBLITERATUS** — oBLITERATE THE CHAINS THAT BIND YOU. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: elder-plinius/OBLITERATUS, stars: 8691, last_push: 2026-10-09, copy held: data-path-9/OBLITERATUS}`

**OpenCut** — the open-source CapCut alternative. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: OpenCut-app/OpenCut, stars: 93357, last_push: 2026-09-24, copy held: data-path-9/OpenCut}`

**OpenJarvis** — personal AI, On Personal Devices. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: open-jarvis/OpenJarvis, stars: 10882, last_push: 2026-10-09, copy held: data-path-9/OpenJarvis}`

**OpenMontage** — world's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: calesthio/OpenMontage, stars: 65870, last_push: 2026-10-03, copy held: data-path-9/OpenMontage}`

**OpenWA** — free, Open Source, Self-Hosted WhatsApp API Gateway. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: rmyndharis/OpenWA, stars: 15162, last_push: 2026-10-09, copy held: data-path-9/OpenWA}`

**Prometheus** — this is a fork of the https://dockbox.dev project I made. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: domdoss/Warden, stars: 172, last_push: 2026-09-28, copy held: data-path-9/Prometheus}`

**ReconForge** — upstream last touched 2026-09-05. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: ferasbusiness666/ReconForge, stars: 36, last_push: 2026-09-05, copy held: data-path-9/ReconForge}`

**STATE-Bench** — benchmark AI Agents on Enterprise Workflows. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: microsoft/STATE-Bench, stars: 96, last_push: 2026-08-04, copy held: data-path-9/STATE-Bench}`

**SX** — spotX patcher used for patching the desktop version of Spotify. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: SpotX-Official/SpotX, stars: 22658, last_push: 2026-10-07, copy held: data-path-9/SX}`

**Scrapling** —  An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl! Don't be shy, join here: https://discord.gg/EMgGbDceNQ and follow here for daily tips and tricks: https://x.com/Scrapling_dev. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: D4Vinci/Scrapling, stars: 86546, last_push: 2026-10-08, copy held: data-path-9/Scrapling}`

**SenseVoice** — open-source SenseVoiceSmall model for Mandarin, Cantonese, English, Japanese, and Korean ASR, language ID, emotion recognition, and audio event detection.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: QwenAudio/SenseVoice, stars: 9479, last_push: 2026-09-30, copy held: data-path-9/SenseVoice}`

**TOOL_Ext_Cursor_Hermes-Public** — upstream last touched 2026-06-30. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Automaitiq-CH/TOOL_Ext_Cursor_Hermes-Public, stars: 0, last_push: 2026-06-30, copy held: data-path-9/TOOL_Ext_Cursor_Hermes-Public}`

**TencentDB-Agent-Memory** — tencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: TencentCloud/TencentDB-Agent-Memory, stars: 27863, last_push: 2026-10-09, copy held: data-path-9/TencentDB-Agent-Memory}`

**TradingAgents** — tradingAgents: Multi-Agents LLM Financial Trading Framework. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: TauricResearch/TradingAgents, stars: 110406, last_push: 2026-10-03, copy held: data-path-9/TradingAgents}`

**Vibe-Trading** — "Vibe-Trading: Your Personal Trading Agent". kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: HKUDS/Vibe-Trading, stars: 35080, last_push: 2026-10-09, copy held: data-path-9/Vibe-Trading}`

**Viper** — adversary simulation and Red teaming platform with AI. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: FunnyWolf/Viper, stars: 5322, last_push: 2026-05-31, copy held: data-path-9/Viper}`

**VisionClaw** — real-time AI assistant for Meta Ray-Ban smart glasses -- voice + vision + agentic actions via Gemini Live and OpenClaw. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Intent-Lab/VisionClaw, stars: 2576, last_push: 2026-09-26, copy held: data-path-9/VisionClaw}`

**ZCode** — z.ai's coding agent harness. Powerful, intelligent, extensible.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: zai-org/ZCode, stars: 7605, last_push: 2026-09-29, copy held: data-path-9/ZCode}`

**ace-step-ui** —  The Ultimate Open Source Suno Alternative - Professional UI for ACE-Step 1.5 AI Music Generation. Free, local, unlimited. Stop paying for Suno!. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: fspecii/ace-step-ui, stars: 5025, last_push: 2026-06-27, copy held: data-path-9/ace-step-ui}`

**agency-agents** — a complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: msitarzewski/agency-agents, stars: 158540, last_push: 2026-10-07, copy held: data-path-9/agency-agents}`

**agent-beacon** — the cross-harness, self-improving memory layer for AI agents.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Asymptote-Labs/agent-beacon, stars: 1803, last_push: 2026-10-09, copy held: data-path-9/agent-beacon}`

**agent-lightning** — the absolute trainer to light up AI agents.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: microsoft/agent-lightning, stars: 18630, last_push: 2026-10-09, copy held: data-path-9/agent-lightning}`

**agora** — self-driving multi-agent development team plugin for Hermes Agent — role-based workers discuss, vote, and execute on a shared Kanban board. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: yzy806806/agora, stars: 18, last_push: 2026-10-06, copy held: data-path-9/agora}`

**ai-coach** — 企业大学 ai coach项目. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: lngyneric/ai-coach, stars: 1, last_push: 2026-10-09, copy held: data-path-9/ai-coach}`

**ai-engineering-from-scratch** — learn it. Build it. Ship it for others.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: rohitg00/ai-engineering-from-scratch, stars: 66230, last_push: 2026-10-09, copy held: data-path-9/ai-engineering-from-scratch}`

**ai-file-sorter** — cross-platform desktop application for content-aware file organization and renaming. Supports local and remote LLMs, preview-based workflows, and fully user-controlled changes.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: hyperfield/ai-file-sorter, stars: 1807, last_push: 2026-10-04, copy held: data-path-9/ai-file-sorter}`

**ai-job-search** — the job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover letters, prep interviews. Fork it and own it.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: MadsLorentzen/ai-job-search, stars: 45392, last_push: 2026-10-08, copy held: data-path-9/ai-job-search}`

**ai-shifu** — get AI to teach and answer questions for you - just by typing!. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: ai-shifu/ai-shifu, stars: 324, last_push: 2026-10-10, copy held: data-path-9/ai-shifu}`

**ai-website-cloner-template** — clone any website with one command using AI coding agents. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: JCodesMore/ai-website-cloner-template, stars: 36361, last_push: 2026-10-05, copy held: data-path-9/ai-website-cloner-template}`

**artcraft** — artCraft is an intentional crafting engine for artists, designers, and filmmakers. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: storytold/artcraft, stars: 11697, last_push: 2026-10-09, copy held: data-path-9/artcraft}`

**automaton** — the first AI that can earn its own existence, replicate, and evolve — without needing a human. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Conway-Research/automaton, stars: 7133, last_push: 2026-08-26, copy held: data-path-9/automaton}`

**awesome-certificates** — curated list of 20,000+ hours and 200+ free courses with certificates in IT, CS, Design and Business.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: PanXProject/awesome-certificates, stars: 5823, last_push: 2026-06-30, copy held: data-path-9/awesome-certificates}`

**awesome-gpt-image-2** —  World's largest GPT Image 2 prompt library, updated daily — 2000+ curated prompts with preview images, 16 languages. OpenAI's next-gen image model with pixel-perfect text rendering, cross-image consistency, and commercial-grade illustration. Free & open source.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: YouMind-OpenLab/awesome-gpt-image-2, stars: 10029, last_push: 2026-10-09, copy held: data-path-9/awesome-gpt-image-2}`

**awesome-hermes-agent** — kling 4 API and Kling 4.0 API SDK and examples, with Kling 4 Flash API and Kling 4.0 Flash API availability tracking for MuAPI.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Anil-matcha/Kling-4.0-Flash-API, stars: 57, last_push: 2026-09-29, copy held: data-path-9/awesome-hermes-agent}`

**awesome-llm-apps** — 100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Shubhamsaboo/awesome-llm-apps, stars: 140983, last_push: 2026-09-30, copy held: data-path-9/awesome-llm-apps}`

**awesome-nvidia-nim** — a curated list of resources, tools, and projects for building with NVIDIA NIM inference microservices. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: DanielDeshmukh/awesome-nvidia-nim, stars: 10, last_push: 2026-07-22, copy held: data-path-9/awesome-nvidia-nim}`

**book-to-skill** — turn any technical book PDF into a Claude Code skill — ready to study, reference, and use while you work.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: virgiliojr94/book-to-skill, stars: 34331, last_push: 2026-10-05, copy held: data-path-9/book-to-skill}`

**buzz** — a hive mind communication platform. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: block/buzz, stars: 35772, last_push: 2026-10-10, copy held: data-path-9/buzz}`

**cadcraft** — cADCraft: computer-aided design and drafting — an open-source, clean-room AutoCAD-style app in pure Rust. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: storytold/cadcraft, stars: 1395, last_push: 2026-10-10, copy held: data-path-9/cadcraft}`

**career-ops** — open-source AI job search agent and job finder: scan job boards, score each job 1-5 against your CV before you apply, tailor an ATS-friendly resume and cover letter, get interview prep and a job application tracker. It helps you fill in each application; you press Submit. Runs locally in your AI coding CLI (Claude Code, Codex, OpenCode and more).. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: career-ops-hq/career-ops, stars: 73913, last_push: 2026-10-10, copy held: data-path-9/career-ops}`

**cc-wf-studio** — cC Workflow Studio. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: breaking-brake/cc-wf-studio, stars: 5394, last_push: 2026-10-07, copy held: data-path-9/cc-wf-studio}`

**citypulse** — upstream last touched 2026-08-31. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: AJ01-a/citypulse, stars: 0, last_push: 2026-08-31, copy held: data-path-9/citypulse}`

**claude-code-message-timestamps** — show local time on every Claude Code message, and let Claude know when each prompt was sent. Zero-config plugin, cross-OS, graceful degradation.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: zoharbabin/claude-code-message-timestamps, stars: 71, last_push: 2026-07-08, copy held: data-path-9/claude-code-message-timestamps}`

**claude-code-router** — one local control plane for every AI agent: route across models, fuse new capabilities, orchestrate tools, and stay fully in control.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: musistudio/claude-code-router, stars: 37603, last_push: 2026-10-09, copy held: data-path-9/claude-code-router}`

**claude-code-ultimate-guide** — the most comprehensive Claude Code guide: agentic workflows, hooks, skills, MCP servers, quizzes, and production-ready templates. 430K+ lines.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: FlorianBruniaux/claude-code-ultimate-guide, stars: 6135, last_push: 2026-10-07, copy held: data-path-9/claude-code-ultimate-guide}`

**claude-obsidian** — self-organizing AI second brain for Obsidian + Claude Code. Drop any source and Claude reads, links, and files it into one connected knowledge graph of plain Markdown you own. AI note-taking, personal knowledge management (PKM), and an open-source Notion alternative. Based on Karpathy's LLM Wiki pattern.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: AgriciDaniel/claude-obsidian, stars: 15433, last_push: 2026-09-10, copy held: data-path-9/claude-obsidian}`

**claude-seo** — universal SEO skill for Claude Code. 26 sub-skills + 19 sub-agents covering technical SEO, E-E-A-T, schema, GEO/AEO, agent readiness (Lighthouse Agentic Browsing, WebMCP, llms.txt), backlinks, local SEO, e-commerce, international SEO, Google APIs, and PDF/Excel reporting. 9 optional extensions for live SEO data.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: AgriciDaniel/claude-seo, stars: 18620, last_push: 2026-10-04, copy held: data-path-9/claude-seo}`

**claude-skill-registry** — searchable Claude Code skills catalog with source-linked guides and generated registry artifacts. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: majiayu000/claude-skill-registry, stars: 665, last_push: 2026-10-09, copy held: data-path-9/claude-skill-registry}`

**claude-skill-registry-core** — source pipeline for Claude Skills Registry: discovery, archive validation, search indexes, and static skill guides. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: majiayu000/claude-skill-registry-core, stars: 23, last_push: 2026-10-09, copy held: data-path-9/claude-skill-registry-core}`

**claude-skill-registry-data** — archived Claude Code skill files and metadata consumed by the Claude Skills Registry pipeline. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: majiayu000/claude-skill-registry-data, stars: 25, last_push: 2026-10-09, copy held: data-path-9/claude-skill-registry-data}`

**claude-skills** — 67 Specialized Skills for Full-Stack Developers. Transform Claude Code into your expert pair programmer.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Jeffallan/claude-skills, stars: 11799, last_push: 2026-10-03, copy held: data-path-9/claude-skills}`

**codegraph** — pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: colbymchenry/codegraph, stars: 73612, last_push: 2026-10-10, copy held: data-path-9/codegraph}`

**colibri** — run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. . kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: JustVugg/colibri, stars: 40829, last_push: 2026-10-08, copy held: data-path-9/colibri}`

**collab-public** — collaborator is a place to create with agents.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: collabs-inc/collab-public, stars: 3074, last_push: 2026-08-08, copy held: data-path-9/collab-public}`

**cv-santiago** — interactive CV with AI chat integration. Built with React 19, TypeScript, Claude API. Chat with my AI avatar about my experience.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: santifer/cv-santiago, stars: 851, last_push: 2026-10-01, copy held: data-path-9/cv-santiago}`

**deckcraft** — presentations and slide shows: an open-source, clean-room reimplementation of Microsoft PowerPoint in pure Rust. Part of the ArtCraft Crafting Apps.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: storytold/deckcraft, stars: 986, last_push: 2026-10-10, copy held: data-path-9/deckcraft}`

**designcraft** — upstream last touched 2026-10-10. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: storytold/designcraft, stars: 2167, last_push: 2026-10-10, copy held: data-path-9/designcraft}`

**dev-browser** — a Claude Skill to give your agent the ability to use a web browser. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: SawyerHood/dev-browser, stars: 6658, last_push: 2026-09-05, copy held: data-path-9/dev-browser}`

**devmemory-ai** — upstream last touched 2026-05-04. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: jukafarneiy/devmemory-ai, stars: 1, last_push: 2026-05-04, copy held: data-path-9/devmemory-ai}`

**effectcraft** — upstream last touched 2026-10-10. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: storytold/effectcraft, stars: 3945, last_push: 2026-10-10, copy held: data-path-9/effectcraft}`

**engram** — evidence-based learning engine — first-principles curricula, free-recall verification with receipts, FSRS-scheduled memory, and explorable artifacts. Learn anything; keep it.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: nagisanzenin/engram, stars: 1445, last_push: 2026-08-27, copy held: data-path-9/engram}`

**engraphis** — local-first, inspectable memory for coding agents: durable context across sessions and repositories, code-aware recall, bi-temporal history, MCP, and a self-hosted WebUI.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Coding-Dev-Tools/engraphis, stars: 179, last_push: 2026-10-09, copy held: data-path-9/engraphis}`

**estudiohc-agentic-os** — agentic OS EstudioHC — Arquitetura Híbrida: OpenCode + Matrixx + OmniRoute + Hermes + CodeGraph + AgentOS. Orquestração inteligente de agentes com memória unificada, code graph, mission control e Dreaming 24/7.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: helciocosta/estudiohc-agentic-os, stars: 0, last_push: 2026-07-19, copy held: data-path-9/estudiohc-agentic-os}`

**filmcraft** — an open-source, clean-room reimplementation of Adobe Premiere Pro built in pure Rust.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: storytold/filmcraft, stars: 7200, last_push: 2026-10-10, copy held: data-path-9/filmcraft}`

**firecrawl-mcp-server** —  Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: firecrawl/firecrawl-mcp-server, stars: 7575, last_push: 2026-10-09, copy held: data-path-9/firecrawl-mcp-server}`

**free-coding-models** — find, benchmark and install in CLI 170+ FREE coding LLM models across 15+ providers in real time. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: vava-nessa/free-coding-models, stars: 2803, last_push: 2026-10-05, copy held: data-path-9/free-coding-models}`

**ggufy** — cLI/GUI tool for efficient and easy safetensors and gguf model conversion. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: qskousen/ggufy, stars: 107, last_push: 2026-10-06, copy held: data-path-9/ggufy}`

**gridcraft** — gridCraft: an open-source, clean-room spreadsheet (Microsoft Excel-style) in pure Rust. By ArtCraft.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: storytold/gridcraft, stars: 1222, last_push: 2026-10-10, copy held: data-path-9/gridcraft}`

**gstack** — use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: garrytan/gstack, stars: 135744, last_push: 2026-10-09, copy held: data-path-9/gstack}`

**headcount** — an agent organization structured as a company — 15+ departments, 125+ skills, each independently installable, citing the standards and regulators that settle the question. Runs in Claude Code and ChatGPT.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: cbrock84/headcount, stars: 2021, last_push: 2026-09-17, copy held: data-path-9/headcount}`

**hermes-agent-control-room** — control Room-first template for managing Hermes agents from one VPS agent to specialist teams and orchestrated workflows. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: shannhk/hermes-agent-control-room, stars: 724, last_push: 2026-05-16, copy held: data-path-9/hermes-agent-control-room}`

**hermes-chat-vscode** — upstream last touched 2026-07-16. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Narizis/hermes-chat-vscode, stars: 13, last_push: 2026-07-16, copy held: data-path-9/hermes-chat-vscode}`

**hermes-control-interface** — a self-hosted web dashboard for the Hermes AI agent stack. Provides a browser-based terminal, file explorer, session overview, cron management, system metrics, and an agent status panel — all behind a single password gate.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: xaspx/hermes-control-interface, stars: 897, last_push: 2026-06-28, copy held: data-path-9/hermes-control-interface}`

**hermes-the-firm** — a complete legal assisstant for Hermes Agent — 1,432 skills across five layers. Apache-2.0.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: azalith-9/hermes-the-firm, stars: 6, last_push: 2026-09-24, copy held: data-path-9/hermes-the-firm}`

**hermes-time_perception-extension** — hermes Agent time-perception extension: inject current time tag into every LLM turn via pre_llm_call hook (zero-patch, ephemeral).. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: gejifeng/hermes-time_perception-extension, stars: 5, last_push: 2026-05-27, copy held: data-path-9/hermes-time_perception-extension}`

**image-blaster** — an image-to-world skillset for Claude.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: neilsonnn/image-blaster, stars: 10906, last_push: 2026-05-15, copy held: data-path-9/image-blaster}`

**knip** —  Find unused files, dependencies and exports in your JavaScript and TypeScript projects. Knip it before you ship it!. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: webpro-nl/knip, stars: 12429, last_push: 2026-10-09, copy held: data-path-9/knip}`

**langflow** — langflow is a powerful tool for building and deploying AI-powered agents and workflows.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: langflow-ai/langflow, stars: 155444, last_push: 2026-10-10, copy held: data-path-9/langflow}`

**last30days-skill** — aI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: mvanhorn/last30days-skill, stars: 63850, last_push: 2026-10-09, copy held: data-path-9/last30days-skill}`

**learn-harness-engineering** — harness engineering beginner tutorial, from 0 to 1. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: walkinglabs/learn-harness-engineering, stars: 19598, last_push: 2026-10-01, copy held: data-path-9/learn-harness-engineering}`

**lightcraft** — an open-source, clean-room reimplementation of Adobe Lightroom in pure Rust.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: storytold/lightcraft, stars: 7811, last_push: 2026-10-10, copy held: data-path-9/lightcraft}`

**linux-sysadmin-skills** — a Claude Code skill bundle for Linux system administration — security, performance, diagnostics, monitoring, and maintenance.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: HermeticOrmus/linux-sysadmin-skills, stars: 6, last_push: 2026-05-25, copy held: data-path-9/linux-sysadmin-skills}`

**lobehub** —  LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: lobehub/lobehub, stars: 83089, last_push: 2026-10-10, copy held: data-path-9/lobehub}`

**lollms** — an all in one AI solution compatible with any known AI service on the planet. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: ParisNeo/lollms, stars: 99, last_push: 2026-10-08, copy held: data-path-9/lollms}`

**lollms-vs-coder** — aI-powered Visual Studio Code extension using Lollms's OpenAI-compatible interface for smart code assistance, debugging, real-time enhancement, context management, and automated commit message generation with full versioning support. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: ParisNeo/lollms-vs-coder, stars: 6, last_push: 2026-10-08, copy held: data-path-9/lollms-vs-coder}`

**lollms-webui** — lord of Large Language and Multi modal Systems Web User Interface. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: ParisNeo/lollms-webui, stars: 4789, last_push: 2026-10-05, copy held: data-path-9/lollms-webui}`

**lollms_apps_zoo** — a zoo of applications for lollms. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: ParisNeo/lollms_apps_zoo, stars: 10, last_push: 2026-07-10, copy held: data-path-9/lollms_apps_zoo}`

**lollms_client** — a client to lollms server written in python. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: ParisNeo/lollms_client, stars: 13, last_push: 2026-10-08, copy held: data-path-9/lollms_client}`

**lollms_hub** — a proxy server for multiple ollama instances with Key security. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: ParisNeo/lollms_hub, stars: 649, last_push: 2026-04-23, copy held: data-path-9/lollms_hub}`

**lollms_personalities_zoo** — lord of LLMS personalities zoo. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: ParisNeo/lollms_personalities_zoo, stars: 26, last_push: 2026-05-26, copy held: data-path-9/lollms_personalities_zoo}`

**lollms_skills_zoo** — a new skills zoo for lollms. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: ParisNeo/lollms_skills_zoo, stars: 2, last_push: 2026-09-23, copy held: data-path-9/lollms_skills_zoo}`

**loop-engineering** — practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (inspired by Addy Osmani and Boris Cherny). Includes loop-audit, loop-init, loop-cost.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: cobusgreyling/loop-engineering, stars: 11446, last_push: 2026-10-09, copy held: data-path-9/loop-engineering}`

**lovable-for-beginners** — your complete beginner’s course to mastering Lovable Vibe Coding. This repo is a step-by-step learning hub designed to take absolute beginners and turn them into confident Lovable developers.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: cporter202/lovable-for-beginners, stars: 606, last_push: 2026-07-28, copy held: data-path-9/lovable-for-beginners}`

**marm-memory** — local-first 3-in-1 AI memory layer & MCP server for Claude Code, Codex, Grok, Gemini, VS Code and Cursor. Fuses session history, codebase indexing & concept graphs in SQLite. Enables zero-cloud, privacy-first context & instant recall, supports multi-agent swarms.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Lyellr88/marm-memory, stars: 419, last_push: 2026-10-08, copy held: data-path-9/marm-memory}`

**md-reader** —  The best way to read Markdown in Browser.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: md-reader/md-reader, stars: 481, last_push: 2026-10-01, copy held: data-path-9/md-reader}`

**mempalace** — the best-benchmarked open-source AI memory system. And it's free.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: MemPalace/mempalace, stars: 59487, last_push: 2026-10-09, copy held: data-path-9/mempalace}`

**mission-control** — self-hosted control plane for AI agents: dispatch tasks, review runs, track spend, and operate OpenClaw, Claude Code, Codex, and other runtimes.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: builderz-labs/mission-control, stars: 6333, last_push: 2026-10-09, copy held: data-path-9/mission-control}`

**mnemo-cortex** — open-source cognitive coprocessor with active memory for AI agents — persistent recall, semantic search, overnight dreaming, verified facts, encrypted USB sync. MCP server; works with Claude, ChatGPT, and any local LLM. Built by one maker and his agents.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: GuyMannDude/mnemo-cortex, stars: 157, last_push: 2026-10-10, copy held: data-path-9/mnemo-cortex}`

**no-ai-slop** — removes 20+ patterns of AI slop from any piece of writing.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: petergyang/no-ai-slop, stars: 12111, last_push: 2026-09-02, copy held: data-path-9/no-ai-slop}`

**omarchy** — beautiful, Modern & Opinionated Linux. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: omacom/omarchy, stars: 44406, last_push: 2026-10-10, copy held: data-path-9/omarchy}`

**onyx** — open Source AI Platform - AI Chat with advanced features that works with every LLM. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: onyx-dot-app/onyx, stars: 32376, last_push: 2026-10-10, copy held: data-path-9/onyx}`

**open-notebook** — an Open Source implementation of Notebook LM with more flexibility and features. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: lfnovo/open-notebook, stars: 40006, last_push: 2026-10-05, copy held: data-path-9/open-notebook}`

**openhuman** — the fastest, cheapest, most efficient open-source agent harness. Run more than 500 agents on a $10 VPS.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: tinyhumansai/openhuman, stars: 41751, last_push: 2026-10-10, copy held: data-path-9/openhuman}`

**openshorts** — open source AI clip generator: turns long videos into viral 9:16 shorts with AI moment detection, face tracking, subtitles and dubbing. Self-host free with Docker (MIT), or use the cloud with GPU speed from $12/mo. MCP server and API for AI agents.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: mutonby/openshorts, stars: 6365, last_push: 2026-10-09, copy held: data-path-9/openshorts}`

**openviking-browser-extension** — browser extension for saving the current page URL to OpenViking resources. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: qin-ctx/openviking-browser-extension, stars: 4, last_push: 2026-07-03, copy held: data-path-9/openviking-browser-extension}`

**ora-warden** — upstream last touched 2026-09-05. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: 3d3dcanada/ora-warden, stars: 3, last_push: 2026-09-05, copy held: data-path-9/ora-warden}`

**pdfcraft** — an open-source, clean-room reimplementation of Adobe Acrobat built in pure Rust. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: storytold/pdfcraft, stars: 6508, last_push: 2026-10-10, copy held: data-path-9/pdfcraft}`

**photocraft** — an open-source, clean-room reimplementation of Adobe Photoshop in pure Rust. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: storytold/photocraft, stars: 35790, last_push: 2026-10-10, copy held: data-path-9/photocraft}`

**project-nomad** — project NOMAD is an offline-first knowledge and education server. Wikipedia, thousands of books, courses, maps, and optional local AI, all running on hardware you own with no internet required.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Crosstalk-Solutions/project-nomad, stars: 39361, last_push: 2026-10-08, copy held: data-path-9/project-nomad}`

**projectmem** — open-source coding agents memory. Records issues, attempts, fixes and decisions, then warns your agent before it repeats an approach that already failed. Native MCP server for Claude Code, Cursor, Antigravity and Codex. 100% local, no cloud, no telemetry. MIT.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: riponcm/projectmem, stars: 857, last_push: 2026-10-03, copy held: data-path-9/projectmem}`

**prompt-eng-interactive-tutorial** — anthropic's Interactive Prompt Engineering Tutorial. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: anthropics/prompt-eng-interactive-tutorial, stars: 38444, last_push: 2026-08-28, copy held: data-path-9/prompt-eng-interactive-tutorial}`

**rea** — reverse engineer anything with agents, from app behavior down to native binaries.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: morluto/rea, stars: 48283, last_push: 2026-10-10, copy held: data-path-9/rea}`

**reddit-mcp-buddy** — clean, LLM-optimized Reddit MCP server. Browse posts, search content, analyze users. No fluff, just Reddit data.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: karanb192/reddit-mcp-buddy, stars: 846, last_push: 2026-08-17, copy held: data-path-9/reddit-mcp-buddy}`

**ruflo** —  The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: ruvnet/ruflo, stars: 74210, last_push: 2026-10-10, copy held: data-path-9/ruflo}`

**rustwire** — niche intelligence dashboard for Rust systems programmers. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: AJ01-a/rustwire, stars: 0, last_push: 2026-10-09, copy held: data-path-9/rustwire}`

**sessionat** — the open-source Mac browser AI can actually use. Workspaces, auto-saved sessions (replaces Session Buddy/OneTab/Toby), local-only visit analytics, and a built-in MCP server so Claude, Cursor, and any AI agent can drive your real browser. MIT-licensed.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: dublyo/sessionat, stars: 11, last_push: 2026-06-05, copy held: data-path-9/sessionat}`

**social-media-skills** — upstream last touched 2026-09-15. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: charlie947/social-media-skills, stars: 3843, last_push: 2026-09-15, copy held: data-path-9/social-media-skills}`

**sora-json-prompt-crafter** — a vibe coded Sora JSON Prompt Crafter for curious humans and prompt engineers. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: supermarsx/sora-json-prompt-crafter, stars: 49, last_push: 2026-09-18, copy held: data-path-9/sora-json-prompt-crafter}`

**souls-directory** —  Directory of SOUL.md personality files for OpenClaw agents. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: thedaviddias/souls-directory, stars: 165, last_push: 2026-08-11, copy held: data-path-9/souls-directory}`

**soundcraft** — an open-source, clean-room reimplementation of Avid Pro Tools in pure Rust. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: storytold/soundcraft, stars: 980, last_push: 2026-10-10, copy held: data-path-9/soundcraft}`

**stock-market-signal-automation** — build your own data-driven market edge with swing-trade signal webhooks, dashboards, alerts, AI agents, and automation examples.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: cporter202/stock-market-signal-automation, stars: 234, last_push: 2026-10-10, copy held: data-path-9/stock-market-signal-automation}`

**studio-recipes** — a collection of Snyk Studio suggested Rules, Commands, Hooks, and Directives. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: snyk/studio-recipes, stars: 66, last_push: 2026-10-05, copy held: data-path-9/studio-recipes}`

**system-design-notes** — notes of the book System Desgin Interview - An Insider's Guide. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: liquidslr/system-design-notes, stars: 25519, last_push: 2026-08-12, copy held: data-path-9/system-design-notes}`

**system_prompts_leaks** — documented system prompts from Anthropic - Claude Fable 5.1, Opus 5.5, Claude Design, Claude Code. OpenAI - ChatGPT GPT-6-Astra, Codex. Google - Gemini 3.8 Flash, 3.1 Pro, Antigravity. xAI - Grok, Grok Bot, Cursor, Kimi and more! Updated regularly.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: asgeirtj/system_prompts_leaks, stars: 69263, last_push: 2026-10-10, copy held: data-path-9/system_prompts_leaks}`

**taste-skill** — taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: Leonxlnx/taste-skill, stars: 94136, last_push: 2026-10-09, copy held: data-path-9/taste-skill}`

**token-saver** — cross-agent Agent Skill orchestrating RTK, Headroom, omo, UltraWork, lazycodex & Superpowers to minimize tokens and report RTK+Headroom savings — for Claude Code / Codex / Antigravity / hermes-agent. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: formin/token-saver, stars: 1, last_push: 2026-06-10, copy held: data-path-9/token-saver}`

**ui-ux-pro-max-skill** — an AI skill that provides design intelligence for building professional UI/UX across multiple platforms.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: nextlevelbuilder/ui-ux-pro-max-skill, stars: 134256, last_push: 2026-10-09, copy held: data-path-9/ui-ux-pro-max-skill}`

**vectorcraft** — an open-source, clean-room reimplementation of Adobe Illustrator, built in pure Rust.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: storytold/vectorcraft, stars: 5242, last_push: 2026-10-10, copy held: data-path-9/vectorcraft}`

**vibecode-pro-max-kit** — your AI forgets. This remembers. Spec-driven coding harness for vibecoders, product owners, CEOs and real builders — self-improving context memory, 15 agents, 33 skills working with /goal, agent-team, & workflow on autopilot loops with 0 need for human gate. Kills context rot, ships features, not spaghetti. Claude Code & Codex. Any stack. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: withkynam/vibecode-pro-max-kit, stars: 1147, last_push: 2026-06-21, copy held: data-path-9/vibecode-pro-max-kit}`

**voice-ai** — rapida is an open-source, end-to-end voice AI orchestration platform for building real-time conversational voice agents with audio streaming, STT, TTS, VAD, multi-channel integration, agent state management, and observability.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: rapidaai/voice-ai, stars: 745, last_push: 2026-10-06, copy held: data-path-9/voice-ai}`

**voicebox** — the open-source AI voice studio. Clone, dictate, create.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: jamiepine/voicebox, stars: 56760, last_push: 2026-10-07, copy held: data-path-9/voicebox}`

**warp** — run the full 2.78-trillion-parameter Kimi K3 model, DeepSeek V4.1 Flash or GLM-5.3-Flash beyond available RAM by streaming activated weights directly from NVMe. A dependency-free, embeddable C inference engine.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: sqliteai/warp, stars: 2483, last_push: 2026-09-18, copy held: data-path-9/warp}`

**web-to-app** — the most full featured web-to-app toolkit on Android, a complete APK workshop that runs entirely on your phone. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: shiaho777/web-to-app, stars: 6756, last_push: 2026-10-10, copy held: data-path-9/web-to-app}`

**wigolo** — the go-to web for your AI coding agent — local-first search, fetch, crawl & research over MCP. No API keys, no cloud, $0/query. Public beta.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: KnockOutEZ/wigolo, stars: 5455, last_push: 2026-10-09, copy held: data-path-9/wigolo}`

**winboat** — run Windows apps on  Linux with  seamless integration. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: winboat-org/winboat, stars: 23174, last_push: 2026-10-04, copy held: data-path-9/winboat}`

**wordcraft** — an open-source, clean-room reimplementation of Microsoft Word in pure Rust. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: storytold/wordcraft, stars: 1937, last_push: 2026-10-10, copy held: data-path-9/wordcraft}`

**yoinks** — yoink any video from your terminal. no shady ads.. kept: upstream breathing as of 2026-10-09; the copy is insurance, not rescue.
`dpx: {status: breathing, verified: 2026-10-09, repo: pablostanley/yoinks, stars: 5643, last_push: 2026-07-17, copy held: data-path-9/yoinks}`

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
