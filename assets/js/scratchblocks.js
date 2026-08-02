/* =====================================================================
   GRADE NEXT — visual Scratch block renderer
   Turns plain block pseudocode into real, colour-coded Scratch-shaped
   blocks: hat blocks, C-blocks that wrap their children, oval number
   inputs, rounded text inputs and hexagonal booleans.

       when green flag clicked
       forever
         if <touching [Enemy]?> then
           change [score] by 1
         end
       end

   ...renders as the stack a child actually sees in Scratch.
   ===================================================================== */
(function (w) {
  "use strict";

  var COLOR = {
    Motion:    "#4c97ff", Looks:   "#9966ff", Sound:     "#cf63cf",
    Events:    "#ffbf00", Control: "#ffab19", Sensing:   "#5cb1d6",
    Operators: "#59c059", Variables: "#ff8c1a", MyBlocks: "#ff6680",
    Pen:       "#0fbd8c", Music:   "#d65cd6", Unknown:  "#7d8aa3"
  };

  /* Ordered most-specific first — "set x to" is Motion, "set size to" is
     Looks, "set [score] to" is Variables. Order decides correctness. */
  var RULES = [
    [/^when .*clone/i, "Control"],
    [/^when/i, "Events"],
    [/^(broadcast)/i, "Events"],
    [/^(forever|repeat|if |else|end$|wait |stop |create clone|delete this clone)/i, "Control"],

    [/^set (x|y) to/i, "Motion"],
    [/^change (x|y) by/i, "Motion"],
    [/^(move|turn|go to|glide|point|if on edge|set rotation)/i, "Motion"],

    [/^set size to/i, "Looks"], [/^change size by/i, "Looks"],
    [/^change \[?(ghost|color|colour|brightness)/i, "Looks"],
    [/^(say|think|switch costume|next costume|switch backdrop|next backdrop|show$|hide$|clear graphic)/i, "Looks"],

    [/^set tempo/i, "Music"], [/^(play drum|play note|rest for)/i, "Music"],
    [/^change volume/i, "Sound"],
    [/^(play sound|start sound|stop all sounds)/i, "Sound"],

    [/^set pen/i, "Pen"], [/^change pen/i, "Pen"],
    [/^(pen down|pen up|erase all)/i, "Pen"],

    [/^(ask|answer|reset timer|timer$)/i, "Sensing"],
    [/^(touching|key |distance to|mouse )/i, "Sensing"],

    [/^define/i, "MyBlocks"],

    [/^(set|change) /i, "Variables"],
    [/^(show variable|hide variable|add |delete |insert |replace )/i, "Variables"],
    [/^(item |length of)/i, "Variables"],

    [/^(join|pick random|round|not |abs)/i, "Operators"]
  ];

  function categoryOf(text) {
    var t = String(text).trim();
    for (var i = 0; i < RULES.length; i++) if (RULES[i][0].test(t)) return RULES[i][1];
    return "Unknown";
  }

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  /* Split a block's label into text and its input slots. */
  function labelHTML(text) {
    var out = "", i = 0, s = String(text);
    while (i < s.length) {
      var ch = s[i];
      if (ch === "(" || ch === "[" || ch === "<") {
        var close = ch === "(" ? ")" : (ch === "[" ? "]" : ">");
        var depth = 1, j = i + 1;
        while (j < s.length && depth > 0) {
          if (s[j] === ch) depth++;
          else if (s[j] === close) depth--;
          if (depth === 0) break;
          j++;
        }
        var inner = s.slice(i + 1, j);
        var cls = ch === "(" ? "sb-in-num" : (ch === "[" ? "sb-in-txt" : "sb-in-bool");
        // a nested reporter inside an input keeps its own colour
        var nestedCat = categoryOf(inner);
        var style = "";
        if (ch !== "<" && nestedCat !== "Unknown" && /^[a-z]/i.test(inner) && inner.length > 2) {
          style = ' style="background:' + COLOR[nestedCat] + ';color:#fff;border-color:rgba(0,0,0,.18)"';
        }
        out += '<span class="sb-input ' + cls + '"' + style + '>' + labelHTML(inner) + "</span>";
        i = j + 1;
      } else {
        var next = s.slice(i).search(/[(\[<]/);
        var chunk = next < 0 ? s.slice(i) : s.slice(i, i + next);
        out += esc(chunk);
        i += chunk.length || 1;
      }
    }
    return out;
  }

  function isCBlock(t) {
    return /^(forever|repeat\b|repeat until|if .*then$|else$)/i.test(t.trim());
  }
  function isHat(t) {
    return /^(when|define)/i.test(t.trim());
  }
  function isCap(t) {
    return /^(stop \[?all|delete this clone)/i.test(t.trim());
  }

  /* Build a nested tree from lines, using `end` / `else` to close and open. */
  function parse(code) {
    var lines = String(code).replace(/\t/g, "  ").split("\n");
    var root = { children: [] }, stack = [root];
    lines.forEach(function (raw) {
      var t = raw.trim();
      if (!t) return;
      var top = stack[stack.length - 1];
      if (/^end$/i.test(t)) { if (stack.length > 1) stack.pop(); return; }
      if (/^else$/i.test(t)) {
        if (stack.length > 1) stack.pop();
        var parent = stack[stack.length - 1];
        var node = { text: "else", children: [], c: true };
        parent.children.push(node); stack.push(node);
        return;
      }
      var n = { text: t, children: [], c: isCBlock(t) };
      top.children.push(n);
      if (n.c) stack.push(n);
    });
    return root;
  }

  function renderNode(n) {
    var cat = categoryOf(n.text), color = COLOR[cat];
    var cls = "sb-block sb-" + cat.toLowerCase();
    if (isHat(n.text)) cls += " sb-hat";
    if (isCap(n.text)) cls += " sb-cap";

    var el = document.createElement("div");
    el.className = "sb-wrap";

    var top = document.createElement("div");
    top.className = cls;
    top.style.background = color;
    top.innerHTML = labelHTML(n.text);
    el.appendChild(top);

    if (n.c) {
      var body = document.createElement("div");
      body.className = "sb-body";
      body.style.borderColor = color;
      if (!n.children.length) {
        var ph = document.createElement("div");
        ph.className = "sb-empty";
        body.appendChild(ph);
      }
      n.children.forEach(function (k) { body.appendChild(renderNode(k)); });
      el.appendChild(body);

      var foot = document.createElement("div");
      foot.className = "sb-foot";
      foot.style.background = color;
      el.appendChild(foot);
    }
    return el;
  }

  /* Public: return a DOM element showing `code` as Scratch blocks. */
  function render(code) {
    var wrap = document.createElement("div");
    wrap.className = "sb-stack";
    var tree = parse(code);
    tree.children.forEach(function (n) { wrap.appendChild(renderNode(n)); });
    if (!tree.children.length) wrap.textContent = code;
    return wrap;
  }

  /* Public: a single inline block chip (for "the block is `move 10 steps`"). */
  function chip(text) {
    var cat = categoryOf(text);
    var el = document.createElement("span");
    el.className = "sb-chip sb-" + cat.toLowerCase();
    el.style.background = COLOR[cat];
    el.innerHTML = labelHTML(text);
    return el;
  }

  /* Public: replace every matching <pre>/<code> on the page with real blocks. */
  function upgradeAll(root, selector) {
    (root || document).querySelectorAll(selector).forEach(function (node) {
      var code = node.textContent;
      if (!code || !code.trim()) return;
      var out = render(code);
      node.parentNode.replaceChild(out, node);
    });
  }

  w.SB = { render: render, chip: chip, upgradeAll: upgradeAll,
           categoryOf: categoryOf, COLOR: COLOR };
})(window);
