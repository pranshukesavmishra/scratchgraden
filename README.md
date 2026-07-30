# 🐱 Grade Next — Scratch Coding Academy

A topic-by-topic, **game-focused Scratch curriculum and exercise platform for ages 7–12**, built to drop straight into the Grade Next tutoring platform.

Students learn every part of Scratch — all the block types and how to use them — through **100 hands-on sessions** across **two levels**, building real games inspired by the things kids already love (Minecraft, Roblox, Flappy Bird, Mario, Pong, Space shooters, tycoons and more). The goal: by the time a student finishes, coding concepts feel natural and moving on to any language is easy.

It's a **single static web app** — no build step, no server, no dependencies, no internet required. Just open `index.html`.

---

## ✨ What's inside

| | |
|---|---|
| **2 levels** | Level 1 *Coder Cadet* (foundations → first games) · Level 2 *Game Architect* (advanced mechanics → big games) |
| **100 sessions** | 50 per level, each ~60 min, grouped into topical **modules** so students learn topic-wise |
| **300 exercises** | Ordered, do-able steps in every session |
| **100 game projects** | Every session builds toward a game; whole modules are dedicated to platformers, top-down adventures, shooters, endless runners and tycoons |
| **All Scratch blocks** | Motion, Looks, Sound, Events, Control, Sensing, Operators, Variables, Lists, My Blocks (custom blocks/functions) and Pen — colour-coded to match real Scratch |
| **🐱 Scratch starter projects** | Every session ships a ready-made Scratch project (`.sb3`) **pre-loaded with the sprites for that exercise** on a themed backdrop — students open Scratch and start building, never from a blank canvas |
| **🧪 Block Lab** | A built-in, offline tap-to-code playground so young students grasp sequence, turning, loops and debugging *before* wrestling with dragging in real Scratch |
| **Progress tracking** | Per-session completion + "I can…" checklists, saved in the browser; live progress rings and bars |
| **Teacher Guide** | Session shape, block colour key, full curriculum map, assessment rubric, and embedding instructions |
| **Deep-linkable** | Every level and session has its own URL, so exercises are easy to find, assign and segment |
| **Embed-ready** | `?embed=1` hides the site chrome; a `postMessage` + JS API report progress back to the host |

---

## 🚀 Quick start

Open `index.html` in any modern browser. That's it — it runs from `file://`, from a USB stick, or from any static host.

Prefer a **single file**? Open `standalone.html` instead — it's the whole platform (all CSS + JS inlined) in one self-contained HTML file, ideal for offline classrooms or dropping straight into another system. Regenerate it any time after editing the source files by concatenating them (see *Project structure* below).

To serve it locally (optional):

```bash
# from the project root
python3 -m http.server 8000
# then visit http://localhost:8000
```

---

## 🗂️ Curriculum structure

### Level 1 — *Coder Cadet* (sessions 1–50)
1. **Welcome to Scratch** (1–5) — interface, sprites, stage, motion, coordinates, looks
2. **Move & Look** (6–12) — costumes, animation, backdrops, effects, sprite design, dialogue
3. **Loops & Repetition** (13–18) — repeat, forever, nested loops, pen patterns, a dance game
4. **Events & Control** (19–24) — events, keyboard & mouse control, broadcasting, timing
5. **Decisions & Sensing** (25–32) — if/then, if/else, touching, distance, booleans, ask/answer, collision
6. **Variables & Scoring** (33–38) — variables, score, timers, lives/health, difficulty
7. **Level 1 Game Builds** (39–50) — Catch, Maze, Whack-a-Creeper (Minecraft), Flappy Bird, Pong, and a capstone + showcase

### Level 2 — *Game Architect* (sessions 1–50)
1. **Level Up: Advanced Motion** (1–6) — velocity, easing, gravity & jumping, scrolling worlds
2. **Clones — Many at Once** (7–13) — projectiles, enemies, particles, and a full space shooter
3. **Lists & Data** (14–20) — inventories (Minecraft), high scores, quiz banks, save systems
4. **Custom Blocks & Clean Code** (21–27) — functions, parameters, recursion, organising & debugging big projects
5. **Game Genres Deep Dive** (28–39) — full builds: platformer (Mario/Roblox obby), top-down adventure (Zelda/Minecraft), endless runner (Subway Surfers/Geometry Dash), clicker/tycoon (Roblox tycoon/Cookie Clicker), survival/tower-defense
6. **Polish & Pro Skills** (40–45) — menus, sound, game feel/juice, persistent high scores, 2-player, sharing & remixing
7. **Capstone** (46–50) — design doc → core → content → polish/playtest → showcase & graduation

