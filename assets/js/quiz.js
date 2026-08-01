/* =====================================================================
   GRADE NEXT — Recall Test (multiple choice)
   Stage 2 of every session. 10 questions drawn from the concept's bank,
   shuffled each attempt, with instant feedback and an explanation that
   teaches. Passing unlocks the build.
   ===================================================================== */
(function () {
  "use strict";
  var P = window.GN_PLATFORM, GN = window.GN, U = window.GNUI, h = U.h;
  var app, S, quiz;   // quiz = {qs:[], i, answers:[], done}

  function qs_(k) { return new URLSearchParams(location.search).get(k); }

  function shuffle(a) {
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  /* Build an attempt: pick N questions for this concept, shuffle the
     questions AND each question's options (tracking the new correct index). */
  function newAttempt() {
    var pool = (P.questions[S.conceptKey] || []).slice();
    var picked = shuffle(pool).slice(0, Math.min(P.meta.quizLength, pool.length));
    var qs = picked.map(function (q) {
      var idx = q.options.map(function (_, i) { return i; });
      var order = shuffle(idx);
      return {
        id: q.id, stem: q.stem, why: q.why,
        options: order.map(function (i) { return q.options[i]; }),
        correct: order.indexOf(q.correct)
      };
    });
    return { qs: qs, i: 0, answers: [], done: false };
  }

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
        h("span", {}, [" / Level " + S.level + " · Session " + S.n + " / Recall Test"])
      ]),
      h("div", { class: "lp-titlerow" }, [
        h("div", {}, [h("h1", {}, ["🧠 Recall Test — " + S.title]),
          h("div", { class: "lp-tags" }, [
            h("span", { class: "strand-chip", style: "background:" + S.strandColor + "22;color:" + U.shade(S.strandColor, -50) }, [S.concept]),
            h("span", { class: "pill" }, [quiz.qs.length + " questions"]),
            h("span", { class: "pill" }, ["Pass mark " + P.meta.quizPass + "/" + quiz.qs.length])
          ])])
      ]),
      journey("quiz")
    ]);
  }

  /* ---------------- question view ---------------- */
  function questionView() {
    var q = quiz.qs[quiz.i];
    var given = quiz.answers[quiz.i];      // undefined until answered
    var answered = given !== undefined;

    var wrap = h("div", { class: "quiz-wrap" });

    /* progress */
    var pct = Math.round((quiz.i / quiz.qs.length) * 100);
    wrap.appendChild(h("div", { class: "quiz-prog" }, [
      h("div", { class: "quiz-prog-txt" }, ["Question " + (quiz.i + 1) + " of " + quiz.qs.length]),
      U.bar(pct, S.strandColor),
      h("div", { class: "quiz-dots" }, quiz.answers.map(function (a, i) {
        return h("span", { class: "qdot " + (a === quiz.qs[i].correct ? "right" : "wrong") });
      }))
    ]));

    var card = h("section", { class: "quiz-card" }, [h("h2", { class: "quiz-stem" }, [q.stem])]);
    var opts = h("div", { class: "quiz-opts" });
    q.options.forEach(function (opt, i) {
      var cls = "qopt";
      if (answered) {
        if (i === q.correct) cls += " correct";
        else if (i === given) cls += " chosen-wrong";
        else cls += " dim";
      }
      opts.appendChild(h("button", { class: cls, disabled: answered || null,
        onclick: function () { if (!answered) { quiz.answers[quiz.i] = i; render(); } } }, [
        h("span", { class: "qletter" }, ["ABCD"[i]]),
        h("span", { class: "qtext" }, [opt]),
        answered && i === q.correct ? h("span", { class: "qmark" }, ["✓"]) : null,
        answered && i === given && i !== q.correct ? h("span", { class: "qmark" }, ["✗"]) : null
      ]));
    });
    card.appendChild(opts);

    if (answered) {
      var right = given === q.correct;
      card.appendChild(h("div", { class: "qwhy " + (right ? "ok" : "no") }, [
        h("b", {}, [right ? "✓ Correct — " : "Not quite — "]),
        q.why
      ]));
      card.appendChild(h("div", { class: "quiz-actions" }, [
        h("button", { class: "btn primary big", onclick: function () {
          if (quiz.i < quiz.qs.length - 1) { quiz.i++; } else { quiz.done = true; finish(); }
          render();
        } }, [quiz.i < quiz.qs.length - 1 ? "Next question →" : "See my result →"])
      ]));
    }
    wrap.appendChild(card);
    return wrap;
  }

  function score() {
    return quiz.answers.reduce(function (n, a, i) { return n + (a === quiz.qs[i].correct ? 1 : 0); }, 0);
  }

  function finish() {
    GN.saveQuiz(S.id, score(), quiz.qs.length, P.meta.quizPass);
  }

  /* ---------------- result view ---------------- */
  function resultView() {
    var sc = score(), total = quiz.qs.length, pct = Math.round((sc / total) * 100);
    var passed = sc >= P.meta.quizPass;
    var st = GN.stages(S.id);

    var wrap = h("div", { class: "quiz-wrap" });
    wrap.appendChild(h("section", { class: "quiz-result " + (passed ? "pass" : "fail") }, [
      h("div", { class: "qr-emoji" }, [passed ? (pct === 100 ? "🏆" : "🎉") : "💪"]),
      h("h2", {}, [passed ? (pct === 100 ? "Perfect score!" : "You passed!") : "Nearly there"]),
      U.ring(pct, passed ? "#2fae66" : "#e9930b", "score"),
      h("p", { class: "qr-score" }, [sc + " out of " + total + " correct"]),
      h("p", { class: "qr-msg" }, [passed
        ? "You've shown you understand this. Time to build it for real."
        : "You need " + P.meta.quizPass + "/" + total + " to pass. Read the explanations below, then try again — the questions get reshuffled."]),
      st.attempts > 1 ? h("p", { class: "qr-best" }, ["Best score so far: " + st.quizBest + "/" + st.quizTotal + " over " + st.attempts + " attempts"]) : null,
      h("div", { class: "quiz-actions" }, [
        passed && S.content
          ? h("a", { class: "btn primary big", href: S.content.href, onclick: function () { GN.markApplied(S.id); } }, ["🛠 Build it now →"])
          : h("button", { class: "btn primary big", onclick: function () { quiz = newAttempt(); render(); } }, ["↻ Try again"]),
        passed ? h("button", { class: "btn ghost", onclick: function () { quiz = newAttempt(); render(); } }, ["↻ Retake"]) : null,
        h("a", { class: "btn ghost", href: "learn.html?s=" + S.id }, ["📖 Back to Learn"])
      ])
    ]));

    /* review every question */
    var rev = h("section", { class: "lp-card" }, [
      h("h3", { class: "lp-h" }, [h("span", { class: "lp-ico" }, ["📋"]), "Review your answers"])
    ]);
    quiz.qs.forEach(function (q, i) {
      var given = quiz.answers[i], right = given === q.correct;
      rev.appendChild(h("div", { class: "qrev " + (right ? "ok" : "no") }, [
        h("div", { class: "qrev-h" }, [h("span", { class: "qrev-n" }, [right ? "✓" : "✗"]), q.stem]),
        h("div", { class: "qrev-a" }, [
          h("span", {}, ["Your answer: "]), h("b", {}, [given != null ? q.options[given] : "—"])
        ]),
        !right ? h("div", { class: "qrev-a" }, [h("span", {}, ["Correct: "]), h("b", {}, [q.options[q.correct]])]) : null,
        h("div", { class: "qrev-why" }, [q.why])
      ]));
    });
    wrap.appendChild(rev);
    return wrap;
  }

  function render() {
    app.innerHTML = "";
    app.appendChild(U.header("curriculum"));
    var main = h("main", { class: "c-main" });
    main.appendChild(head());
    main.appendChild(quiz.done ? resultView() : questionView());
    app.appendChild(main);
    app.appendChild(U.footer());
    window.scrollTo(0, 0);
  }

  function boot() {
    app = document.getElementById("app");
    S = P && P.sessions ? P.sessions[qs_("s")] : null;
    if (!S) { app.innerHTML = '<div style="padding:40px;text-align:center">Session not found. <a href="curriculum.html">Back to curriculum</a></div>'; return; }
    if (!(P.questions[S.conceptKey] || []).length) {
      app.innerHTML = '<div style="padding:40px;text-align:center">No questions for this topic yet. <a href="learn.html?s=' + S.id + '">Back to Learn</a></div>';
      return;
    }
    quiz = newAttempt();
    render();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
