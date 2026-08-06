/* =====================================================================
   GRADE NEXT — Curriculum browser
   The full 2-level, 100-session scope & sequence with live progress.
   ===================================================================== */
(function () {
  "use strict";
  var P = window.GN_PLATFORM, GN = window.GN, U = window.GNUI, h = U.h;
  var app, filter = { level: 0, strand: "", q: "", show: "all" };

  function statusOf(sid) {
    var r = GN.sessionRecord(sid);
    return r ? (r.status || "started") : "none";
  }

  function sessionRow(s) {
    var st = statusOf(s.id);
    var mark = st === "done" ? "✓" : (st === "started" ? "◐" : s.n);
    var c = s.content;
    var stg = GN.stages(s.id);
    return h("div", { class: "sess-row " + st }, [
      h("a", { class: "sess-hit", href: "learn.html?s=" + s.id }, [
        h("span", { class: "sess-n", style: "background:" + (st === "done" ? "var(--good)" : st === "started" ? "var(--warn)" : "#e9eef8") +
                   (st === "none" ? "" : ";color:#fff") }, [String(mark)]),
        h("div", { class: "sess-main" }, [
          h("div", { class: "sess-title" }, [s.title]),
          h("div", { class: "sess-meta" }, [
            h("span", { class: "strand-dot", style: "background:" + s.strandColor }),
            h("span", { class: "sess-concept" }, [s.concept]),
            c ? h("span", { class: "sess-content" }, [(c.kind === "project" ? "🚀 " : "🎮 ") + c.title]) : h("span", { class: "sess-content build" }, ["🛠 Build session"])
          ])
        ])
      ]),
      h("div", { class: "sess-side" }, [
        h("div", { class: "sess-stages", title: "Learn · Recall Test · Build" }, [
          h("span", { class: "sdot" + (stg.learn ? " on" : ""), title: "Learn" }, ["📖"]),
          h("span", { class: "sdot" + (stg.quiz ? " on" : ""), title: "Recall Test" }, ["🧠"]),
          h("span", { class: "sdot" + (stg.apply ? " on" : ""), title: "Build" }, ["🛠"])
        ]),
        h("a", { class: "sess-plan", href: "lesson.html?s=" + s.id, title: "Tutor lesson plan" }, ["👩‍🏫 Plan"])
      ])
    ]);
  }

  function levelSection(lv) {
    var ls = GN.levelStats(P, lv.level);
    var ids = lv.sessions.filter(function (id) {
      var s = P.sessions[id];
      if (filter.strand && s.strand !== filter.strand) return false;
      if (filter.show === "done" && statusOf(id) !== "done") return false;
      if (filter.show === "todo" && statusOf(id) === "done") return false;
      if (filter.q) {
        var hay = (s.title + " " + s.concept + " " + (s.content ? s.content.title : "")).toLowerCase();
        if (hay.indexOf(filter.q) < 0) return false;
      }
      return true;
    });
    if (!ids.length) return null;

    var sec = h("section", { class: "lv-sec" }, [
      h("div", { class: "lv-head", style: "--lvc:" + lv.color }, [
        h("span", { class: "lv-emoji" }, [lv.emoji]),
        h("div", { class: "lv-txt" }, [
          h("h2", {}, [lv.title]),
          h("p", {}, [lv.blurb])
        ]),
        h("div", { class: "lv-prog" }, [
          h("div", { class: "lv-pct" }, [ls.done + " / " + ls.total]),
          U.bar(ls.pct, lv.color),
          h("div", { class: "lv-sub" }, [ls.pct + "% complete"])
        ])
      ])
    ]);
    var list = h("div", { class: "sess-list" });
    ids.forEach(function (id) { list.appendChild(sessionRow(P.sessions[id])); });
    sec.appendChild(list);
    return sec;
  }

  function toolbar() {
    var q = h("input", { class: "c-search", type: "search", placeholder: "🔎 Search sessions, concepts or projects" });
    q.value = filter.q;
    q.addEventListener("input", function () { filter.q = q.value.toLowerCase(); render(true); });

    var strandSel = h("select", { class: "gn-select", onchange: function () { filter.strand = strandSel.value; render(true); } },
      [h("option", { value: "" }, ["All strands"])].concat(
        Object.keys(P.strands).map(function (s) {
          var o = h("option", { value: s }, [s]);
          if (filter.strand === s) o.selected = true;
          return o;
        })));

    var showSel = h("select", { class: "gn-select", onchange: function () { filter.show = showSel.value; render(true); } },
      [["all", "All sessions"], ["todo", "Not finished"], ["done", "Completed"]].map(function (p) {
        var o = h("option", { value: p[0] }, [p[1]]);
        if (filter.show === p[0]) o.selected = true;
        return o;
      }));

    return h("div", { class: "gn-toolbar" }, [q, strandSel, showSel]);
  }

  function render(keepScroll) {
    var y = window.scrollY;
    app.innerHTML = "";
    app.appendChild(U.header("curriculum"));
    var main = h("main", { class: "c-main" });

    var st = GN.stats(P);
    main.appendChild(h("section", { class: "c-hero" }, [
      h("h1", {}, ["The Scratch Academy curriculum"]),
      h("p", {}, [P.meta.sessionCount + " sessions · " + P.meta.levelCount + " levels · " +
                  P.meta.conceptCount + " concepts · every session is a full " + P.meta.minutes +
                  "-minute lesson plan with objectives, teaching script, assessment and homework."]),
      GN.active() ? h("p", { class: "gn-hero-prog" }, [
        h("b", {}, [GN.active().name]), " has completed ", h("b", {}, [String(st.done)]),
        " of " + st.total + " sessions."
      ]) : null
    ]));

    main.appendChild(toolbar());
    // The curriculum shows ONE level at a time — switch with the header control.
    var LV = GN.level();
    var other = LV === 1 ? 2 : 1;
    main.appendChild(h("div", { class: "lv-note" }, [
      h("span", { class: "lv-chip l" + LV }, ["LEVEL " + LV]),
      h("span", {}, [LV === 1 ? "Foundations — sessions 1–50" : "Logic, Data & Game Engineering — sessions 1–50"]),
      h("button", { class: "linkish", onclick: function () { GN.setLevel(other); location.reload(); } },
        ["Switch to Level " + other + " →"])
    ]));
    var any = false;
    P.levels.filter(function (lv) { return lv.level === LV; }).forEach(function (lv) {
      var sec = levelSection(lv);
      if (sec) { main.appendChild(sec); any = true; }
    });
    if (!any) main.appendChild(h("div", { class: "empty" }, ["No sessions match those filters."]));

    app.appendChild(main);
    app.appendChild(U.footer());
    if (keepScroll) window.scrollTo(0, y); else window.scrollTo(0, 0);
  }

  function boot() {
    app = document.getElementById("app");
    if (!P || !P.order) { app.innerHTML = '<div style="padding:40px;text-align:center">Curriculum data failed to load.</div>'; return; }
    render();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
