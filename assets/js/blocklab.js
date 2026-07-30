/* =====================================================================
   GRADE NEXT — SCRATCH CODING ACADEMY
   BLOCK LAB — a tiny, offline, tap-to-code playground
   ---------------------------------------------------------------------
   Why it exists: young students (7–9) struggle to DRAG blocks and to
   read a 120-block palette. Block Lab lets concepts land first —
   sequence, turning, loops, debugging — with TAP-to-add blocks in
   Scratch-faithful colours. When they open real Scratch later, they
   already know what a loop is; they just have to find the block.

   No libraries, no network. Everything is drawn on a <canvas> + DOM.
   Progress (best stars per challenge) is saved to localStorage.
   ===================================================================== */
(function () {
  "use strict";

  // ---- Grid direction helpers -------------------------------------------
  var DIRS = ["up", "right", "down", "left"]; // clockwise
  var DELTA = {
    up: { dc: 0, dr: -1 },
    right: { dc: 1, dr: 0 },
    down: { dc: 0, dr: 1 },
    left: { dc: -1, dr: 0 }
  };

  // ---- Built-in challenges ----------------------------------------------
  // Each challenge maps to a core coding idea. Par = shortest known block
  // count → 3 stars. Correct-but-long earns 1–2 stars (efficiency lesson).
  var LEVELS = [
    {
      title: "Wake Up, Pip",
      idea: "A program is a plan",
      mission: "Press GO. Nothing happens! Add a Move block, set it to 3, and reach the star.",
      hint: "Tap the blue 'move' block once. Tap + until it says 3. Then press GO.",
      cols: 6, rows: 4, par: 1,
      start: { col: 1, row: 2, dir: "right" },
      stars: [{ col: 4, row: 2 }],
      walls: []
    },
    {
      title: "Around the Corner",
      idea: "Turning and facing",
      mission: "The star is up and to the right. Move, turn, and move again to collect it.",
      hint: "Move to below the star, then 'turn left' to face up, then move up.",
      cols: 6, rows: 5, par: 3,
      start: { col: 1, row: 4, dir: "right" },
      stars: [{ col: 4, row: 1 }],
      walls: []
    },
    {
      title: "The Long Path",
      idea: "Collect them all",
      mission: "Collect all three stars in a row. One big Move is tidier than three small ones!",
      hint: "Try a single 'move 4' instead of four separate moves. Fewer blocks = more stars.",
      cols: 7, rows: 3, par: 1,
      start: { col: 1, row: 1, dir: "right" },
      stars: [{ col: 3, row: 1 }, { col: 4, row: 1 }, { col: 5, row: 1 }],
      walls: []
    },
    {
      title: "The Staircase",
      idea: "Repeat (loops!)",
      mission: "Climb the staircase of stars. Notice the pattern: move, turn, move, turn… Use a REPEAT!",
      hint: "The pattern 'move 1, turn left, move 1, turn right' repeats. Wrap it in a repeat block.",
      cols: 6, rows: 6, par: 4,
      start: { col: 0, row: 5, dir: "right" },
      stars: [{ col: 1, row: 4 }, { col: 2, row: 3 }, { col: 3, row: 2 }, { col: 4, row: 1 }],
      walls: []
    },
    {
      title: "Hedge Maze",
      idea: "Debugging",
      mission: "Guide Pip through the hedges to the star. Bumping a hedge crashes the program!",
      hint: "Plan the whole path first. If you crash, look at the block that ran just before.",
      cols: 7, rows: 5, par: 6,
      start: { col: 0, row: 0, dir: "right" },
      stars: [{ col: 6, row: 4 }],
      walls: [
        { col: 2, row: 0 }, { col: 2, row: 1 }, { col: 2, row: 2 },
        { col: 4, row: 2 }, { col: 4, row: 3 }, { col: 4, row: 4 }
      ]
    },
    {
      title: "The Square Dance",
      idea: "Loops make shapes",
      mission: "Collect the four corner stars by walking a square. A repeat 4 is perfect here.",
      hint: "repeat 4 [ move 3, turn right ]. Start facing right from the top-left star.",
      cols: 6, rows: 6, par: 3,
      start: { col: 1, row: 1, dir: "right" },
      stars: [{ col: 1, row: 1 }, { col: 4, row: 1 }, { col: 4, row: 4 }, { col: 1, row: 4 }],
      walls: []
    },
    {
      title: "Pip's Playground",
      idea: "Free creation (Sandbox)",
      mission: "No goals here — just play! Try every block. Make Pip walk, spin, talk, and loop.",
      hint: "Try a repeat with 'turn right' and 'say' inside it to make Pip spin and chat.",
      cols: 8, rows: 6, par: 0, sandbox: true,
      start: { col: 3, row: 3, dir: "right" },
      stars: [],
      walls: []
    }
  ];

  // ---- Palette definition (Scratch-faithful colours) --------------------
  var PALETTE = [
    { type: "move", cat: "motion", label: "move ( ) steps", stepper: true },
    { type: "left", cat: "motion", label: "turn ↺ left" },
    { type: "right", cat: "motion", label: "turn ↻ right" },
    { type: "say", cat: "looks", label: "say ( )", text: true },
    { type: "wait", cat: "control", label: "wait ( ) sec", stepper: true, frac: true },
    { type: "repeat", cat: "control", label: "repeat ( )", stepper: true, container: true }
  ];

  var SPEEDS = [
    { label: "🐢 Slow", ms: 620 },
    { label: "🚶 Medium", ms: 320 },
    { label: "🐇 Fast", ms: 130 }
  ];

  var uidCounter = 0;
  function uid() { return "b" + (++uidCounter); }

  // ---- The Block Lab object ---------------------------------------------
  var BL = {
    mounted: false,
    el: {},          // cached DOM elements
    levelIndex: 0,
    program: [],     // AST: array of block objects
    selectedId: null,
    insertTargetId: null, // id of a repeat block whose children we insert into, or null = root
    running: false,
    speedIndex: 1,
    sprite: null,
    stars: [],       // remaining stars {col,row}
    bubble: "",      // current say text
    crashed: false
  };

  var STORE_KEY = "gn_blocklab_stars";

  function loadStars() {
    try { return JSON.parse(localStorage.getItem(STORE_KEY) || "{}"); }
    catch (e) { return {}; }
  }
  function saveStars(idx, stars) {
    var s = loadStars();
    if (!s[idx] || s[idx] < stars) { s[idx] = stars; }
    try { localStorage.setItem(STORE_KEY, JSON.stringify(s)); } catch (e) {}
  }

  // ---------------------------------------------------------------------
  //  MOUNTING / DOM
  // ---------------------------------------------------------------------
  BL.mount = function (container) {
    if (this.mounted && this.el.root && this.el.root.parentNode === container) {
      return; // already mounted here
    }
    container.innerHTML = "";
    var root = document.createElement("div");
    root.className = "bl-root";
    root.innerHTML = [
      '<div class="bl-head">',
      '  <h2>🧪 Block Lab <span class="bl-sub">tap-to-code playground</span></h2>',
      '  <p class="bl-intro">Practise the big ideas — sequence, turning, loops, debugging — before you open real Scratch. Tap a coloured block to add it. Tap a block in your program to move, copy or delete it.</p>',
      '</div>',
      '<div class="bl-levels" role="tablist" aria-label="Challenges"></div>',
      '<div class="bl-mission">',
      '  <div class="bl-mission-text"><strong class="bl-mtitle"></strong> <span class="bl-idea"></span><br><span class="bl-mbody"></span></div>',
      '  <div class="bl-mission-btns">',
      '    <button class="bl-btn bl-read" title="Read the mission aloud">🔊 Read</button>',
      '    <button class="bl-btn bl-hint" title="Show a hint">💡 Hint</button>',
      '  </div>',
      '</div>',
      '<div class="bl-main">',
      '  <div class="bl-stagewrap">',
      '    <canvas class="bl-stage" width="480" height="360" aria-label="Game stage"></canvas>',
      '    <div class="bl-status"></div>',
      '    <div class="bl-controls">',
      '      <button class="bl-btn bl-go">▶ GO</button>',
      '      <button class="bl-btn bl-stop" disabled>■ Stop</button>',
      '      <button class="bl-btn bl-reset">↺ Reset Pip</button>',
      '      <button class="bl-btn bl-speed"></button>',
      '      <button class="bl-btn bl-clear">🗑 Clear</button>',
      '    </div>',
      '  </div>',
      '  <div class="bl-code">',
      '    <div class="bl-palette"></div>',
      '    <div class="bl-scriptwrap">',
      '      <div class="bl-scripthead"><span>Your program</span> <span class="bl-count"></span></div>',
      '      <div class="bl-script" tabindex="0"></div>',
      '    </div>',
      '  </div>',
      '</div>'
    ].join("");
    container.appendChild(root);

    // cache elements
    this.el.root = root;
    this.el.levels = root.querySelector(".bl-levels");
    this.el.mtitle = root.querySelector(".bl-mtitle");
    this.el.idea = root.querySelector(".bl-idea");
    this.el.mbody = root.querySelector(".bl-mbody");
    this.el.canvas = root.querySelector(".bl-stage");
    this.el.ctx = this.el.canvas.getContext("2d");
    this.el.status = root.querySelector(".bl-status");
    this.el.palette = root.querySelector(".bl-palette");
    this.el.script = root.querySelector(".bl-script");
    this.el.count = root.querySelector(".bl-count");
    this.el.go = root.querySelector(".bl-go");
    this.el.stop = root.querySelector(".bl-stop");
    this.el.reset = root.querySelector(".bl-reset");
    this.el.speed = root.querySelector(".bl-speed");
    this.el.clear = root.querySelector(".bl-clear");

    // wire controls
    var self = this;
    this.el.go.addEventListener("click", function () { self.run(); });
    this.el.stop.addEventListener("click", function () { self.stop(); });
    this.el.reset.addEventListener("click", function () { self.resetSprite(); });
    this.el.clear.addEventListener("click", function () { self.clearProgram(); });
    this.el.speed.addEventListener("click", function () {
      self.speedIndex = (self.speedIndex + 1) % SPEEDS.length;
      self.el.speed.textContent = SPEEDS[self.speedIndex].label;
    });
    root.querySelector(".bl-read").addEventListener("click", function () { self.readAloud(); });
    root.querySelector(".bl-hint").addEventListener("click", function () { self.showHint(); });
    this.el.script.addEventListener("click", function (e) {
      if (e.target === self.el.script) { self.insertTargetId = null; self.selectedId = null; self.renderScript(); }
    });

    this.el.speed.textContent = SPEEDS[this.speedIndex].label;
    this.buildPalette();
    this.buildLevelTabs();
    this.mounted = true;
    this.loadLevel(this.levelIndex);
  };

  BL.buildLevelTabs = function () {
    var self = this;
    var best = loadStars();
    this.el.levels.innerHTML = "";
    LEVELS.forEach(function (lv, i) {
      var b = document.createElement("button");
      b.className = "bl-lvtab" + (i === self.levelIndex ? " on" : "");
      var stars = best[i] ? " " + "★".repeat(best[i]) : "";
      b.innerHTML = (lv.sandbox ? "🎨 " : (i + 1) + ". ") + escapeHtml(lv.title) +
        '<span class="bl-lvstars">' + stars + "</span>";
      b.addEventListener("click", function () { self.loadLevel(i); });
      self.el.levels.appendChild(b);
    });
  };

  BL.buildPalette = function () {
    var self = this;
    this.el.palette.innerHTML = '<div class="bl-palette-title">Blocks</div>';
    PALETTE.forEach(function (p) {
      var b = document.createElement("button");
      b.className = "bl-pblock cat-" + p.cat;
      b.textContent = p.label;
      b.addEventListener("click", function () { self.addBlock(p.type); });
      self.el.palette.appendChild(b);
    });
    var tip = document.createElement("div");
    tip.className = "bl-palette-tip";
    tip.textContent = "Tip: tap the dotted slot inside a repeat to drop blocks INSIDE the loop.";
    this.el.palette.appendChild(tip);
  };

  // ---------------------------------------------------------------------
  //  LEVEL / STATE
  // ---------------------------------------------------------------------
  BL.loadLevel = function (i) {
    this.stop();
    this.levelIndex = i;
    this.program = [];
    this.selectedId = null;
    this.insertTargetId = null;
    var lv = LEVELS[i];
    this.el.mtitle.textContent = lv.title;
    this.el.idea.textContent = "— " + lv.idea;
    this.el.mbody.textContent = lv.mission;
    this.resetSprite();
    this.renderScript();
    this.buildLevelTabs();
    this.setStatus(lv.sandbox ? "Sandbox: play freely!" : "Add blocks, then press GO.", "");
  };

  BL.resetSprite = function () {
    var lv = LEVELS[this.levelIndex];
    this.sprite = { col: lv.start.col, row: lv.start.row, dir: lv.start.dir };
    this.stars = lv.stars.map(function (s) { return { col: s.col, row: s.row }; });
    this.bubble = "";
    this.crashed = false;
    this.draw();
  };

  BL.clearProgram = function () {
    if (this.running) return;
    this.program = [];
    this.selectedId = null;
    this.insertTargetId = null;
    this.renderScript();
  };

  // ---------------------------------------------------------------------
  //  AST manipulation
  // ---------------------------------------------------------------------
  function newBlock(type) {
    var b = { id: uid(), type: type };
    if (type === "move") b.n = 1;
    if (type === "wait") b.n = 1;
    if (type === "repeat") { b.n = 2; b.children = []; }
    if (type === "say") b.text = "Hi!";
    return b;
  }

  // find target array to insert into + the block by id (returns {arr, block, parentArr, index})
  function findBlock(arr, id, parent) {
    for (var i = 0; i < arr.length; i++) {
      if (arr[i].id === id) return { arr: arr, block: arr[i], parent: parent, index: i };
      if (arr[i].children) {
        var r = findBlock(arr[i].children, id, arr[i]);
        if (r) return r;
      }
    }
    return null;
  }

  BL.addBlock = function (type) {
    if (this.running) return;
    var block = newBlock(type);
    var target = this.program;
    if (this.insertTargetId) {
      var r = findBlock(this.program, this.insertTargetId);
      if (r && r.block.children) target = r.block.children;
    }
    target.push(block);
    this.selectedId = block.id;
    this.renderScript();
  };

  BL.changeNum = function (id, delta) {
    var r = findBlock(this.program, id);
    if (!r) return;
    var b = r.block;
    if (b.type === "wait") {
      b.n = Math.max(0, Math.round((b.n + delta) * 10) / 10);
    } else {
      b.n = Math.max(b.type === "repeat" ? 1 : 0, b.n + delta);
    }
    this.renderScript();
  };

  BL.setText = function (id, text) {
    var r = findBlock(this.program, id);
    if (r) r.block.text = text;
  };

  BL.deleteBlock = function (id) {
    var r = findBlock(this.program, id);
    if (!r) return;
    r.arr.splice(r.index, 1);
    if (this.selectedId === id) this.selectedId = null;
    if (this.insertTargetId === id) this.insertTargetId = null;
    this.renderScript();
  };

  BL.duplicateBlock = function (id) {
    var r = findBlock(this.program, id);
    if (!r) return;
    var copy = deepCopy(r.block);
    r.arr.splice(r.index + 1, 0, copy);
    this.selectedId = copy.id;
    this.renderScript();
  };

  BL.moveBlock = function (id, dir) {
    var r = findBlock(this.program, id);
    if (!r) return;
    var ni = r.index + dir;
    if (ni < 0 || ni >= r.arr.length) return;
    var tmp = r.arr[ni]; r.arr[ni] = r.arr[r.index]; r.arr[r.index] = tmp;
    this.renderScript();
  };

  function deepCopy(b) {
    var c = { id: uid(), type: b.type };
    if ("n" in b) c.n = b.n;
    if ("text" in b) c.text = b.text;
    if (b.children) c.children = b.children.map(deepCopy);
    return c;
  }

  // ---------------------------------------------------------------------
  //  Rendering the script area
  // ---------------------------------------------------------------------
  BL.renderScript = function () {
    var self = this;
    var s = this.el.script;
    s.innerHTML = "";
    if (this.program.length === 0) {
      var empty = document.createElement("div");
      empty.className = "bl-empty";
      empty.textContent = "Tap a coloured block on the left to start your program.";
      s.appendChild(empty);
    } else {
      this.program.forEach(function (b) { s.appendChild(self.renderBlock(b)); });
    }
    this.el.count.textContent = countBlocks(this.program) + " block" + (countBlocks(this.program) === 1 ? "" : "s");
  };

  function countBlocks(arr) {
    var n = 0;
    arr.forEach(function (b) { n++; if (b.children) n += countBlocks(b.children); });
    return n;
  }

  BL.renderBlock = function (b) {
    var self = this;
    var meta = paletteMeta(b.type);
    var wrap = document.createElement("div");
    wrap.className = "bl-block cat-" + meta.cat + (this.selectedId === b.id ? " sel" : "");

    var row = document.createElement("div");
    row.className = "bl-block-row";

    var label = document.createElement("span");
    label.className = "bl-block-label";
    label.textContent = blockText(b);
    label.addEventListener("click", function (e) {
      e.stopPropagation();
      self.selectedId = (self.selectedId === b.id ? null : b.id);
      self.renderScript();
    });
    row.appendChild(label);

    // steppers for numeric blocks
    if (b.type === "move" || b.type === "wait" || b.type === "repeat") {
      var minus = mkMini("−", function (e) { e.stopPropagation(); self.changeNum(b.id, b.type === "wait" ? -0.5 : -1); });
      var plus = mkMini("+", function (e) { e.stopPropagation(); self.changeNum(b.id, b.type === "wait" ? 0.5 : 1); });
      row.appendChild(minus); row.appendChild(plus);
    }

    // text input for say
    if (b.type === "say") {
      var inp = document.createElement("input");
      inp.className = "bl-say-input";
      inp.value = b.text;
      inp.maxLength = 24;
      inp.addEventListener("click", function (e) { e.stopPropagation(); });
      inp.addEventListener("input", function () { self.setText(b.id, inp.value); });
      row.appendChild(inp);
    }

    wrap.appendChild(row);

    // toolbar when selected
    if (this.selectedId === b.id) {
      var tb = document.createElement("div");
      tb.className = "bl-toolbar";
      tb.appendChild(mkTool("▲", "Move up", function (e) { e.stopPropagation(); self.moveBlock(b.id, -1); }));
      tb.appendChild(mkTool("▼", "Move down", function (e) { e.stopPropagation(); self.moveBlock(b.id, 1); }));
      tb.appendChild(mkTool("⧉", "Copy", function (e) { e.stopPropagation(); self.duplicateBlock(b.id); }));
      tb.appendChild(mkTool("✕", "Delete", function (e) { e.stopPropagation(); self.deleteBlock(b.id); }));
      wrap.appendChild(tb);
    }

    // children slot for repeat
    if (b.children) {
      var slot = document.createElement("div");
      slot.className = "bl-slot" + (this.insertTargetId === b.id ? " active" : "");
      slot.addEventListener("click", function (e) {
        e.stopPropagation();
        self.insertTargetId = (self.insertTargetId === b.id ? null : b.id);
        self.renderScript();
      });
      if (b.children.length === 0) {
        var ph = document.createElement("div");
        ph.className = "bl-slot-ph";
        ph.textContent = (this.insertTargetId === b.id) ? "▶ blocks land here — now tap a block" : "tap to add blocks inside";
        slot.appendChild(ph);
      } else {
        b.children.forEach(function (c) { slot.appendChild(self.renderBlock(c)); });
      }
      wrap.appendChild(slot);
      var end = document.createElement("div");
      end.className = "bl-repeat-end cat-" + meta.cat;
      wrap.appendChild(end);
    }
    return wrap;
  };

  function mkMini(txt, fn) {
    var b = document.createElement("button");
    b.className = "bl-mini"; b.textContent = txt; b.addEventListener("click", fn);
    return b;
  }
  function mkTool(txt, title, fn) {
    var b = document.createElement("button");
    b.className = "bl-tool"; b.textContent = txt; b.title = title; b.addEventListener("click", fn);
    return b;
  }
  function paletteMeta(type) {
    for (var i = 0; i < PALETTE.length; i++) if (PALETTE[i].type === type) return PALETTE[i];
    return { cat: "control" };
  }
  function blockText(b) {
    switch (b.type) {
      case "move": return "move " + b.n + " step" + (b.n === 1 ? "" : "s");
      case "left": return "turn ↺ left";
      case "right": return "turn ↻ right";
      case "say": return "say";
      case "wait": return "wait " + b.n + " sec";
      case "repeat": return "repeat " + b.n;
    }
    return b.type;
  }

  // ---------------------------------------------------------------------
  //  Execution — unroll AST into primitive steps, then animate
  // ---------------------------------------------------------------------
  BL.unroll = function (arr, out, guard) {
    for (var i = 0; i < arr.length; i++) {
      if (guard.count > 4000) return; // safety cap
      var b = arr[i];
      if (b.type === "move") {
        for (var m = 0; m < b.n; m++) { out.push({ op: "step", id: b.id }); guard.count++; }
      } else if (b.type === "left") { out.push({ op: "left", id: b.id }); guard.count++; }
      else if (b.type === "right") { out.push({ op: "right", id: b.id }); guard.count++; }
      else if (b.type === "say") { out.push({ op: "say", id: b.id, text: b.text }); guard.count++; }
      else if (b.type === "wait") { out.push({ op: "wait", id: b.id, sec: b.n }); guard.count++; }
      else if (b.type === "repeat") {
        for (var r = 0; r < b.n; r++) { this.unroll(b.children, out, guard); }
      }
    }
  };

  BL.run = function () {
    if (this.running) return;
    if (this.program.length === 0) { this.setStatus("Add some blocks first!", "warn"); return; }
    this.resetSprite();
    var steps = [];
    this.unroll(this.program, steps, { count: 0 });
    if (steps.length === 0) { this.setStatus("Nothing to run yet.", "warn"); return; }

    this.running = true;
    this.crashed = false;
    this.el.go.disabled = true;
    this.el.stop.disabled = false;
    this.el.clear.disabled = true;
    this.setStatus("Running…", "");

    var self = this;
    var idx = 0;
    function tick() {
      if (!self.running) return;
      if (idx >= steps.length) { self.finish(); return; }
      var st = steps[idx++];
      var ok = self.doStep(st);
      self.draw();
      if (!ok) { self.crash(); return; }
      if (self.checkWin()) { self.finish(true); return; }
      var delay = SPEEDS[self.speedIndex].ms;
      if (st.op === "wait") delay = Math.max(delay, st.sec * 1000);
      self._timer = setTimeout(tick, delay);
    }
    tick();
  };

  BL.doStep = function (st) {
    var sp = this.sprite, lv = LEVELS[this.levelIndex];
    if (st.op === "left") { sp.dir = DIRS[(DIRS.indexOf(sp.dir) + 3) % 4]; return true; }
    if (st.op === "right") { sp.dir = DIRS[(DIRS.indexOf(sp.dir) + 1) % 4]; return true; }
    if (st.op === "say") { this.bubble = st.text; return true; }
    if (st.op === "wait") { return true; }
    if (st.op === "step") {
      var d = DELTA[sp.dir];
      var nc = sp.col + d.dc, nr = sp.row + d.dr;
      // off-grid?
      if (nc < 0 || nr < 0 || nc >= lv.cols || nr >= lv.rows) return false;
      // wall?
      for (var i = 0; i < lv.walls.length; i++) {
        if (lv.walls[i].col === nc && lv.walls[i].row === nr) return false;
      }
      sp.col = nc; sp.row = nr;
      // collect star
      for (var j = this.stars.length - 1; j >= 0; j--) {
        if (this.stars[j].col === nc && this.stars[j].row === nr) this.stars.splice(j, 1);
      }
      return true;
    }
    return true;
  };

  BL.checkWin = function () {
    var lv = LEVELS[this.levelIndex];
    if (lv.sandbox) return false;
    return this.stars.length === 0;
  };

  BL.crash = function () {
    this.crashed = true;
    this.running = false;
    this._resetButtons();
    this.setStatus("💥 Crash! Pip hit something. Which block sent Pip there?", "bad");
    this.draw();
  };

  BL.finish = function (won) {
    this.running = false;
    this._resetButtons();
    var lv = LEVELS[this.levelIndex];
    if (lv.sandbox) { this.setStatus("Nice — sandbox run finished. Keep experimenting!", "good"); return; }
    if (won || this.checkWin()) {
      var blocks = countBlocks(this.program);
      var stars = 1;
      if (blocks <= lv.par) stars = 3;
      else if (blocks <= lv.par + 2) stars = 2;
      saveStars(this.levelIndex, stars);
      this.buildLevelTabs();
      var msg = "🎉 Solved! " + "★".repeat(stars) + "☆".repeat(3 - stars) +
        "  (" + blocks + " blocks, par " + lv.par + ")";
      if (stars < 3) msg += " — can you do it in fewer blocks for 3 stars?";
      this.setStatus(msg, "good");
    } else {
      this.setStatus("Program finished, but not all stars collected. Try again!", "warn");
    }
  };

  BL.stop = function () {
    if (this._timer) { clearTimeout(this._timer); this._timer = null; }
    this.running = false;
    this._resetButtons();
  };

  BL._resetButtons = function () {
    if (!this.el.go) return;
    this.el.go.disabled = false;
    this.el.stop.disabled = true;
    this.el.clear.disabled = false;
  };

  BL.setStatus = function (text, kind) {
    if (!this.el.status) return;
    this.el.status.textContent = text;
    this.el.status.className = "bl-status" + (kind ? " " + kind : "");
  };

  // ---------------------------------------------------------------------
  //  Canvas drawing
  // ---------------------------------------------------------------------
  BL.draw = function () {
    var ctx = this.el.ctx, lv = LEVELS[this.levelIndex];
    var W = this.el.canvas.width, H = this.el.canvas.height;
    var cell = Math.min(W / lv.cols, H / lv.rows);
    var ox = (W - cell * lv.cols) / 2, oy = (H - cell * lv.rows) / 2;

    ctx.clearRect(0, 0, W, H);
    // background
    ctx.fillStyle = "#eaf3ff";
    ctx.fillRect(0, 0, W, H);

    // grid
    ctx.strokeStyle = "#c7ddf5";
    ctx.lineWidth = 1;
    for (var c = 0; c <= lv.cols; c++) {
      ctx.beginPath(); ctx.moveTo(ox + c * cell, oy); ctx.lineTo(ox + c * cell, oy + lv.rows * cell); ctx.stroke();
    }
    for (var r = 0; r <= lv.rows; r++) {
      ctx.beginPath(); ctx.moveTo(ox, oy + r * cell); ctx.lineTo(ox + lv.cols * cell, oy + r * cell); ctx.stroke();
    }

    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    var fs = Math.floor(cell * 0.6);
    ctx.font = fs + "px sans-serif";

    // walls
    lv.walls.forEach(function (w) {
      ctx.fillText("🌳", ox + (w.col + 0.5) * cell, oy + (w.row + 0.5) * cell);
    });
    // stars
    this.stars.forEach(function (s) {
      ctx.fillText("⭐", ox + (s.col + 0.5) * cell, oy + (s.row + 0.5) * cell);
    });

    // sprite (a friendly creature that shows facing)
    var sp = this.sprite;
    var cx = ox + (sp.col + 0.5) * cell, cy = oy + (sp.row + 0.5) * cell;
    var rad = cell * 0.34;
    // direction pointer
    var d = DELTA[sp.dir];
    ctx.fillStyle = this.crashed ? "#d63838" : "#ff8c1a";
    ctx.beginPath();
    ctx.moveTo(cx + d.dc * rad * 1.5, cy + d.dr * rad * 1.5);
    // perpendicular base
    var px = -d.dr, py = d.dc;
    ctx.lineTo(cx + px * rad, cy + py * rad);
    ctx.lineTo(cx - px * rad, cy - py * rad);
    ctx.closePath();
    ctx.fill();
    // body
    ctx.fillStyle = this.crashed ? "#e15a5a" : "#ffb14d";
    ctx.beginPath();
    ctx.arc(cx, cy, rad, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = "#a85a00"; ctx.lineWidth = 2; ctx.stroke();
    // eyes
    ctx.fillStyle = "#2b2b2b";
    var ex = d.dc * rad * 0.25, ey = d.dr * rad * 0.25;
    ctx.beginPath(); ctx.arc(cx + ex - py * rad * 0.3, cy + ey + px * rad * 0.3, rad * 0.12, 0, Math.PI * 2); ctx.fill();
    ctx.beginPath(); ctx.arc(cx + ex + py * rad * 0.3, cy + ey - px * rad * 0.3, rad * 0.12, 0, Math.PI * 2); ctx.fill();

    // speech bubble
    if (this.bubble) {
      var text = this.bubble;
      ctx.font = Math.floor(cell * 0.3) + "px sans-serif";
      var tw = ctx.measureText(text).width + 16;
      var bx = cx + rad, by = cy - rad - cell * 0.5;
      bx = Math.min(bx, W - tw - 6); by = Math.max(by, 6);
      ctx.fillStyle = "#fff"; ctx.strokeStyle = "#8ab4e8";
      roundRect(ctx, bx, by, tw, cell * 0.5, 8); ctx.fill(); ctx.stroke();
      ctx.fillStyle = "#333"; ctx.textAlign = "center";
      ctx.fillText(text, bx + tw / 2, by + cell * 0.25);
    }
  };

  function roundRect(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r);
    ctx.closePath();
  }

  // ---------------------------------------------------------------------
  //  Read-aloud + hint
  // ---------------------------------------------------------------------
  BL.readAloud = function () {
    var lv = LEVELS[this.levelIndex];
    var text = lv.title + ". " + lv.mission;
    if ("speechSynthesis" in window) {
      try {
        window.speechSynthesis.cancel();
        var u = new SpeechSynthesisUtterance(text);
        u.rate = 0.95;
        window.speechSynthesis.speak(u);
        this.setStatus("🔊 Reading the mission…", "");
      } catch (e) { this.setStatus(text, ""); }
    } else {
      this.setStatus(text, "");
    }
  };

  BL.showHint = function () {
    this.setStatus("💡 " + LEVELS[this.levelIndex].hint, "warn");
  };

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  window.GN_BlockLab = BL;
})();
