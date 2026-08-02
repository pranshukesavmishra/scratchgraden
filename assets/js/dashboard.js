/* =====================================================================
   GRADE NEXT — Dashboard (home)
   Where a tutor or student lands: continue where you left off, see
   progress, jump into the curriculum, projects or reports.
   ===================================================================== */
(function () {
  "use strict";
  var P = window.GN_PLATFORM, GN = window.GN, U = window.GNUI, h = U.h;
  var app;

  function tile(href, emoji, title, text, color) {
    return h("a", { class: "tile", href: href, style: "--tc:" + color }, [
      h("span", { class: "tile-emoji" }, [emoji]),
      h("div", {}, [h("h3", {}, [title]), h("p", {}, [text])]),
      h("span", { class: "tile-go" }, ["→"])
    ]);
  }

  function continueCard() {
    var stu = GN.active();
    if (!stu) {
      if (!GN.isTutor()) {
        // Students never manage accounts — send them straight into the course.
        var first = P.order[0];
        return h("section", { class: "cont-card" }, [
          h("div", { class: "cont-txt" }, [
            h("div", { class: "cont-kicker" }, ["Start here"]),
            h("h2", {}, ["Session 1 · " + P.sessions[first].title]),
            h("p", {}, ["Learn the blocks, take the Recall Test, then build it for real."])
          ]),
          h("div", { class: "cont-actions" }, [
            h("a", { class: "btn primary big", href: "learn.html?s=" + first }, ["▶ Start learning"]),
            h("a", { class: "btn ghost", href: "curriculum.html" }, ["See all 100 sessions"])
          ])
        ]);
      }
      return h("section", { class: "cont-card" }, [
        h("div", { class: "cont-txt" }, [
          h("div", { class: "cont-kicker" }, ["Get started"]),
          h("h2", {}, ["Add your first student"]),
          h("p", {}, ["Progress, assessments and parent reports are all tracked per student. Add one to begin."])
        ]),
        h("button", { class: "btn primary big", onclick: function () { U.addStudentFlow(); } }, ["＋ Add a student"])
      ]);
    }
    var nid = GN.nextSession(P), s = P.sessions[nid];
    var st = GN.stats(P);
    return h("section", { class: "cont-card" }, [
      h("div", { class: "cont-txt" }, [
        h("div", { class: "cont-kicker" }, ["Next up for " + stu.name]),
        h("h2", {}, ["Session " + s.n + " · " + s.title]),
        h("p", {}, [s.concept + (s.content ? " — building " + s.content.title : "")]),
        h("div", { class: "cont-prog" }, [
          U.bar(st.pct, "#4c97ff"),
          h("span", {}, [st.done + " of " + st.total + " sessions complete"])
        ])
      ]),
      h("div", { class: "cont-actions" }, [
        h("a", { class: "btn primary big", href: "learn.html?s=" + s.id }, ["▶ Start learning"]),
        h("a", { class: "btn ghost", href: "quiz.html?s=" + s.id }, ["🧠 Recall Test"]),
        GN.isTutor() ? h("a", { class: "btn ghost", href: "lesson.html?s=" + s.id }, ["👩‍🏫 Lesson plan"]) : null
      ])
    ]);
  }

  function masteryCard() {
    var stu = GN.active();
    if (!stu) return null;
    var m = GN.mastery(P);
    var keys = Object.keys(m).sort(function (a, b) { return m[b].pct - m[a].pct; });
    return h("section", { class: "panel" }, [
      h("h2", { class: "panel-h" }, ["🧠 Skills map"]),
      h("p", { class: "panel-sub" }, ["Mastery across the Scratch block families, from the rubric level recorded in each completed session."]),
      h("div", { class: "mastery" }, keys.map(function (k) {
        var x = m[k];
        return h("div", { class: "mrow" }, [
          h("span", { class: "mname" }, [h("span", { class: "strand-dot", style: "background:" + x.color }), k]),
          U.bar(x.pct, x.color),
          h("span", { class: "mpct" }, [x.pct + "%"]),
          h("span", { class: "mcount" }, [x.touched + "/" + x.total])
        ]);
      }))
    ]);
  }

  function levelsCard() {
    return h("section", { class: "panel" }, [
      h("h2", { class: "panel-h" }, ["📚 Your two levels"]),
      h("div", { class: "lv-cards" }, P.levels.map(function (lv) {
        var ls = GN.levelStats(P, lv.level);
        return h("a", { class: "lv-card", href: "curriculum.html", style: "--lvc:" + lv.color }, [
          h("span", { class: "lv-card-emoji" }, [lv.emoji]),
          h("h3", {}, [lv.title]),
          h("p", {}, [lv.blurb]),
          U.bar(ls.pct, lv.color),
          h("span", { class: "lv-card-meta" }, [ls.done + " / " + ls.total + " sessions"])
        ]);
      }))
    ]);
  }

  function render() {
    app.innerHTML = "";
    app.appendChild(U.header("home"));
    var main = h("main", { class: "c-main" });

    main.appendChild(h("section", { class: "c-hero dash-hero" }, [
      h("h1", {}, ["Grade Next Scratch Academy"]),
      h("p", {}, ["A complete teaching system for ages 7–12: " + P.meta.sessionCount +
                  " lesson-planned sessions, " + P.meta.projectCount + " guided projects and " +
                  P.meta.exerciseCount + " exercises — with assessment and parent reports built in."])
    ]));

    main.appendChild(continueCard());

    main.appendChild(U.modeBanner());
    main.appendChild(h("div", { class: "tiles" }, [
      tile("curriculum.html", "📚", "Curriculum", P.meta.sessionCount + " sessions · learn, test, then build", "#4c97ff"),
      tile("blocklab.html", "🧪", "Block Lab", P.meta.blockCount + " Scratch blocks explained with examples", "#f59e0b"),
      tile("projects.html", "🚀", "Project Library", P.meta.projectCount + " real guided Scratch projects", "#7c3aed"),
      GN.isTutor() ? tile("report.html", "📊", "Progress & reports", "Parent-ready report cards and certificates", "#34d399") : null
    ]));

    var m = masteryCard(); if (m) main.appendChild(m);
    main.appendChild(levelsCard());

    app.appendChild(main);
    app.appendChild(U.footer());
  }

  function boot() {
    app = document.getElementById("app");
    if (!P || !P.order) { app.innerHTML = '<div style="padding:40px;text-align:center">Platform data failed to load.</div>'; return; }
    render();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
