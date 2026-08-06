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
    return h("div", { class: "journey no-print" }, steps.map(function (s, i) {
      return h("a", { class: "jstep" + (s.key === active ? " on" : "") + (s.done ? " done" : ""), href: s.href,
        onclick: s.key === "apply" && S.content ? function () { GN.markApplied(S.id); } : null }, [
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
        h("div", { class: "lp-headactions no-print" }, [
          ttsButton(),
          h("button", { class: "btn ghost sm", onclick: function () { window.print(); }, title: "Print this lesson as a handout" }, ["🖨 Handout"]),
          GN.isTutor() ? h("a", { class: "btn ghost sm", href: "lesson.html?s=" + S.id }, ["👩‍🏫 Lesson plan"]) : null
        ])
      ]),
      journey("learn")
    ]);
  }

  /* read the lesson aloud for young readers (Web Speech API) */
  var speaking = false;
  function ttsButton() {
    if (!("speechSynthesis" in window)) return null;
    var btn = h("button", { class: "tts-btn", title: "Read this lesson aloud", onclick: function () {
      if (speaking) { speechSynthesis.cancel(); speaking = false; btn.classList.remove("on"); return; }
      var d = S.deep;
      var text = [S.title + ".", S.hook].concat(S.objectives)
        .concat(d ? d.explain.map(function (t) { return t.replace(/\*\*/g, ""); }) : [])
        .join(" ");
      var u = new SpeechSynthesisUtterance(text);
      u.rate = 0.95; u.pitch = 1.05;
      u.onend = function () { speaking = false; btn.classList.remove("on"); };
      speechSynthesis.cancel();
      speechSynthesis.speak(u);
      speaking = true; btn.classList.add("on");
    } }, ["🔊 Read aloud"]);
    return btn;
  }

  function blockCard(b) {
    return h("div", { class: "bcard", style: "--bc:" + b.color }, [
      h("div", { class: "bcard-top" }, [
        window.SB ? SB.chip(b.key) : h("code", { class: "bchip", style: "background:" + b.color }, [b.key]),
        h("span", { class: "bcat" }, [b.category])
      ]),
      h("p", { class: "bwhat" }, [b.what]),
      window.SB ? SB.render(b.example) : h("div", { class: "bex" }, [h("code", {}, [b.example])]),
      h("p", { class: "btip" }, ["💡 " + b.tip]),
      (b.uses && b.uses.length) ? h("div", { class: "buses" }, [
        h("div", { class: "buses-h" }, ["Ways to use it"]),
        h("ul", {}, b.uses.map(function (u) { return h("li", {}, [u]); }))
      ]) : null
    ]);
  }

  /* the subject content: what this topic actually IS */
  function deepSection() {
    var d = S.deep;
    if (!d) return null;
    var out = [];
    out.push(h("section", { class: "lp-card" }, [
      h("h3", { class: "lp-h" }, [h("span", { class: "lp-ico" }, ["📗"]), "Understanding " + S.concept]),
      h("div", { class: "deep-text" }, d.explain.map(function (para) {
        return h("p", { html: mdBold(para) });
      })),
      h("div", { class: "deep-why" }, [h("b", {}, ["Why this matters: "]), d.why]),
      h("div", { class: "deep-real" }, [h("b", {}, ["Where you've seen it: "]), d.real])
    ]));
    if (d.examples && d.examples.length) {
      out.push(h("section", { class: "lp-card" }, [
        h("h3", { class: "lp-h" }, [h("span", { class: "lp-ico" }, ["💻"]), "Worked examples"]),
        h("div", { class: "wex-list" }, d.examples.map(function (ex) {
          return h("div", { class: "wex" }, [
            h("div", { class: "wex-t" }, [ex.title]),
            window.SB ? SB.render(ex.code) : h("pre", { class: "wex-code" }, [ex.code]),
            h("p", { class: "wex-n" }, ["→ " + ex.note])
          ]);
        }))
      ]));
    }
    if (d.extend && d.extend.length) {
      out.push(h("section", { class: "lp-card lp-hw" }, [
        h("h3", { class: "lp-h" }, [h("span", { class: "lp-ico" }, ["🚀"]), "Go further"]),
        h("ul", { class: "lp-obj" }, d.extend.map(function (e) { return h("li", {}, [e]); }))
      ]));
    }
    return out;
  }

  /* tiny **bold** support for the teaching paragraphs */
  function mdBold(t) {
    return String(t).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  }

  /* the staged build brief — the long-form exercise */
  function briefSection() {
    var c = S.content;
    if (!c || !c.brief) return null;
    var b = c.brief;
    var sec = h("section", { class: "lp-card lp-brief" }, [
      h("h3", { class: "lp-h" }, [h("span", { class: "lp-ico" }, ["🛠"]),
        "Build brief — " + b.stages.length + " stages, about " + b.minutes + " minutes"]),
      h("p", { class: "lp-note" }, ["Work through the stages in order. Each one ends with a checkpoint — do not move on until it passes."])
    ]);
    b.stages.forEach(function (st, i) {
      sec.appendChild(h("details", { class: "stage", open: i === 0 ? "open" : null }, [
        h("summary", {}, [
          h("span", { class: "stage-n" }, [String(i + 1)]),
          h("span", { class: "stage-t" }, [st.title]),
          h("span", { class: "stage-m" }, [st.minutes + " min"])
        ]),
        h("p", { class: "stage-goal" }, [st.goal]),
        h("ul", { class: "stage-tasks" }, st.tasks.map(function (t) { return h("li", {}, [t]); })),
        h("div", { class: "stage-check" }, [h("b", {}, ["✅ Checkpoint: "]), st.check])
      ]));
    });
    return sec;
  }

  function render() {
    app.innerHTML = "";
    app.appendChild(U.header("curriculum"));
    var main = h("main", { class: "c-main" });
    main.appendChild(U.modeBanner());
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

    /* the subject content */
    var deep = deepSection();
    if (deep) deep.forEach(function (d) { col.appendChild(d); });

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

    /* the long-form staged build */
    var brief = briefSection();
    if (brief) col.appendChild(brief);

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
        S.content ? h("a", { class: "btn ghost", href: S.content.href,
          onclick: function () { GN.markApplied(S.id); } }, ["Skip to the build"]) : null
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
    if (GN && GN.ensureLearner && !GN.isTutor()) GN.ensureLearner();
    S = P && P.sessions ? P.sessions[qs("s")] : null;
    if (!S) { app.innerHTML = '<div style="padding:40px;text-align:center">Session not found. <a href="curriculum.html">Back to curriculum</a></div>'; return; }
    render();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
