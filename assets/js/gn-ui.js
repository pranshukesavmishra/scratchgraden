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

  /* ---- header shared by every page ---- */
  function header(activeKey) {
    var nav = [
      ["index.html", "🏠 Dashboard", "home"],
      ["curriculum.html", "📚 Curriculum", "curriculum"],
      ["blocklab.html", "🧪 Block Lab", "blocklab"],
      ["projects.html", "🚀 Projects", "projects"],
      ["report.html", "📊 Reports", "report"]
    ];
    return h("header", { class: "c-head" }, [
      h("a", { class: "c-brand", href: "index.html" }, [
        h("span", { class: "c-mark" }, ["🐱"]),
        h("div", {}, [h("div", { class: "c-name" }, ["Grade Next"]),
                      h("div", { class: "c-sub" }, ["Scratch Academy"])])
      ]),
      h("nav", { class: "c-nav" }, nav.map(function (n) {
        return h("a", { class: "c-navbtn" + (n[2] === activeKey ? " active" : ""), href: n[0] }, [n[1]]);
      })),
      studentSwitcher()
    ]);
  }

  /* ---- student switcher (drives all progress) ---- */
  function studentSwitcher() {
    var GN = w.GN;
    var list = GN.students(), active = GN.active();
    var wrap = h("div", { class: "gn-switch" });

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
      h("p", {}, ["Grade Next Scratch Academy · 100 sessions across 2 levels · ",
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

  w.GNUI = { h: h, shade: shade, bar: bar, ring: ring, header: header, footer: footer,
             studentSwitcher: studentSwitcher, addStudentFlow: addStudentFlow, emptyState: emptyState };
})(window);
