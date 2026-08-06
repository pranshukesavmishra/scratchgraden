/* =====================================================================
   GRADE NEXT — shared state layer
   Student profiles, session progress, assessment records and the mastery
   map. Everything is kept in localStorage so the platform works offline and
   needs no backend; export/import moves a student between devices.
   ===================================================================== */
(function (w) {
  "use strict";
  var K_STUDENTS = "gn_students", K_ACTIVE = "gn_active", K_PROGRESS = "gn_progress";
  var K_ROLE = "gn_role";
  var RUBRIC = ["emerging", "secure", "mastered"];

  function read(k, d) { try { return JSON.parse(localStorage.getItem(k)) || d; } catch (e) { return d; } }
  function write(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  function uid() { return "s" + Date.now().toString(36) + Math.random().toString(36).slice(2, 6); }

  var GN = {
    RUBRIC: RUBRIC,

    /* ---------- role: one global setting for the whole platform ----------
       'student' is the safe default: solutions, answers and teaching notes
       are never shown. 'tutor' unlocks them so the tutor can guide. */
    role: function () {
      var r = null;
      try { r = localStorage.getItem(K_ROLE); } catch (e) {}
      return r === "tutor" ? "tutor" : "student";
    },
    setRole: function (r) {
      try { localStorage.setItem(K_ROLE, r === "tutor" ? "tutor" : "student"); } catch (e) {}
    },
    isTutor: function () { return this.role() === "tutor"; },

    /* ---------- tutor PIN ----------
       Switching into Tutor Mode needs a PIN, so a student can't just flip
       the switch and read the solutions. Default is 2468 until changed. */
    pin: function () {
      var p = null; try { p = localStorage.getItem("gn_pin"); } catch (e) {}
      return (p && /^\d{4,6}$/.test(p)) ? p : "2468";
    },
    setPin: function (p) {
      p = String(p == null ? "" : p).replace(/\D/g, "");
      if (p.length < 4 || p.length > 6) return false;
      try { localStorage.setItem("gn_pin", p); } catch (e) {}
      return true;
    },
    checkPin: function (p) { return String(p == null ? "" : p).trim() === this.pin(); },

    /* ---------- active level: the platform is split into two parts ---------- */
    level: function () {
      var n = 1; try { n = parseInt(localStorage.getItem("gn_level") || "1", 10); } catch (e) {}
      return n === 2 ? 2 : 1;
    },
    setLevel: function (n) {
      try { localStorage.setItem("gn_level", n === 2 ? "2" : "1"); } catch (e) {}
    },

    /* ---------- students ---------- */
    students: function () { return read(K_STUDENTS, []); },
    addStudent: function (name, level) {
      var list = this.students();
      var st = { id: uid(), name: (name || "New student").trim(), level: level || 1,
                 createdAt: new Date().toISOString() };
      list.push(st); write(K_STUDENTS, list);
      if (!this.activeId()) this.setActive(st.id);
      return st;
    },
    removeStudent: function (id) {
      write(K_STUDENTS, this.students().filter(function (s) { return s.id !== id; }));
      var p = read(K_PROGRESS, {}); delete p[id]; write(K_PROGRESS, p);
      if (this.activeId() === id) {
        var rest = this.students();
        write(K_ACTIVE, rest.length ? rest[0].id : null);
      }
    },
    renameStudent: function (id, name) {
      var l = this.students();
      l.forEach(function (s) { if (s.id === id) s.name = name; });
      write(K_STUDENTS, l);
    },
    /* Progress tracking must ALWAYS work, in either role. If no profile
       exists yet we create a default learner silently, so a student never
       loses their session history just because nobody pressed "Add student". */
    ensureLearner: function () {
      if (this.students().length) return this.active();
      var st = this.addStudent("My progress", 1);
      this.setActive(st.id);
      return st;
    },
    activeId: function () { return read(K_ACTIVE, null); },
    setActive: function (id) { write(K_ACTIVE, id); },
    active: function () {
      var id = this.activeId(), list = this.students();
      return list.filter(function (s) { return s.id === id; })[0] || list[0] || null;
    },

    /* ---------- progress ---------- */
    allProgress: function () { return read(K_PROGRESS, {}); },
    progress: function (studentId) {
      var st = studentId || this.activeId();
      return this.allProgress()[st] || {};
    },
    sessionRecord: function (sessionId, studentId) {
      return this.progress(studentId)[sessionId] || null;
    },
    /* rec: {status:'done'|'started', rubric, notes, date} */
    saveSession: function (sessionId, rec, studentId) {
      var st = studentId || this.activeId();
      if (!st) return null;
      var all = this.allProgress();
      all[st] = all[st] || {};
      var cur = all[st][sessionId] || {};
      Object.keys(rec).forEach(function (k) { cur[k] = rec[k]; });
      cur.date = cur.date || new Date().toISOString();
      cur.updated = new Date().toISOString();
      all[st][sessionId] = cur;
      write(K_PROGRESS, all);
      try {
        var act = read("gn_activity", {});
        var days = act[st] || [];
        var today = new Date().toISOString().slice(0, 10);
        if (days.indexOf(today) < 0) { days.push(today); act[st] = days; write("gn_activity", act); }
      } catch (e) {}
      return cur;
    },
    clearSession: function (sessionId, studentId) {
      var st = studentId || this.activeId();
      var all = this.allProgress();
      if (all[st]) { delete all[st][sessionId]; write(K_PROGRESS, all); }
    },

    /* ---------- the Learn -> Practice -> Apply journey ---------- */
    markLearned: function (sessionId, studentId) {
      return this.saveSession(sessionId, { learned: true, status: "started" }, studentId);
    },
    markApplied: function (sessionId, studentId) {
      return this.saveSession(sessionId, { applied: true, status: "started" }, studentId);
    },
    /* record a Recall Test attempt; keeps the best score */
    saveQuiz: function (sessionId, score, total, passMark, studentId) {
      var rec = this.sessionRecord(sessionId, studentId) || {};
      var q = rec.quiz || { attempts: 0, best: 0, total: total };
      q.attempts += 1;
      q.last = score;
      q.total = total;
      if (score > q.best) q.best = score;
      q.passed = q.best >= passMark;
      return this.saveSession(sessionId, { quiz: q, status: "started" }, studentId);
    },
    /* which of the three stages are done */
    stages: function (sessionId, studentId) {
      var r = this.sessionRecord(sessionId, studentId) || {};
      return {
        learn: !!r.learned,
        quiz: !!(r.quiz && r.quiz.passed),
        apply: !!r.applied,
        quizBest: r.quiz ? r.quiz.best : null,
        quizTotal: r.quiz ? r.quiz.total : null,
        attempts: r.quiz ? r.quiz.attempts : 0,
        done: r.status === "done"
      };
    },
    /* percent through the 3-stage journey for one session */
    journeyPct: function (sessionId, studentId) {
      var s = this.stages(sessionId, studentId), n = 0;
      if (s.learn) n++; if (s.quiz) n++; if (s.apply) n++;
      return Math.round((n / 3) * 100);
    },

    /* ---------- derived stats ---------- */
    stats: function (P, studentId) {
      var prog = this.progress(studentId), done = 0, started = 0, rub = { emerging: 0, secure: 0, mastered: 0 };
      Object.keys(prog).forEach(function (k) {
        var r = prog[k];
        if (r.status === "done") done++; else if (r.status === "started") started++;
        if (r.rubric && rub[r.rubric] != null) rub[r.rubric]++;
      });
      var total = (P && P.order) ? P.order.length : 0;
      return { done: done, started: started, total: total, rubric: rub,
               pct: total ? Math.round((done / total) * 100) : 0 };
    },
    levelStats: function (P, level, studentId) {
      var prog = this.progress(studentId), ids = [], done = 0;
      (P.levels || []).forEach(function (lv) { if (lv.level === level) ids = lv.sessions; });
      ids.forEach(function (id) { if ((prog[id] || {}).status === "done") done++; });
      return { done: done, total: ids.length, pct: ids.length ? Math.round((done / ids.length) * 100) : 0 };
    },
    /* Mastery per Scratch strand, 0-100. Blends the tutor's rubric judgement with
       the child's Recall Test score, so mastery reflects both observed work and
       tested understanding. Sessions only assessed one way still count. */
    mastery: function (P, studentId) {
      var prog = this.progress(studentId), out = {};
      Object.keys(P.skills || {}).forEach(function (strand) {
        var sk = P.skills[strand], score = 0, max = 0, touched = 0;
        sk.sessions.forEach(function (sid) {
          max += 1;
          var r = prog[sid];
          if (!r) return;
          var parts = [];
          if (r.status === "done" || r.rubric) {
            var i = RUBRIC.indexOf(r.rubric);
            parts.push(i >= 0 ? (i + 1) / 3 : 2 / 3);
          }
          if (r.quiz && r.quiz.total) parts.push(r.quiz.best / r.quiz.total);
          if (!parts.length) return;
          touched++;
          var avg = parts.reduce(function (a, b) { return a + b; }, 0) / parts.length;
          score += avg;
        });
        out[strand] = { strand: strand, color: sk.color, total: sk.sessions.length,
                        touched: touched, pct: max ? Math.round((score / max) * 100) : 0 };
      });
      return out;
    },
    /* the next session that isn't finished */
    nextSession: function (P, studentId) {
      var prog = this.progress(studentId);
      var ids = P.order || [];
      for (var i = 0; i < ids.length; i++) {
        if ((prog[ids[i]] || {}).status !== "done") return ids[i];
      }
      return ids[ids.length - 1] || null;
    },

    /* ---------- streaks (days in a row with activity) ---------- */
    streak: function (studentId) {
      var st = studentId || this.activeId();
      var days = (read("gn_activity", {})[st]) || [];
      var set = {}; days.forEach(function (d) { set[d] = 1; });
      function key(d) { return d.toISOString().slice(0, 10); }
      var cur = 0, d = new Date();
      if (!set[key(d)]) d.setDate(d.getDate() - 1);
      while (set[key(d)]) { cur++; d.setDate(d.getDate() - 1); }
      var best = 0, run = 0, sorted = days.slice().sort();
      for (var i = 0; i < sorted.length; i++) {
        if (i > 0) {
          var gap = (new Date(sorted[i]) - new Date(sorted[i - 1])) / 86400000;
          run = gap === 1 ? run + 1 : 1;
        } else run = 1;
        if (run > best) best = run;
      }
      return { current: cur, best: best, days: days.length };
    },
    /* how many of the last 7 days (today included) had any activity */
    weekActive: function (studentId) {
      var st = studentId || this.activeId();
      var days = (read("gn_activity", {})[st]) || [];
      var n = 0, now = new Date();
      for (var i = 0; i < 7; i++) {
        var d = new Date(now); d.setDate(now.getDate() - i);
        if (days.indexOf(d.toISOString().slice(0, 10)) >= 0) n++;
      }
      return n;
    },

    unlockedCount: function (P, studentId) {
      var prog = this.progress(studentId), n = 0;
      Object.keys(P.blocks || {}).forEach(function (k) {
        var ok = P.blocks[k].sessions.some(function (sid) {
          var r = prog[sid]; return r && (r.learned || r.status === "done");
        });
        if (ok) n++;
      });
      return n;
    },

    /* ---------- achievements ---------- */
    achievements: function (P, studentId) {
      var st = this.stats(P, studentId), prog = this.progress(studentId);
      var applied = 0, perfect = 0, passes = 0, sSum = 0, sN = 0;
      Object.keys(prog).forEach(function (k) {
        var r = prog[k];
        if (r.applied) applied++;
        if (r.quiz) {
          if (r.quiz.passed) passes++;
          if (r.quiz.total && r.quiz.best === r.quiz.total) perfect++;
          if (r.quiz.total) { sSum += r.quiz.best / r.quiz.total; sN++; }
        }
      });
      var l1 = this.levelStats(P, 1, studentId), l2 = this.levelStats(P, 2, studentId);
      var stk = this.streak(studentId), un = this.unlockedCount(P, studentId);
      function A(id, emoji, name, desc, earned) {
        return { id: id, emoji: emoji, name: name, desc: desc, earned: !!earned };
      }
      return [
        A("first", "🐣", "First Steps", "Complete your first session", st.done >= 1),
        A("ten", "🚀", "Explorer", "Complete 10 sessions", st.done >= 10),
        A("quarter", "🌟", "Scholar", "Complete 25 sessions", st.done >= 25),
        A("half", "🏔️", "Half Way", "Complete 50 sessions", st.done >= 50),
        A("l1", "🎓", "Level 1 Graduate", "Finish all of Level 1", l1.pct >= 100),
        A("l2", "🏆", "Level 2 Graduate", "Finish all of Level 2", l2.pct >= 100),
        A("perfect", "💯", "Perfect Score", "Get 10/10 on a Recall Test", perfect >= 1),
        A("passes5", "🧠", "Quiz Master", "Pass 5 Recall Tests", passes >= 5),
        A("brain", "⚡", "Brainbox", "Average 90%+ across 5 tests", sN >= 5 && (sSum / sN) >= 0.9),
        A("build5", "🛠️", "Builder", "Build 5 projects", applied >= 5),
        A("build15", "🏗️", "Maker", "Build 15 projects", applied >= 15),
        A("streak3", "🔥", "On Fire", "Learn 3 days in a row", stk.current >= 3),
        A("streak7", "🌋", "Unstoppable", "Learn 7 days in a row", stk.current >= 7),
        A("blocks25", "🧩", "Block Collector", "Unlock 25 blocks", un >= 25),
        A("blocks60", "📦", "Block Master", "Unlock 60 blocks", un >= 60)
      ];
    },

    /* ---------- portability ---------- */
    exportAll: function () {
      return JSON.stringify({ v: 2, exported: new Date().toISOString(),
                              students: this.students(), progress: this.allProgress(),
                              activity: read("gn_activity", {}), level: this.level() }, null, 1);
    },
    importAll: function (text) {
      var d = JSON.parse(text);
      if (!d || !d.students) throw new Error("Not a Grade Next backup file.");
      write(K_STUDENTS, d.students); write(K_PROGRESS, d.progress || {});
      if (d.activity) write("gn_activity", d.activity);
      if (d.students.length) write(K_ACTIVE, d.students[0].id);
      return d.students.length;
    }
  };

  w.GN = GN;
  try {
    if ("serviceWorker" in navigator && location.protocol !== "file:") {
      navigator.serviceWorker.register("sw.js").catch(function () {});
    }
  } catch (e) {}
})(window);