The full map (with session ranges) is inside the app under **Teacher Guide → Curriculum map**.

---

## 🔌 Embedding in the Grade Next platform

The app is intentionally dependency-free so it embeds cleanly.

### 1. Drop-in iframe

```html
<iframe
  src="scratch-academy/index.html?embed=1#/session/1/5"
  style="width:100%;height:800px;border:0"
  title="Scratch Coding Academy"></iframe>
```

- `?embed=1` hides the top navigation bar so it blends into your own shell.
- The hash (`#/session/1/5`) or query (`?session=1-5`, `?level=2`) deep-links straight to content.

### 2. Deep-link URLs (for assigning exercises / segmentation)

| URL | Opens |
|---|---|
| `#/` | Home |
| `#/level/1` | Level 1 overview |
| `#/session/1/13` | Level 1, session 13 |
| `#/session/2/28` | Level 2, session 28 |
| `#/lab` | Block Lab |
| `#/teacher` | Teacher Guide |

On first load you can also use query params instead of a hash: `index.html?session=2-28` or `index.html?level=1`.

### 3. Read progress back from the embed

The app posts messages to the parent window on navigation and progress changes:

```js
window.addEventListener("message", function (e) {
  if (e.data && e.data.source === "gradenext-scratch") {
    // e.data.type is "navigate" or "progress"
    // for "progress": e.data.data = { level, session, complete, overall }
    console.log(e.data.type, e.data.data);
  }
});
```

### 4. Control it from the host (same-page or via iframe scripting)

A small API is exposed on `window.GradeNext`:

```js
GradeNext.openSession(1, 13);      // navigate to L1 S13
GradeNext.openLevel(2);            // open Level 2
GradeNext.getProgress();           // { overall: 42, completed: ["1-1","1-2", ...] }
GradeNext.markComplete(1, 13);     // mark a session complete
```

---

## 🐱 Scratch starter projects (the important bit)

A link to a blank Scratch editor isn't much help. So every session's **"Do this exercise in Scratch"** panel gives students a real Scratch project that **already contains the sprites for that exercise**, positioned on a fitting backdrop:

| Exercise / game | Starter ships with |
|---|---|
| Catch game | Basket, Apple, Gem · Sky |
| Maze | Player, Goal, Coin · Maze walls |
| Whack-a-Creeper (Minecraft) | Creeper ×2, Villager · Grass |
| Flappy Bird | Bird, Pipe, Coin · Sky |
| Pong / Breakout | Paddle, Ball, Bricks · Space |
| Platformer (Mario / Roblox obby) | Player, Platform, Coin, Enemy, Goal · Sky |
| Top-down adventure (Zelda / Minecraft) | Hero, Gem, Enemy, Coin · Dungeon |
| Space shooter (Galaga) | Ship, Bullet, Aliens · Space |
| Clicker / tycoon (Cookie Clicker) | Cookie, Coin · Plain |
| …and every other session | a relevant sprite set + a green-flag starter script |

**How a student uses it**
1. Click **⬇ Download this starter (.sb3)** on the exercise page.
2. Click **↗ Open Scratch**.
3. In Scratch: **File → Load from your computer** → pick the downloaded file. The sprites are there, ready to code.

This works with **real Scratch** (`scratch.mit.edu`) and needs **no account**. The `.sb3` files are also **embedded in the app** (base64), so the download works offline, from `file://`, and inside the single-file `standalone.html`.

**One-click loading (optional, for your hosted deployment):** host the `starters/` folder on your site and set `window.GN_STARTER_BASEURL` to its public URL (e.g. `"https://your-cdn.com/scratch/starters/"`). Each panel then also shows a **⚡ Open pre-loaded (1-click)** button that opens a Scratch-compatible editor (TurboWarp) with the project already loaded — no download step.

Every generated `.sb3` passes the **official `scratch-parser`** validator (the same check Scratch runs on upload), so they load cleanly.

### Regenerating / customizing the starters

The starters are generated from a small toolchain so you can change sprites, positions or add starter scripts:

```bash
# 1. (only if you edited the curriculum) refresh the session list the generator reads:
node -e 'global.window={};require("./assets/js/curriculum-level1.js");require("./assets/js/curriculum-level2.js");
const o=[];window.GN_LEVELS.forEach(l=>l.sessions.forEach((s,i)=>o.push({key:"L"+l.level+"-"+String(i+1).padStart(2,"0"),
level:l.level,n:i+1,module:s.module,title:s.title,theme:s.theme,projectTitle:s.project?s.project.title:"",objective:s.objective||""})));
require("fs").writeFileSync("tools/sessions.json",JSON.stringify(o,null,1))'

# 2. regenerate all .sb3 files + the manifest + embedded data:
python3 tools/generate_starters.py
```

