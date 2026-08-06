/* =====================================================================
   GRADE NEXT — Progress reports
   A printable, parent-facing report card: what the child has learned,
   mastery by skill, tutor notes, and a certificate when a level is done.
   ===================================================================== */
(function () {
  "use strict";
  var P = window.GN_PLATFORM, GN = window.GN, U = window.GNUI, h = U.h;
  var app;

  function fmt(d) {
    if (!d) return "";
    try { return new Date(d).toLocaleDateString(undefined, { day: "numeric", month: "short", year: "numeric" }); }
    catch (e) { return ""; }
  }

  function completedSessions(stu) {
    var prog = GN.progress(stu.id);
    return P.order.filter(function (id) { return (prog[id] || {}).status === "done"; })
                  .map(function (id) { return { s: P.sessions[id], r: prog[id] }; });
  }

  function summary(stu) {
    var st = GN.stats(P, stu.id);
    var l1 = GN.levelStats(P, 1, stu.id), l2 = GN.levelStats(P, 2, stu.id);
    return h("section", { class: "rep-summary" }, [
      h("div", { class: "rep-rings" }, [
        U.ring(st.pct, "#4c97ff", "overall"),
        U.ring(l1.pct, "#34d399", "level 1"),
        U.ring(l2.pct, "#818cf8", "level 2")
      ]),
      h("div", { class: "rep-numbers" }, [
        h("div", { class: "rep-num" }, [h("b", {}, [String(st.done)]), h("span", {}, ["sessions completed"])]),
        h("div", { class: "rep-num" }, [h("b", {}, [String(st.rubric.mastered)]), h("span", {}, ["skills mastered"])]),
        h("div", { class: "rep-num" }, [h("b", {}, [String(st.rubric.secure)]), h("span", {}, ["skills secure"])]),
        h("div", { class: "rep-num" }, [h("b", {}, [String(st.done * P.meta.minutes / 60)]), h("span", {}, ["hours taught"])])
      ])
    ]);
  }

  function masteryTable(stu) {
    var m = GN.mastery(P, stu.id);
    var keys = Object.keys(m).sort(function (a, b) { return m[b].pct - m[a].pct; });
    return h("section", { class: "panel" }, [
      h("h2", { class: "panel-h" }, ["Skills mastery"]),
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

  function journal(stu) {
    var done = completedSessions(stu);
    if (!done.length) {
      return h("section", { class: "panel" }, [
        h("h2", { class: "panel-h" }, ["Session record"]),
        h("p", { class: "panel-sub" }, ["No sessions marked complete yet. Complete a session from its lesson plan to build this record."])
      ]);
    }
    var rows = done.map(function (d) {
      return h("tr", {}, [
        h("td", {}, [fmt(d.r.date)]),
        h("td", {}, [h("b", {}, ["L" + d.s.level + "S" + d.s.n]), " " + d.s.title]),
        h("td", {}, [d.s.concept]),
        h("td", {}, [d.r.rubric ? h("span", { class: "rub-pill " + d.r.rubric }, [d.r.rubric]) : "—"]),
        GN.isTutor() ? h("td", { class: "rep-notes" }, [d.r.notes || ""]) : null
      ]);
    });
    return h("section", { class: "panel" }, [
      h("h2", { class: "panel-h" }, ["Session record (" + done.length + ")"]),
      h("div", { class: "rep-tablewrap" }, [
        h("table", { class: "rep-table" }, [
          h("thead", {}, [h("tr", {}, [h("th", {}, ["Date"]), h("th", {}, ["Session"]),
            h("th", {}, ["Concept"]), h("th", {}, ["Level"]),
            GN.isTutor() ? h("th", {}, ["Tutor notes"]) : null])]),
          h("tbody", {}, rows)
        ])
      ])
    ]);
  }

  function certificate(stu) {
    var l1 = GN.levelStats(P, 1, stu.id), l2 = GN.levelStats(P, 2, stu.id);
    var earned = [];
    if (l1.pct >= 100) earned.push({ lv: 1, name: "Level 1 — Foundations", color: "#34d399" });
    if (l2.pct >= 100) earned.push({ lv: 2, name: "Level 2 — Logic, Data & Game Engineering", color: "#818cf8" });
    if (!earned.length) {
      var next = l1.pct < 100 ? l1 : l2;
      return h("section", { class: "panel" }, [
        h("h2", { class: "panel-h" }, ["Certificate"]),
        h("p", { class: "panel-sub" }, ["A certificate unlocks when a level is fully completed — " +
          (next.total - next.done) + " sessions to go."])
      ]);
    }
    return h("section", { class: "panel" }, [
      h("h2", { class: "panel-h" }, ["Certificates earned"]),
      h("div", {}, earned.map(function (e) {
        return h("div", { class: "cert", style: "--cc:" + e.color }, [
          h("div", { class: "cert-seal" }, ["🏆"]),
          h("div", { class: "cert-body" }, [
            h("div", { class: "cert-kicker" }, ["Certificate of completion"]),
            h("h3", {}, [stu.name]),
            h("p", {}, ["has successfully completed ", h("b", {}, [e.name]),
                        " of the Grade Next Scratch Academy."]),
            h("div", { class: "cert-foot" }, ["Grade Next · " + fmt(new Date().toISOString())])
          ])
        ]);
      }))
    ]);
  }

  function dataTools() {
    if (!GN.isTutor()) {
      return h("section", { class: "panel no-print" }, [
        h("h2", { class: "panel-h" }, ["Save your report"]),
        h("p", { class: "panel-sub" }, ["Print this page or save it as a PDF to show your family."]),
        h("button", { class: "btn primary", onclick: function () { window.print(); } }, ["🖨 Print / save as PDF"])
      ]);
    }
    return h("section", { class: "panel no-print" }, [
      h("h2", { class: "panel-h" }, ["Records"]),
      h("p", { class: "panel-sub" }, ["Progress is stored in this browser. Export a backup to move a student to another device or to keep an off-line record."]),
      h("div", { class: "rep-tools" }, [
        h("button", { class: "btn ghost", onclick: function () {
          var blob = new Blob([GN.exportAll()], { type: "application/json" });
          var a = document.createElement("a");
          a.href = URL.createObjectURL(blob);
          a.download = "gradenext-progress-" + new Date().toISOString().slice(0, 10) + ".json";
          a.click();
        } }, ["⬇ Export backup"]),
        (function () {
          var inp = h("input", { type: "file", accept: "application/json", style: "display:none",
            onchange: function () {
              var f = inp.files[0]; if (!f) return;
              var fr = new FileReader();
              fr.onload = function () {
                try { var n = GN.importAll(fr.result); alert("Imported " + n + " student(s)."); location.reload(); }
                catch (e) { alert("Could not import: " + e.message); }
              };
              fr.readAsText(f);
            } });
          var btn = h("button", { class: "btn ghost", onclick: function () { inp.click(); } }, ["⬆ Import backup"]);
          return h("span", {}, [btn, inp]);
        })(),
        h("button", { class: "btn primary", onclick: function () { window.print(); } }, ["🖨 Print / save as PDF"]),
        h("a", { class: "btn ghost", target: "_blank", rel: "noopener",
          href: "https://wa.me/?text=" + shareText() }, ["💬 Share on WhatsApp"]),
        h("a", { class: "btn ghost",
          href: "mailto:?subject=" + encodeURIComponent("Scratch progress update") + "&body=" + shareText() }, ["✉️ Email to parent"])
      ])
    ]);
  }

  /* a parent-friendly progress summary for WhatsApp / email */
  function shareText() {
    var stu = GN.active(); if (!stu) return "";
    var st = GN.stats(P, stu.id), stk = GN.streak(stu.id);
    var l1 = GN.levelStats(P, 1, stu.id), l2 = GN.levelStats(P, 2, stu.id);
    var badges = GN.achievements(P, stu.id).filter(function (b) { return b.earned; });
    var txt = "🎓 " + stu.name + " — Scratch Academy by GradeNext progress\n" +
      "Sessions completed: " + st.done + " of " + st.total + "\n" +
      "Level 1: " + l1.pct + "% · Level 2: " + l2.pct + "%\n" +
      "Skills mastered: " + st.rubric.mastered + " · Learning streak: " + stk.current + " days\n" +
      "Achievements: " + (badges.length ? badges.map(function (b) { return b.emoji + " " + b.name; }).join(", ") : "coming soon!");
    return encodeURIComponent(txt);
  }

  function render() {
    app.innerHTML = "";
    app.appendChild(U.header("report"));
    var main = h("main", { class: "c-main" });
    var stu = GN.isTutor() ? GN.active() : GN.ensureLearner();

    if (!stu) {
      main.appendChild(h("section", { class: "c-hero" }, [h("h1", {}, ["Progress reports"])]));
      main.appendChild(U.emptyState("Add a student to start building report cards.",
        "＋ Add student", function () { U.addStudentFlow(); }));
    } else {
      main.appendChild(h("section", { class: "rep-head" }, [
        h("div", {}, [
          h("div", { class: "rep-kicker" }, [GN.isTutor() ? "Progress report" : "My progress"]),
          h("h1", {}, [GN.isTutor() ? stu.name : "Your Scratch journey"]),
          h("p", {}, ["Grade Next Scratch Academy · started " + fmt(stu.createdAt)])
        ]),
        h("div", { class: "rep-logo" }, ["🐱"])
      ]));
      main.appendChild(summary(stu));
      main.appendChild(U.badgesPanel(P));
      main.appendChild(masteryTable(stu));
      main.appendChild(certificate(stu));
      main.appendChild(journal(stu));
      main.appendChild(dataTools());
    }

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
