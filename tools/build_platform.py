#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_platform.py — merge the curriculum spine, the teaching knowledge base and
both content pools into one file the web app consumes.

Produces a full LESSON PLAN for every one of the 100 sessions: a timed run
sheet, the tutor's teaching script, misconceptions, assessment questions,
differentiation, rubric and homework — bound to the real project or exercise
the child will build.

Outputs:
  assets/js/platform.js   -> window.GN_PLATFORM   (used by every page)
  imported/platform.json  -> same data, readable

Run: python3 tools/build_platform.py
"""
import os, sys, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from concepts import CONCEPTS, STRANDS
from spine import build_sessions, LEVELS
from blocks import BLOCKS, CATEGORIES, PLACEHOLDERS, resolve, USES
from questions import BANK
from deepdive import DEEP
from briefs import build_brief

SESSION_MINUTES = 60
TW_EDITOR = "https://turbowarp.org/editor?project_url="
SITE_BASE = os.environ.get("GN_SITE_BASE",
                           "https://pranshukesavmishra.github.io/scratchgraden/")
from urllib.parse import quote as _q
QUIZ_LENGTH = 10        # questions per Recall Test
QUIZ_PASS = 7           # marks needed to pass


def load(path, default=None):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        return default
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def run_sheet(concept, session, content):
    """A minute-by-minute plan a tutor can actually follow in a 60-min class."""
    build_label = content["title"] if content else "today's build"
    return [
        {"min": 5,  "phase": "Warm-up",   "icon": "\U0001F525",
         "what": "Hook and recall",
         "detail": concept["hook"],
         "note": "Also ask one recall question from last session."},
        {"min": 5,  "phase": "Objectives", "icon": "\U0001F3AF",
         "what": "Share what success looks like",
         "detail": "Read the 'I can' statements with the child so they know the target: "
                   + " ".join(concept["objectives"]),
         "note": "Introduce the key words: " + "; ".join(v.split(" — ")[0] for v in concept["vocab"]) + "."},
        {"min": 12, "phase": "I do",      "icon": "\U0001F468‍\U0001F3EB",
         "what": "Demonstrate the new blocks",
         "detail": "Share your screen and work through the teaching steps. Blocks introduced: "
                   + ", ".join("`%s`" % b for b in concept["blocks"]) + ".",
         "note": "Ask the child to PREDICT before you run anything."},
        {"min": 10, "phase": "We do",     "icon": "\U0001F91D",
         "what": "Build it together",
         "detail": "Child shares their screen and rebuilds what you demonstrated, with you prompting rather than telling.",
         "note": "Hands off the mouse — prompt with questions."},
        {"min": 20, "phase": "You do",    "icon": "\U0001F6E0️",
         "what": "Independent build — " + build_label,
         "detail": ("Open the exercise and let the child build it. Use the Desired Output to check the target, "
                    "and the hints only when they are genuinely stuck."),
         "note": "Let them struggle productively for 2 minutes before helping."},
        {"min": 5,  "phase": "Check",     "icon": "✅",
         "what": "Assess understanding",
         "detail": "Ask the check questions and note the rubric level reached.",
         "note": "Record the outcome in the progress tracker."},
        {"min": 3,  "phase": "Wrap",      "icon": "\U0001F3C1",
         "what": "Recap and set homework",
         "detail": "Child explains in their own words what they learned. Set: " + session["homework"],
         "note": "End on something they are proud of."},
    ]


def build():
    course = load("starters/course.json", {"sessions": [], "exercises": {}})
    rpi = load("imported/rpi_catalog.json", {"paths": [], "projects": {}})
    exercises = course.get("exercises", {})
    projects = rpi.get("projects", {})

    # group the MCQ bank by concept
    by_concept = {}
    for i, q in enumerate(BANK):
        by_concept.setdefault(q["concept"], []).append({
            "id": "q%d" % i, "stem": q["stem"], "options": q["options"],
            "correct": q["correct"], "why": q["why"]})

    sessions_out = {}
    order = []
    for s in build_sessions():
        c = CONCEPTS[s["conceptKey"]]
        kind, ref = s["contentKind"], s["contentRef"]

        content = None
        if kind == "project" and ref in projects:
            p = projects[ref]
            content = {
                "kind": "project", "ref": ref, "title": p["title"],
                "emoji": p["emoji"], "steps": p["stepCount"],
                "href": "projects.html#/p/" + ref,
                "studentOpen": p.get("studentOpen", ""), "studentMode": p.get("studentMode", "blank"),
                "tutorOpen": p.get("tutorOpen", ""),
                "openUrl": p.get("studentOpen", ""), "embedUrl": p.get("embedUrl", ""),
                "difficulty": p.get("difficultyLabel", ""),
                "source": "Raspberry Pi / Code Club",
            }
        elif kind == "exercise" and ref in exercises:
            e = exercises[ref]
            content = {
                "kind": "exercise", "ref": ref, "title": e["title"],
                "emoji": e.get("emoji", "\U0001F3AE"), "steps": len(e.get("hints", [])),
                "href": "exercise.html?ex=" + ref,
                # the code-free starter, straight into the TurboWarp editor
                "studentOpen": (TW_EDITOR + _q(SITE_BASE + e["starter"], safe="")) if e.get("desired") else "",
                "studentMode": "starter" if e.get("desired") else "",
                # the finished game (solution) — tutor only
                "tutorOpen": (TW_EDITOR + _q(SITE_BASE + e["desired"], safe="")) if e.get("desired") else "",
                "openUrl": "", "embedUrl": "",
                "difficulty": e.get("level", ""),
                "sprites": e.get("sprites", []),
                "source": "Grade Next",
                "brief": build_brief(e.get("template", "generic"), e["title"],
                                     e.get("sprites", []), e.get("backdrop", "")),
            }

        # resolve this session's blocks to full reference entries
        block_refs = []
        for label in c["blocks"]:
            if label in PLACEHOLDERS:
                continue
            key = resolve(label)
            if key and key not in [b["key"] for b in block_refs]:
                b = BLOCKS[key]
                block_refs.append({"key": key, "category": b["category"],
                                   "color": CATEGORIES[b["category"]]["color"],
                                   "what": b["what"], "example": b["example"], "tip": b["tip"],
                                   "uses": USES.get(key, [])})

        rec = {
            "id": s["id"], "level": s["level"], "n": s["n"], "title": s["title"],
            "conceptKey": s["conceptKey"], "concept": c["name"], "strand": c["strand"],
            "strandColor": STRANDS.get(c["strand"], "#64748b"),
            "blockRefs": block_refs,
            "deep": DEEP.get(s["conceptKey"]),
            "quizCount": min(QUIZ_LENGTH, len(by_concept.get(s["conceptKey"], []))),
            "blocks": c["blocks"], "vocab": c["vocab"], "objectives": c["objectives"],
            "hook": c["hook"], "teach": c["teach"], "watch": c["watch"], "ask": c["ask"],
            "support": c["support"], "stretch": c["stretch"], "rubric": c["rubric"],
            "homework": s["homework"], "minutes": SESSION_MINUTES,
            "content": content, "contentKind": kind,
            "runSheet": run_sheet(c, s, content),
        }
        sessions_out[s["id"]] = rec
        order.append(s["id"])

    levels_out = []
    for lv in LEVELS:
        ids = [i for i in order if sessions_out[i]["level"] == lv["level"]]
        levels_out.append({
            "level": lv["level"], "title": lv["title"], "blurb": lv["blurb"],
            "emoji": lv["emoji"], "color": lv["color"], "sessions": ids,
        })

    # skills map: strand -> the sessions that build it
    skills = {}
    for sid in order:
        s = sessions_out[sid]
        skills.setdefault(s["strand"], {"strand": s["strand"],
                                        "color": s["strandColor"], "sessions": []})
        skills[s["strand"]]["sessions"].append(sid)

    # block library for the Block Lab: every block, plus which session teaches it
    taught_in = {}
    for sid in order:
        for b in sessions_out[sid]["blockRefs"]:
            taught_in.setdefault(b["key"], []).append(sid)
    block_lib = {}
    for key, b in BLOCKS.items():
        block_lib[key] = {
            "key": key, "category": b["category"],
            "color": CATEGORIES[b["category"]]["color"],
            "what": b["what"], "example": b["example"], "tip": b["tip"],
            "uses": USES.get(key, []),
            "sessions": taught_in.get(key, []),
        }

    data = {
        "meta": {
            "name": "Grade Next Scratch Academy",
            "sessionCount": len(order),
            "levelCount": len(levels_out),
            "conceptCount": len(CONCEPTS),
            "projectCount": len(projects),
            "exerciseCount": len(exercises),
            "blockCount": len(block_lib),
            "questionCount": len(BANK),
            "useCount": sum(len(v) for v in USES.values()),
            "deepCount": len(DEEP),
            "minutes": SESSION_MINUTES,
            "quizLength": QUIZ_LENGTH,
            "quizPass": QUIZ_PASS,
        },
        "levels": levels_out,
        "sessions": sessions_out,
        "order": order,
        "skills": skills,
        "strands": STRANDS,
        "blocks": block_lib,
        "blockCategories": CATEGORIES,
        "questions": by_concept,
    }

    js = ("/* AUTO-GENERATED by tools/build_platform.py - do not edit by hand.\n"
          "   Curriculum spine + teaching knowledge base + content pools. */\n"
          "window.GN_PLATFORM = " + json.dumps(data, separators=(",", ":")) + ";\n")
    open(os.path.join(ROOT, "assets", "js", "platform.js"), "w", encoding="utf-8").write(js)
    open(os.path.join(ROOT, "imported", "platform.json"), "w", encoding="utf-8").write(
        json.dumps(data, indent=1, ensure_ascii=False))

    linked = sum(1 for i in order if sessions_out[i]["content"])
    thin = [i for i in order if sessions_out[i]["quizCount"] < QUIZ_LENGTH]
    print("Built %d sessions across %d levels." % (len(order), len(levels_out)))
    print("  %d concepts, %d sessions linked to real content (%d unlinked build sessions)."
          % (len(CONCEPTS), linked, len(order) - linked))
    print("  %d blocks documented, %d quiz questions (%d per Recall Test, pass %d)."
          % (len(block_lib), len(BANK), QUIZ_LENGTH, QUIZ_PASS))
    if thin:
        print("  ! sessions with fewer than %d questions: %s" % (QUIZ_LENGTH, thin[:5]))
    print("  strands: %s" % ", ".join("%s(%d)" % (k, len(v["sessions"])) for k, v in sorted(skills.items())))
    print("Wrote assets/js/platform.js and imported/platform.json")


if __name__ == "__main__":
    build()
