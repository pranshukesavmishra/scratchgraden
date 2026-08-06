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

  function lvSessions() {
    var lv = GN.level();
    var row = P.levels.filter(function (l) { return l.level === lv; })[0];
    return row ? row.sessions : P.order;
  }

  function continueCard() {
    // A learner profile always exists so progress is always tracked.
    var stu = GN.isTutor() ? GN.active() : GN.ensureLearner();
    if (!stu) {
      return h("section", { class: "cont-card" }, [
        h("div", { class: "cont-txt" }, [
          h("div", { class: "cont-kicker" }, ["Get started"]),
          h("h2", {}, ["Add your first student"]),
          h("p", {}, ["Progress, assessments and parent reports are all tracked per student. Add one to begin."])
        ]),
        h("button", { class: "btn primary big", onclick: function () { U.addStudentFlow(); } }, ["＋ Add a student"])
      ]);
    }
    // next unfinished session WITHIN the active level
    var ids = lvSessions(), prog = GN.progress(), nid = null;
    for (var i = 0; i < ids.length; i++) {
      if ((prog[ids[i]] || {}).status !== "done") { nid = ids[i]; break; }
    }
    if (!nid) nid = ids[ids.length - 1] || P.order[0];
    var s = P.sessions[nid];
    var st = GN.stats(P);
    var learnedN = 0;
    Object.keys(prog).forEach(function (k) { if (prog[k].learned) learnedN++; });
    return h("section", { class: "cont-card" }, [
      h("div", { class: "cont-txt" }, [
        h("div", { class: "cont-kicker" }, [(GN.isTutor() ? ("Next up for " + stu.name) : "Next up") + " · Level " + GN.level()]),
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
        GN.isTutor() ? h("a", { class: "btn ghost", href: "lesson.html?s=" + s.id }, ["👩‍🏫 Lesson plan"]) : null,
        learnedN >= 3 ? h("a", { class: "btn ghost review-pill", href: "quiz.html?mode=review",
          title: "10 questions from everything you have learned so far" }, ["🔀 Mixed Review"]) : null
      ])
    ]);
  }

  /* At-a-glance analytics: sessions done, stages passed, tests passed, time. */
  function statsStrip() {
    var stu = GN.isTutor() ? GN.active() : GN.ensureLearner();
    if (!stu) return h("span", {});
    var st = GN.stats(P), prog = GN.progress(stu.id);
    var learned = 0, quizzed = 0, built = 0, bestSum = 0, bestN = 0;
    Object.keys(prog).forEach(function (k) {
      var r = prog[k];
      if (r.learned) learned++;
      if (r.quiz && r.quiz.passed) quizzed++;
      if (r.applied) built++;
      if (r.quiz && r.quiz.total) { bestSum += (r.quiz.best / r.quiz.total) * 100; bestN++; }
    });
    var avg = bestN ? Math.round(bestSum / bestN) : 0;
    var lvIds = lvSessions(), lvDone = 0;
    lvIds.forEach(function (id) { if ((prog[id] || {}).status === "done") lvDone++; });
    var stk = GN.streak(stu.id);
    function stat(n, label, color) {
      return h("div", { class: "stat", style: "--sc2:" + color }, [
        h("b", {}, [String(n)]), h("span", {}, [label])]);
    }
    return h("section", { class: "panel stats-panel" }, [
      h("h2", { class: "panel-h" }, ["📈 " + (GN.isTutor() ? stu.name + "'s progress" : "Your progress")]),
      h("div", { class: "stat-row" }, [
        stat(lvDone + " / " + lvIds.length, "Level " + GN.level() + " sessions", "#703D84"),
        stat(st.done + " / " + st.total, "sessions overall", "#4c97ff"),
        stat(learned, "topics learned", "#9966ff"),
        stat(quizzed, "recall tests passed", "#34d399"),
        stat(built, "projects built", "#f59e0b"),
        stat(avg + "%", "average test score", "#ec4899"),
        stat("🔥 " + stk.current, "day streak", "#F5007E"),
        stat(GN.weekActive(stu.id) + " / 7", "days active this week", "#7F5DF9")
      ]),
      h("div", { class: "stat-bar" }, [
        U.bar(st.pct, "#4c97ff"),
        h("span", {}, [st.pct + "% of the whole course"])
      ])
    ]);
  }

  function masteryCard() {
    var stu = GN.isTutor() ? GN.active() : GN.ensureLearner();
    if (!stu) return null;
    var m = GN.mastery(P);
    var keys = Object.keys(m).sort(function (a, b) { return m[b].pct - m[a].pct; });
    return h("section", { class: "panel" }, [
      h("h2", { class: "panel-h" }, ["🧠 Skills map"]),
      h("p", { class: "panel-sub" }, [GN.isTutor()
        ? "Mastery across the Scratch block families, from the rubric level recorded in each completed session."
        : "How much of each Scratch block family you have covered so far — from your completed sessions and Recall Test scores."]),
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

  /* class leaderboard — tutors with 2+ students */
  function leaderboard() {
    if (!GN.isTutor()) return null;
    var list = GN.students();
    if (list.length < 2) return null;
    var rows = list.map(function (stu) {
      var st = GN.stats(P, stu.id), prog = GN.progress(stu.id);
      var sSum = 0, sN = 0;
      Object.keys(prog).forEach(function (k) {
        var q = prog[k].quiz;
        if (q && q.total) { sSum += q.best / q.total; sN++; }
      });
      return { stu: stu, done: st.done, avg: sN ? Math.round((sSum / sN) * 100) : 0,
               streak: GN.streak(stu.id).current };
    }).sort(function (a, b) { return b.done - a.done || b.avg - a.avg; });
    var act = GN.activeId();
    return h("section", { class: "panel" }, [
      h("h2", { class: "panel-h" }, ["🏁 Class leaderboard"]),
      h("p", { class: "panel-sub" }, ["All your students, ranked by sessions completed then average test score."]),
      h("table", { class: "lb-table" }, [
        h("thead", {}, [h("tr", {}, [h("th", {}, ["#"]), h("th", {}, ["Student"]),
          h("th", {}, ["Sessions"]), h("th", {}, ["Avg test"]), h("th", {}, ["Streak"])])]),
        h("tbody", {}, rows.map(function (r, i) {
          return h("tr", { class: r.stu.id === act ? "lb-me" : "" }, [
            h("td", { class: "lb-rank" }, [String(i + 1)]),
            h("td", {}, [r.stu.name]),
            h("td", {}, [r.done + " / " + P.order.length]),
            h("td", {}, [r.avg + "%"]),
            h("td", {}, ["🔥 " + r.streak])
          ]);
        }))
      ])
    ]);
  }

  function levelsCard() {
    return h("section", { class: "panel" }, [
      h("h2", { class: "panel-h" }, ["📚 Your two levels"]),
      h("div", { class: "lv-cards" }, P.levels.map(function (lv) {
        var ls = GN.levelStats(P, lv.level);
        return h("div", { class: "lv-card" + (lv.level === GN.level() ? " lv-active" : ""),
          style: "--lvc:" + lv.color }, [
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
      h("h1", {}, ["Scratch Academy by GradeNext"]),
      h("p", {}, ["A complete teaching system for ages 7–12: " + P.meta.sessionCount +
                  " lesson-planned sessions, " + P.meta.projectCount + " guided projects and " +
                  P.meta.exerciseCount + " exercises — with assessment and parent reports built in."])
    ]));

    main.appendChild(continueCard());
    main.appendChild(statsStrip());

    main.appendChild(U.modeBanner());
    main.appendChild(h("div", { class: "tiles" }, [
      tile("curriculum.html", "📚", "Curriculum", P.meta.sessionCount + " sessions · learn, test, then build", "#4c97ff"),
      tile("puzzles.html", "🧩", "Code Puzzles", "Rebuild real scripts from shuffled blocks — earn stars", "#F5007E"),
      tile("flashcards.html", "🃏", "Flashcards", "Coding words trainer that remembers what you find hard", "#7F5DF9"),
      tile("blocklab.html", "🧪", "Block Lab", P.meta.blockCount + " Scratch blocks explained with examples", "#f59e0b"),
      tile("projects.html", "🚀", "Project Library", P.meta.projectCount + " real guided Scratch projects", "#7c3aed"),
      GN.isTutor()
        ? tile("report.html", "📊", "Progress & reports", "Parent-ready report cards and certificates", "#34d399")
        : tile("report.html", "📊", "My progress", "Sessions completed, skills mastered and certificates", "#34d399")
    ]));

    var m = masteryCard(); if (m) main.appendChild(m);
    main.appendChild(U.badgesPanel(P));
    var lb = leaderboard(); if (lb) main.appendChild(lb);
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
