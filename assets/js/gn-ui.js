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

  /* ---- brand mark + the full platform name, exactly as specified ---- */
  function logoEl() {
    var mark = '<svg class="gn-mark" viewBox="0 0 64 64" aria-hidden="true">' +
      '<rect width="64" height="64" rx="15" fill="#703D84"/>' +
      '<text x="32" y="41" text-anchor="middle" font-family="Poppins,Arial,sans-serif" font-weight="800" font-size="30" fill="#fff">G</text>' +
      '<path d="M32 8 12 16l20 8 15-6v7h4v-9z" fill="#F5007E"/>' +
      '<rect x="17" y="47" width="30" height="5" rx="2.5" fill="#F5007E"/></svg>';
    return h("span", { class: "gn-brandline" }, [
      h("span", { class: "gn-markwrap", html: mark }),
      h("span", { class: "gn-brandtxt" }, [
        h("span", { class: "gn-brand-main" }, ["Scratch Academy"]),
        h("span", { class: "gn-brand-by" }, ["by GradeNext"])
      ])
    ]);
  }

  /* ---- header shared by every page ---- */
  function header(activeKey) {
    var nav = [
      ["index.html", "🏠 Home", "home"],
      ["curriculum.html", "📚 Curriculum", "curriculum"],
      ["puzzles.html", "🧩 Puzzles", "puzzles"],
      ["flashcards.html", "🃏 Cards", "cards"],
      ["blocklab.html", "🧪 Block Lab", "blocklab"],
      ["projects.html", "🚀 Projects", "projects"],
      ["report.html", "📊 Reports", "report"]
    ];
    initPaletteOnce();
    return h("header", { class: "c-head" }, [
      h("a", { class: "c-brand", href: "index.html" }, [logoEl()]),
      h("nav", { class: "c-nav" }, nav.map(function (n) {
        return h("a", { class: "c-navbtn" + (n[2] === activeKey ? " active" : ""), href: n[0] }, [n[1]]);
      })),
      h("div", { class: "head-right" }, [
        themeBtn(),
        h("button", { class: "search-btn", title: "Search (Ctrl+K)", onclick: openPalette }, ["🔍"]),
        levelSwitch(), roleSwitch(), studentSwitcher()
      ])
    ]);
  }

  /* ---- one-tap light / dark switch; no reload needed ---- */
  function themeBtn() {
    var GN = w.GN;
    function icon(t) { return t === "dark" ? "☀️" : "🌙"; }
    function tip(t) { return t === "dark" ? "Switch to light theme" : "Switch to dark theme"; }
    var cur = GN.theme();
    var btn = h("button", { class: "theme-btn", title: tip(cur), "aria-label": tip(cur) }, [icon(cur)]);
    btn.addEventListener("click", function () {
      var next = GN.setTheme(GN.theme() === "dark" ? "light" : "dark");
      btn.textContent = icon(next);
      btn.title = tip(next);
      btn.setAttribute("aria-label", tip(next));
    });
    return btn;
  }

  /* ---- Level 1 / Level 2: the platform is split into two parts ----
     Students are pinned to their assigned level; the other side of the
     switch shows a lock. Tutors switch freely. */
  function levelSwitch() {
    var GN = w.GN, lv = GN.level(), pinned = !GN.isTutor();
    function btn(n, label) {
      var locked = pinned && lv !== n;
      return h("button", {
        class: "lv-btn" + (lv === n ? " on" : "") + (locked ? " locked" : ""),
        title: locked ? "Locked — your tutor moves you up when you're ready"
             : n === 1 ? "Level 1 — Foundations (sessions 1–50)"
                       : "Level 2 — Logic, Data & Game Engineering (sessions 1–50)",
        onclick: function () {
          if (lv === n) return;
          if (locked) {
            alert("🔒 You're a Level " + lv + " student, so Level " + n +
                  " is locked. Your tutor moves you up when you're ready!");
            return;
          }
          GN.setLevel(n); location.reload();
        }
      }, [locked ? "🔒 " + label : label]);
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
        title: r === "tutor" ? "Tutor Mode — needs the tutor PIN. Solutions, answers and teaching notes become visible."
                             : "Student Mode — solutions hidden",
        onclick: function () {
          if (role === r) return;
          if (r === "tutor") {
            var p = prompt("🔒 Enter the tutor PIN to unlock Tutor Mode:");
            if (p === null) return;
            if (!GN.checkPin(p)) { alert("That PIN isn't right. Tutor Mode stays locked."); return; }
          }
          GN.setRole(r); location.reload();
        }
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
        GN.setActive(sel.value);
        // land the tutor on the chosen student's level
        var chosen = GN.students().filter(function (s) { return s.id === sel.value; })[0];
        if (chosen) GN.setLevel(chosen.level);
        location.reload();
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

  /* the screen a student sees when a link points into the other level */
  function lockedHTML(wantLv, myLv) {
    return '<div style="padding:70px 20px;text-align:center">' +
      '<div style="font-size:46px">🔒</div>' +
      '<h1 style="font-size:22px;margin:12px 0 6px">This is a Level ' + wantLv + ' session</h1>' +
      '<p style="color:var(--ink-faint);max-width:420px;margin:0 auto 18px">You\'re a Level ' + myLv +
      ' student — your tutor unlocks the other level when you\'re ready.</p>' +
      '<a class="btn primary" href="curriculum.html">← Back to my level</a></div>';
  }

  function emptyState(msg, ctaLabel, ctaFn) {
    return h("div", { class: "gn-empty" }, [
      h("div", { class: "gn-empty-emoji" }, ["🎈"]),
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
  /* Students search ONLY their assigned level — sessions, blocks and
     projects from the other level never appear. Tutors search everything. */
  function paletteItems() {
    var items = [], P = w.GN_PLATFORM, R = w.GN_RPI, GN = w.GN;
    var tutor = GN.isTutor(), LV = GN.level();
    if (P && P.order) P.order.forEach(function (id) {
      var s = P.sessions[id];
      if (!tutor && s.level !== LV) return;
      items.push({ t: "Session", label: "L" + s.level + " S" + s.n + " · " + s.title,
                   sub: s.concept, href: "learn.html?s=" + id });
    });
    if (P && P.blocks) Object.keys(P.blocks).forEach(function (k) {
      var b = P.blocks[k];
      if (!tutor && b.sessions && b.sessions.length && !b.sessions.some(function (sid) {
        return P.sessions[sid] && P.sessions[sid].level === LV; })) return;
      items.push({ t: "Block", label: k, sub: b.category,
                   href: "blocklab.html?q=" + encodeURIComponent(k) });
    });
    if (R && R.projects) {
      var projLv = {};
      if (P && P.sessions) Object.keys(P.sessions).forEach(function (id) {
        var s = P.sessions[id];
        if (s.content && s.content.kind === "project") {
          var cur = projLv[s.content.ref];
          projLv[s.content.ref] = cur ? Math.min(cur, s.level) : s.level;
        }
      });
      Object.keys(R.projects).forEach(function (k) {
        if (!tutor && (projLv[k] || 2) !== LV) return;
        var p = R.projects[k];
        items.push({ t: "Project", label: p.title, sub: p.concept, href: "projects.html#/p/" + k });
      });
    }
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
             lockedHTML: lockedHTML,
             openPalette: openPalette, confetti: confetti, badgesPanel: badgesPanel };
})(window);
