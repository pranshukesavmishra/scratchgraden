#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rpi_starters.py — build a CODE-FREE STARTER for every imported project.

A student should open Scratch and find the sprites and backdrop already there,
ready to be programmed — but with NO block code, so nothing is given away.
Six of the imported projects ship their own starter; this generates one for the
other twenty-two.

How it decides which sprites a project needs:
  1. read every step of the project's instructions,
  2. pull out the sprite and backdrop names it tells the student to add
     ("Add the 'rocketship' sprite", "Add the 'Stars' backdrop", ...),
  3. match those against the real Scratch library (339 sprites, 85 backdrops),
  4. fall back to a sensible themed set if a project names nothing usable.

The result is written to starters/rpi/<slug>.sb3 with every sprite placed and
zero blocks, and is opened through the TurboWarp editor (which can load a
project by URL — scratch.mit.edu cannot).

Run: python3 tools/rpi_starters.py
"""
import os, re, sys, json, difflib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from game_engine import SPRITES, BACKDROPS, Factory, target_sprite, make_stage, write_project

OUT_DIR = os.path.join(ROOT, "starters", "rpi")
os.makedirs(OUT_DIR, exist_ok=True)

# Words that appear in quotes but are never sprites.
STOP = {"scratch", "stage", "code", "costumes", "sounds", "backdrop", "backdrops",
        "sprite", "sprites", "green flag", "when", "forever", "repeat", "if",
        "else", "wait", "say", "move", "turn", "go to", "glide", "hide", "show",
        "play", "stop", "score", "lives", "timer", "variable", "list", "my blocks",
        "run", "start", "left", "right", "up", "down", "space", "pen", "music"}

# Themed fallbacks when a project's text does not name library sprites.
FALLBACK = {
    "game":      (["Ball", "Star", "Bat"], "Blue Sky"),
    "animation": (["Cat", "Ballerina", "Star"], "Blue Sky"),
    "quiz":      (["Abby", "Star"], "Chalkboard"),
    "chatbot":   (["Robot", "Abby"], "Chalkboard"),
    "music":     (["Drum", "Guitar", "Keyboard"], "Concert"),
    "art":       (["Ball", "Star"], "Blue Sky"),
    "puzzle":    (["Ladybug1", "Star"], "Garden Rock"),
    "sandbox":   (["Cat", "Tree1", "Star"], "Blue Sky"),
}

# Names the projects use that differ from the library's naming.
ALIAS = {
    "rocketship": "Rocketship", "earth": "Earth", "ghost": "Ghost",
    "parrot": "Parrot", "bowl": "Bowl", "ball": "Ball", "bat": "Bat",
    "cat": "Cat", "dog": "Dog", "star": "Star", "balloon": "Balloon1",
    "butterfly": "Butterfly 2", "fish": "Fish", "crab": "Crab",
    "shark": "Shark", "monkey": "Monkey", "dinosaur": "Dinosaur1",
    "wizard": "Wizard", "witch": "Witch", "dragon": "Dragon",
    "drum": "Drum", "guitar": "Guitar", "keyboard": "Keyboard",
    "microphone": "Microphone", "saxophone": "Saxophone", "trumpet": "Trumpet",
    "robot": "Robot", "bus": "Bus", "car": "Convertible", "boat": "Sailboat",
    "arrow": "Arrow1", "apple": "Apple", "bananas": "Bananas",
    "goalie": "Goalie", "soccer ball": "Soccer Ball", "beachball": "Beachball",
    "octopus": "Octopus", "penguin": "Penguin 2", "bear": "Bear",
    "frog": "Frog", "bird": "Parrot", "hedgehog": "Hedgehog",
    "jellyfish": "Jellyfish", "starfish": "Starfish", "pufferfish": "Pufferfish",
    "spaceship": "Rocketship", "rocket": "Rocketship", "planet": "Earth",
    "target": "Ball", "arrow1": "Arrow1", "pencil": "Pencil", "paintbrush": "Paintbrush",
}

BACKDROP_ALIAS = {
    "stars": "Stars", "space": "Space", "night city": "Night City",
    "forest": "Forest", "underwater": "Underwater 1", "beach": "Beach Malibu",
    "castle": "Castle 1", "desert": "Desert", "jungle": "Jungle",
    "hill": "Hill", "blue sky": "Blue Sky", "farm": "Farm", "party": "Party",
    "concert": "Concert", "chalkboard": "Chalkboard", "arctic": "Arctic",
    "playing field": "Playing Field", "soccer": "Soccer", "school": "School",
    "spotlight": "Spotlight", "theater": "Theater", "urban": "Urban",
    "woods": "Woods", "garden": "Garden Rock", "moon": "Moon", "nebula": "Nebula",
}


def strip_html(md):
    md = re.sub(r"<[^>]+>", " ", md)
    md = re.sub(r"```.*?```", " ", md, flags=re.S)      # drop code blocks
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", md)        # drop images
    return md


def match_sprite(name):
    """Match a name from the instructions to a real library sprite."""
    n = name.strip().lower()
    if not n or n in STOP or len(n) < 3:
        return None
    if n in ALIAS and ALIAS[n] in SPRITES:
        return ALIAS[n]
    for key in SPRITES:                                   # exact, case-insensitive
        if key.lower() == n:
            return key
    close = difflib.get_close_matches(n, [k.lower() for k in SPRITES], n=1, cutoff=0.86)
    if close:
        for key in SPRITES:
            if key.lower() == close[0]:
                return key
    return None


def match_backdrop(name):
    n = name.strip().lower()
    if not n:
        return None
    if n in BACKDROP_ALIAS and BACKDROP_ALIAS[n] in BACKDROPS:
        return BACKDROP_ALIAS[n]
    for key in BACKDROPS:
        if key.lower() == n:
            return key
    close = difflib.get_close_matches(n, [k.lower() for k in BACKDROPS], n=1, cutoff=0.86)
    if close:
        for key in BACKDROPS:
            if key.lower() == close[0]:
                return key
    return None


# Library names that are really Scratch UI words, or the default cat the
# instructions tell you to DELETE — never what the project wants.
# Hard exclusions: Scratch UI words that happen to be library sprite names,
# plus the default cat that the instructions tell the student to DELETE.
NOISE = {"Green Flag", "Stop", "Key", "Line", "Cat", "Button1", "Button2",
         "Button3", "Block-X", "Glow-0", "Glow-1", "Glow-2"}
# "Keyboard" is a real instrument for music projects but is usually the word
# "keyboard" (the thing you type on) everywhere else.
MUSIC_ONLY = {"Keyboard", "Drum"}


# Hand-curated sets for projects whose instructions do not name their sprites
# clearly enough. Curation beats a bad guess.
OVERRIDES = {
    "archery":               (["Arrow1", "Ball", "Star"], "Blue Sky"),
    "binary-hero":           (["Drum", "Star", "Ball"], "Concert"),
    "brain-game":            (["Abby", "Star"], "Chalkboard"),
    "memory":                (["Ball", "Star", "Bat", "Apple"], "Blue Sky"),
    "clone-wars":            (["Rocketship", "Earth", "Star"], "Stars"),
    "create-your-own-world": (["Cat", "Tree1", "Star"], "Woods"),
    "synchronised-swimming": (["Cat Flying", "Star"], "Underwater 1"),
    "music-maker":           (["Guitar", "Keyboard", "Drum"], "Concert"),
    "paint-box":             (["Pencil", "Paintbrush"], "Blue Sky"),
    "butterfly-garden":      (["Butterfly 1", "Butterfly 2"], "Garden Rock"),
    "catch-the-dots":        (["Dot", "Star", "Ball"], "Blue Sky"),
    "boat-race":             (["Sailboat", "Shark", "Star"], "Underwater 1"),
    "ghostbusters":          (["Ghost", "Bat", "Star"], "Woods"),
    "balloons":              (["Balloon1", "Star", "Ball"], "Blue Sky"),
    "space-junk":            (["Earth", "Rocks", "Planet2"], "Stars"),
    "chatbot":               (["Robot", "Abby"], "Chalkboard"),
    "flappy-parrot":         (["Parrot", "Rocks", "Star"], "Blue Sky"),
}


def extract(project):
    """Work out which library sprites and backdrop a project actually needs.

    Scans the instructions for real library names (word-boundary, so 'ghost'
    finds Ghost), then scores each candidate: names mentioned near the word
    'sprite' or 'add' are far more likely to be what the student must add.
    """
    text = strip_html(" ".join(s.get("html", "") for s in project["steps"]))
    low = text.lower()

    cat = project.get("category", "game")
    scored = {}
    for name in SPRITES:
        if name in NOISE:
            continue
        if name in MUSIC_ONLY and cat != "music":
            continue
        n = name.lower()
        if len(n) < 3:
            continue
        hits = [m.start() for m in re.finditer(r"\b" + re.escape(n) + r"\b", low)]
        if not hits:
            continue
        score = len(hits)
        for pos in hits:                      # context boost
            near = low[max(0, pos - 70): pos + 70]
            if "sprite" in near or "add " in near:
                score += 4
                break
        if len(n.split()) > 1:                # distinctive multi-word names
            score += 2
        scored[name] = (score, hits[0])

    picked = [n for n, (sc, _) in sorted(scored.items(), key=lambda kv: (-kv[1][0], kv[1][1]))
              if sc > 0][:5]

    # backdrop: prefer one the text explicitly asks for
    backdrop = None
    for cand in re.findall(r"[Aa]dd (?:the |a |an )?['\"‘’“”]?([A-Za-z0-9 \-]{3,24}?)['\"‘’“”]?\s+backdrop", text):
        backdrop = match_backdrop(cand)
        if backdrop:
            break
    # Deliberately do NOT guess a backdrop from any stray matching word — that
    # produced nonsense like a desert for a boat race. Fall back to the theme.
    return picked, backdrop


def layout(n):
    """Sensible starting positions so sprites do not overlap."""
    spots = [(0, -60), (-140, 60), (140, 60), (-140, -120), (140, -120), (0, 110)]
    return spots[:max(1, n)]


def build_starter(slug, project):
    if slug in OVERRIDES:
        sprites, backdrop = OVERRIDES[slug]
        sprites = [s for s in sprites if s in SPRITES]
    else:
        sprites, backdrop = extract(project)
    cat = project.get("category", "game")
    if not sprites:
        sprites, fb = FALLBACK.get(cat, FALLBACK["game"])[0][:], FALLBACK.get(cat, FALLBACK["game"])[1]
        backdrop = backdrop or fb
    if not backdrop:
        backdrop = FALLBACK.get(cat, FALLBACK["game"])[1]
    if backdrop not in BACKDROPS:
        backdrop = "Blue Sky"

    pos = layout(len(sprites))
    targets = [make_stage(backdrop)]
    for i, name in enumerate(sprites):
        x, y = pos[i % len(pos)]
        f = Factory("s%d" % i)              # a factory with NO blocks added
        targets.append(target_sprite(name, name, x, y, 100, f, i + 1))

    out = os.path.join(OUT_DIR, slug + ".sb3")
    write_project(targets, [], out, agent="GradeNext starter (%s)" % slug)
    # sanity: a starter must contain no blocks at all
    for t in targets:
        if not t["isStage"] and t["blocks"]:
            raise AssertionError("starter %s has code in %s" % (slug, t["name"]))
    return sprites, backdrop


def build():
    cat_path = os.path.join(ROOT, "imported", "rpi_catalog.json")
    cat = json.load(open(cat_path, encoding="utf-8"))
    made = {}
    for slug, p in cat["projects"].items():
        if p.get("starterId"):
            continue                        # already has a real starter from RPi
        sprites, backdrop = build_starter(slug, p)
        made[slug] = {"sprites": sprites, "backdrop": backdrop}
        print("  + %-24s %-22s %s" % (slug, backdrop, ", ".join(sprites)))

    with open(os.path.join(ROOT, "imported", "rpi_starters.json"), "w", encoding="utf-8") as f:
        json.dump(made, f, indent=1, ensure_ascii=False)
    print("\nGenerated %d code-free starters in starters/rpi/." % len(made))
    return made


if __name__ == "__main__":
    build()
