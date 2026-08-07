/* =====================================================================
   GRADE NEXT — Recall Test (multiple choice)
   Stage 2 of every session. 10 questions drawn from the concept's bank,
   shuffled each attempt, with instant feedback and an explanation that
   teaches. Passing unlocks the build.
   ===================================================================== */
(function () {
  "use strict";
  var P = window.GN_PLATFORM, GN = window.GN, U = window.GNUI, h = U.h;
  var app, S, quiz;   // quiz = {qs:[], i, answers:[], done, practice}
  var REVIEW = false; // mixed-review mode: questions from every learned topic

  function qs_(k) { return new URLSearchParams(location.search).get(k); }

  /* tiny WebAudio feedback sounds — no files, and silent on old browsers */
  var AC = null;
  function ping(kind) {
    try {
      AC = AC || new (window.AudioContext || window.webkitAudioContext)();
      if (AC.state === "suspended") AC.resume();
      var t0 = AC.currentTime;
      var notes = kind === "right" ? [[660, 0, 0.09], [988, 0.09, 0.14]]
                : kind === "wrong" ? [[196, 0, 0.22]]
                : [[523, 0, 0.13], [659, 0.13, 0.13], [784, 0.26, 0.13], [1047, 0.39, 0.3]];
      notes.forEach(function (n) {
        var o = AC.createOscillator(), g = AC.createGain();
        o.type = kind === "wrong" ? "triangle" : "sine";
        o.frequency.value = n[0];
        g.gain.setValueAtTime(0.0001, t0 + n[1]);
        g.gain.exponentialRampToValueAtTime(0.12, t0 + n[1] + 0.015);
        g.gain.exponentialRampToValueAtTime(0.0001, t0 + n[1] + n[2]);
        o.connect(g); g.connect(AC.destination);
        o.start(t0 + n[1]); o.stop(t0 + n[1] + n[2] + 0.05);
      });
    } catch (e) {}
  }

  function answer(i) {
    var q = quiz.qs[quiz.i];
    quiz.answers[quiz.i] = i;
    ping(i === q.correct ? "right" : "wrong");
    render();
  }

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
  function reviewPool() {
    var prog = GN.progress(), keys = {};
    Object.keys(prog).forEach(function (sid) {
      var r = prog[sid], sess = P.sessions[sid];
      if (sess && (r.learned || r.status === "done")) keys[sess.conceptKey] = 1;
    });
    var pool = [];
    Object.keys(keys).forEach(function (k) {
      (P.questions[k] || []).forEach(function (q) { pool.push(q); });
    });
    return pool;
  }

  function reshape(picked) {
    return picked.map(function (q) {
      var idx = q.options.map(function (_, i) { return i; });
      var order = shuffle(idx);
      return { id: q.id, stem: q.stem, why: q.why,
               options: order.map(function (i) { return q.options[i]; }),
               correct: order.indexOf(q.correct) };
    });
  }

  function newAttempt() {
    var pool = REVIEW ? reviewPool() : (P.questions[S.conceptKey] || []).slice();
    var picked = shuffle(pool).slice(0, Math.min(P.meta.quizLength, pool.length));
    return { qs: reshape(picked), i: 0, answers: [], done: false };
  }

  function journey(active) {
    if (REVIEW) return h("span", {});
    var st = GN.stages(S.id);
    var steps = [
      { key: "learn", n: 1, label: "Learn", icon: "📖", href: "learn.html?s=" + S.id, done: st.learn },
      { key: "quiz",  n: 2, label: "Recall Test", icon: "🧠", href: "quiz.html?s=" + S.id, done: st.quiz },
      { key: "apply", n: 3, label: "Build it", icon: "🛠", href: S.content ? S.content.href : "#", done: st.apply }
    ];
    return h("div", { class: "journey" }, steps.map(function (s, i) {
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
        h("a", { href: REVIEW ? "index.html" : "curriculum.html" }, [REVIEW ? "← Dashboard" : "← Curriculum"]),
        h("span", {}, [REVIEW ? " / Mixed Review" : (" / Level " + S.level + " · Session " + S.n + " / Recall Test")])
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
        onclick: function () { if (!answered) answer(i); } }, [
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
    var sc = score();
    if (!REVIEW && !quiz.practice) GN.saveQuiz(S.id, sc, quiz.qs.length, P.meta.quizPass);
    var passed = REVIEW ? (sc / quiz.qs.length >= 0.7) : sc >= P.meta.quizPass;
    if (passed) { ping("pass"); if (U.confetti) U.confetti(); }
  }

  /* ---------------- result view ---------------- */
  function resultView() {
    var sc = score(), total = quiz.qs.length, pct = Math.round((sc / total) * 100);
    var passed = (REVIEW || quiz.practice) ? pct >= 70 : sc >= P.meta.quizPass;
    var st = GN.stages(S.id);
    var wrongQs = quiz.qs.filter(function (q, i) { return quiz.answers[i] !== q.correct; });

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
        wrongQs.length ? h("button", { class: "btn ghost", onclick: function () {
          quiz = { qs: reshape(wrongQs), i: 0, answers: [], done: false, practice: true }; render();
        } }, ["🎯 Practice my mistakes (" + wrongQs.length + ")"]) : null,
        REVIEW ? h("a", { class: "btn ghost", href: "index.html" }, ["🏠 Dashboard"])
               : h("a", { class: "btn ghost", href: "learn.html?s=" + S.id }, ["📖 Back to Learn"])
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
    if (GN && GN.ensureLearner && !GN.isTutor()) GN.ensureLearner();
    REVIEW = qs_("mode") === "review";
    if (REVIEW) {
      S = { id: "REVIEW", level: GN.level(), n: "★", title: "Mixed Review",
            concept: "Everything you have learned so far", strand: "Review",
            strandColor: "#703D84", conceptKey: "__review", content: null };
      if (!reviewPool().length) {
        app.innerHTML = '<div style="padding:40px;text-align:center">Learn a few sessions first, then come back for a Mixed Review. <a href="curriculum.html">Curriculum</a></div>';
        return;
      }
      quiz = newAttempt();
      document.addEventListener("keydown", quizKeys);
      render();
      return;
    }
    S = P && P.sessions ? P.sessions[qs_("s")] : null;
    if (!S) { app.innerHTML = '<div style="padding:40px;text-align:center">Session not found. <a href="curriculum.html">Back to curriculum</a></div>'; return; }
    if (!GN.isTutor() && S.level !== GN.level()) { app.innerHTML = U.lockedHTML(S.level, GN.level()); return; }
    if (!(P.questions[S.conceptKey] || []).length) {
      app.innerHTML = '<div style="padding:40px;text-align:center">No questions for this topic yet. <a href="learn.html?s=' + S.id + '">Back to Learn</a></div>';
      return;
    }
    quiz = newAttempt();
    document.addEventListener("keydown", quizKeys);
    render();
  }

  /* keyboard play: 1–4 answer, Enter continues */
  function quizKeys(e) {
    if (!quiz || document.querySelector(".cmdk")) return;
    var tag = (document.activeElement || {}).tagName || "";
    if (tag === "INPUT" || tag === "TEXTAREA") return;
    if (!quiz.done) {
      var given = quiz.answers[quiz.i] !== undefined;
      if (!given && /^[1-4]$/.test(e.key)) {
        var i = parseInt(e.key, 10) - 1;
        if (i < quiz.qs[quiz.i].options.length) { answer(i); e.preventDefault(); }
      } else if (given && (e.key === "Enter" || e.key === " ")) {
        var btn = document.querySelector(".quiz-actions .btn.primary");
        if (btn) { btn.click(); e.preventDefault(); }
      }
    }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
