/* =====================================================================
   GRADE NEXT — SCRATCH CODING ACADEMY
   app.js — navigation, rendering, progress, deep-links, integration
   ---------------------------------------------------------------------
   Self-contained, no dependencies, works from file:// or any host.
   Designed to be embedded in the Grade Next platform (see README):
     • Hash routing gives every level & session a shareable URL.
     • ?embed=1 hides the site chrome so it drops cleanly into an iframe.
     • ?session=1-5 (or ?level=2) deep-links straight to content.
     • window.GradeNext API + postMessage let the host track progress.
   ===================================================================== */
(function () {
  "use strict";

  var LEVELS = window.GN_LEVELS || [];
  var app;                 // #app container
  var STORE_KEY = "gn_progress_v1";
  var params = new URLSearchParams(location.search);
  var EMBED = params.get("embed") === "1";

  /* ---------------- Scratch-faithful block colouring ---------------- */
  var CAT_COLORS = {
    motion: "#4C97FF", looks: "#9966FF", sound: "#CF63CF", events: "#FFBF00",
    control: "#FFAB19", sensing: "#5CB1D6", operators: "#59C059",
    variables: "#FF8C1A", myblocks: "#FF6680", pen: "#0FBD8C", other: "#9aa4b2"
  };
  function blockCategory(raw) {
    var s = String(raw).toLowerCase();
    // explicit "— Category" hints first
    if (/—\s*motion|\(motion\)/.test(s)) return "motion";
    if (/—\s*looks|\(looks\)/.test(s)) return "looks";
    if (/—\s*sound|\(sound\)/.test(s)) return "sound";
    if (/—\s*events|\(events\)/.test(s)) return "events";
    if (/—\s*control|\(control\)/.test(s)) return "control";
    if (/—\s*sensing|\(sensing\)/.test(s)) return "sensing";
    if (/—\s*operators|\(operators\)/.test(s)) return "operators";
    if (/—\s*variables|\(variables\)/.test(s)) return "variables";
    if (/my ?blocks/.test(s)) return "myblocks";
    if (/—\s*pen|\bpen\b/.test(s)) return "pen";
    // keyword fallback
    if (/\bpen\b|stamp/.test(s)) return "pen";
    if (/custom block|define\b|recursion/.test(s)) return "myblocks";
    if (/variable|\bset \[|change \[|\blist\b|add \(|item \(|insert |replace item|contains\?/.test(s)) return "variables";
    if (/\+|\*|random|\bjoin\b|\band\b|\bor\b|\bnot\b|<|>|=|operator/.test(s)) return "operators";
    if (/touching|mouse|pressed\?|distance|\bask\b|answer|timer|sensing/.test(s)) return "sensing";
    if (/repeat|forever|if |else|wait|stop|clone|control/.test(s)) return "control";
    if (/when |broadcast|green flag|event/.test(s)) return "events";
    if (/say|think|costume|backdrop|size|effect|show|hide|graphic|looks/.test(s)) return "looks";
    if (/\bsound\b|play |volume/.test(s)) return "sound";
    if (/move |turn|glide|go to|point|change x|change y|set x|set y|on edge|direction|velocity|gravity/.test(s)) return "motion";
    return "other";
  }

  /* ---------------- Progress store ---------------- */
  function loadProgress() {
    try { return JSON.parse(localStorage.getItem(STORE_KEY) || "{}"); }
    catch (e) { return {}; }
  }
  function saveProgress(p) {
    try { localStorage.setItem(STORE_KEY, JSON.stringify(p)); } catch (e) {}
  }
  var PROGRESS = loadProgress();
  PROGRESS.completed = PROGRESS.completed || {};
  PROGRESS.checks = PROGRESS.checks || {};

  function sessionKey(lv, n) { return lv + "-" + n; }
  function isComplete(lv, n) { return !!PROGRESS.completed[sessionKey(lv, n)]; }
  function setComplete(lv, n, val) {
    PROGRESS.completed[sessionKey(lv, n)] = val;
    if (!val) delete PROGRESS.completed[sessionKey(lv, n)];
    saveProgress(PROGRESS);
    notifyHost("progress", { level: lv, session: n, complete: val, overall: overallPercent() });
  }
  function levelPercent(levelObj) {
    var total = levelObj.sessions.length, done = 0;
    for (var i = 1; i <= total; i++) if (isComplete(levelObj.level, i)) done++;
    return total ? Math.round(done / total * 100) : 0;
  }
  function overallPercent() {
    var total = 0, done = 0;
    LEVELS.forEach(function (l) {
      total += l.sessions.length;
      for (var i = 1; i <= l.sessions.length; i++) if (isComplete(l.level, i)) done++;
    });
    return total ? Math.round(done / total * 100) : 0;
  }

  /* ---------------- Host integration ---------------- */
  function notifyHost(type, data) {
    try {
      if (window.parent && window.parent !== window) {
        window.parent.postMessage({ source: "gradenext-scratch", type: type, data: data }, "*");
      }
    } catch (e) {}
  }
  // Public API for the host platform
  window.GradeNext = {
    version: "1.0",
    levels: LEVELS,
    go: function (hash) { location.hash = hash; },
    openSession: function (level, n) { location.hash = "#/session/" + level + "/" + n; },
    openLevel: function (level) { location.hash = "#/level/" + level; },
    getProgress: function () {
      return { overall: overallPercent(), completed: Object.keys(PROGRESS.completed) };
    },
    markComplete: function (level, n, val) { setComplete(level, n, val !== false); render(); }
  };

  /* ---------------- Small DOM helpers ---------------- */
  function h(tag, attrs, kids) {
    var e = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "class") e.className = attrs[k];
      else if (k === "html") e.innerHTML = attrs[k];
      else if (k.slice(0, 2) === "on" && typeof attrs[k] === "function") e.addEventListener(k.slice(2), attrs[k]);
      else e.setAttribute(k, attrs[k]);
    });
    (kids || []).forEach(function (c) {
      if (c == null) return;
      e.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
    });
    return e;
  }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function levelByNum(n) { for (var i = 0; i < LEVELS.length; i++) if (LEVELS[i].level === n) return LEVELS[i]; return null; }

  /* ---------------- Header ---------------- */
  function renderHeader() {
    if (EMBED) return null;
    var route = parseHash();
    function navBtn(label, hash, active) {
      return h("button", {
        class: "nav-btn" + (active ? " active" : ""),
        onclick: function () { location.hash = hash; }
      }, [label]);
    }
    return h("header", { class: "site-head" }, [
      h("div", { class: "brand", onclick: function () { location.hash = "#/"; }, role: "button", tabindex: "0" }, [
        h("span", { class: "brand-mark" }, ["🐱"]),
        h("div", {}, [
          h("div", { class: "brand-name" }, ["Grade Next"]),
          h("div", { class: "brand-sub" }, ["Scratch Coding Academy"])
        ])
      ]),
      h("nav", { class: "site-nav" }, [
        navBtn("Home", "#/", route.view === "home"),
        navBtn("🚀 Level 1", "#/level/1", route.view === "level" && route.level === 1),
        navBtn("🏗️ Level 2", "#/level/2", route.view === "level" && route.level === 2),
        navBtn("🧪 Block Lab", "#/lab", route.view === "lab"),
        navBtn("🍎 Teacher Guide", "#/teacher", route.view === "teacher")
      ]),
      h("div", { class: "head-progress", title: "Your overall progress" }, [
        progressRing(overallPercent())
      ])
    ]);
  }

  function progressRing(pct) {
    var wrap = h("div", { class: "ring" });
    wrap.innerHTML =
      '<svg viewBox="0 0 36 36"><path class="ring-bg" d="M18 2a16 16 0 1 1 0 32 16 16 0 0 1 0-32"/>' +
      '<path class="ring-fg" stroke-dasharray="' + pct + ',100" d="M18 2a16 16 0 1 1 0 32 16 16 0 0 1 0-32"/></svg>' +
      '<span class="ring-label">' + pct + '%</span>';
    return wrap;
  }

  /* ---------------- Home view ---------------- */
  function viewHome() {
    var wrap = h("div", { class: "view home" });
    wrap.appendChild(h("section", { class: "hero" }, [
      h("h1", {}, ["Learn to code by building games 🎮"]),
      h("p", { class: "hero-sub" }, [
        "A topic-by-topic Scratch journey for ages 7–12. Two levels, 100 hands-on sessions, and real games inspired by Minecraft, Roblox, Flappy Bird and more — so every concept sticks."
      ]),
      h("div", { class: "hero-cta" }, [
        h("button", { class: "btn primary", onclick: function () { location.hash = "#/level/1"; } }, ["Start Level 1 →"]),
        h("button", { class: "btn ghost", onclick: function () { location.hash = "#/lab"; } }, ["🧪 Try the Block Lab"])
      ])
    ]));

    // level cards
    var cards = h("div", { class: "level-cards" });
    LEVELS.forEach(function (lv) {
      var pct = levelPercent(lv);
      cards.appendChild(h("div", { class: "level-card", style: "--accent:" + lv.color }, [
        h("div", { class: "lc-top" }, [
          h("span", { class: "lc-emoji" }, [lv.emoji]),
          h("div", {}, [
            h("div", { class: "lc-eyebrow" }, ["Level " + lv.level]),
            h("h3", {}, [lv.codename])
          ])
        ]),
        h("p", { class: "lc-tag" }, [lv.tagline]),
        h("p", { class: "lc-age" }, [lv.ageNote]),
        h("div", { class: "lc-meta" }, [
          h("span", { class: "pill" }, [lv.sessions.length + " sessions"]),
          h("span", { class: "pill" }, [lv.modules.length + " modules"])
        ]),
        h("div", { class: "lc-progress" }, [
          h("div", { class: "bar" }, [h("div", { class: "bar-fill", style: "width:" + pct + "%" })]),
          h("span", { class: "bar-label" }, [pct + "% complete"])
        ]),
        h("button", { class: "btn primary block", onclick: function () { location.hash = "#/level/" + lv.level; } },
          [pct > 0 ? "Continue Level " + lv.level + " →" : "Open Level " + lv.level + " →"])
      ]));
    });
    wrap.appendChild(cards);

    // block lab + teacher strip
    wrap.appendChild(h("div", { class: "home-strip" }, [
      h("div", { class: "strip-card", onclick: function () { location.hash = "#/lab"; } }, [
        h("span", { class: "sc-emoji" }, ["🧪"]),
        h("div", {}, [h("h4", {}, ["Block Lab"]), h("p", {}, ["A tap-to-code playground. Practise sequence, turning and loops offline — no dragging, no reading barrier."])])
      ]),
      h("div", { class: "strip-card", onclick: function () { location.hash = "#/teacher"; } }, [
        h("span", { class: "sc-emoji" }, ["🍎"]),
        h("div", {}, [h("h4", {}, ["Teacher Guide"]), h("p", {}, ["Session shape, the block colour key, the assessment rubric, and how to embed this in your platform."])])
      ])
    ]));

    // quick topic search
    wrap.appendChild(renderSearch());
    return wrap;
  }

  function renderSearch() {
    var box = h("div", { class: "search-block" });
    var input = h("input", { class: "search-input", type: "search", placeholder: "🔎 Search topics, blocks or games (e.g. 'loops', 'gravity', 'Minecraft')" });
    var results = h("div", { class: "search-results" });
    function doSearch() {
      var q = input.value.trim().toLowerCase();
      results.innerHTML = "";
      if (q.length < 2) return;
      var hits = [];
      LEVELS.forEach(function (lv) {
        lv.sessions.forEach(function (s, i) {
          var hay = (s.title + " " + s.module + " " + s.theme + " " + s.concept + " " + (s.blocks || []).join(" ")).toLowerCase();
          if (hay.indexOf(q) >= 0) hits.push({ lv: lv.level, n: i + 1, s: s });
        });
      });
      if (!hits.length) { results.appendChild(h("div", { class: "search-empty" }, ["No matches — try another word."])); return; }
      hits.slice(0, 12).forEach(function (hit) {
        results.appendChild(h("button", { class: "search-hit", onclick: function () { location.hash = "#/session/" + hit.lv + "/" + hit.n; } }, [
          h("span", { class: "sh-emoji" }, [hit.s.emoji]),
          h("span", { class: "sh-title" }, ["L" + hit.lv + " · " + hit.s.title]),
          h("span", { class: "sh-module" }, [hit.s.module])
        ]));
      });
      if (hits.length > 12) results.appendChild(h("div", { class: "search-more" }, [hits.length - 12 + " more…"]));
    }
    input.addEventListener("input", doSearch);
    box.appendChild(input);
    box.appendChild(results);
    return box;
  }

  /* ---------------- Level view ---------------- */
  var levelFilter = { module: "all", level: null };
  function viewLevel(levelNum) {
    var lv = levelByNum(levelNum);
    if (!lv) return viewHome();
    if (levelFilter.level !== levelNum) { levelFilter = { module: "all", level: levelNum }; }
    var wrap = h("div", { class: "view level", style: "--accent:" + lv.color });

    wrap.appendChild(h("div", { class: "crumbs" }, [
      crumb("Home", "#/"), sep(), h("span", {}, ["Level " + lv.level + " · " + lv.codename])
    ]));

    var pct = levelPercent(lv);
    wrap.appendChild(h("div", { class: "level-hero" }, [
      h("div", {}, [
        h("div", { class: "lh-eyebrow" }, [lv.emoji + " Level " + lv.level]),
        h("h1", {}, [lv.codename]),
        h("p", { class: "lh-tag" }, [lv.tagline]),
        h("p", { class: "lh-age" }, [lv.ageNote])
      ]),
      h("div", { class: "lh-progress" }, [progressRing(pct), h("span", {}, [pct + "% complete"])])
    ]));

    // module filter chips
    var chips = h("div", { class: "module-chips" });
    chips.appendChild(chip("All topics", levelFilter.module === "all", function () { levelFilter.module = "all"; render(); }));
    lv.modules.forEach(function (m) {
      chips.appendChild(chip(m, levelFilter.module === m, function () { levelFilter.module = m; render(); }));
    });
    wrap.appendChild(chips);

    // sessions grouped by module
    var list = h("div", { class: "session-groups" });
    lv.modules.forEach(function (mod) {
      if (levelFilter.module !== "all" && levelFilter.module !== mod) return;
      var group = lv.sessions
        .map(function (s, i) { return { s: s, n: i + 1 }; })
        .filter(function (o) { return o.s.module === mod; });
      if (!group.length) return;
      var groupDone = group.filter(function (o) { return isComplete(lv.level, o.n); }).length;
      list.appendChild(h("div", { class: "sg-head" }, [
        h("h2", {}, [mod]),
        h("span", { class: "sg-count" }, [groupDone + "/" + group.length + " done"])
      ]));
      var grid = h("div", { class: "session-grid" });
      group.forEach(function (o) { grid.appendChild(sessionCard(lv.level, o.n, o.s)); });
      list.appendChild(grid);
    });
    wrap.appendChild(list);
    return wrap;
  }

  function sessionCard(levelNum, n, s) {
    var done = isComplete(levelNum, n);
    return h("div", { class: "session-card" + (done ? " done" : ""), onclick: function () { location.hash = "#/session/" + levelNum + "/" + n; } }, [
      h("div", { class: "sc-num" }, [String(n)]),
      h("div", { class: "sc-body" }, [
        h("div", { class: "sc-emoji-title" }, [
          h("span", { class: "sc-emoji" }, [s.emoji]),
          h("h3", {}, [s.title])
        ]),
        h("p", { class: "sc-concept" }, [s.concept]),
        h("div", { class: "sc-tags" }, [
          h("span", { class: "tag theme" }, ["🎮 " + s.theme]),
          s.project ? h("span", { class: "tag proj" }, ["🏗️ " + s.project.title]) : null
        ])
      ]),
      done ? h("span", { class: "sc-check", title: "Completed" }, ["✓"]) : null
    ]);
  }

  /* ---------------- Session detail view ---------------- */
  function viewSession(levelNum, n) {
    var lv = levelByNum(levelNum);
    if (!lv) return viewHome();
    var idx = n - 1;
    var s = lv.sessions[idx];
    if (!s) return viewLevel(levelNum);
    var globalNum = (levelNum - 1) * 50 + n;
    var wrap = h("div", { class: "view session", style: "--accent:" + lv.color });

    wrap.appendChild(h("div", { class: "crumbs" }, [
      crumb("Home", "#/"), sep(),
      crumb("Level " + lv.level, "#/level/" + lv.level), sep(),
      h("span", {}, [s.module])
    ]));

    // header
    var done = isComplete(levelNum, n);
    wrap.appendChild(h("div", { class: "session-head" }, [
      h("div", { class: "sh-left" }, [
        h("div", { class: "sh-eyebrow" }, ["Session " + n + " of " + lv.sessions.length + " · #" + globalNum + " overall · ~" + (s.minutes || 60) + " min"]),
        h("h1", {}, [s.emoji + "  " + s.title]),
        h("div", { class: "sh-chips" }, [
          h("span", { class: "tag theme" }, ["🎮 " + s.theme]),
          h("span", { class: "tag mod" }, [s.module])
        ])
      ]),
      h("button", {
        class: "btn complete" + (done ? " is-done" : ""),
        onclick: function () { setComplete(levelNum, n, !done); render(); }
      }, [done ? "✓ Completed" : "Mark complete"])
    ]));

    // concept + objective callout
    wrap.appendChild(h("div", { class: "callout big-idea" }, [
      h("div", { class: "co-icon" }, ["💡"]),
      h("div", {}, [
        h("div", { class: "co-label" }, ["The big idea"]),
        h("p", {}, [s.concept]),
        s.objective ? h("p", { class: "objective" }, [h("strong", {}, ["Goal: "]), s.objective]) : null
      ])
    ]));

    // blocks used
    if (s.blocks && s.blocks.length) {
      var blockWrap = h("div", { class: "panel blocks-panel" }, [
        h("h3", {}, ["🧩 Scratch blocks in this session"])
      ]);
      var chipsB = h("div", { class: "block-chips" });
      s.blocks.forEach(function (b) {
        var cat = blockCategory(b);
        chipsB.appendChild(h("span", {
          class: "block-chip cat-" + cat,
          style: "--bc:" + CAT_COLORS[cat]
        }, [b]));
      });
      blockWrap.appendChild(chipsB);
      wrap.appendChild(blockWrap);
    }

    // warm-up
    if (s.warmup) {
      wrap.appendChild(panel("🤸 Warm-up", [h("p", {}, [s.warmup])]));
    }

    // exercises
    if (s.exercises && s.exercises.length) {
      var ol = h("ol", { class: "exercise-list" });
      s.exercises.forEach(function (ex) {
        if (typeof ex === "string") { ol.appendChild(h("li", {}, [ex])); }
        else { ol.appendChild(h("li", {}, [h("strong", {}, [ex.t + " — "]), ex.d])); }
      });
      wrap.appendChild(panel("✏️ Exercises", [ol]));
    }

    // project
    if (s.project) {
      var p = s.project;
      var must = h("div", { class: "must-chips" });
      (p.must || []).forEach(function (m) { must.appendChild(h("span", { class: "must-chip" }, [m])); });
      wrap.appendChild(h("div", { class: "panel project-panel" }, [
        h("div", { class: "pp-head" }, [h("span", { class: "pp-emoji" }, ["🏗️"]), h("h3", {}, ["Project: " + p.title])]),
        h("p", { class: "pp-brief" }, [p.brief]),
        p.must && p.must.length ? h("div", {}, [h("div", { class: "pp-label" }, ["Must include"]), must]) : null,
        p.stretch ? h("p", { class: "pp-stretch" }, [h("strong", {}, ["⭐ Stretch: "]), p.stretch]) : null
      ]));
    }

    // challenge
    if (s.challenge) {
      wrap.appendChild(h("div", { class: "callout challenge" }, [
        h("div", { class: "co-icon" }, ["🔥"]),
        h("div", {}, [h("div", { class: "co-label" }, ["Challenge for fast finishers"]), h("p", {}, [s.challenge])])
      ]));
    }

    // vocab + checklist side by side
    var twoCol = h("div", { class: "two-col" });
    if (s.vocab && s.vocab.length) {
      var vlist = h("div", { class: "vocab-list" });
      s.vocab.forEach(function (v) { vlist.appendChild(h("span", { class: "vocab" }, [v])); });
      twoCol.appendChild(panel("🔑 Key words", [vlist]));
    }
    if (s.checklist && s.checklist.length) {
      twoCol.appendChild(renderChecklist(levelNum, n, s));
    }
    wrap.appendChild(twoCol);

    // do it in Scratch — with a starter project pre-loaded with this exercise's sprites
    wrap.appendChild(starterPanel(levelNum, n));

    // prev / next
    var nav = h("div", { class: "session-nav" });
    if (n > 1) nav.appendChild(h("button", { class: "btn ghost", onclick: function () { location.hash = "#/session/" + levelNum + "/" + (n - 1); } }, ["← " + lv.sessions[idx - 1].title]));
    else if (levelNum > 1) {
      var prevLv = levelByNum(levelNum - 1);
      if (prevLv) nav.appendChild(h("button", { class: "btn ghost", onclick: function () { location.hash = "#/session/" + (levelNum - 1) + "/" + prevLv.sessions.length; } }, ["← Level " + (levelNum - 1)]));
    }
    nav.appendChild(h("span", { class: "sn-spacer" }));
    if (n < lv.sessions.length) nav.appendChild(h("button", { class: "btn primary", onclick: function () { markAndGo(levelNum, n, "#/session/" + levelNum + "/" + (n + 1)); } }, [lv.sessions[idx + 1].title + " →"]));
    else if (levelByNum(levelNum + 1)) nav.appendChild(h("button", { class: "btn primary", onclick: function () { markAndGo(levelNum, n, "#/session/" + (levelNum + 1) + "/1"); } }, ["Start Level " + (levelNum + 1) + " →"]));
    else nav.appendChild(h("button", { class: "btn primary", onclick: function () { markAndGo(levelNum, n, "#/"); } }, ["🎓 Finish the Academy"]));
    wrap.appendChild(nav);

    return wrap;
  }

  function markAndGo(lv, n, hash) { location.hash = hash; }

  function renderChecklist(levelNum, n, s) {
    var key = sessionKey(levelNum, n);
    var checks = PROGRESS.checks[key] || [];
    var panel = h("div", { class: "panel checklist-panel" }, [h("h3", {}, ["✅ I can…"])]);
    var ul = h("div", { class: "checklist" });
    s.checklist.forEach(function (item, i) {
      var cb = h("input", { type: "checkbox" });
      cb.checked = !!checks[i];
      cb.addEventListener("change", function () {
        var arr = PROGRESS.checks[key] || [];
        arr[i] = cb.checked;
        PROGRESS.checks[key] = arr;
        // auto-complete session when all boxes ticked
        if (arr.length >= s.checklist.length && arr.slice(0, s.checklist.length).every(Boolean)) {
          if (!isComplete(levelNum, n)) { setComplete(levelNum, n, true); refreshProgressUI(levelNum, n); }
        }
        saveProgress(PROGRESS);
        li.classList.toggle("ticked", cb.checked);
      });
      var li = h("label", { class: "check-item" + (checks[i] ? " ticked" : "") }, [cb, h("span", {}, [item])]);
      ul.appendChild(li);
    });
    panel.appendChild(ul);
    return panel;
  }

  // update the complete button + header ring in place (no full re-render / no scroll jump)
  function refreshProgressUI(levelNum, n) {
    var btn = document.querySelector(".session-head .btn.complete");
    if (btn) {
      var done = isComplete(levelNum, n);
      btn.textContent = done ? "✓ Completed" : "Mark complete";
      btn.classList.toggle("is-done", done);
    }
    var hp = document.querySelector(".head-progress");
    if (hp) { hp.innerHTML = ""; hp.appendChild(progressRing(overallPercent())); }
  }

  /* ---------------- Scratch starter projects ---------------- */
  // manifest keys are zero-padded, e.g. "L1-01", "L2-37"
  function padKey(levelNum, n) { return "L" + levelNum + "-" + (n < 10 ? "0" + n : "" + n); }

  function downloadStarter(key, fname) {
    var data = window.GN_STARTERS_DATA && window.GN_STARTERS_DATA[key];
    if (data) {
      try {
        var bin = atob(data), len = bin.length, arr = new Uint8Array(len);
        for (var i = 0; i < len; i++) arr[i] = bin.charCodeAt(i);
        var url = URL.createObjectURL(new Blob([arr], { type: "application/octet-stream" }));
        var a = h("a", { href: url, download: fname });
        document.body.appendChild(a); a.click();
        setTimeout(function () { URL.revokeObjectURL(url); if (a.parentNode) a.parentNode.removeChild(a); }, 2000);
        return;
      } catch (e) { /* fall through to path */ }
    }
    var base = window.GN_STARTER_BASEURL || "starters/";
    var a2 = h("a", { href: base + fname, download: fname, target: "_blank", rel: "noopener" });
    document.body.appendChild(a2); a2.click();
    setTimeout(function () { if (a2.parentNode) a2.parentNode.removeChild(a2); }, 1000);
  }

  function spriteEmoji(name) {
    var n = name.toLowerCase();
    if (/hero|player/.test(n)) return "🐱";
    if (/apple/.test(n)) return "🍎";
    if (/gem/.test(n)) return "💎";
    if (/coin/.test(n)) return "🪙";
    if (/star/.test(n)) return "⭐";
    if (/flag|goal|base/.test(n)) return "🚩";
    if (/basket/.test(n)) return "🧺";
    if (/creeper/.test(n)) return "🟩";
    if (/villager/.test(n)) return "🧑";
    if (/bird/.test(n)) return "🐤";
    if (/pipe/.test(n)) return "🟢";
    if (/platform/.test(n)) return "🟫";
    if (/paddle/.test(n)) return "🏓";
    if (/ball/.test(n)) return "⚪";
    if (/brick/.test(n)) return "🧱";
    if (/enemy/.test(n)) return "👹";
    if (/spike/.test(n)) return "🔺";
    if (/ship/.test(n)) return "🚀";
    if (/bullet/.test(n)) return "🔆";
    if (/alien/.test(n)) return "👾";
    if (/cookie/.test(n)) return "🍪";
    if (/dancer/.test(n)) return "🕺";
    return "🎭";
  }

  function starterPanel(levelNum, n) {
    var key = padKey(levelNum, n);
    var meta = (window.GN_STARTERS && window.GN_STARTERS[key]) || null;
    var fname = (meta && meta.file) || (key + ".sb3");
    var wrap = h("div", { class: "panel starter-panel" });

    wrap.appendChild(h("div", { class: "sp-head" }, [
      h("span", { class: "sp-emoji" }, ["🐱"]),
      h("div", {}, [
        h("h3", {}, ["Do this exercise in Scratch"]),
        h("p", {}, ["This starter opens in Scratch with the sprites for this exercise already loaded — no blank canvas, so students start building straight away."])
      ])
    ]));

    if (meta && meta.sprites && meta.sprites.length) {
      var chips = h("div", { class: "sprite-chips" });
      meta.sprites.forEach(function (sName) {
        chips.appendChild(h("span", { class: "sprite-chip" }, [spriteEmoji(sName) + " " + sName]));
      });
      wrap.appendChild(h("div", { class: "sp-sprites" }, [
        h("span", { class: "sp-label" }, ["Sprites already in this project"]),
        chips,
        h("span", { class: "sp-backdrop" }, ["🖼️ Backdrop: " + (meta.backdrop || "Plain")])
      ]));
    }

    var actions = h("div", { class: "sp-actions" });
    actions.appendChild(h("button", { class: "btn primary", onclick: function () { downloadStarter(key, fname); } }, ["⬇ Download this starter (.sb3)"]));
    actions.appendChild(h("a", { class: "btn ghost", href: "https://scratch.mit.edu/projects/editor/", target: "_blank", rel: "noopener" }, ["↗ Open Scratch"]));
    if (window.GN_STARTER_BASEURL) {
      var purl = window.GN_STARTER_BASEURL + fname;
      actions.appendChild(h("a", { class: "btn ghost", href: "https://turbowarp.org/editor?project_url=" + encodeURIComponent(purl), target: "_blank", rel: "noopener", title: "Opens a Scratch-compatible editor with the project already loaded" }, ["⚡ Open pre-loaded (1-click)"]));
    }
    wrap.appendChild(actions);

    wrap.appendChild(h("ol", { class: "sp-steps" }, [
      h("li", {}, [h("strong", {}, ["Download"]), " the starter project above."]),
      h("li", {}, [h("strong", {}, ["Open Scratch"]), " with the button above."]),
      h("li", {}, ["In Scratch choose ", h("strong", {}, ["File → Load from your computer"]), " and pick the file you just downloaded. The sprites appear, ready to code."])
    ]));

    wrap.appendChild(h("p", { class: "sp-note" }, [
      "New to dragging blocks? Try the ",
      h("button", { class: "linkish", onclick: function () { location.hash = "#/lab"; } }, ["Block Lab"]),
      " first — same ideas, no dragging."
    ]));
    return wrap;
  }

  /* ---------------- Block Lab view ---------------- */
  function viewLab() {
    var wrap = h("div", { class: "view lab" });
    wrap.appendChild(h("div", { class: "crumbs" }, [crumb("Home", "#/"), sep(), h("span", {}, ["Block Lab"])]));
    var host = h("div", { class: "lab-host", id: "blocklab-root" });
    wrap.appendChild(host);
    // mount after it's in the DOM
    setTimeout(function () { if (window.GN_BlockLab) window.GN_BlockLab.mount(host); }, 0);
    return wrap;
  }

  /* ---------------- Teacher guide view ---------------- */
  function viewTeacher() {
    var wrap = h("div", { class: "view teacher" });
    wrap.appendChild(h("div", { class: "crumbs" }, [crumb("Home", "#/"), sep(), h("span", {}, ["Teacher Guide"])]));
    wrap.appendChild(h("h1", {}, ["🍎 Teacher Guide"]));
    wrap.appendChild(h("p", { class: "lead" }, ["Everything you need to run the Academy and drop it into the Grade Next platform."]));

    // session shape
    wrap.appendChild(panel("⏱️ Suggested 60-minute session shape", [
      tableFrom(
        ["Minutes", "Segment", "Purpose"],
        [
          ["0–8", "Warm-up (often unplugged)", "Get the concept into the body first"],
          ["8–13", "Demo — teacher on the big screen", "Show one idea, don't tell"],
          ["13–40", "Exercises & project — in pairs", "The core hands-on work"],
          ["40–52", "Challenge / differentiation", "Fast finishers extend; others consolidate"],
          ["52–60", "Show & tell + tick the checklist", "Explaining is where learning sticks"]
        ]
      ),
      h("p", { class: "muted" }, ["Pairs at one device: a Driver (touches) and a Navigator (says what to do). Swap every 8 minutes."])
    ]));

    // scratch starter projects
    wrap.appendChild(panel("🐱 Scratch starter projects (one per session)", [
      h("p", {}, ["Every session's ", h("strong", {}, ["Do this exercise in Scratch"]), " panel gives students a ready-made Scratch project (.sb3) with the exact sprites for that exercise already placed on a themed backdrop — so no one starts from a blank canvas. The Catch lesson ships a basket, apple and gem; the Whack-a-Creeper lesson ships creepers and a villager; the platformer ships a player, platform, coins, an enemy and a goal, and so on."]),
      h("p", {}, ["Students click ", h("strong", {}, ["Download this starter"]), ", open Scratch, then ", h("strong", {}, ["File → Load from your computer"]), " and pick the file. It works with real Scratch and needs no account."]),
      h("p", { class: "muted" }, ["One-click loading: if you host the ", h("code", {}, ["starters/"]), " folder on your site and set ", h("code", {}, ["window.GN_STARTER_BASEURL"]), " to its public URL, each panel also shows a one-click \"Open pre-loaded\" button (opens a Scratch-compatible editor with the project already loaded). The .sb3 files are also embedded in the app, so downloads work offline and in the single-file build."])
    ]));

    // block colour key
    var key = h("div", { class: "cat-key" });
    [["motion", "Motion"], ["looks", "Looks"], ["sound", "Sound"], ["events", "Events"], ["control", "Control"],
     ["sensing", "Sensing"], ["operators", "Operators"], ["variables", "Variables"], ["myblocks", "My Blocks"], ["pen", "Pen"]].forEach(function (c) {
      key.appendChild(h("span", { class: "cat-swatch", style: "--bc:" + CAT_COLORS[c[0]] }, [c[1]]));
    });
    wrap.appendChild(panel("🎨 Scratch block colour key", [
      h("p", {}, ["Block chips in every session are colour-coded to match real Scratch, so colour memory transfers. Motion is blue, Control is orange, and so on."]),
      key
    ]));

    // curriculum map
    var mapWrap = h("div", {});
    LEVELS.forEach(function (lv) {
      mapWrap.appendChild(h("h3", { class: "map-lv" }, [lv.emoji + " Level " + lv.level + " — " + lv.codename + " (" + lv.sessions.length + " sessions)"]));
      var ul = h("ul", { class: "map-modules" });
      lv.modules.forEach(function (m) {
        var group = lv.sessions.map(function (s, i) { return { s: s, n: i + 1 }; }).filter(function (o) { return o.s.module === m; });
        if (!group.length) return;
        var range = group.length ? (group[0].n + "–" + group[group.length - 1].n) : "";
        ul.appendChild(h("li", {}, [h("strong", {}, [m]), " — sessions " + range + " (" + group.length + ")"]));
      });
      mapWrap.appendChild(ul);
    });
    wrap.appendChild(panel("🗺️ Curriculum map", [mapWrap]));

    // rubric
    wrap.appendChild(panel("📊 Assessment rubric (record twice: mid and end of each level)", [
      tableFrom(
        ["Skill", "Emerging", "Developing", "Secure", "Extending"],
        [
          ["Sequence", "Adds blocks randomly", "Builds a sequence with prompting", "Plans before running", "Compares two solutions"],
          ["Loops", "Doesn't use loops", "Uses when told", "Spots patterns unprompted", "Nests loops / explains why shorter"],
          ["Events & control", "One script only", "Uses a key/click trigger", "Coordinates with broadcasts", "Designs clean event flow"],
          ["Variables & data", "Ignores variables", "Uses a score with help", "Uses variables & lists confidently", "Designs a data structure (save/inventory)"],
          ["Debugging", "Deletes & restarts", "Finds bugs with help", "Locates the bug independently", "Predicts bugs before running"],
          ["Game design", "No clear goal", "Copies a build", "Designs a working game", "Iterates from playtest feedback"]
        ]
      )
    ]));

    // integration
    wrap.appendChild(panel("🔌 Embedding in the Grade Next platform", [
      h("p", {}, ["This platform is static and dependency-free, so it embeds anywhere. See the README for the full guide. Quick reference:"]),
      codeBlock([
        '<!-- Drop-in iframe, chrome hidden, deep-linked to a session -->',
        '<iframe src="scratch-academy/index.html?embed=1#/session/1/5"',
        '        style="width:100%;height:800px;border:0"></iframe>',
        '',
        '// Listen for progress from the embedded app',
        'window.addEventListener("message", function (e) {',
        '  if (e.data && e.data.source === "gradenext-scratch") {',
        '    console.log(e.data.type, e.data.data); // "progress", {level, session, complete, overall}',
        '  }',
        '});'
      ]),
      h("p", { class: "muted" }, ["URL parameters: ", h("code", {}, ["?embed=1"]), " hides the site header · ", h("code", {}, ["?session=1-5"]), " or a ", h("code", {}, ["#/session/1/5"]), " hash deep-links to any session · ", h("code", {}, ["?level=2"]), " opens a level."])
    ]));

    return wrap;
  }

  /* ---------------- Shared little components ---------------- */
  function panel(title, kids) {
    return h("div", { class: "panel" }, [h("h3", {}, [title])].concat(kids || []));
  }
  function chip(label, active, fn) {
    return h("button", { class: "chip" + (active ? " on" : ""), onclick: fn }, [label]);
  }
  function crumb(label, hash) { return h("button", { class: "crumb", onclick: function () { location.hash = hash; } }, [label]); }
  function sep() { return h("span", { class: "crumb-sep" }, ["/"]); }
  function tableFrom(headers, rows) {
    var t = h("table", { class: "data-table" });
    var thead = h("thead", {}, [h("tr", {}, headers.map(function (x) { return h("th", {}, [x]); }))]);
    var tbody = h("tbody", {}, rows.map(function (r) { return h("tr", {}, r.map(function (c) { return h("td", {}, [c]); })); }));
    t.appendChild(thead); t.appendChild(tbody);
    return h("div", { class: "table-scroll" }, [t]);
  }
  function codeBlock(lines) { return h("pre", { class: "code-block" }, [lines.join("\n")]); }

  /* ---------------- Router ---------------- */
  function parseHash() {
    var hs = (location.hash || "").replace(/^#\/?/, "");
    var parts = hs.split("/").filter(Boolean);
    if (!parts.length) {
      // support query deep-links on first load
      if (params.get("session")) {
        var m = params.get("session").split("-");
        return { view: "session", level: +m[0], n: +m[1] };
      }
      if (params.get("level")) return { view: "level", level: +params.get("level") };
      return { view: "home" };
    }
    if (parts[0] === "level") return { view: "level", level: +parts[1] };
    if (parts[0] === "session") return { view: "session", level: +parts[1], n: +parts[2] };
    if (parts[0] === "lab") return { view: "lab" };
    if (parts[0] === "teacher") return { view: "teacher" };
    return { view: "home" };
  }

  function render() {
    var route = parseHash();
    app.innerHTML = "";
    var head = renderHeader();
    if (head) app.appendChild(head);
    var main = h("main", { class: "site-main" + (EMBED ? " embed" : "") });
    var view;
    switch (route.view) {
      case "level": view = viewLevel(route.level); break;
      case "session": view = viewSession(route.level, route.n); break;
      case "lab": view = viewLab(); break;
      case "teacher": view = viewTeacher(); break;
      default: view = viewHome();
    }
    main.appendChild(view);
    app.appendChild(main);
    if (!EMBED) app.appendChild(renderFooter());
    if (route.view !== "lab") window.scrollTo(0, 0);
    notifyHost("navigate", route);
  }

  function renderFooter() {
    return h("footer", { class: "site-foot" }, [
      h("p", {}, ["Grade Next · Scratch Coding Academy — 100 game-building sessions for ages 7–12."]),
      h("p", { class: "foot-links" }, [
        h("button", { class: "linkish", onclick: function () { location.hash = "#/teacher"; } }, ["Teacher Guide"]),
        " · ",
        h("a", { href: "https://scratch.mit.edu", target: "_blank", rel: "noopener" }, ["Scratch ↗"])
      ])
    ]);
  }

  /* ---------------- Boot ---------------- */
  function boot() {
    app = document.getElementById("app");
    if (!LEVELS.length) {
      app.innerHTML = '<div style="padding:40px;text-align:center">Curriculum failed to load. Check that the curriculum-level*.js files are present.</div>';
      return;
    }
    // On GitHub Pages the starter .sb3 files are served with permissive CORS,
    // so we can offer the one-click "Open pre-loaded in Scratch" button
    // automatically (unless the host already configured a base URL).
    if (!window.GN_STARTER_BASEURL && /(^|\.)github\.io$/i.test(location.hostname)) {
      window.GN_STARTER_BASEURL = location.origin + location.pathname.replace(/[^/]*$/, "") + "starters/";
    }
    window.addEventListener("hashchange", render);
    // normalise a query deep-link into a hash so navigation is consistent
    var r = parseHash();
    if (!location.hash && (params.get("session") || params.get("level"))) {
      if (r.view === "session") location.replace("#/session/" + r.level + "/" + r.n);
      else if (r.view === "level") location.replace("#/level/" + r.level);
    }
    render();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
