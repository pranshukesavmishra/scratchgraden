/* =====================================================================
   GRADE NEXT — Real Project Library
   Ready-made Scratch projects imported from the Raspberry Pi Foundation /
   Code Club open curriculum (CC BY-SA 4.0). Learning paths -> projects ->
   a step-by-step viewer with the real finished project as "Desired Output".
   ===================================================================== */
(function () {
  "use strict";
  var R = window.GN_RPI || { paths: [], projects: {} };
  var app;
  var DONE_KEY = "gn_rpi_done";

  /* tiny hyperscript */
  function h(tag, attrs, kids) {
    var e = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "class") e.className = attrs[k];
      else if (k === "html") e.innerHTML = attrs[k];
      else if (k.slice(0, 2) === "on" && typeof attrs[k] === "function") e.addEventListener(k.slice(2), attrs[k]);
      else if (attrs[k] != null) e.setAttribute(k, attrs[k]);
    });
    (kids || []).forEach(function (c) { if (c == null) return; e.appendChild(typeof c === "string" ? document.createTextNode(c) : c); });
    return e;
  }
  function shade(hex, amt) {
    var n = parseInt(hex.slice(1), 16), r = (n >> 16) + amt, g = ((n >> 8) & 255) + amt, b = (n & 255) + amt;
    r = Math.max(0, Math.min(255, r)); g = Math.max(0, Math.min(255, g)); b = Math.max(0, Math.min(255, b));
    return "#" + (0x1000000 + r * 0x10000 + g * 0x100 + b).toString(16).slice(1);
  }
  function thumb(emoji, color, big) {
    return h("div", { class: "thumb" + (big ? " big" : ""), style: "background:linear-gradient(135deg," + color + "," + shade(color, -22) + ")" },
      [h("span", { class: "thumb-emoji" }, [emoji])]);
  }
  function diffBar(n) {
    var wrap = h("div", { class: "levelbar" });
    for (var i = 1; i <= 3; i++) wrap.appendChild(h("span", { class: "seg" + (i <= n ? " on lv" + n : "") }));
    return wrap;
  }
  var CAT_COLOR = {
    animation: "#38bdf8", game: "#34d399", puzzle: "#f59e0b", quiz: "#fbbf24",
    chatbot: "#a78bfa", music: "#fb923c", art: "#f472b6", sandbox: "#22d3ee", tool: "#94a3b8"
  };
  function projColor(p) { return CAT_COLOR[p.category] || "#4c97ff"; }

  /* progress in localStorage: { slug: highestStepReached } */
  function loadDone() { try { return JSON.parse(localStorage.getItem(DONE_KEY)) || {}; } catch (e) { return {}; } }
  function saveDone(d) { try { localStorage.setItem(DONE_KEY, JSON.stringify(d)); } catch (e) {} }
  function progressOf(slug) {
    var p = R.projects[slug]; if (!p) return 0;
    var d = loadDone()[slug] || 0;
    return Math.round((d / p.stepCount) * 100);
  }

  /* ---------------- header ---------------- */
  function header() {
    return h("header", { class: "c-head" }, [
      h("a", { class: "c-brand", href: "#/", role: "button" }, [
        h("span", { class: "c-mark" }, ["🐱"]),
        h("div", {}, [h("div", { class: "c-name" }, ["Grade Next"]), h("div", { class: "c-sub" }, ["Real Project Library"])])
      ]),
      h("nav", { class: "c-nav" }, [
        h("a", { class: "c-navbtn", href: "index.html" }, ["🎮 Game Course"]),
        h("a", { class: "c-navbtn", href: "blocklab.html" }, ["🧪 Block Lab"])
      ])
    ]);
  }

  /* ---------------- library home ---------------- */
  function viewHome() {
    var wrap = h("div", { class: "view" });
    var total = Object.keys(R.projects).length;
    var steps = Object.keys(R.projects).reduce(function (a, k) { return a + R.projects[k].stepCount; }, 0);
    wrap.appendChild(h("section", { class: "c-hero rpi-hero" }, [
      h("div", { class: "rpi-hero-badge" }, ["★ Ready-made · real projects"]),
      h("h1", {}, ["The Real Project Library 🚀"]),
      h("p", {}, [total + " complete, professionally-made Scratch projects — " + steps +
        " guided steps in all. Every project shows the real finished game you're building, then walks you through it step by step. Pick a path and start creating!"]),
      h("p", { class: "rpi-hero-src" }, ["Imported from the ",
        h("a", { href: "https://projects.raspberrypi.org", target: "_blank", rel: "noopener" }, ["Raspberry Pi Foundation / Code Club"]),
        " open curriculum · CC BY-SA 4.0"])
    ]));

    R.paths.forEach(function (path) {
      var sec = h("section", { class: "rpi-path" });
      sec.appendChild(h("div", { class: "rpi-path-head" }, [
        h("span", { class: "rpi-path-emoji", style: "background:" + path.color + "22;color:" + shade(path.color, -40) }, [path.emoji]),
        h("div", {}, [h("h2", {}, [path.title]), h("p", {}, [path.blurb])])
      ]));
      var row = h("div", { class: "rpi-row" });
      path.projects.forEach(function (slug) {
        var p = R.projects[slug]; if (p) row.appendChild(projCard(p));
      });
      sec.appendChild(row);
      wrap.appendChild(sec);
    });
    return wrap;
  }

  function projCard(p) {
    var color = projColor(p);
    var pct = progressOf(p.slug);
    var media;
    if (p.heroImage) {
      media = h("div", { class: "pc-hero" }, [
        h("img", { src: p.heroImage, alt: p.title, loading: "lazy" }),
        h("span", { class: "pc-emoji" }, [p.emoji])
      ]);
    } else {
      media = h("div", { class: "pc-hero pc-hero-plain", style: "background:linear-gradient(135deg," + color + "," + shade(color, -22) + ")" },
        [h("span", { class: "pc-emoji big" }, [p.emoji])]);
    }
    return h("a", { class: "pc", href: "#/p/" + p.slug }, [
      media,
      h("div", { class: "pc-body" }, [
        h("div", { class: "pc-top" }, [
          h("span", { class: "type-badge cat-" + p.category }, [p.category]),
          h("span", { class: "pc-steps" }, ["🧩 " + p.stepCount + " steps"])
        ]),
        h("h3", {}, [p.title]),
        h("p", { class: "pc-desc" }, [p.description || p.intro || ""]),
        h("div", { class: "pc-foot" }, [
          h("div", { class: "pc-diff" }, [diffBar(p.difficulty), h("span", {}, [p.difficultyLabel])]),
          h("span", { class: "tag-chip" }, ["⭐ " + p.concept])
        ]),
        pct > 0 ? h("div", { class: "pc-prog" }, [
          h("div", { class: "bar" }, [h("div", { class: "bar-fill", style: "width:" + pct + "%;background:" + color })]),
          h("span", {}, [pct >= 100 ? "✓ Completed" : pct + "% done"])
        ]) : null
      ])
    ]);
  }

  /* ---------------- project viewer ---------------- */
  function viewProject(slug) {
    var p = R.projects[slug];
    if (!p) return viewHome();
    var color = projColor(p);

    // which step? read from hash tail #/p/slug/step
    var m = (location.hash || "").match(/\/p\/[^/]+\/(\d+)/);
    var step = m ? Math.max(1, Math.min(p.stepCount, parseInt(m[1], 10))) : 1;

    // record progress
    var done = loadDone(); if ((done[slug] || 0) < step) { done[slug] = step; saveDone(done); }

    var wrap = h("div", { class: "view rpi-view" });
    wrap.appendChild(h("div", { class: "crumbs" }, [
      h("a", { class: "crumb", href: "#/" }, ["← All projects"]), h("span", {}, [" / "]),
      h("span", {}, [p.title])
    ]));

    // title band
    wrap.appendChild(h("div", { class: "rpi-title", style: "--pc:" + color }, [
      thumb(p.emoji, color, true),
      h("div", { class: "rpi-title-txt" }, [
        h("h1", {}, [p.title]),
        h("p", { class: "rpi-sub" }, [p.intro || p.description || ""]),
        h("div", { class: "rpi-tags" }, [
          h("span", { class: "type-badge cat-" + p.category }, [p.category]),
          h("span", { class: "tag-chip" }, ["⭐ " + p.concept]),
          h("span", { class: "pc-diff mini" }, [diffBar(p.difficulty), h("span", {}, [p.difficultyLabel])])
        ])
      ]),
      h("a", { class: "btn primary big rpi-title-cta", href: p.openUrl, target: "_blank", rel: "noopener" }, ["🐱 Open in Scratch →"])
    ]));

    // layout: main (steps) + sidebar (desired output + tools)
    var grid = h("div", { class: "rpi-grid" });

    /* --- sidebar --- */
    var side = h("aside", { class: "rpi-side" });
    // Desired Output
    var doCard = h("div", { class: "rpi-card" }, [h("div", { class: "rpi-card-h" }, ["🎯 Desired Output"])]);
    if (p.embedUrl) {
      doCard.appendChild(h("div", { class: "rpi-embed" }, [
        h("iframe", { src: p.embedUrl, title: p.title + " — finished project", allowtransparency: "true", frameborder: "0", scrolling: "no", allowfullscreen: "true" })
      ]));
      doCard.appendChild(h("p", { class: "rpi-note" }, ["▶ Click the green flag above to play the finished project — this is what you'll build."]));
      doCard.appendChild(h("a", { class: "btn ghost block", href: p.projectUrl, target: "_blank", rel: "noopener" }, ["↗ Open finished project"]));
    } else if (p.heroImage) {
      doCard.appendChild(h("img", { class: "rpi-embed-img", src: p.heroImage, alt: p.title }));
      doCard.appendChild(h("p", { class: "rpi-note" }, ["This is the kind of result you'll create. Follow the steps to build your own version."]));
    }
    side.appendChild(doCard);

    // Build it — DIRECT redirect into Scratch (with the sprites already loaded)
    var openLabel = { starter: "🐱 Open the starter in Scratch →",
                      seeinside: "🐱 Open in Scratch →",
                      blank: "🐱 Open Scratch editor →" }[p.openMode] || "🐱 Open in Scratch →";
    var openNote = { starter: "The sprites and backdrop are placed for you — just add the code by following the steps. No solution code is included.",
                     seeinside: "Opens the real project in Scratch so you can play it, look inside to see how it works, and remix your own copy — with every sprite already loaded.",
                     blank: "Opens a fresh Scratch editor. Follow the steps to add the sprites and code." }[p.openMode];
    var buildCard = h("div", { class: "rpi-card rpi-buildcard" }, [
      h("div", { class: "rpi-card-h" }, ["🛠 Build it in Scratch"]),
      h("a", { class: "btn primary block big", href: p.openUrl, target: "_blank", rel: "noopener" }, [openLabel]),
      h("p", { class: "rpi-note" }, [openNote]),
      p.openMode !== "blank"
        ? h("a", { class: "btn ghost block", href: p.editorUrl, target: "_blank", rel: "noopener" }, ["Start from a blank editor instead"])
        : null,
      h("a", { class: "btn ghost block", href: "https://scratch.mit.edu/projects/editor/?tutorial=getStarted", target: "_blank", rel: "noopener" }, ["🎬 New to Scratch? Watch the intro"])
    ]);
    side.appendChild(buildCard);

    // Step list
    var stepsCard = h("div", { class: "rpi-card" }, [h("div", { class: "rpi-card-h" }, ["📋 Steps"])]);
    var list = h("ol", { class: "rpi-steplist" });
    p.steps.forEach(function (s) {
      list.appendChild(h("li", { class: (s.n === step ? "active" : "") + (s.n < step ? " seen" : "") }, [
        h("a", { href: "#/p/" + slug + "/" + s.n }, [h("span", { class: "sl-n" }, [String(s.n)]), h("span", {}, [s.title])])
      ]));
    });
    stepsCard.appendChild(list);
    side.appendChild(stepsCard);

    // Attribution
    side.appendChild(h("div", { class: "rpi-attr" }, [
      "Project by the Raspberry Pi Foundation / Code Club, used under ",
      h("a", { href: "https://creativecommons.org/licenses/by-sa/4.0/", target: "_blank", rel: "noopener" }, ["CC BY-SA 4.0"]),
      ". ", h("a", { href: p.sourceUrl, target: "_blank", rel: "noopener" }, ["View original"]), "."
    ]));

    /* --- main step panel --- */
    var cur = p.steps[step - 1];
    var main = h("div", { class: "rpi-main" });
    var pct = Math.round((step / p.stepCount) * 100);
    main.appendChild(h("div", { class: "rpi-prog" }, [
      h("div", { class: "rpi-prog-txt" }, ["Step " + step + " of " + p.stepCount]),
      h("div", { class: "bar" }, [h("div", { class: "bar-fill", style: "width:" + pct + "%;background:" + color })])
    ]));
    var body = h("div", { class: "rpi-step" });
    body.innerHTML = cur.html;
    upgradeStep(body);
    main.appendChild(body);

    // prev / next
    var nav = h("div", { class: "rpi-stepnav" }, [
      step > 1 ? h("a", { class: "btn ghost", href: "#/p/" + slug + "/" + (step - 1) }, ["← Previous"]) : h("span", {}),
      h("span", { class: "rpi-stepnav-mid" }, [cur.title]),
      step < p.stepCount ? h("a", { class: "btn primary", href: "#/p/" + slug + "/" + (step + 1) }, ["Next step →"])
        : h("a", { class: "btn complete is-done", href: "#/" }, ["✓ Finished — back to library"])
    ]);
    main.appendChild(nav);

    grid.appendChild(main);
    grid.appendChild(side);
    wrap.appendChild(grid);
    return wrap;
  }

  /* make imported step HTML a bit friendlier: wrap tasks with a check, lazy imgs */
  function upgradeStep(root) {
    // number the task cards
    var tasks = root.querySelectorAll(".rpi-task");
    for (var i = 0; i < tasks.length; i++) {
      var chip = document.createElement("span");
      chip.className = "rpi-task-chip";
      chip.textContent = "Do this";
      tasks[i].insertBefore(chip, tasks[i].firstChild);
    }
    // open images in a lightbox on click
    root.querySelectorAll("img.rpi-img").forEach(function (img) {
      img.addEventListener("click", function () { lightbox(img.src, img.alt); });
    });
  }

  function lightbox(src, alt) {
    var ov = h("div", { class: "rpi-lb", onclick: function () { document.body.removeChild(ov); } }, [
      h("img", { src: src, alt: alt || "" })
    ]);
    document.body.appendChild(ov);
  }

  /* ---------------- router ---------------- */
  function render() {
    var hs = (location.hash || "").replace(/^#\/?/, "");
    var parts = hs.split("/").filter(Boolean);
    app.innerHTML = "";
    app.appendChild(header());
    var main = h("main", { class: "c-main" });
    if (parts[0] === "p" && parts[1]) main.appendChild(viewProject(parts[1]));
    else main.appendChild(viewHome());
    app.appendChild(main);
    app.appendChild(h("footer", { class: "c-foot" }, [
      h("p", {}, ["Real projects imported from the Raspberry Pi Foundation / Code Club open curriculum, used under CC BY-SA 4.0. ",
        h("a", { href: "ATTRIBUTION.md", target: "_blank", rel: "noopener" }, ["Attribution"]), "."])
    ]));
    if (!(parts[0] === "p" && parts[2])) window.scrollTo(0, 0);
  }

  function boot() {
    app = document.getElementById("app");
    if (!R.paths.length) { app.innerHTML = '<div style="padding:40px;text-align:center">Project library failed to load.</div>'; return; }
    window.addEventListener("hashchange", render);
    render();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
