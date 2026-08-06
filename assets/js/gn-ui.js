/* =====================================================================
   GRADE NEXT — shared UI helpers (hyperscript, header, student switcher)
   ===================================================================== */
(function (w) {
  "use strict";

  function h(tag, attrs, kids) {
    var e = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "class") e.className = attrs[k];
      else if (k === "html") e.innerHTML = attrs[k];
      else if (k.slice(0, 2) === "on" && typeof attrs[k] === "function") e.addEventListener(k.slice(2), attrs[k]);
      else if (attrs[k] != null && attrs[k] !== false) e.setAttribute(k, attrs[k]);
    });
    (kids || []).forEach(function (c) {
      if (c == null || c === false) return;
      e.appendChild(typeof c === "string" || typeof c === "number" ? document.createTextNode(String(c)) : c);
    });
    return e;
  }

  function shade(hex, amt) {
    if (!hex || hex[0] !== "#") return hex || "#4c97ff";
    var n = parseInt(hex.slice(1), 16), r = (n >> 16) + amt, g = ((n >> 8) & 255) + amt, b = (n & 255) + amt;
    r = Math.max(0, Math.min(255, r)); g = Math.max(0, Math.min(255, g)); b = Math.max(0, Math.min(255, b));
    return "#" + (0x1000000 + r * 0x10000 + g * 0x100 + b).toString(16).slice(1);
  }

  function bar(pct, color) {
    return h("div", { class: "bar" }, [
      h("div", { class: "bar-fill", style: "width:" + Math.max(0, Math.min(100, pct)) + "%" +
        (color ? ";background:" + color : "") })
    ]);
  }

  function ring(pct, color, label) {
    var size = 92, r = 38, c = 2 * Math.PI * r, off = c * (1 - Math.max(0, Math.min(100, pct)) / 100);
    var ns = "http://www.w3.org/2000/svg";
    var svg = document.createElementNS(ns, "svg");
    svg.setAttribute("viewBox", "0 0 " + size + " " + size);
    svg.setAttribute("class", "gn-ring");
    function circ(stroke, dash, dashoff, cls) {
      var el = document.createElementNS(ns, "circle");
      el.setAttribute("cx", size / 2); el.setAttribute("cy", size / 2); el.setAttribute("r", r);
      el.setAttribute("fill", "none"); el.setAttribute("stroke", stroke);
      el.setAttribute("stroke-width", "9"); el.setAttribute("stroke-linecap", "round");
      if (dash) { el.setAttribute("stroke-dasharray", dash); el.setAttribute("stroke-dashoffset", dashoff); }
      if (cls) el.setAttribute("class", cls);
      return el;
    }
    svg.appendChild(circ("var(--line)"));
    svg.appendChild(circ(color || "#4c97ff", c, off, "gn-ring-fg"));
    return h("div", { class: "gn-ringwrap" }, [svg,
      h("div", { class: "gn-ringtxt" }, [h("b", {}, [pct + "%"]), label ? h("span", {}, [label]) : null])]);
  }

  /* ---- the GradeNext logo from the brand kit: grad-cap G + coding X ---- */
  function logoEl() {
    var cap = '<svg class="gn-cap" viewBox="0 0 64 44" aria-hidden="true">' +
      '<path d="M32 2 2 15l30 13 24-10.4V30h6V15z" fill="#703D84"/>' +
      '<path d="M14 24v9c0 4.4 8 8.5 18 8.5s18-4.1 18-8.5v-9l-18 7.8z" fill="#5A2F6B"/>' +
      '<circle cx="61" cy="31" r="2.6" fill="#F5007E"/></svg>';
    return h("span", { class: "gn-logo", "aria-label": "GradeNext" }, [
      h("span", { class: "gn-logo-g", html: "G" + cap }),
      h("span", { class: "gn-logo-rest" }, ["rade"]),
      h("span", { class: "gn-logo-rest" }, ["ne"]),
      h("span", { class: "gn-logo-x" }, ["X"]),
      h("span", { class: "gn-logo-rest" }, ["t"])
    ]);
  }

  /* ---- header shared by every page ---- */
  function header(activeKey) {
    var nav = [
      ["index.html", "🏠 Dashboard", "home"],
      ["curriculum.html", "📚 Curriculum", "curriculum"],
      ["blocklab.html", "🧪 Block Lab", "blocklab"],
      ["projects.html", "🚀 Projects", "projects"],
      ["report.html", "📊 Reports", "report"]
    ];
    initPaletteOnce();
    return h("header", { class: "c-head" }, [
      h("a", { class: "c-brand", href: "index.html" }, [
        logoEl(),
        h("div", { class: "c-brand-txt" }, [h("div", { class: "c-sub" }, ["Scratch Academy"])])
      ]),
      h("nav", { class: "c-nav" }, nav.map(function (n) {
        return h("a", { class: "c-navbtn" + (n[2] === activeKey ? " active" : ""), href: n[0] }, [n[1]]);
      })),
      h("div", { class: "head-right" }, [
        h("button", { class: "search-btn", title: "Search (Ctrl+K)", onclick: openPalette }, ["🔍"]),
        levelSwitch(), roleSwitch(), studentSwitcher()
      ])
    ]);
  }

  /* ---- Level 1 / Level 2: the platform is split into two parts ---- */
  function levelSwitch() {
    var GN = w.GN, lv = GN.level();
    function btn(n, label) {
      return h("button", {
        class: "lv-btn" + (lv === n ? " on" : ""),
        title: n === 1 ? "Level 1 — Foundations (sessions 1–50)"
                       : "Level 2 — Logic, Data & Game Engineering (sessions 1–50)",
        onclick: function () { if (lv !== n) { GN.setLevel(n); location.reload(); } }
      }, [label]);
    }
    return h("div", { class: "level-switch", role: "group", "aria-label": "Level" }, [
      btn(1, "Level 1"), btn(2, "Level 2")
    ]);
  }

  /* ---- global Tutor / Student switch (applies to every page) ---- */
  function roleSwitch() {
    var GN = w.GN, role = GN.role();
    function btn(r, label) {
      return h("button", {
        class: "role-btn" + (role === r ? " on " + r : ""),
        title: r === "tutor" ? "Tutor Mode — solutions, answers and teaching notes visible"
                             : "Student Mode — solutions hidden",
        onclick: function () { if (role !== r) { GN.setRole(r); location.reload(); } }
      }, [label]);
    }
    return h("div", { class: "role-switch", role: "group", "aria-label": "Mode" }, [
      btn("student", "🧒 Student"), btn("tutor", "👩‍🏫 Tutor")
    ]);
  }

  /* A banner making the current mode obvious, used on pages that gate content. */
  function modeBanner() {
    var GN = w.GN;
    if (GN.isTutor()) {
      return h("div", { class: "mode-banner tutor no-print" }, [
        h("b", {}, ["👩‍🏫 Tutor Mode"]),
        " — solutions, answers and teaching notes are visible. Switch to Student Mode before sharing your screen.",
        h("button", { class: "linkish", onclick: function () { GN.setRole("student"); location.reload(); } }, ["Switch to Student"])
      ]);
    }
    return h("div", { class: "mode-banner student no-print" }, [
      h("b", {}, ["🧒 Student Mode"]), " — solutions are hidden so you can work it out yourself."
    ]);
  }

  /* ---- student switcher (drives all progress) ----
     Adding and switching students is a TUTOR task. A student never sees
     account management — at most, their own name. */
  function studentSwitcher() {
    var GN = w.GN;
    var list = GN.students(), active = GN.active();
    var wrap = h("div", { class: "gn-switch" });

    if (!GN.isTutor()) {
      if (active) wrap.appendChild(h("span", { class: "gn-whoami" }, ["👋 " + active.name]));
      return wrap;
    }

    if (!list.length) {
      wrap.appendChild(h("button", { class: "btn primary sm", onclick: function () { addStudentFlow(); } },
        ["＋ Add student"]));
      return wrap;
    }
    var sel = h("select", { class: "gn-select", title: "Active student",
      onchange: function () {
        if (sel.value === "__add") { addStudentFlow(); return; }
        GN.setActive(sel.value); location.reload();
      } });
    list.forEach(function (s) {
      var o = h("option", { value: s.id }, [s.name + " · L" + s.level]);
      if (active && s.id === active.id) o.selected = true;
      sel.appendChild(o);
    });
    sel.appendChild(h("option", { value: "__add" }, ["＋ Add student…"]));
    wrap.appendChild(sel);
    return wrap;
  }

  function addStudentFlow() {
    var name = prompt("Student's first name:");
    if (name === null) return;
    var lv = prompt("Start at level 1 or 2?", "1");
    if (lv === null) return;
    var st = w.GN.addStudent(name || "New student", parseInt(lv, 10) === 2 ? 2 : 1);
    w.GN.setActive(st.id);
    location.reload();
  }

  function footer() {
    return h("footer", { class: "c-foot" }, [
      h("p", {}, ["Scratch Academy by GradeNext · 100 sessions across 2 levels · ",
        h("a", { href: "ATTRIBUTION.md", target: "_blank", rel: "noopener" }, ["Attribution & licences"])])
    ]);
  }

  function emptyState(msg, ctaLabel, ctaFn) {
    return h("div", { class: "gn-empty" }, [
      h("div", { class: "gn-empty-emoji" }, ["🐱"]),
      h("p", {}, [msg]),
      ctaLabel ? h("button", { class: "btn primary", onclick: ctaFn }, [ctaLabel]) : null
    ]);
  }

  /* ---- command palette: search sessions, blocks and projects (Ctrl+K) ---- */
  var paletteReady = false;
  function initPaletteOnce() {
    if (paletteReady) return;
    paletteReady = true;
    document.addEventListener("keydown", function (e) {
      if ((e.ctrlKey || e.metaKey) && String(e.key).toLowerCase() === "k") {
        e.preventDefault(); openPalette();
      }
    });
  }
  function paletteItems() {
    var items = [], P = w.GN_PLATFORM, R = w.GN_RPI;
    if (P && P.order) P.order.forEach(function (id) {
      var s = P.sessions[id];
      items.push({ t: "Session", label: "L" + s.level + " S" + s.n + " · " + s.title,
                   sub: s.concept, href: "learn.html?s=" + id });
    });
    if (P && P.blocks) Object.keys(P.blocks).forEach(function (k) {
      items.push({ t: "Block", label: k, sub: P.blocks[k].category,
                   href: "blocklab.html?q=" + encodeURIComponent(k) });
    });
    if (R && R.projects) Object.keys(R.projects).forEach(function (k) {
      var p = R.projects[k];
      items.push({ t: "Project", label: p.title, sub: p.concept, href: "projects.html#/p/" + k });
    });
    return items;
  }
  function openPalette() {
    if (document.querySelector(".cmdk")) return;
    var items = paletteItems();
    if (!items.length) return;
    var sel = 0, shown = [];
    var input = h("input", { class: "cmdk-input", type: "text",
      placeholder: "Search sessions, blocks and projects…" });
    var list = h("div", { class: "cmdk-list" });
    var box = h("div", { class: "cmdk-box" }, [input, list,
      h("div", { class: "cmdk-hint" }, ["↑↓ choose · Enter open · Esc close"])]);
    var ov = h("div", { class: "cmdk", onclick: function (e) { if (e.target === ov) close(); } }, [box]);
    function close() { document.removeEventListener("keydown", onKey, true); ov.remove(); }
    function draw() {
      var q = input.value.trim().toLowerCase();
      shown = items.filter(function (it) {
        return !q || (it.label + " " + it.sub + " " + it.t).toLowerCase().indexOf(q) >= 0;
      }).slice(0, 12);
      if (sel >= shown.length) sel = Math.max(0, shown.length - 1);
      list.innerHTML = "";
      shown.forEach(function (it, i) {
        list.appendChild(h("a", { class: "cmdk-item" + (i === sel ? " sel" : ""), href: it.href,
          onclick: close }, [
          h("span", { class: "cmdk-tag t-" + it.t.toLowerCase() }, [it.t]),
          h("span", { class: "cmdk-label" }, [it.label]),
          h("span", { class: "cmdk-sub" }, [it.sub])
        ]));
      });
      if (!shown.length) list.appendChild(h("div", { class: "cmdk-none" }, ["Nothing matches."]));
    }
    function onKey(e) {
      if (e.key === "Escape") { e.preventDefault(); close(); }
      else if (e.key === "ArrowDown") { e.preventDefault(); sel = Math.min(sel + 1, shown.length - 1); draw(); }
      else if (e.key === "ArrowUp") { e.preventDefault(); sel = Math.max(sel - 1, 0); draw(); }
      else if (e.key === "Enter" && shown[sel]) { e.preventDefault(); location.href = shown[sel].href; close(); }
    }
    input.addEventListener("input", function () { sel = 0; draw(); });
    document.addEventListener("keydown", onKey, true);
    document.body.appendChild(ov);
    input.focus(); draw();
  }

  /* ---- confetti celebration (no dependencies) ---- */
  function confetti() {
    var c = document.createElement("canvas");
    c.className = "gn-confetti";
    c.width = innerWidth; c.height = innerHeight;
    document.body.appendChild(c);
    var x = c.getContext("2d");
    var colors = ["#703D84", "#F5007E", "#7F5DF9", "#FF6AC6", "#FBDD80", "#89E6D5", "#9ECCFA"];
    var bits = [];
    for (var i = 0; i < 140; i++) bits.push({
      x: Math.random() * c.width, y: -20 - Math.random() * c.height * 0.5,
      w: 6 + Math.random() * 6, s: 2 + Math.random() * 3.5,
      r: Math.random() * Math.PI, vr: (Math.random() - 0.5) * 0.25,
      col: colors[i % colors.length]
    });
    var t0 = Date.now();
    (function tick() {
      x.clearRect(0, 0, c.width, c.height);
      bits.forEach(function (b) {
        b.y += b.s; b.x += Math.sin(b.y / 28) * 1.4; b.r += b.vr;
        x.save(); x.translate(b.x, b.y); x.rotate(b.r);
        x.fillStyle = b.col; x.fillRect(-b.w / 2, -b.w / 4, b.w, b.w / 2); x.restore();
      });
      if (Date.now() - t0 < 2600) requestAnimationFrame(tick); else c.remove();
    })();
  }

  /* ---- achievements panel, shared by dashboard and report ---- */
  function badgesPanel(P) {
    var GN = w.GN;
    var list = GN.achievements(P);
    var earned = list.filter(function (b) { return b.earned; }).length;
    return h("section", { class: "panel" }, [
      h("h2", { class: "panel-h" }, ["🏅 Achievements — " + earned + " of " + list.length]),
      h("div", { class: "badge-grid" }, list.map(function (b) {
        return h("div", { class: "badge" + (b.earned ? " earned" : ""), title: b.desc }, [
          h("span", { class: "badge-emoji" }, [b.emoji]),
          h("span", { class: "badge-name" }, [b.name]),
          h("span", { class: "badge-desc" }, [b.desc])
        ]);
      }))
    ]);
  }

  w.GNUI = { h: h, shade: shade, bar: bar, ring: ring, header: header, footer: footer,
             studentSwitcher: studentSwitcher, addStudentFlow: addStudentFlow, emptyState: emptyState,
             roleSwitch: roleSwitch, modeBanner: modeBanner, logoEl: logoEl, levelSwitch: levelSwitch,
             openPalette: openPalette, confetti: confetti, badgesPanel: badgesPanel };
})(window);
