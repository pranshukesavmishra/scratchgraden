#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
import_rpi.py — import real, ready-made Scratch projects from the
Raspberry Pi Foundation / Code Club open-source curriculum on GitHub
(https://github.com/raspberrypilearning), licensed CC BY-SA 4.0.

For each project we pull:
  • en/meta.yml       -> title, description, hero image, ordered step titles
  • en/step_N.md      -> the real, step-by-step build instructions
  • the finished project's Scratch embed id (from step 1) -> "Desired Output"

The RPi markdown (task/hints/collapse/challenge blocks, blocks3 code,
kramdown attribute lists, image references) is converted to clean, safe
HTML so the browser can render it directly. Images are rewritten to
absolute raw.githubusercontent.com URLs so they load in any browser.

Output:
  • assets/js/rpi.js         -> window.GN_RPI  (paths + projects, used by UI)
  • imported/rpi_catalog.json -> the same data, pretty-printed
  • ATTRIBUTION.md            -> required CC BY-SA attribution

Run: python3 tools/import_rpi.py
"""
import os, re, sys, json, html, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CACERT = "/root/.ccr/ca-bundle.crt"
RAW = "https://raw.githubusercontent.com/raspberrypilearning"
BRANCH = "master"

IMPORTED = os.path.join(ROOT, "imported")
os.makedirs(IMPORTED, exist_ok=True)

# ---------------------------------------------------------------------------
# The catalogue: verified-reachable RPi/Code Club Scratch projects, arranged
# into topic-wise learning paths for ages 7-12. Each entry carries the light
# metadata the browser needs (emoji, concept tag, difficulty, category).
# ---------------------------------------------------------------------------
PATHS = [
    {
        "id": "p1", "title": "Starter Animations",
        "emoji": "\u2728", "color": "#38bdf8",
        "blurb": "First steps: move, say, costume changes and simple loops.",
        "projects": [
            ("silly-eyes",        "\U0001F440", "Motion & Looks",       1, "animation"),
            ("space-talk",        "\U0001F680", "Events & Say",         1, "animation"),
            ("surprise-animation","\U0001F389", "Events & Sound",       1, "animation"),
            ("lost-in-space",     "\U0001F6F8", "Motion & Loops",       1, "animation"),
        ],
    },
    {
        "id": "p2", "title": "First Games",
        "emoji": "\U0001F3AE", "color": "#34d399",
        "blurb": "Controls, sensing and simple win/lose - your first playable games.",
        "projects": [
            ("catch-the-bus",   "\U0001F68C", "Motion & Sensing",   1, "game"),
            ("find-the-bug",    "\U0001F41B", "Debugging",          1, "puzzle"),
            ("beat-the-goalie", "\u26BD",     "Motion & Score",     2, "game"),
            ("catch-the-dots",  "\U0001F7E1", "Sensing & Speed",    1, "game"),
            ("balloons",        "\U0001F388", "Click & Score",      2, "game"),
            ("archery",         "\U0001F3F9", "Aiming & Score",     2, "game"),
            ("boat-race",       "\U0001F6A4", "Sensing Colour",     2, "game"),
        ],
    },
    {
        "id": "p3", "title": "Scores & Variables",
        "emoji": "\U0001F3C6", "color": "#fbbf24",
        "blurb": "Keep score, add timers and build quizzes with variables.",
        "projects": [
            ("ghostbusters",    "\U0001F47B", "Variables & Timer",  2, "game"),
            ("dodgeball",       "\U0001F93E", "Sensing & Score",    2, "game"),
            ("brain-game",      "\u2753",     "Variables & Quiz",   2, "quiz"),
            ("guess-the-flag",  "\U0001F6A9", "Quiz & Variables",   2, "quiz"),
            ("memory",          "\U0001F9E0", "Sequence & Memory",  2, "game"),
        ],
    },
    {
        "id": "p4", "title": "Input & Logic",
        "emoji": "\U0001F916", "color": "#a78bfa",
        "blurb": "Ask questions, broadcast messages and use conditions to decide.",
        "projects": [
            ("chatbot",             "\U0001F916", "Ask & Answer",      2, "chatbot"),
            ("broadcasting-spells", "\U0001F9D9", "Broadcast Events",  2, "animation"),
            ("flappy-parrot",       "\U0001F99C", "Gravity & If",      3, "game"),
        ],
    },
    {
        "id": "p5", "title": "Clones & Advanced",
        "emoji": "\U0001F47E", "color": "#f472b6",
        "blurb": "Spawn many sprites with clones - the key to bigger games.",
        "projects": [
            ("clone-wars",            "\U0001F47E", "Clones",           3, "game"),
            ("space-junk",            "\U0001F6F0\uFE0F", "Clones & Sensing", 3, "game"),
            ("binary-hero",           "\U0001F3B8", "Clones & Music",   3, "game"),
            ("synchronised-swimming", "\U0001F3CA", "Clones & Patterns",3, "animation"),
        ],
    },
    {
        "id": "p6", "title": "Music & Art",
        "emoji": "\U0001F3A8", "color": "#fb923c",
        "blurb": "Make sounds, play instruments and draw with the pen.",
        "projects": [
            ("rock-band",             "\U0001F941", "Sound & Events",    1, "music"),
            ("music-maker",           "\U0001F3B9", "Sound & Loops",     2, "music"),
            ("paint-box",             "\U0001F58C\uFE0F", "Pen & Drawing", 2, "art"),
            ("create-your-own-world", "\U0001F30D", "Backdrops & Broadcast", 2, "sandbox"),
            ("butterfly-garden",      "\U0001F98B", "Pen & Clones",      2, "art"),
        ],
    },
]

DIFF_LABEL = {1: "Beginner", 2: "Intermediate", 3: "Advanced"}

# Friendly replacements for RPi "ingredient" includes ([[[ ... ]]]).
INCLUDES = {
    "generic-scratch3-sprite-from-library":
        "**Add a sprite** &mdash; click the *Choose a Sprite* button (bottom-right) and pick one from the Scratch library.",
    "generic-scratch3-backdrop-from-library":
        "**Add a backdrop** &mdash; click the *Choose a Backdrop* button (bottom-right) and pick one from the library.",
    "generic-scratch3-add-variable":
        "**Make a variable** &mdash; in the *Variables* section click *Make a Variable*, give it a name and click *OK*.",
    "generic-scratch3-make-a-list":
        "**Make a list** &mdash; in the *Variables* section click *Make a List*, give it a name and click *OK*.",
    "generic-scratch3-green-flag":
        "**Test it** by clicking the green flag above the stage.",
    "generic-scratch3-save":
        "**Save your work.**",
    "generic-scratch-save-project":
        "**Save your work.**",
    "generic-scratch3-sound-from-library":
        "**Add a sound** &mdash; click the *Sounds* tab, then *Choose a Sound* and pick one from the library.",
    "generic-scratch3-costume-from-library":
        "**Add a costume** &mdash; click the *Costumes* tab, then *Choose a Costume* from the library.",
}

# ---------------------------------------------------------------------------
# fetching
# ---------------------------------------------------------------------------
def fetch(url):
    """Return (text, ok). Uses curl with the proxy CA bundle."""
    try:
        r = subprocess.run(
            ["curl", "-sS", "-f", "--cacert", CACERT, url],
            capture_output=True, text=True, timeout=40)
        if r.returncode == 0:
            return r.stdout, True
    except Exception as e:
        sys.stderr.write("fetch error %s: %s\n" % (url, e))
    return "", False


# ---------------------------------------------------------------------------
# tiny YAML-ish reader for meta.yml (only the fields we need)
# ---------------------------------------------------------------------------
def parse_meta(text):
    meta = {"title": "", "description": "", "hero_image": "",
            "original_url": "", "steps": []}
    in_steps = False
    for line in text.splitlines():
        if re.match(r"^steps:\s*$", line):
            in_steps = True
            continue
        if in_steps:
            m = re.match(r"^-\s*title:\s*(.+?)\s*$", line)
            if m:
                meta["steps"].append(m.group(1).strip().strip('"\''))
            # step sub-keys (completion/challenge) are ignored
            continue
        for key in ("title", "description", "hero_image", "original_url"):
            m = re.match(r"^%s:\s*(.+?)\s*$" % key, line)
            if m:
                meta[key] = m.group(1).strip().strip('"\'')
    return meta


# ---------------------------------------------------------------------------
# markdown -> HTML  (tuned for the Raspberry Pi project dialect)
# ---------------------------------------------------------------------------
def _abs_img(slug, src):
    src = src.strip()
    if src.startswith("http"):
        return src
    src = src.lstrip("./")
    return "%s/%s/%s/en/%s" % (RAW, slug, BRANCH, src)


def _inline(slug, text):
    """Inline markdown -> HTML on a single line of already text (not code)."""
    # images  ![alt](src)
    def img(m):
        alt = html.escape(m.group(1), quote=True)
        return ('<img class="rpi-img" loading="lazy" alt="%s" src="%s">'
                % (alt, html.escape(_abs_img(slug, m.group(2)), quote=True)))
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", img, text)

    # links  [text](url){:attrs}
    def link(m):
        return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (
            html.escape(m.group(2), quote=True), m.group(1))
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)(\{:[^}]*\})?", link, text)

    # inline block references  `text`{:class="block3xxx"}  and plain `code`
    def code(m):
        cls = m.group(2) or ""
        c = re.search(r'class="([^"]+)"', cls or "")
        klass = " " + c.group(1) if c else ""
        return '<code class="blk%s">%s</code>' % (klass, html.escape(m.group(1)))
    text = re.sub(r"`([^`]+)`(\{:[^}]*\})?", code, text)

    # bold / italics
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)

    # strip any leftover kramdown attribute lists
    text = re.sub(r"\{:[^}]*\}", "", text)
    return text


def md_to_html(slug, md):
    """Convert one RPi step's markdown into an HTML string."""
    lines = md.replace("\r\n", "\n").split("\n")
    out = []
    i, n = 0, len(lines)
    skip_print = False          # inside --- print-only ---
    list_type = None            # 'ul' | 'ol' | None

    def close_list():
        nonlocal list_type
        if list_type:
            out.append("</%s>" % list_type)
            list_type = None

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # ---- region markers ------------------------------------------------
        mk = re.match(r"^---\s*([a-z/-]+)\s*---\s*$", stripped)
        if mk:
            tag = mk.group(1)
            close_list()
            if tag == "print-only":
                skip_print = True
            elif tag == "/print-only":
                skip_print = False
            elif tag == "no-print" or tag == "/no-print":
                pass  # screen content: keep, marker itself dropped
            elif tag == "task":
                out.append('<div class="rpi-task">')
            elif tag == "/task":
                out.append('</div>')
            elif tag in ("hints", "hint"):
                out.append('<div class="rpi-hints">')
            elif tag in ("/hints", "/hint"):
                out.append('</div>')
            elif tag == "challenge":
                out.append('<div class="rpi-challenge"><div class="rpi-chip">Challenge</div>')
            elif tag == "/challenge":
                out.append('</div>')
            elif tag == "collapse":
                # next non-empty block is  --- \n title: X \n ---
                title = "More detail"
                j = i + 1
                buf = []
                while j < n and not re.match(r"^---\s*$", lines[j].strip()):
                    j += 1
                # lines[j] is the opening '---' of the front-matter-ish title
                k = j + 1
                while k < n and not re.match(r"^---\s*$", lines[k].strip()):
                    tt = re.match(r"^title:\s*(.+?)\s*$", lines[k].strip())
                    if tt:
                        title = tt.group(1).strip().strip('"\'')
                    k += 1
                out.append('<details class="rpi-collapse"><summary>%s</summary>'
                           % html.escape(title))
                i = k  # jump past the title front-matter close '---'
            elif tag == "/collapse":
                out.append('</details>')
            i += 1
            continue

        if skip_print:
            i += 1
            continue

        # ---- fenced code (```blocks3 / ```python / ```) --------------------
        mf = re.match(r"^```(\w*)\s*$", stripped)
        if mf:
            close_list()
            lang = mf.group(1) or "text"
            code_lines = []
            i += 1
            while i < n and not re.match(r"^```\s*$", lines[i].strip()):
                code_lines.append(lines[i])
                i += 1
            i += 1  # consume closing ```
            label = "Blocks" if lang.startswith("blocks") else lang
            out.append('<pre class="rpi-blocks" data-lang="%s"><span class="rpi-blabel">%s</span>%s</pre>'
                       % (html.escape(lang), html.escape(label),
                          html.escape("\n".join(code_lines))))
            continue

        # ---- includes  [[[ name ]]] ---------------------------------------
        mi = re.match(r"^\[\[\[\s*([a-z0-9-]+)\s*\]\]\]\s*$", stripped)
        if mi:
            close_list()
            repl = INCLUDES.get(mi.group(1))
            if repl:
                out.append('<p class="rpi-howto">%s</p>' % _inline(slug, repl))
            i += 1
            continue

        # ---- raw HTML lines (RPi's own <div>/<iframe>/<img>) : drop --------
        if stripped.startswith("<"):
            i += 1
            continue

        # ---- headings ------------------------------------------------------
        mh = re.match(r"^(#{2,4})\s+(.*)$", stripped)
        if mh:
            close_list()
            lvl = len(mh.group(1))
            tag = {2: "h3", 3: "h4", 4: "h5"}[lvl]
            out.append("<%s>%s</%s>" % (tag, _inline(slug, mh.group(2)), tag))
            i += 1
            continue

        # ---- horizontal rule / stray front-matter dashes -------------------
        if re.match(r"^---\s*$", stripped):
            i += 1
            continue

        # ---- lists ---------------------------------------------------------
        mul = re.match(r"^[-+*]\s+(.*)$", stripped)
        mol = re.match(r"^\d+[.)]\s+(.*)$", stripped)
        if mul or mol:
            want = "ul" if mul else "ol"
            if list_type != want:
                close_list()
                out.append("<%s>" % want)
                list_type = want
            item = (mul or mol).group(1)
            out.append("<li>%s</li>" % _inline(slug, item))
            i += 1
            continue

        # ---- blank line ----------------------------------------------------
        if stripped == "":
            close_list()
            i += 1
            continue

        # ---- paragraph -----------------------------------------------------
        close_list()
        out.append("<p>%s</p>" % _inline(slug, stripped))
        i += 1

    close_list()
    # tidy: drop empty task/hint wrappers
    htmlstr = "\n".join(out)
    htmlstr = re.sub(r'<div class="rpi-(task|hints)">\s*</div>', "", htmlstr)
    return htmlstr.strip()


def extract_embed_id(md):
    m = re.search(r"scratch\.mit\.edu/projects/embed/(\d+)", md)
    return m.group(1) if m else None


def extract_starter_id(md):
    """Find a ready-made STARTER project link (sprites placed, no solution
    code) so students can open Scratch already set up. Returns id or None."""
    # 1) a markdown link whose visible text mentions starter/template
    for m in re.finditer(r"\[([^\]]*)\]\((https://scratch\.mit\.edu/projects/(\d+)[^)]*)\)", md):
        text = m.group(1).lower()
        if "starter" in text or "template" in text:
            return m.group(3)
    # 2) the phrase 'starter project' near a plain projects/<id> link
    for m in re.finditer(r"starter project.{0,120}?scratch\.mit\.edu/projects/(\d+)", md, re.S | re.I):
        return m.group(1)
    for m in re.finditer(r"scratch\.mit\.edu/projects/(\d+).{0,60}?starter", md, re.S | re.I):
        return m.group(1)
    return None


def extract_intro(md):
    """Short human intro = first paragraph after the first '## What you will make'."""
    m = re.search(r"##\s*What you will make\s*\n+(.+)", md)
    if m:
        para = m.group(1).strip().splitlines()[0].strip()
        para = re.sub(r"\{:[^}]*\}", "", para)
        para = re.sub(r"\*\*([^*]+)\*\*", r"\1", para)
        return para
    return ""


# ---------------------------------------------------------------------------
# build one project
# ---------------------------------------------------------------------------
def build_project(slug, emoji, concept, difficulty, category):
    meta_txt, ok = fetch("%s/%s/%s/en/meta.yml" % (RAW, slug, BRANCH))
    if not ok:
        print("  ! meta missing for %s" % slug); return None
    meta = parse_meta(meta_txt)
    step_titles = meta["steps"] or []
    n_steps = len(step_titles) or 8

    steps, embed_id, starter_id, intro, is_scratch, full_md = [], None, None, "", False, []
    for idx in range(1, n_steps + 1):
        smd, ok = fetch("%s/%s/%s/en/step_%d.md" % (RAW, slug, BRANCH, idx))
        if not ok:
            break
        full_md.append(smd)
        if "```blocks3" in smd or "scratch.mit.edu" in smd or "block3" in smd:
            is_scratch = True
        if embed_id is None:
            embed_id = extract_embed_id(smd)
        if starter_id is None:
            starter_id = extract_starter_id(smd)
        if idx == 1 and not intro:
            intro = extract_intro(smd)
        title = step_titles[idx - 1] if idx - 1 < len(step_titles) else ("Step %d" % idx)
        steps.append({"n": idx, "title": title, "html": md_to_html(slug, smd)})
    # don't mistake the finished-project embed for a starter
    if starter_id and starter_id == embed_id:
        starter_id = None

    if not steps:
        print("  ! no steps for %s" % slug); return None
    if not is_scratch:
        print("  ! SKIP %s - not a Scratch project (no blocks3/scratch signals)" % slug)
        return None

    proj = {
        "id": slug,
        "slug": slug,
        "title": meta["title"] or slug.replace("-", " ").title(),
        "emoji": emoji,
        "concept": concept,
        "difficulty": difficulty,
        "difficultyLabel": DIFF_LABEL[difficulty],
        "category": category,
        "description": meta["description"] or intro,
        "intro": intro,
        "heroImage": _abs_img(slug, meta["hero_image"]) if meta["hero_image"] else "",
        "embedId": embed_id,
        "embedUrl": ("https://scratch.mit.edu/projects/embed/%s/?autostart=false" % embed_id) if embed_id else "",
        "projectUrl": ("https://scratch.mit.edu/projects/%s/" % embed_id) if embed_id else "",
        "starterId": starter_id,
        # Direct "open in Scratch" link. Prefer a ready-made starter (sprites,
        # no solution); else open the finished project's editor (see-inside);
        # else a blank editor.
        "openUrl": ("https://scratch.mit.edu/projects/%s/editor/" % starter_id) if starter_id
                   else (("https://scratch.mit.edu/projects/%s/editor/" % embed_id) if embed_id
                         else "https://scratch.mit.edu/projects/editor/"),
        "openMode": ("starter" if starter_id else ("seeinside" if embed_id else "blank")),
        "editorUrl": "https://scratch.mit.edu/projects/editor/",
        "sourceUrl": meta["original_url"] or ("https://github.com/raspberrypilearning/%s" % slug),
        "githubUrl": "https://github.com/raspberrypilearning/%s" % slug,
        "stepCount": len(steps),
        "steps": steps,
    }
    print("  + %-22s %2d steps  embed=%s  open=%s(%s)"
          % (slug, len(steps), embed_id, proj["openMode"], starter_id or embed_id or "blank"))
    return proj


def build():
    paths_out, projects, count = [], {}, 0
    for path in PATHS:
        print("Path: %s" % path["title"])
        ids = []
        for (slug, emoji, concept, diff, cat) in path["projects"]:
            proj = build_project(slug, emoji, concept, diff, cat)
            if proj:
                projects[slug] = proj
                ids.append(slug)
                count += 1
        paths_out.append({k: path[k] for k in ("id", "title", "emoji", "color", "blurb")}
                         | {"projects": ids})

    catalog = {
        "source": "Raspberry Pi Foundation / Code Club",
        "license": "CC BY-SA 4.0",
        "licenseUrl": "https://creativecommons.org/licenses/by-sa/4.0/",
        "paths": paths_out,
        "projects": projects,
    }

    js = ("/* AUTO-GENERATED by tools/import_rpi.py.\n"
          "   Content imported from the Raspberry Pi Foundation / Code Club\n"
          "   Scratch projects (https://github.com/raspberrypilearning),\n"
          "   licensed CC BY-SA 4.0. See ATTRIBUTION.md. Do not edit by hand. */\n"
          "window.GN_RPI = " + json.dumps(catalog, separators=(",", ":")) + ";\n")
    open(os.path.join(ROOT, "assets", "js", "rpi.js"), "w", encoding="utf-8").write(js)
    open(os.path.join(IMPORTED, "rpi_catalog.json"), "w", encoding="utf-8").write(
        json.dumps(catalog, indent=1, ensure_ascii=False))

    write_attribution(projects)
    print("\nImported %d projects across %d learning paths." % (count, len(paths_out)))
    print("Wrote assets/js/rpi.js, imported/rpi_catalog.json, ATTRIBUTION.md")


def write_attribution(projects):
    lines = [
        "# Attribution",
        "",
        "The **Real Project Library** in this platform imports open-source Scratch",
        "projects created and published by the **Raspberry Pi Foundation** and",
        "**Code Club**.",
        "",
        "These projects are licensed under a **Creative Commons",
        "Attribution-ShareAlike 4.0 International licence (CC BY-SA 4.0)**:",
        "<https://creativecommons.org/licenses/by-sa/4.0/>",
        "",
        "Source: <https://github.com/raspberrypilearning> and",
        "<https://projects.raspberrypi.org>.",
        "",
        "The instruction text and images are used and adapted under CC BY-SA 4.0.",
        "In keeping with the ShareAlike term, this imported material remains under",
        "CC BY-SA 4.0. \u201cRaspberry Pi\u201d is a trademark of the Raspberry Pi",
        "Foundation; this project is not endorsed by or affiliated with the",
        "Foundation.",
        "",
        "## Imported projects",
        "",
        "| Project | Source |",
        "| --- | --- |",
    ]
    for slug, p in sorted(projects.items()):
        lines.append("| %s | <https://github.com/raspberrypilearning/%s> |"
                     % (p["title"], slug))
    lines.append("")
    open(os.path.join(ROOT, "ATTRIBUTION.md"), "w", encoding="utf-8").write("\n".join(lines))


if __name__ == "__main__":
    build()
