/* =====================================================================
   GRADE NEXT — Block Lab
   Every Scratch block taught in the curriculum: what it does, an example,
   the gotcha, and which session teaches it. Shows what the student has
   already unlocked.
   ===================================================================== */
(function () {
  "use strict";
  var P = window.GN_PLATFORM, GN = window.GN, U = window.GNUI, h = U.h;
  var app, filter = { cat: "", q: "", only: "all" };

  function qs(k) { return new URLSearchParams(location.search).get(k); }

  /* a block is "unlocked" once the student has learned a session that teaches it */
  function unlockedSet() {
    var prog = GN.progress(), out = {};
    Object.keys(P.blocks).forEach(function (k) {
      var b = P.blocks[k];
      out[k] = b.sessions.some(function (sid) {
        var r = prog[sid];
        return r && (r.learned || r.status === "done");
      });
    });
    return out;
  }

  function blockCard(b, unlocked) {
    var first = b.sessions[0];
    var s = first ? P.sessions[first] : null;
    return h("div", { class: "bcard" + (unlocked ? " unlocked" : ""), style: "--bc:" + b.color }, [
      h("div", { class: "bcard-top" }, [
        window.SB ? SB.chip(b.key) : h("code", { class: "bchip", style: "background:" + b.color }, [b.key]),
        unlocked ? h("span", { class: "bunlock" }, ["✓ learned"]) : null
      ]),
      h("p", { class: "bwhat" }, [b.what]),
      window.SB ? SB.render(b.example) : h("div", { class: "bex" }, [h("code", {}, [b.example])]),
      h("p", { class: "btip" }, ["💡 " + b.tip]),
      (b.uses && b.uses.length) ? h("div", { class: "buses" }, [
        h("div", { class: "buses-h" }, ["Ways to use it"]),
        h("ul", {}, b.uses.map(function (u) { return h("li", {}, [u]); }))
      ]) : null,
      s ? h("a", { class: "btaught", href: "learn.html?s=" + s.id }, [
        "Taught in L" + s.level + " S" + s.n + " · " + s.title + " →"]) : null
    ]);
  }

  function toolbar() {
    var q = h("input", { class: "c-search", type: "search", placeholder: "🔎 Search blocks (e.g. clone, score, touching)" });
    q.value = filter.q;
    q.addEventListener("input", function () { filter.q = q.value.toLowerCase(); render(true); });

    var cats = h("select", { class: "gn-select", onchange: function () { filter.cat = cats.value; render(true); } },
      [h("option", { value: "" }, ["All categories"])].concat(
        Object.keys(P.blockCategories).map(function (c) {
          var o = h("option", { value: c }, [P.blockCategories[c].emoji + " " + c]);
          if (filter.cat === c) o.selected = true;
          return o;
        })));

    var only = h("select", { class: "gn-select", onchange: function () { filter.only = only.value; render(true); } },
      [["all", "All blocks"], ["unlocked", "Only what I've learned"], ["locked", "Not learned yet"]].map(function (p) {
        var o = h("option", { value: p[0] }, [p[1]]);
        if (filter.only === p[0]) o.selected = true;
        return o;
      }));

    return h("div", { class: "gn-toolbar" }, [q, cats, only]);
  }

  function render(keep) {
    if (!GN.isTutor()) GN.ensureLearner();   // progress must always be tracked
    var y = window.scrollY;
    app.innerHTML = "";
    app.appendChild(U.header("blocklab"));
    var main = h("main", { class: "c-main" });
    var un = unlockedSet();
    var nUn = Object.keys(un).filter(function (k) { return un[k]; }).length;

    main.appendChild(h("section", { class: "c-hero" }, [
      h("h1", {}, ["🧪 Block Lab"]),
      h("p", {}, ["Every one of the " + P.meta.blockCount + " Scratch blocks taught across the course — what it does, an example you can copy, and the mistake to avoid. " +
                  (GN.isTutor() && GN.active() ? GN.active().name + " has unlocked " + nUn + " so far."
                                               : "You have unlocked " + nUn + " so far.")])
    ]));
    main.appendChild(toolbar());

    var cats = Object.keys(P.blockCategories);
    var shown = 0;
    cats.forEach(function (cat) {
      if (filter.cat && filter.cat !== cat) return;
      var meta = P.blockCategories[cat];
      var list = Object.keys(P.blocks).filter(function (k) {
        var b = P.blocks[k];
        if (b.category !== cat) return false;
        if (filter.only === "unlocked" && !un[k]) return false;
        if (filter.only === "locked" && un[k]) return false;
        if (filter.q && (k + " " + b.what + " " + b.example).toLowerCase().indexOf(filter.q) < 0) return false;
        return true;
      });
      if (!list.length) return;
      shown += list.length;
      main.appendChild(h("section", { class: "blab-sec" }, [
        h("div", { class: "blab-head", style: "--bc:" + meta.color }, [
          h("span", { class: "blab-emoji", style: "background:" + meta.color + "22" }, [meta.emoji]),
          h("div", {}, [h("h2", {}, [cat]), h("p", {}, [meta.blurb])]),
          h("span", { class: "blab-count" }, [list.length + " blocks"])
        ]),
        h("div", { class: "bgrid" }, list.map(function (k) { return blockCard(P.blocks[k], un[k]); }))
      ]));
    });
    if (!shown) main.appendChild(h("div", { class: "empty" }, ["No blocks match that search."]));

    app.appendChild(main);
    app.appendChild(U.footer());
    if (keep) window.scrollTo(0, y); else window.scrollTo(0, 0);
  }

  function boot() {
    app = document.getElementById("app");
    if (!P || !P.blocks) { app.innerHTML = '<div style="padding:40px;text-align:center">Block data failed to load.</div>'; return; }
    var s = qs("strand");
    // the curriculum uses strand names; map the ones that match a block category
    if (s && P.blockCategories[s]) filter.cat = s;
    render();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
