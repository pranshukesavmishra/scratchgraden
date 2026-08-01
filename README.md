# Grade Next · Scratch Academy

A complete **teaching system** for running Scratch classes for ages 7–12 —
not just a library of exercises. Everything is static HTML, CSS and vanilla
JavaScript: no build step, no dependencies, no backend. Drop it on any web
host (or GitHub Pages) and it runs.

---

## What it is

| | |
|---|---|
| **100 sessions** | 2 levels × 50, each a full 60-minute lesson plan |
| **49 concepts** | every Scratch block family, from first block to clones, lists and physics |
| **28 guided projects** | real Raspberry Pi / Code Club projects (CC BY-SA 4.0), 227 steps |
| **90 exercises** | generated game exercises with sprites pre-loaded and no solution code |
| **Assessment** | 3-level rubric per session, tutor notes, skills mastery map |
| **Parent reports** | printable report card and certificates |

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
| `lesson.html?s=L1S24` | The lesson plan — **Tutor Mode** and **Student Mode** |
| `projects.html` | The Real Project Library (28 imported guided projects) |
| `exercise.html?ex=S1E1` | Exercise launcher — opens Scratch with the sprites loaded |
| `report.html` | Parent progress report, certificates, export/import |
| `blocklab.html` | Reference: every Scratch block by category |
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
