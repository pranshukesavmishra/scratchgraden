/* =====================================================================
   GRADE NEXT — Code Puzzles
   Parsons problems for Scratch: every puzzle is a real worked example
   from the active level, chopped into blocks and shuffled. The student
   rebuilds the script by clicking blocks in the right order and watches
   the real, colour-coded stack assemble. Fewer mistakes = more stars.
   ===================================================================== */
(function () {
  "use strict";
  var P = window.GN_PLATFORM, GN = window.GN, U = window.GNUI, h = U.h;
  var app, view = { mode: "grid" }, pz = null;

  /* ---------- puzzle bank: one good example per concept in this level ---------- */
  function buildPuzzles() {
    var LV = GN.level(), seen = {}, out = [];
    P.order.forEach(function (id) {
      var s = P.sessions[id];
      if (s.level !== LV || seen[s.conceptKey]) return;
      var exs = (s.deep && s.deep.examples) || [];
      for (var i = 0; i < exs.length; i++) {
        var lines = String(exs[i].code).split("\n").filter(function (l) { return l.trim(); });
        if (lines.length >= 4 && lines.length <= 12) {
          seen[s.conceptKey] = 1;
          out.push({ id: s.conceptKey + "-" + i, sid: id, n: s.n, concept: s.concept,
                     strandColor: s.strandColor, title: exs[i].title, note: exs[i].note,
                     lines: lines });
          break;
        }
      }
    });
    return out;
  }

  /* ---------- best-stars store, kept per student ---------- */
  function starsAll() { try { return JSON.parse(localStorage.getItem("gn_puzzles")) || {}; } catch (e) { return {}; } }
  function starsMine() {
    var stu = GN.isTutor() ? GN.active() : GN.ensureLearner();
    return (stu && starsAll()[stu.id]) || {};
  }
  function saveStars(pid, stars) {
    var stu = GN.isTutor() ? GN.active() : GN.ensureLearner();
    if (!stu) return;
    var all = starsAll(); all[stu.id] = all[stu.id] || {};
    if ((all[stu.id][pid] || 0) < stars) all[stu.id][pid] = stars;
    try { localStorage.setItem("gn_puzzles", JSON.stringify(all)); } catch (e) {}
  }

  function shuffle(a) {
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  /* tiny click/win sounds */
  var AC = null;
  function ping(kind) {
    try {
      AC = AC || new (window.AudioContext || window.webkitAudioContext)();
      if (AC.state === "suspended") AC.resume();
      var t0 = AC.currentTime;
      var notes = kind === "snap" ? [[740, 0, 0.07]]
                : kind === "no" ? [[185, 0, 0.18]]
                : [[523, 0, 0.12], [659, 0.12, 0.12], [784, 0.24, 0.12], [1047, 0.36, 0.28]];
      notes.forEach(function (n) {
        var o = AC.createOscillator(), g = AC.createGain();
        o.type = kind === "no" ? "triangle" : "sine";
        o.frequency.value = n[0];
        g.gain.setValueAtTime(0.0001, t0 + n[1]);
        g.gain.exponentialRampToValueAtTime(0.11, t0 + n[1] + 0.012);
        g.gain.exponentialRampToValueAtTime(0.0001, t0 + n[1] + n[2]);
        o.connect(g); g.connect(AC.destination);
        o.start(t0 + n[1]); o.stop(t0 + n[1] + n[2] + 0.05);
      });
    } catch (e) {}
  }

  function starRow(n, big) {
    return h("span", { class: "pz-stars" + (big ? " big" : "") },
      [1, 2, 3].map(function (i) { return h("span", { class: i <= n ? "on" : "" }, ["★"]); }));
  }
  function starsFor(mistakes) { return mistakes === 0 ? 3 : (mistakes <= 2 ? 2 : 1); }

  /* ---------- play state ---------- */
  function startPuzzle(p) {
    var tray, tries = 0;
    do {
      tray = shuffle(p.lines.map(function (l, i) { return { i: i, text: l.trim() }; }));
    } while (++tries < 10 && p.lines.length > 1 &&
             tray.every(function (c, k) { return c.text === p.lines[k].trim(); }));
    pz = { p: p, tray: tray, placed: 0, mistakes: 0, done: false };
    view.mode = "play";
    render();
  }

  function clickChip(chip, btn) {
    if (pz.done) return;
    var expected = pz.p.lines[pz.placed].trim();
    if (chip.text === expected) {
      var at = pz.tray.indexOf(chip);
      if (at < 0) return;               // stale node from a double-tap
      pz.placed++;
      pz.tray.splice(at, 1);
      if (pz.placed >= pz.p.lines.length) {
        pz.done = true;
        var st = starsFor(pz.mistakes);
        saveStars(pz.p.id, st);
        ping("win");
        if (st === 3 && U.confetti) U.confetti();
      } else ping("snap");
      render();
    } else {
      pz.mistakes++;
      ping("no");
      btn.classList.add("shake");
      var mc = document.querySelector(".pz-mist b");
      if (mc) mc.textContent = String(pz.mistakes);
      setTimeout(function () { btn.classList.remove("shake"); }, 420);
    }
  }

  /* ---------- views ---------- */
  function hero(bank) {
    var mine = starsMine();
    var solved = bank.filter(function (p) { return mine[p.id]; }).length;
    var total3 = bank.filter(function (p) { return mine[p.id] === 3; }).length;
    return h("section", { class: "c-hero" }, [
      h("h1", {}, ["🧩 Code Puzzles — Level " + GN.level()]),
      h("p", {}, ["Every puzzle is a real script, chopped up and shuffled. Click the blocks in the right order to rebuild it — no mistakes earns 3 stars."]),
      h("p", { class: "gn-hero-prog" }, [
        h("b", {}, [String(solved)]), " of " + bank.length + " puzzles solved · ",
        h("b", {}, [String(total3)]), " perfect ★★★"
      ])
    ]);
  }

  function gridView(bank) {
    var mine = starsMine();
    return h("div", { class: "pz-grid" }, bank.map(function (p) {
      var st = mine[p.id] || 0;
      return h("div", { class: "pz-card" + (st ? " solved" : ""), style: "--sc:" + p.strandColor }, [
        h("div", { class: "pz-card-top" }, [
          h("span", { class: "strand-chip", style: "background:" + p.strandColor + "22;color:" + U.shade(p.strandColor, -50) }, [p.concept]),
          starRow(st)
        ]),
        h("h3", {}, [p.title]),
        h("p", { class: "pz-meta" }, [p.lines.length + " blocks · from Session " + p.n]),
        h("button", { class: "btn " + (st ? "ghost" : "primary"), onclick: function () { startPuzzle(p); } },
          [st ? "↻ Play again" : "▶ Play"])
      ]);
    }));
  }

  function playView() {
    var p = pz.p;
    var wrap = h("div", { class: "pz-play" });
    wrap.appendChild(h("div", { class: "lp-crumbs" }, [
      h("a", { href: "puzzles.html", onclick: function (e) { e.preventDefault(); view.mode = "grid"; pz = null; render(); } }, ["← All puzzles"]),
      h("span", {}, [" / " + p.concept])
    ]));
    wrap.appendChild(h("div", { class: "pz-playhead" }, [
      h("h2", {}, ["🧩 " + p.title]),
      h("div", { class: "pz-mist" }, ["Mistakes: ", h("b", {}, [String(pz.mistakes)])])
    ]));
    wrap.appendChild(h("div", { class: "pz-progress" }, [
      U.bar(Math.round((pz.placed / p.lines.length) * 100), p.strandColor),
      h("span", {}, [pz.placed + " of " + p.lines.length + " blocks placed"])
    ]));

    /* the script assembling, rendered as real blocks */
    var built = p.lines.slice(0, pz.placed).join("\n");
    wrap.appendChild(h("div", { class: "pz-board" }, [
      h("div", { class: "pz-board-h" }, ["Your script"]),
      pz.placed ? (window.SB ? SB.render(built) : h("pre", {}, [built]))
                : h("div", { class: "pz-board-empty" }, ["Click the first block below to start building…"])
    ]));

    if (pz.done) {
      var st = starsFor(pz.mistakes);
      wrap.appendChild(h("section", { class: "pz-done" }, [
        h("div", { class: "pz-done-emoji" }, [st === 3 ? "🏆" : "🎉"]),
        h("h2", {}, [st === 3 ? "Perfect build!" : "Puzzle solved!"]),
        starRow(st, true),
        h("p", { class: "pz-note" }, ["→ " + p.note]),
        h("div", { class: "quiz-actions" }, [
          h("button", { class: "btn primary big", onclick: function () {
            var bank = buildPuzzles(), mine = starsMine();
            var next = bank.filter(function (q) { return !mine[q.id]; })[0] || bank[(bank.indexOf(bank.filter(function (q) { return q.id === p.id; })[0]) + 1) % bank.length];
            if (next) startPuzzle(next); else { view.mode = "grid"; pz = null; render(); }
          } }, ["Next puzzle →"]),
          h("button", { class: "btn ghost", onclick: function () { startPuzzle(p); } }, ["↻ Try for " + (st < 3 ? "3 stars" : "fun")]),
          h("button", { class: "btn ghost", onclick: function () { view.mode = "grid"; pz = null; render(); } }, ["🧩 All puzzles"])
        ])
      ]));
    } else {
      var tray = h("div", { class: "pz-tray" });
      pz.tray.forEach(function (chip) {
        var btn = h("button", { class: "pz-chip", onclick: function () { clickChip(chip, btn); } });
        btn.appendChild(window.SB ? SB.chip(chip.text) : h("code", {}, [chip.text]));
        tray.appendChild(btn);
      });
      wrap.appendChild(h("div", { class: "pz-traywrap" }, [
        h("div", { class: "pz-board-h" }, ["Blocks to place — which comes next?"]), tray]));
    }
    return wrap;
  }

  function render() {
    app.innerHTML = "";
    app.appendChild(U.header("puzzles"));
    var main = h("main", { class: "c-main" });
    var bank = buildPuzzles();
    if (view.mode === "play" && pz) {
      main.appendChild(playView());
    } else {
      main.appendChild(hero(bank));
      main.appendChild(bank.length ? gridView(bank)
        : h("div", { class: "empty" }, ["No puzzles for this level yet."]));
    }
    app.appendChild(main);
    app.appendChild(U.footer());
    window.scrollTo(0, 0);
  }

  function boot() {
    app = document.getElementById("app");
    if (!P || !P.order) { app.innerHTML = '<div style="padding:40px;text-align:center">Platform data failed to load.</div>'; return; }
    if (!GN.isTutor()) GN.ensureLearner();
    render();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