- Sprite art lives in `tools/svg_assets.py` (simple inline SVGs — edit or add your own).
- The session → sprite-set mapping is the `RULES` list in `tools/generate_starters.py`.
- Outputs: `starters/*.sb3`, `starters/manifest.json`, `assets/js/starters-manifest.js`, `assets/js/starters-data.js`.

---

## 🧪 Block Lab

Real Scratch asks a 7-year-old to *read* a 120-block palette and *drag with precision* — two things that get in the way of the actual thinking. Block Lab removes both barriers so concepts land first:

- **Tap to add** blocks (no dragging); tap a block for a ▲ ▼ ⧉ ✕ toolbar to reorder/copy/delete.
- **Scratch-faithful colours** — Motion blue, Looks purple, Control orange — so colour memory transfers to real Scratch.
- **Goal-based challenges** teaching sequence → turning → efficiency → **loops** → debugging, plus a free Sandbox.
- **Block-count par:** solving earns stars; solving *efficiently* earns 3 — how we teach loops without lecturing.
- **Crashes stop the program** with a "which block sent Pip there?" prompt — debugging is designed in.
- **🔊 Read-aloud** the mission and **💡 Hint** for non-readers and stuck students.
- Best stars per challenge are saved in the browser.

Use it heavily in the earliest sessions; students who find dragging hard can stay here an extra week while building motor confidence.

---

## 📁 Project structure

```
index.html                      # app shell; loads everything below
standalone.html                 # the whole platform inlined into ONE file (offline/embed)
assets/
  css/
    styles.css                  # all styling (light + dark), one file
  js/
    curriculum-level1.js        # Level 1 data (50 sessions)
    curriculum-level2.js        # Level 2 data (50 sessions)
    starters-manifest.js        # per-session starter metadata (sprites, backdrop) [generated]
    starters-data.js            # base64 of every .sb3 so downloads work offline [generated]
    blocklab.js                 # the interactive Block Lab playground
    app.js                      # router, rendering, progress, host integration
starters/                       # one Scratch starter project per session [generated]
  L1-01.sb3 … L2-50.sb3
  manifest.json
tools/                          # the starter-project generator
  svg_assets.py                 # sprite + backdrop art (inline SVG)
  generate_starters.py          # builds the .sb3 files + manifest + embedded data
  sessions.json                 # session list the generator reads
README.md
```

No bundler, no npm install. Plain `<script>` tags (not ES modules) so it works from `file://`.

---

## ✏️ Editing or extending the curriculum

All content lives in `assets/js/curriculum-level1.js` and `curriculum-level2.js`. Each session is a plain object:

```js
{
  module: "Loops & Repetition",     // which module this session belongs to
  title: "Repeat — The Big Idea",
  emoji: "🔁",
  theme: "Core concept",            // the game/interest tag shown on the card
  minutes: 60,
  concept: "…the one big idea…",
  blocks: [                         // blocks introduced; add "— Category" so the
    "repeat () — Control"           // chip is coloured correctly (e.g. "— Motion")
  ],
  objective: "What the student can DO after this session.",
  warmup: "An unplugged / quick starter.",
  exercises: [                      // ordered steps; string OR { t: title, d: detail }
    { t: "The long way", d: "Make a square with 8 blocks…" }
  ],
  project: {                        // the build (usually a game)
    title: "Shape Stamper",
    brief: "…what to make…",
    must: ["repeat", "move", "turn"],
    stretch: "An optional extension."
  },
  challenge: "For fast finishers.",
  vocab: ["loop", "repeat"],
  checklist: ["I can wrap blocks in a repeat loop", "…"]
}
```

- **To add a session:** push another object into the `sessions` array. Its `module` must match one of the level's `modules` list (which controls the section order and the topic-filter chips).
- **To add a module:** add its name to the level's `modules` array *and* give sessions that `module` value.
- **Block chip colours** are inferred from the block text (it looks for the category name or common block names). Adding `— Motion`, `— Control`, etc. guarantees the right colour.

There's nothing to rebuild — save the file and refresh.

---

## ♿ Notes

- **Offline & private:** everything runs client-side. Progress is stored in the browser's `localStorage`; nothing is sent anywhere.
- **Responsive:** works on tablets and phones as well as desktops.
- **Theme-aware:** follows the device's light/dark preference.
- **"Open in Scratch"** buttons link to `scratch.mit.edu` for when students build the real thing (the only feature that needs internet).
- **Accessibility:** read-aloud in Block Lab uses the browser's speech synthesis; keyboard and large tap targets throughout.

---

*Built for Grade Next — a coding journey where kids learn by making the games they love.*
