/* =====================================================================
   GRADE NEXT — Flashcards
   A coding-vocabulary trainer built from every "Words to know" list in
   the active level. Spaced repetition, kid-sized: each card lives in
   box 1, 2 or 3 — get it right and it climbs a box and waits longer
   before coming back; miss it and it drops to box 1 and returns today.
   ===================================================================== */
(function () {
  "use strict";
  var P = window.GN_PLATFORM, GN = window.GN, U = window.GNUI, h = U.h;
  var app, mode = "home", fc = null, browseOpen = {};

  function today() { return new Date().toISOString().slice(0, 10); }
  function plusDays(n) {
    var d = new Date(); d.setDate(d.getDate() + n);
    return d.toISOString().slice(0, 10);
  }
  function shuffle(a) {
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  /* ---------- deck: dedup'd vocabulary of the active level ---------- */
  function buildDeck() {
    var LV = GN.level(), seen = {}, deck = [];
    P.order.forEach(function (id) {
      var s = P.sessions[id];
      if (s.level !== LV) return;
      (s.vocab || []).forEach(function (v) {
        var i = v.indexOf("—");
        if (i < 1) return;
        var term = v.slice(0, i).trim(), def = v.slice(i + 1).trim();
        var key = term.toLowerCase();
        if (!term || !def || seen[key]) return;
        seen[key] = 1;
        deck.push({ key: key, term: term, def: def, n: s.n, concept: s.concept,
                    strandColor: s.strandColor });
      });
    });
    return deck;
  }

  /* ---------- per-student card memory ---------- */
  function memAll() { try { return JSON.parse(localStorage.getItem("gn_cards")) || {}; } catch (e) { return {}; } }
  function stuId() {
    var stu = GN.isTutor() ? GN.active() : GN.ensureLearner();
    return stu ? stu.id : null;
  }
  function memMine() { return memAll()[stuId()] || {}; }
  function saveMem(key, rec) {
    var id = stuId(); if (!id) return;
    var all = memAll(); all[id] = all[id] || {};
    all[id][key] = rec;
    try { localStorage.setItem("gn_cards", JSON.stringify(all)); } catch (e) {}
  }
  function isDue(card, mem) {
    var r = mem[card.key];
    return !r || (r.due || "") <= today();
  }

  /* ---------- grading ---------- */
  function grade(g) {
    var card = fc.current, mem = memMine();
    var r = mem[card.key] || { box: 0, seen: 0 };
    r.seen = (r.seen || 0) + 1;
    if (g === "again") {
      r.box = 1; r.due = today();
      fc.queue.push(card);            // comes back later this session
      fc.again++;
    } else if (g === "easy") {
      r.box = 3; r.due = plusDays(7);
      fc.done++;
    } else {                          // "good"
      r.box = Math.min(3, (r.box || 0) + 1);
      r.due = plusDays(r.box === 1 ? 1 : r.box === 2 ? 3 : 7);
      fc.done++;
    }
    saveMem(card.key, r);
    next();
  }
  function next() {
    fc.current = fc.queue.shift() || null;
    fc.flipped = false;
    if (!fc.current) {
      mode = "done";
      if (U.confetti && fc.done) U.confetti();
    }
    render();
  }

  function startStudy(all) {
    var deck = buildDeck(), mem = memMine();
    var pool = all ? deck : deck.filter(function (c) { return isDue(c, mem); });
    if (!pool.length) return;
    var cards = shuffle(pool).slice(0, 15);
    fc = { queue: cards.slice(1), current: cards[0], flipped: false,
           total: cards.length, done: 0, again: 0 };
    mode = "study";
    render();
  }

  /* ---------- views ---------- */
  function counts() {
    var deck = buildDeck(), mem = memMine();
    var c = { fresh: 0, learning: 0, mastered: 0, due: 0, total: deck.length };
    deck.forEach(function (card) {
      var r = mem[card.key];
      if (!r) c.fresh++;
      else if (r.box >= 3) c.mastered++;
      else c.learning++;
      if (isDue(card, mem)) c.due++;
    });
    return c;
  }

  function homeView() {
    var c = counts();
    var wrap = h("div", {});
    wrap.appendChild(h("section", { class: "c-hero" }, [
      h("h1", {}, ["🃏 Flashcards — Level " + GN.level()]),
      h("p", {}, ["All the coding words from your sessions, on flip cards that remember which ones you find hard and bring them back at just the right time."]),
      h("div", { class: "fc-counts" }, [
        h("span", { class: "fc-count new" }, [h("b", {}, [String(c.fresh)]), " new"]),
        h("span", { class: "fc-count learning" }, [h("b", {}, [String(c.learning)]), " learning"]),
        h("span", { class: "fc-count mastered" }, [h("b", {}, [String(c.mastered)]), " mastered"]),
        h("span", { class: "fc-count due" }, [h("b", {}, [String(c.due)]), " ready to study"])
      ])
    ]));
    wrap.appendChild(h("div", { class: "fc-cta" }, c.due
      ? [h("button", { class: "btn primary big", onclick: function () { startStudy(false); } },
           ["▶ Study now — " + Math.min(15, c.due) + " cards"]),
         h("button", { class: "btn ghost", onclick: function () { startStudy(true); } }, ["🔀 Practice everything"])]
      : [h("div", { class: "fc-alldone" }, ["🎉 Nothing is due today — your memory is up to date. Come back tomorrow!"]),
         h("button", { class: "btn ghost", onclick: function () { startStudy(true); } }, ["🔀 Practice anyway"])]));

    /* browse the whole deck */
    var deck = buildDeck(), mem = memMine();
    wrap.appendChild(h("section", { class: "panel" }, [
      h("h2", { class: "panel-h" }, ["📖 All " + deck.length + " words in this level"]),
      h("p", { class: "panel-sub" }, ["Tap a card to peek at its meaning. The box shows how well you know it — box 3 means mastered."]),
      h("div", { class: "fc-browse" }, deck.map(function (card) {
        var r = mem[card.key];
        var box = r ? r.box : 0;
        var el = h("button", { class: "fc-mini" + (browseOpen[card.key] ? " open" : ""),
          style: "--sc:" + card.strandColor,
          onclick: function () { browseOpen[card.key] = !browseOpen[card.key]; render(); } }, [
          h("span", { class: "fc-mini-term" }, [card.term]),
          h("span", { class: "fc-box b" + box }, [box ? "box " + box : "new"]),
          browseOpen[card.key] ? h("span", { class: "fc-mini-def" }, [card.def]) : null
        ]);
        return el;
      }))
    ]));
    return wrap;
  }

  function studyView() {
    var card = fc.current;
    var wrap = h("div", { class: "fc-study" });
    wrap.appendChild(h("div", { class: "lp-crumbs" }, [
      h("a", { href: "flashcards.html", onclick: function (e) { e.preventDefault(); mode = "home"; fc = null; render(); } }, ["← All cards"]),
      h("span", {}, [" / studying"])
    ]));
    wrap.appendChild(h("div", { class: "pz-progress" }, [
      U.bar(Math.round((fc.done / fc.total) * 100), "#7F5DF9"),
      h("span", {}, [fc.done + " of " + fc.total + " done" + (fc.again ? " · " + fc.again + " to retry" : "")])
    ]));
    var face = fc.flipped
      ? h("div", { class: "fc-face back" }, [
          h("div", { class: "fc-facelabel" }, ["means…"]),
          h("div", { class: "fc-def" }, [card.def]),
          h("div", { class: "fc-src" }, ["from Session " + card.n + " · " + card.concept])])
      : h("div", { class: "fc-face front" }, [
          h("div", { class: "fc-facelabel" }, ["what does this mean?"]),
          h("div", { class: "fc-term" }, [card.term]),
          h("div", { class: "fc-hint" }, ["tap the card to flip it"])]);
    wrap.appendChild(h("button", { class: "fc-card" + (fc.flipped ? " flipped" : ""),
      style: "--sc:" + card.strandColor,
      onclick: function () { fc.flipped = !fc.flipped; render(); } }, [face]));
    wrap.appendChild(fc.flipped
      ? h("div", { class: "fc-grade" }, [
          h("button", { class: "btn fc-again", onclick: function () { grade("again"); } }, ["↻ Again", h("small", {}, ["didn't know it"])]),
          h("button", { class: "btn fc-good", onclick: function () { grade("good"); } }, ["✓ Got it", h("small", {}, ["had to think"])]),
          h("button", { class: "btn fc-easy", onclick: function () { grade("easy"); } }, ["⚡ Easy", h("small", {}, ["knew it instantly"])])
        ])
      : h("div", { class: "fc-grade ghost-row" }, [
          h("span", { class: "fc-kbd" }, ["Space flips · then 1 = Again, 2 = Got it, 3 = Easy"])]));
    return wrap;
  }

  function doneView() {
    var c = counts();
    return h("section", { class: "quiz-result pass fc-done" }, [
      h("div", { class: "qr-emoji" }, ["🧠"]),
      h("h2", {}, ["Study session complete!"]),
      h("p", { class: "qr-score" }, [fc.done + " cards reviewed" + (fc.again ? " · " + fc.again + " needed a retry" : " · flawless!")]),
      h("p", { class: "qr-msg" }, [c.mastered + " of " + c.total + " words are now in box 3 — mastered."]),
      h("div", { class: "quiz-actions" }, [
        c.due ? h("button", { class: "btn primary big", onclick: function () { startStudy(false); } }, ["▶ Keep going — " + Math.min(15, c.due) + " more"]) : null,
        h("button", { class: "btn ghost", onclick: function () { mode = "home"; fc = null; render(); } }, ["🃏 Back to cards"]),
        h("a", { class: "btn ghost", href: "index.html" }, ["🏠 Dashboard"])
      ])
    ]);
  }

  function render() {
    app.innerHTML = "";
    app.appendChild(U.header("cards"));
    var main = h("main", { class: "c-main" });
    main.appendChild(mode === "study" && fc && fc.current ? studyView()
      : mode === "done" && fc ? doneView() : homeView());
    app.appendChild(main);
    app.appendChild(U.footer());
    if (mode !== "home") window.scrollTo(0, 0);
  }

  function keys(e) {
    if (mode !== "study" || !fc || !fc.current || document.querySelector(".cmdk")) return;
    var tag = (document.activeElement || {}).tagName || "";
    if (tag === "INPUT" || tag === "TEXTAREA") return;
    if (e.key === " " || e.key === "Enter") { e.preventDefault(); fc.flipped = !fc.flipped; render(); }
    else if (fc.flipped && e.key === "1") { e.preventDefault(); grade("again"); }
    else if (fc.flipped && e.key === "2") { e.preventDefault(); grade("good"); }
    else if (fc.flipped && e.key === "3") { e.preventDefault(); grade("easy"); }
  }

  function boot() {
    app = document.getElementById("app");
    if (!P || !P.order) { app.innerHTML = '<div style="padding:40px;text-align:center">Platform data failed to load.</div>'; return; }
    if (!GN.isTutor()) GN.ensureLearner();
    document.addEventListener("keydown", keys);
    render();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
