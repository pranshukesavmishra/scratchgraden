/* =====================================================================
   GRADE NEXT — Lesson view
   Tutor Mode : the full lesson plan (run sheet, teaching script,
                misconceptions, assessment, differentiation, rubric).
   Student Mode: the same session as a friendly "what am I building" page.
   ===================================================================== */
(function () {
  "use strict";
  var P = window.GN_PLATFORM, GN = window.GN, U = window.GNUI, h = U.h;
  var app, S, mode;

  function qs(k) { return new URLSearchParams(location.search).get(k); }
  /* Mode is now a GLOBAL platform setting (header switch), not per session. */
  function setMode(m) { GN.setRole(m); location.reload(); }

  function card(title, icon, kids, cls) {
    return h("section", { class: "lp-card " + (cls || "") }, [
      h("h3", { class: "lp-h" }, [h("span", { class: "lp-ico" }, [icon]), title])
    ].concat(kids));
  }

  function pair(text) {
    var i = text.indexOf("→");
    if (i < 0) return h("li", {}, [text]);
    return h("li", {}, [h("b", {}, [text.slice(0, i).trim()]),
                        h("span", { class: "lp-arrow" }, [" → "]),
                        text.slice(i + 1).trim()]);
  }

  /* the student's 3-stage journey, shown so the tutor can see where they are */
  function journeyBar() {
    var st = GN.stages(S.id);
    var steps = [
      { n: 1, label: "Learn", icon: "📖", href: "learn.html?s=" + S.id, done: st.learn },
      { n: 2, label: "Recall Test", icon: "🧠", href: "quiz.html?s=" + S.id, done: st.quiz },
      { n: 3, label: "Build it", icon: "🛠", href: S.content ? S.content.href : "#", done: st.apply }
    ];
    return h("div", { class: "journey" }, steps.map(function (s, i) {
      return h("a", { class: "jstep" + (s.done ? " done" : ""), href: s.href }, [
        h("span", { class: "jn" }, [s.done ? "✓" : String(s.n)]),
        h("span", { class: "jlabel" }, [s.icon + " " + s.label]),
        i < 2 ? h("span", { class: "jarrow" }, ["→"]) : null
      ]);
    }).concat([
      st.quizBest != null ? h("span", { class: "jscore" }, ["Recall Test best: " + st.quizBest + "/" + st.quizTotal]) : null
    ]));
  }

  /* ---------------- header block ---------------- */
  function sessionHead() {
    var lvl = P.levels.filter(function (l) { return l.level === S.level; })[0] || {};
    var idx = P.order.indexOf(S.id);
    var prev = idx > 0 ? P.order[idx - 1] : null, next = idx < P.order.length - 1 ? P.order[idx + 1] : null;
    return h("div", { class: "lp-head", style: "--sc:" + S.strandColor }, [
      h("div", { class: "lp-crumbs" }, [
        h("a", { href: "curriculum.html" }, ["← Curriculum"]),
        h("span", {}, [" / " + (lvl.title || ("Level " + S.level)) + " / Session " + S.n])
      ]),
      h("div", { class: "lp-titlerow" }, [
        h("div", {}, [
          h("h1", {}, [S.title]),
          h("div", { class: "lp-tags" }, [
            h("span", { class: "strand-chip", style: "background:" + S.strandColor + "22;color:" + U.shade(S.strandColor, -50) }, [S.strand]),
            h("span", { class: "tag-chip" }, ["⭐ " + S.concept]),
            h("span", { class: "pill" }, ["⏱ " + S.minutes + " min"])
          ])
        ]),
        h("div", { class: "lp-modehint" }, [
          h("span", {}, [mode === "tutor" ? "👩‍🏫 Tutor Mode" : "🧒 Student Mode"]),
          h("button", { class: "linkish", onclick: function () { setMode(mode === "tutor" ? "student" : "tutor"); } },
            ["switch to " + (mode === "tutor" ? "Student" : "Tutor")])
        ])
      ]),
      journeyBar(),
      h("div", { class: "lp-nav" }, [
        prev ? h("a", { class: "btn ghost sm", href: "lesson.html?s=" + prev }, ["← " + P.sessions[prev].title]) : h("span", {}),
        next ? h("a", { class: "btn ghost sm", href: "lesson.html?s=" + next }, [P.sessions[next].title + " →"]) : h("span", {})
      ])
    ]);
  }

  /* ---------------- the build (content link) ---------------- */
  function buildCard() {
    var c = S.content;
    if (!c) {
      return card("Today's build", "🛠", [
        h("p", { class: "lp-note" }, ["This is an open build / consolidation session — the child works on their own project. Use the run sheet and the homework below."])
      ], "lp-build");
    }
    var kids = [
      h("div", { class: "lp-buildrow" }, [
        h("span", { class: "lp-buildemoji" }, [c.emoji || "🎮"]),
        h("div", {}, [
          h("div", { class: "lp-buildtitle" }, [c.title]),
          h("div", { class: "lp-buildmeta" }, [
            (c.kind === "project" ? "Guided project" : "Exercise") +
            (c.steps ? " · " + c.steps + (c.kind === "project" ? " steps" : " hints") : "") +
            (c.difficulty ? " · " + c.difficulty : "") + " · " + c.source
          ])
        ])
      ]),
      h("a", { class: "btn primary block big", href: c.href }, ["▶ Open the build"])
    ];
    if (c.studentOpen) kids.push(h("a", { class: "btn ghost block", href: c.studentOpen, target: "_blank", rel: "noopener" }, ["🐱 Open the student's starter"]));
    if (GN.isTutor() && c.tutorOpen) {
      kids.push(h("div", { class: "tutor-only" }, [
        h("div", { class: "tutor-only-h" }, ["👩‍🏫 Tutor only"]),
        h("a", { class: "btn ghost block", href: c.tutorOpen, target: "_blank", rel: "noopener" }, ["🔍 Open the finished code (solution)"]),
        h("p", { class: "lp-note" }, ["Do not share this screen with the student."])
      ]));
    }
    return card("Today's build", "🛠", kids, "lp-build");
  }

  function mdBold(t) {
    return String(t).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  }

  /* WHAT to teach (subject matter), not just how */
  function subjectCards() {
    var d = S.deep, out = [];
    if (!d) return out;
    out.push(card("The content to teach — " + S.concept, "\uD83D\uDCD7", [
      h("div", { class: "deep-text" }, d.explain.map(function (p) { return h("p", { html: mdBold(p) }); })),
      h("div", { class: "deep-why" }, [h("b", {}, ["Why it matters: "]), d.why]),
      h("div", { class: "deep-real" }, [h("b", {}, ["Real-world link: "]), d.real])
    ]));
    if (d.examples && d.examples.length) {
      out.push(card("Worked examples to demonstrate", "\uD83D\uDCBB", [
        h("div", { class: "wex-list" }, d.examples.map(function (ex) {
          return h("div", { class: "wex" }, [
            h("div", { class: "wex-t" }, [ex.title]),
            h("pre", { class: "wex-code" }, [ex.code]),
            h("p", { class: "wex-n" }, ["\u2192 " + ex.note])
          ]);
        }))
      ]));
    }
    if (d.extend && d.extend.length) {
      out.push(card("If there is time — go further", "\uD83D\uDE80", [
        h("ul", { class: "lp-obj" }, d.extend.map(function (e) { return h("li", {}, [e]); }))
      ], "lp-hw"));
    }
    return out;
  }

  /* the staged build the student works through */
  function briefCard() {
    var c = S.content;
    if (!c || !c.brief) return null;
    var b = c.brief;
    var kids = [h("p", { class: "lp-note" }, [
      "The student works through these " + b.stages.length + " stages (about " + b.minutes +
      " minutes, " + b.taskCount + " tasks). Use the checkpoints to see whether they are on track."])];
    b.stages.forEach(function (st, i) {
      kids.push(h("details", { class: "stage" }, [
        h("summary", {}, [
          h("span", { class: "stage-n" }, [String(i + 1)]),
          h("span", { class: "stage-t" }, [st.title]),
          h("span", { class: "stage-m" }, [st.minutes + " min"])
        ]),
        h("p", { class: "stage-goal" }, [st.goal]),
        h("ul", { class: "stage-tasks" }, st.tasks.map(function (t) { return h("li", {}, [t]); })),
        h("div", { class: "stage-check" }, [h("b", {}, ["\u2705 Checkpoint: "]), st.check])
      ]));
    });
    return card("Build brief the student follows", "\uD83D\uDEE0", kids, "lp-brief");
  }

  /* ---------------- tutor mode ---------------- */
  function tutorView() {
    var wrap = h("div", { class: "lp-grid" });
    var main = h("div", { class: "lp-main" });
    var side = h("aside", { class: "lp-side" });

    /* run sheet */
    var rs = h("ol", { class: "runsheet" });
    S.runSheet.forEach(function (r) {
      rs.appendChild(h("li", { class: "rs-item" }, [
        h("div", { class: "rs-min" }, [r.min + "′"]),
        h("div", { class: "rs-body" }, [
          h("div", { class: "rs-phase" }, [h("span", { class: "rs-ico" }, [r.icon]), r.phase, h("span", { class: "rs-what" }, [" · " + r.what])]),
          h("p", { class: "rs-detail" }, [r.detail]),
          r.note ? h("p", { class: "rs-note" }, ["💡 " + r.note]) : null
        ])
      ]));
    });
    main.appendChild(card("Run sheet — " + S.minutes + " minutes", "⏱", [rs], "lp-runsheet"));

    /* WHAT to teach */
    subjectCards().forEach(function (c) { main.appendChild(c); });

    /* teaching script */
    main.appendChild(card("Teaching script — what to actually do", "👩‍🏫", [
      h("ol", { class: "lp-steps" }, S.teach.map(function (t) { return h("li", {}, [t]); }))
    ]));

    /* misconceptions */
    main.appendChild(card("Watch for these mistakes", "⚠️", [
      h("ul", { class: "lp-watch" }, S.watch.map(pair))
    ], "lp-warn"));

    /* assessment */
    main.appendChild(card("Check for understanding", "✅", [
      h("ul", { class: "lp-ask" }, S.ask.map(pair)),
      h("div", { class: "lp-diff" }, [
        h("div", { class: "lp-diffbox support" }, [h("b", {}, ["🫱 If they're stuck"]), h("p", {}, [S.support])]),
        h("div", { class: "lp-diffbox stretch" }, [h("b", {}, ["🚀 If they finish early"]), h("p", {}, [S.stretch])])
      ])
    ]));

    /* the staged build */
    var bc = briefCard();
    if (bc) main.appendChild(bc);

    /* rubric + record */
    main.appendChild(assessCard());

    /* ---- sidebar ---- */
    side.appendChild(buildCard());
    side.appendChild(card("Learning objectives", "🎯", [
      h("ul", { class: "lp-obj" }, S.objectives.map(function (o) { return h("li", {}, [o]); }))
    ]));
    side.appendChild(card("Blocks introduced", "🧩", [
      h("div", { class: "blk-list" }, S.blocks.map(function (b) {
        return h("code", { class: "blk", style: "background:" + S.strandColor + "22;color:" + U.shade(S.strandColor, -55) }, [b]);
      }))
    ]));
    side.appendChild(card("Key vocabulary", "📖", [
      h("dl", { class: "lp-vocab" }, S.vocab.reduce(function (acc, v) {
        var i = v.indexOf("—");
        acc.push(h("dt", {}, [i > 0 ? v.slice(0, i).trim() : v]));
        if (i > 0) acc.push(h("dd", {}, [v.slice(i + 1).trim()]));
        return acc;
      }, []))
    ]));
    side.appendChild(card("Homework", "🏠", [h("p", {}, [S.homework])], "lp-hw"));
    side.appendChild(card("Warm-up hook", "🔥", [h("p", {}, [S.hook])], "lp-hook"));

    wrap.appendChild(main); wrap.appendChild(side);
    return wrap;
  }

  /* ---------------- assessment recording ---------------- */
  function assessCard() {
    var stu = GN.active();
    if (!stu) {
      return card("Record the outcome", "📝", [
        U.emptyState("Add a student to start tracking progress and build report cards.",
          "＋ Add student", function () { U.addStudentFlow(); })
      ], "lp-assess");
    }
    var rec = GN.sessionRecord(S.id) || {};
    var box = h("div", { class: "assess" });

    var rubricRow = h("div", { class: "rub-row" });
    GN.RUBRIC.forEach(function (level) {
      var on = rec.rubric === level;
      rubricRow.appendChild(h("button", { class: "rub-btn " + level + (on ? " on" : ""),
        onclick: function () {
          GN.saveSession(S.id, { rubric: level, status: rec.status === "done" ? "done" : "started" });
          render();
        } }, [
        h("b", {}, [level[0].toUpperCase() + level.slice(1)]),
        h("span", {}, [S.rubric[level]])
      ]));
    });

    var notes = h("textarea", { class: "assess-notes", rows: "3",
      placeholder: "Notes for the parent report — what went well, what to revisit…" });
    notes.value = rec.notes || "";

    var doneBtn = h("button", { class: "btn " + (rec.status === "done" ? "complete is-done" : "primary"),
      onclick: function () {
        GN.saveSession(S.id, { status: rec.status === "done" ? "started" : "done", notes: notes.value });
        render();
      } }, [rec.status === "done" ? "✓ Completed" : "Mark session complete"]);

    var saveBtn = h("button", { class: "btn ghost", onclick: function () {
      GN.saveSession(S.id, { notes: notes.value });
      saveBtn.textContent = "Saved ✓";
      setTimeout(function () { saveBtn.textContent = "Save notes"; }, 1200);
    } }, ["Save notes"]);

    box.appendChild(h("p", { class: "lp-note" }, ["Assessing " + stu.name + " against this session's rubric:"]));
    box.appendChild(rubricRow);
    box.appendChild(notes);
    box.appendChild(h("div", { class: "assess-actions" }, [doneBtn, saveBtn,
      rec.status ? h("button", { class: "linkish", onclick: function () { GN.clearSession(S.id); render(); } }, ["clear"]) : null]));
    return card("Record the outcome", "📝", [box], "lp-assess");
  }

  /* ---------------- student mode ---------------- */
  function studentView() {
    var wrap = h("div", { class: "lp-grid" });
    var main = h("div", { class: "lp-main" });
    var side = h("aside", { class: "lp-side" });

    main.appendChild(card("What you'll be able to do", "🎯", [
      h("ul", { class: "lp-obj big" }, S.objectives.map(function (o) { return h("li", {}, [o]); }))
    ], "lp-student-obj"));

    main.appendChild(card("New blocks you'll use", "🧩", [
      h("div", { class: "blk-list big" }, S.blocks.map(function (b) {
        return h("code", { class: "blk", style: "background:" + S.strandColor + "22;color:" + U.shade(S.strandColor, -55) }, [b]);
      }))
    ]));

    main.appendChild(card("Words to know", "📖", [
      h("dl", { class: "lp-vocab" }, S.vocab.reduce(function (acc, v) {
        var i = v.indexOf("—");
        acc.push(h("dt", {}, [i > 0 ? v.slice(0, i).trim() : v]));
        if (i > 0) acc.push(h("dd", {}, [v.slice(i + 1).trim()]));
        return acc;
      }, []))
    ]));

    main.appendChild(card("Stuck? Try this", "🫱", [h("p", {}, [S.support])], "lp-hook"));
    main.appendChild(card("Finished early? Challenge", "🚀", [h("p", {}, [S.stretch])], "lp-hw"));

    side.appendChild(buildCard());
    side.appendChild(card("Your homework", "🏠", [h("p", {}, [S.homework])], "lp-hw"));

    wrap.appendChild(main); wrap.appendChild(side);
    return wrap;
  }

  function render() {
    app.innerHTML = "";
    app.appendChild(U.header("curriculum"));
    var main = h("main", { class: "c-main" });
    main.appendChild(sessionHead());
    main.appendChild(mode === "student" ? studentView() : tutorView());
    app.appendChild(main);
    app.appendChild(U.footer());
  }

  function boot() {
    app = document.getElementById("app");
    var id = qs("s") || (P && P.order && P.order[0]);
    S = P && P.sessions ? P.sessions[id] : null;
    if (!S) { app.innerHTML = '<div style="padding:40px;text-align:center">Session not found. <a href="curriculum.html">Back to curriculum</a></div>'; return; }
    mode = GN.isTutor() ? "tutor" : "student";
    render();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
