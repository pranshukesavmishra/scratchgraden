/* =====================================================================
   GRADE NEXT — printable certificate
   A parent-frameable, brand-styled certificate for finishing a level.
   Students see it once the level is 100% complete; tutors can preview a
   SAMPLE-watermarked copy any time from the report page.
   ===================================================================== */
(function () {
  "use strict";
  var P = window.GN_PLATFORM, GN = window.GN, U = window.GNUI, h = U.h;
  var app;

  function qs_(k) { return new URLSearchParams(location.search).get(k); }
  function fmt(d) {
    try { return new Date(d).toLocaleDateString(undefined, { day: "numeric", month: "long", year: "numeric" }); }
    catch (e) { return ""; }
  }

  function render() {
    app.innerHTML = "";
    app.appendChild(U.header("report"));
    var main = h("main", { class: "c-main" });

    var lv = parseInt(qs_("lv") || GN.level(), 10) === 2 ? 2 : 1;
    var lvRow = P.levels.filter(function (l) { return l.level === lv; })[0] || {};
    var stu = GN.isTutor() ? GN.active() : GN.ensureLearner();
    var ls = GN.levelStats(P, lv, stu && stu.id);
    var earned = ls.pct >= 100;

    if (!stu || (!earned && !GN.isTutor())) {
      main.appendChild(h("section", { class: "panel", style: "max-width:640px;margin:40px auto;text-align:center" }, [
        h("h2", { class: "panel-h" }, ["🔒 Not unlocked yet"]),
        h("p", { class: "panel-sub" }, ["The Level " + lv + " certificate appears when every session in the level is complete — " +
          (ls.total - ls.done) + " to go. Keep building!"]),
        U.bar(ls.pct, lvRow.color || "#703D84"),
        h("p", {}, [""]),
        h("a", { class: "btn primary", href: "curriculum.html" }, ["📚 Back to the curriculum"])
      ]));
      app.appendChild(main); app.appendChild(U.footer());
      return;
    }

    var conceptN = 0, seen = {};
    (lvRow.sessions || []).forEach(function (id) {
      var s = P.sessions[id];
      if (s && !seen[s.conceptKey]) { seen[s.conceptKey] = 1; conceptN++; }
    });

    main.appendChild(h("div", { class: "cert2-tools no-print" }, [
      h("a", { class: "btn ghost", href: "report.html" }, ["← Back to the report"]),
      h("button", { class: "btn primary big", onclick: function () { window.print(); } }, ["🖨 Print / save as PDF"]),
      !earned ? h("span", { class: "cert2-samplenote" }, ["Tutor preview — the SAMPLE watermark disappears once the level is really finished."]) : null
    ]));

    main.appendChild(h("div", { class: "cert2" + (earned ? "" : " sample") }, [
      h("div", { class: "cert2-frame" }, [
        !earned ? h("div", { class: "cert2-watermark" }, ["SAMPLE"]) : null,
        h("div", { class: "cert2-brand" }, [U.logoEl()]),
        h("div", { class: "cert2-title" }, ["Certificate of Achievement"]),
        h("div", { class: "cert2-line" }, ["This certifies that"]),
        h("div", { class: "cert2-name" }, [stu.name]),
        h("div", { class: "cert2-line" }, ["has successfully completed"]),
        h("div", { class: "cert2-level" }, [(lvRow.emoji || "🎓") + " " + (lvRow.title || ("Level " + lv))]),
        h("div", { class: "cert2-detail" }, [ls.total + " sessions · " + conceptN + " coding concepts · real Scratch projects built and tested"]),
        h("div", { class: "cert2-sig" }, [
          h("div", { class: "cert2-sigcol" }, [h("div", { class: "cert2-sigline" }), h("span", {}, ["Tutor"])]),
          h("div", { class: "cert2-seal" }, ["🏆"]),
          h("div", { class: "cert2-sigcol" }, [h("div", { class: "cert2-date" }, [fmt(new Date())]), h("span", {}, ["Date"])])
        ]),
        h("div", { class: "cert2-foot" }, ["Scratch Academy by GradeNext"])
      ])
    ]));

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
