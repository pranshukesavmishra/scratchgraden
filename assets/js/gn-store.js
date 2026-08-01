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

    /* ---------- portability ---------- */
    exportAll: function () {
      return JSON.stringify({ v: 1, exported: new Date().toISOString(),
                              students: this.students(), progress: this.allProgress() }, null, 1);
    },
    importAll: function (text) {
      var d = JSON.parse(text);
      if (!d || !d.students) throw new Error("Not a Grade Next backup file.");
      write(K_STUDENTS, d.students); write(K_PROGRESS, d.progress || {});
      if (d.students.length) write(K_ACTIVE, d.students[0].id);
      return d.students.length;
    }
  };

  w.GN = GN;
})(window);
