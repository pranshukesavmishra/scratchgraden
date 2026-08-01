/* =====================================================================
   GRADE NEXT — Learn stage (student facing)
   Stage 1 of every session: understand the idea, meet the blocks, see a
   worked example. Then Practice (Recall Test) and Apply (build).
   ===================================================================== */
(function () {
  "use strict";
  var P = window.GN_PLATFORM, GN = window.GN, U = window.GNUI, h = U.h;
  var app, S;

  function qs(k) { return new URLSearchParams(location.search).get(k); }

  /* the 3-stage journey bar, shared look with quiz.js */
  function journey(active) {
    var st = GN.stages(S.id);
    var steps = [
      { key: "learn", n: 1, label: "Learn", icon: "📖", href: "learn.html?s=" + S.id, done: st.learn },
      { key: "quiz",  n: 2, label: "Recall Test", icon: "🧠", href: "quiz.html?s=" + S.id, done: st.quiz },
      { key: "apply", n: 3, label: "Build it", icon: "🛠", href: S.content ? S.content.href : "#", done: st.apply }
    ];
    return h("div", { class: "journey" }, steps.map(function (s, i) {
      return h("a", { class: "jstep" + (s.key === active ? " on" : "") + (s.done ? " done" : ""), href: s.href }, [
        h("span", { class: "jn" }, [s.done ? "✓" : String(s.n)]),
        h("span", { class: "jlabel" }, [s.icon + " " + s.label]),
        i < 2 ? h("span", { class: "jarrow" }, ["→"]) : null
      ]);
    }));
  }

  function head() {
    return h("div", { class: "lp-head", style: "--sc:" + S.strandColor }, [
      h("div", { class: "lp-crumbs" }, [
        h("a", { href: "curriculum.html" }, ["← Curriculum"]),
        h("span", {}, [" / Level " + S.level + " · Session " + S.n])
      ]),
      h("div", { class: "lp-titlerow" }, [
        h("div", {}, [
          h("h1", {}, [S.title]),
          h("div", { class: "lp-tags" }, [
            h("span", { class: "strand-chip", style: "background:" + S.strandColor + "22;color:" + U.shade(S.strandColor, -50) }, [S.strand]),
            h("span", { class: "tag-chip" }, ["⭐ " + S.concept])
          ])
        ]),
        h("a", { class: "btn ghost sm", href: "lesson.html?s=" + S.id }, ["👩‍🏫 Tutor view"])
      ]),
      journey("learn")
    ]);
  }

  function blockCard(b) {
    return h("div", { class: "bcard", style: "--bc:" + b.color }, [
      h("div", { class: "bcard-top" }, [
        h("code", { class: "bchip", style: "background:" + b.color }, [b.key]),
        h("span", { class: "bcat" }, [b.category])
      ]),
      h("p", { class: "bwhat" }, [b.what]),
      h("div", { class: "bex" }, [h("span", { class: "bex-l" }, ["Example"]), h("code", {}, [b.example])]),
      h("p", { class: "btip" }, ["💡 " + b.tip])
    ]);
  }

  function render() {
    app.innerHTML = "";
    app.appendChild(U.header("curriculum"));
    var main = h("main", { class: "c-main" });
    main.appendChild(head());

    var grid = h("div", { class: "lp-grid" });
    var col = h("div", { class: "lp-main" });
    var side = h("aside", { class: "lp-side" });

    /* what you'll be able to do */
    col.appendChild(h("section", { class: "lp-card lp-student-obj" }, [
      h("h3", { class: "lp-h" }, [h("span", { class: "lp-ico" }, ["🎯"]), "What you'll be able to do"]),
      h("ul", { class: "lp-obj big" }, S.objectives.map(function (o) { return h("li", {}, [o]); }))
    ]));

    /* the idea (hook, written for the student) */
    col.appendChild(h("section", { class: "lp-card lp-hook" }, [
      h("h3", { class: "lp-h" }, [h("span", { class: "lp-ico" }, ["💡"]), "The big idea"]),
      h("p", { class: "learn-idea" }, [S.hook])
    ]));

    /* blocks introduced — the heart of the Learn stage */
    if (S.blockRefs && S.blockRefs.length) {
      col.appendChild(h("section", { class: "lp-card" }, [
        h("h3", { class: "lp-h" }, [h("span", { class: "lp-ico" }, ["🧩"]),
          "Your new blocks (" + S.blockRefs.length + ")"]),
        h("p", { class: "lp-note" }, ["Read what each block does, then try it in Scratch. These are the tools for today's build."]),
        h("div", { class: "bgrid" }, S.blockRefs.map(blockCard))
      ]));
    }

    /* vocabulary */
    col.appendChild(h("section", { class: "lp-card" }, [
      h("h3", { class: "lp-h" }, [h("span", { class: "lp-ico" }, ["📖"]), "Words to know"]),
      h("dl", { class: "lp-vocab" }, S.vocab.reduce(function (acc, v) {
        var i = v.indexOf("—");
        acc.push(h("dt", {}, [i > 0 ? v.slice(0, i).trim() : v]));
        if (i > 0) acc.push(h("dd", {}, [v.slice(i + 1).trim()]));
        return acc;
      }, []))
    ]));

    /* watch out for */
    col.appendChild(h("section", { class: "lp-card lp-warn" }, [
      h("h3", { class: "lp-h" }, [h("span", { class: "lp-ico" }, ["⚠️"]), "Mistakes to avoid"]),
      h("ul", { class: "lp-watch" }, S.watch.map(function (t) {
        var i = t.indexOf("→");
        return i < 0 ? h("li", {}, [t])
          : h("li", {}, [h("b", {}, [t.slice(0, i).trim()]), h("span", { class: "lp-arrow" }, [" → "]), t.slice(i + 1).trim()]);
      }))
    ]));

    /* next step */
    var st = GN.stages(S.id);
    col.appendChild(h("section", { class: "lp-card lp-next" }, [
      h("h3", { class: "lp-h" }, [h("span", { class: "lp-ico" }, ["✅"]), "Ready?"]),
      h("p", { class: "lp-note" }, ["When you've read the blocks above, take the Recall Test to check you've understood — then build it for real."]),
      h("div", { class: "next-actions" }, [
        h("button", { class: "btn primary big", onclick: function () {
          GN.markLearned(S.id);
          location.href = "quiz.html?s=" + S.id;
        } }, [st.learn ? "🧠 Retake the Recall Test →" : "🧠 I've read this — Recall Test →"]),
        S.content ? h("a", { class: "btn ghost", href: S.content.href }, ["Skip to the build"]) : null
      ])
    ]));

    /* sidebar: today's build preview */
    if (S.content) {
      var c = S.content;
      side.appendChild(h("section", { class: "lp-card lp-build" }, [
        h("h3", { class: "lp-h" }, [h("span", { class: "lp-ico" }, ["🛠"]), "What you'll build"]),
        h("div", { class: "lp-buildrow" }, [
          h("span", { class: "lp-buildemoji" }, [c.emoji || "🎮"]),
          h("div", {}, [h("div", { class: "lp-buildtitle" }, [c.title]),
            h("div", { class: "lp-buildmeta" }, [(c.kind === "project" ? "Guided project" : "Exercise") +
              (c.steps ? " · " + c.steps + (c.kind === "project" ? " steps" : " hints") : "")])])
        ]),
        h("p", { class: "lp-note" }, ["Finish Learn and the Recall Test first — you'll build it much faster."])
      ]));
    }
    side.appendChild(h("section", { class: "lp-card lp-hw" }, [
      h("h3", { class: "lp-h" }, [h("span", { class: "lp-ico" }, ["🏠"]), "Homework"]),
      h("p", {}, [S.homework])
    ]));
    side.appendChild(h("section", { class: "lp-card" }, [
      h("h3", { class: "lp-h" }, [h("span", { class: "lp-ico" }, ["🧪"]), "Explore more blocks"]),
      h("p", { class: "lp-note" }, ["Every Scratch block, with what it does and an example."]),
      h("a", { class: "btn ghost block", href: "blocklab.html?strand=" + encodeURIComponent(S.strand) }, ["Open Block Lab →"])
    ]));

    grid.appendChild(col); grid.appendChild(side);
    main.appendChild(grid);
    app.appendChild(main);
    app.appendChild(U.footer());
  }

  function boot() {
    app = document.getElementById("app");
    S = P && P.sessions ? P.sessions[qs("s")] : null;
    if (!S) { app.innerHTML = '<div style="padding:40px;text-align:center">Session not found. <a href="curriculum.html">Back to curriculum</a></div>'; return; }
    render();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
