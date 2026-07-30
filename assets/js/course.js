/* =====================================================================
   GRADE NEXT — Scratch Coding Academy (exercise browser)
   Reference-style: Sessions -> Exercises, opening the embedded editor.
   ===================================================================== */
(function () {
  "use strict";
  var C = window.GN_COURSE || { sessions: [], exercises: {} };
  var app;
  var LEVELS = { "Easy": 1, "Medium": 2, "Hard": 3 };

  function h(tag, attrs, kids) {
    var e = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "class") e.className = attrs[k];
      else if (k === "html") e.innerHTML = attrs[k];
      else if (k.slice(0, 2) === "on" && typeof attrs[k] === "function") e.addEventListener(k.slice(2), attrs[k]);
      else e.setAttribute(k, attrs[k]);
    });
    (kids || []).forEach(function (c) { if (c == null) return; e.appendChild(typeof c === "string" ? document.createTextNode(c) : c); });
    return e;
  }
  function thumb(emoji, color, big) {
    return h("div", { class: "thumb" + (big ? " big" : ""), style: "background:linear-gradient(135deg," + color + "," + shade(color, -18) + ")" }, [
      h("span", { class: "thumb-emoji" }, [emoji])
    ]);
  }
  function shade(hex, amt) {
    var n = parseInt(hex.slice(1), 16), r = (n >> 16) + amt, g = ((n >> 8) & 255) + amt, b = (n & 255) + amt;
    r = Math.max(0, Math.min(255, r)); g = Math.max(0, Math.min(255, g)); b = Math.max(0, Math.min(255, b));
    return "#" + (0x1000000 + r * 0x10000 + g * 0x100 + b).toString(16).slice(1);
  }
  function levelBar(level) {
    var n = LEVELS[level] || 1;
    var wrap = h("div", { class: "levelbar" });
    for (var i = 1; i <= 3; i++) wrap.appendChild(h("span", { class: "seg" + (i <= n ? " on lv" + n : "") }));
    return h("div", { class: "level-wrap" }, [wrap, h("span", { class: "level-txt" }, ["Level : " + level])]);
  }

  /* ---------------- header ---------------- */
  function header() {
    return h("header", { class: "c-head" }, [
      h("div", { class: "c-brand", onclick: function () { location.hash = "#/"; }, role: "button", tabindex: "0" }, [
        h("span", { class: "c-mark" }, ["🐱"]),
        h("div", {}, [h("div", { class: "c-name" }, ["Grade Next"]), h("div", { class: "c-sub" }, ["Scratch Coding Academy"])])
      ]),
      h("nav", { class: "c-nav" }, [
        h("a", { class: "c-navbtn", href: "blocklab.html" }, ["🧪 Block Lab"]),
        h("a", { class: "c-navbtn", href: "index-classic.html" }, ["📚 Full Curriculum"])
      ])
    ]);
  }

  /* ---------------- sessions grid ---------------- */
  function viewHome() {
    var wrap = h("div", { class: "view" });
    wrap.appendChild(h("section", { class: "c-hero" }, [
      h("h1", {}, ["Build real games, one session at a time 🎮"]),
      h("p", {}, ["Pick a session, open an exercise, and the Scratch editor opens right here — pre-loaded with the sprites. Read the Instructions, watch the Desired Output, then build it."])
    ]));
    var grid = h("div", { class: "session-grid" });
    C.sessions.forEach(function (s) {
      grid.appendChild(h("div", { class: "s-card", onclick: function () { location.hash = "#/session/" + s.id; } }, [
        thumb(s.emoji, s.color),
        h("div", { class: "s-body" }, [
          h("div", { class: "s-eyebrow" }, ["Session " + s.n]),
          h("h3", {}, [s.title]),
          h("p", {}, [s.concept]),
          h("div", { class: "s-meta" }, [h("span", { class: "pill" }, ["💡 " + s.exercises.length + " exercises"])])
        ])
      ]));
    });
    wrap.appendChild(grid);
    return wrap;
  }

  /* ---------------- exercises in a session ---------------- */
  function viewSession(sid) {
    var s = C.sessions.filter(function (x) { return x.id === sid; })[0];
    if (!s) return viewHome();
    var wrap = h("div", { class: "view" });
    wrap.appendChild(h("div", { class: "crumbs" }, [
      h("a", { class: "crumb", href: "#/" }, ["← Go Back"]), h("span", {}, [" / "]),
      h("span", {}, ["Session " + s.n + " · " + s.title])
    ]));
    wrap.appendChild(h("h1", { class: "s-title" }, [s.emoji + "  Session " + s.n + " — " + s.title]));
    wrap.appendChild(h("p", { class: "s-concept" }, [s.concept]));

    var search = h("input", { class: "c-search", type: "search", placeholder: "🔎 Search exercises by name" });
    var grid = h("div", { class: "ex-grid" });
    function draw() {
      var q = (search.value || "").toLowerCase();
      grid.innerHTML = "";
      s.exercises.map(function (id) { return C.exercises[id]; }).filter(function (ex) {
        return !q || (ex.title + " " + ex.tag + " " + ex.type).toLowerCase().indexOf(q) >= 0;
      }).forEach(function (ex) { grid.appendChild(exCard(ex)); });
      if (!grid.children.length) grid.appendChild(h("div", { class: "empty" }, ["No exercises match."]));
    }
    search.addEventListener("input", draw);
    wrap.appendChild(h("div", { class: "c-searchwrap" }, [search]));
    wrap.appendChild(grid);
    draw();
    return wrap;
  }

  function exCard(ex) {
    var typeClass = ex.type.replace(/\s+/g, "").toLowerCase();
    return h("a", { class: "ex-card", href: "exercise.html?ex=" + encodeURIComponent(ex.id) }, [
      thumb(ex.emoji, ex.color, true),
      h("div", { class: "ex-body" }, [
        h("div", { class: "ex-toprow" }, [
          h("span", { class: "type-badge " + typeClass }, [ex.type]),
        ]),
        h("h3", {}, [ex.title]),
        h("p", { class: "ex-story" }, [ex.story]),
        h("div", { class: "ex-footer" }, [
          levelBar(ex.level),
          h("span", { class: "tag-chip" }, ["⭐ " + ex.tag])
        ])
      ]),
      h("span", { class: "ex-go" }, ["Open →"])
    ]);
  }

  /* ---------------- router ---------------- */
  function render() {
    var hs = (location.hash || "").replace(/^#\/?/, "");
    var parts = hs.split("/").filter(Boolean);
    app.innerHTML = "";
    app.appendChild(header());
    var main = h("main", { class: "c-main" });
    if (parts[0] === "session" && parts[1]) main.appendChild(viewSession(parts[1]));
    else main.appendChild(viewHome());
    app.appendChild(main);
    app.appendChild(h("footer", { class: "c-foot" }, [
      h("p", {}, ["Grade Next · Scratch Coding Academy — game-building exercises for ages 7–12."])
    ]));
    window.scrollTo(0, 0);
  }

  function boot() {
    app = document.getElementById("app");
    if (!C.sessions.length) { app.innerHTML = '<div style="padding:40px;text-align:center">Course data failed to load.</div>'; return; }
    window.addEventListener("hashchange", render);
    render();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
