# Scratch Academy by GradeNext

A complete **teaching system** for running Scratch classes for ages 7–12 —
not just a library of exercises. Everything is static HTML, CSS and vanilla
JavaScript: no build step, no dependencies, no backend. Drop it on any web
host (or GitHub Pages) and it runs.

---

## What it is

| | |
|---|---|
| **100 sessions** | 2 levels × 50, each a full 60-minute lesson plan |
| **Learn → Practice → Apply** | every session: study the blocks, pass a Recall Test, then build |
| **104 blocks** | every Scratch block explained with an example and the gotcha |
| **490 MCQ questions** | 10 per topic, shuffled each attempt, with teaching explanations |
| **49 concepts** | every Scratch block family, from first block to clones, lists and physics |
| **28 guided projects** | real Raspberry Pi / Code Club projects (CC BY-SA 4.0), 227 steps |
| **90 exercises** | generated game exercises with sprites pre-loaded and no solution code |
| **Assessment** | 3-level rubric per session, tutor notes, skills mastery map |
| **Parent reports** | printable report card and certificates |

### The learning loop

Content alone does not teach. Every session runs the same three stages, and
progress is tracked for each one:

1. **Learn** (`learn.html`) — the idea in plain language, then every new block
   with what it does, a copyable example and the mistake to avoid.
2. **Practice** (`quiz.html`) — a 10-question multiple-choice **Recall Test**
   drawn from a bank of 10+ per topic. Questions and options are reshuffled
   every attempt, each answer gets an explanation that teaches, and 7/10 is
   needed to pass.
3. **Apply** — the real build: a guided project or an exercise, opened
   directly in Scratch with the sprites already loaded.

The **Block Lab** shows all 104 blocks by category, which session teaches each
one, and which the student has already unlocked.

### The part that matters

Content is commoditised — anyone can collect Scratch projects. What makes a
tutoring business work is the **delivery system**, so every session ships with:

- a **minute-by-minute run sheet** (warm-up → objectives → I do → we do → you do → check → wrap)
- a **teaching script** — what the tutor actually says and demonstrates
- **misconceptions** children really have, each with the fix
- **check-for-understanding questions**, with answers
- **differentiation** — what to do if they are stuck, and if they finish early
- a **3-level rubric** (emerging / secure / mastered) for recording the outcome
- **homework** for every session

## Pages

| Page | Purpose |
|---|---|
| `index.html` | Dashboard — continue where you left off, skills map, progress |
| `curriculum.html` | The 100-session scope & sequence, searchable and filterable |
| `learn.html?s=L1S24` | **Learn** — the idea, the new blocks, examples and pitfalls |
| `quiz.html?s=L1S24` | **Recall Test** — 10 MCQs, instant feedback, pass to unlock |
| `lesson.html?s=L1S24` | The lesson plan — **Tutor Mode** and **Student Mode** |
| `projects.html` | The Real Project Library (28 imported guided projects) |
| `exercise.html?ex=S1E1` | Exercise launcher — opens Scratch with the sprites loaded |
| `report.html` | Parent progress report, certificates, export/import |
| `blocklab.html` | Every Scratch block by category, with unlock tracking |
| `index-classic.html` | The original written curriculum (kept for reference) |

Every project and exercise opens **directly in Scratch with the sprites already
loaded** — six projects open a ready-made starter (sprites placed, no solution
code); the rest open the real project so every sprite is present.

## Student progress

Progress is per-student and stored in `localStorage`, so the platform works
offline and needs no server. Use **Reports → Export backup** to move a student
between devices or to keep an off-line record.

## Rebuilding the content

```bash
python3 tools/import_rpi.py      # re-import the CC BY-SA project library
python3 tools/build_content.py   # regenerate exercise .sb3 files + manifest
python3 tools/build_platform.py  # merge spine + concepts + content -> platform.js
```

### Source layout

```
tools/concepts.py        the teaching knowledge base (49 concepts) — edit to improve teaching
tools/blocks.py          the block reference (104 blocks: meaning, example, gotcha)
tools/questions.py       the MCQ bank (490 questions, 10+ per concept)
tools/spine.py           the 100-session curriculum scope & sequence
tools/build_platform.py  merges everything into assets/js/platform.js
tools/import_rpi.py      imports the Raspberry Pi / Code Club projects
tools/game_engine.py     Scratch .sb3 generator (blocks, sprites, verification)
tools/templates.py       15 parameterised game templates
tools/curriculum.py      exercise definitions for the generated pool
assets/js/gn-store.js    student profiles, progress, mastery (localStorage)
assets/js/gn-ui.js       shared UI helpers and header
```

To improve teaching quality, edit `tools/concepts.py` and re-run
`build_platform.py` — every lesson plan regenerates from it.

> Note: the embedded players and pre-loaded projects need the site to be
> **hosted** (they fetch `.sb3` files over the network). On GitHub Pages this
> works out of the box.

## Licence and attribution

The imported project library comes from the **Raspberry Pi Foundation /
Code Club** and is used under **CC BY-SA 4.0**; that material remains under
CC BY-SA 4.0. See [ATTRIBUTION.md](ATTRIBUTION.md). Raspberry Pi is a
trademark of the Raspberry Pi Foundation; this project is not endorsed by or
affiliated with the Foundation.
