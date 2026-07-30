#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate a Scratch 3 starter project (.sb3) for every session, pre-loaded with
the sprites relevant to that session's exercise/game, plus a themed backdrop
and a friendly "when green flag clicked -> say <task>" starter script.

Outputs:
  starters/<KEY>.sb3               one loadable Scratch project per session
  starters/manifest.json           metadata (title, sprites, backdrop) per key
  assets/js/starters-manifest.js   same metadata as window.GN_STARTERS (for the app)

Run:  python3 tools/generate_starters.py
The generated .sb3 files load in Scratch (scratch.mit.edu -> File -> Load from
your computer) and in any Scratch-compatible editor (e.g. TurboWarp).
"""
import os, json, hashlib, zipfile, io, sys, base64

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from svg_assets import SPRITES, BACKDROPS

STARTERS_DIR = os.path.join(ROOT, "starters")
os.makedirs(STARTERS_DIR, exist_ok=True)

# ----------------------------------------------------------------------------
# Sprite sets  (asset, display name, x, y, size)
# ----------------------------------------------------------------------------
S = lambda *a: list(a)
CATCH     = S(("Basket","Basket",0,-140,100), ("Apple","Apple",-60,150,80), ("Gem","Gem",90,150,70))
MAZE      = S(("Hero","Player",-200,150,45), ("Flag","Goal",200,-150,90), ("Coin","Coin",-10,-10,60))
WHACK     = S(("Creeper","Creeper",-90,-30,90), ("Creeper","Creeper2",110,-50,90), ("Villager","Villager",20,70,90))
FLAPPY    = S(("Bird","Bird",-120,20,90), ("Pipe","Pipe",150,-30,100), ("Coin","Coin",40,90,60))
PONG      = S(("Paddle","Paddle",0,-150,100), ("Ball","Ball",0,0,100), ("Brick","Brick1",-90,120,100), ("Brick","Brick2",0,120,100), ("Brick","Brick3",90,120,100))
PLATFORM  = S(("Hero","Player",-150,-40,80), ("Platform","Platform",0,-120,100), ("Coin","Coin",40,-40,60), ("Enemy","Enemy",130,-70,70), ("Flag","Goal",205,-40,90))
TOPDOWN   = S(("Hero","Hero",-40,0,80), ("Gem","Gem",120,80,70), ("Enemy","Enemy",-130,-70,80), ("Coin","Coin",70,-90,60))
SHOOTER   = S(("Ship","Ship",0,-140,90), ("Bullet","Bullet",0,-90,80), ("Alien","Alien1",-100,120,80), ("Alien","Alien2",0,120,80), ("Alien","Alien3",100,120,80))
RUNNER    = S(("Hero","Player",-150,-70,80), ("Spikes","Spikes",120,-120,90), ("Coin","Coin",40,-40,60))
CLICKER   = S(("Cookie","Cookie",0,10,120), ("Coin","Coin",165,120,70))
DANCE     = S(("Dancer1","Dancer1",-90,-30,100), ("Dancer2","Dancer2",90,-30,100))
LOOKS     = S(("Hero","Hero",-40,0,100), ("Star","Star",130,70,70))
INVENTORY = S(("Hero","Hero",-120,0,80), ("Gem","Gem",60,40,70), ("Apple","Apple",150,-20,70), ("Coin","Coin",150,90,60))
SENSING   = S(("Hero","Hero",-120,0,80), ("Apple","Apple",70,0,80), ("Flag","Goal",190,-60,90))
COLLECT   = S(("Hero","Player",-140,0,80), ("Coin","Coin1",30,20,60), ("Coin","Coin2",120,-50,60), ("Coin","Coin3",150,90,60))
SURVIVAL  = S(("Hero","Hero",-30,0,80), ("Enemy","Enemy1",120,-60,80), ("Enemy","Enemy2",150,70,80), ("Flag","Base",-190,-40,90))
SCORE     = S(("Hero","Player",-120,0,80), ("Coin","Coin",50,40,60), ("Star","Star",150,-40,70))
CELEBRATE = S(("Hero","Hero",-100,-30,80), ("Coin","Coin",50,40,60), ("Star","Star",160,-50,70), ("Enemy","Enemy",130,90,70))
EXPLORE   = S(("Hero","Hero",0,0,90), ("Coin","Coin",-140,60,60), ("Star","Star",150,80,70))
DEFAULT   = S(("Hero","Hero",0,0,100), ("Star","Star",140,80,70))

# ordered (keywords, set, backdrop). First keyword match wins.
RULES = [
    (["catch"], CATCH, "Sky"),
    (["maze"], MAZE, "Maze"),
    (["whack", "creeper"], WHACK, "Grass"),
    (["flappy"], FLAPPY, "Sky"),
    (["pong", "breakout", "brick bounce"], PONG, "Space"),
    (["platformer", "obby", "platform "], PLATFORM, "Sky"),
    (["top-down", "adventure", "zelda"], TOPDOWN, "Dungeon"),
    (["shooter", "galaga", "invader", "invasion", "blaster", "space "], SHOOTER, "Space"),
    (["clone", "particle", "swarm", "rain", "projectile"], SHOOTER, "Space"),
    (["runner", "subway", "geometry dash"], RUNNER, "Sky"),
    (["clicker", "tycoon", "cookie", "economy", "upgrade"], CLICKER, "Plain"),
    (["survival", "defense", "defence", "last stand", "tower"], SURVIVAL, "Grass"),
    (["dance", "dancing", "beat"], DANCE, "Stage"),
    (["inventory", "backpack"], INVENTORY, "Dungeon"),
    (["list", "quiz", "save", "data", "leaderboard", "high-score", "high score"], INVENTORY, "Dungeon"),
    (["collect", "coin"], COLLECT, "Sky"),
    (["variable", "score", "timer", "lives", "health", "difficulty"], SCORE, "Plain"),
    (["sensing", "collision", "if /", "boolean", "ask", "decision", "touch"], SENSING, "Plain"),
    (["menu", "sound", "juice", "feel", "multiplayer", "sharing", "persistent", "showcase", "graduation", "capstone"], CELEBRATE, "Sky"),
    (["custom block", "recursion", "function", "debug", "organis", "clean", "rebuild", "remaster", "pen", "pattern", "loop"], LOOKS, "Plain"),
    (["costume", "animation", "backdrop", "looks", "effect", "sprite", "postcard", "dialogue", "talking", "scene"], LOOKS, "Plain"),
    (["controller", "explorer", "character", "keyboard", "mouse", "roam"], EXPLORE, "Grass"),
    (["event", "broadcast", "timing", "control", "velocity", "gravity", "jump", "motion", "scroll"], EXPLORE, "Sky"),
]


def pick_spec(sess):
    text = " ".join([sess.get("module", ""), sess.get("title", ""),
                     sess.get("theme", ""), sess.get("projectTitle", "")]).lower()
    for keys, sset, bd in RULES:
        for k in keys:
            if k in text:
                return sset, bd
    return DEFAULT, "Plain"


# ----------------------------------------------------------------------------
# sb3 assembly
# ----------------------------------------------------------------------------
def md5_of(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def costume_entry(name, svg, cx, cy):
    m = md5_of(svg)
    return {
        "assetId": m, "name": name, "bitmapResolution": 1,
        "md5ext": m + ".svg", "dataFormat": "svg",
        "rotationCenterX": cx, "rotationCenterY": cy,
    }, (m + ".svg", svg)


def main_blocks(idx, task):
    p = "s%d" % idx
    return {
        p + "flag": {"opcode": "event_whenflagclicked", "next": p + "say", "parent": None,
                     "inputs": {}, "fields": {}, "shadow": False, "topLevel": True, "x": 60, "y": 60},
        p + "say": {"opcode": "looks_sayforsecs", "next": None, "parent": p + "flag",
                    "inputs": {"MESSAGE": [1, [10, task]], "SECS": [1, [4, "3"]]},
                    "fields": {}, "shadow": False, "topLevel": False},
    }


def build_project(sess):
    sprites, backdrop_name = pick_spec(sess)
    assets = {}   # md5ext -> svg (dedupe)
    targets = []

    # ----- Stage -----
    bd_svg = BACKDROPS.get(backdrop_name, BACKDROPS["Plain"])
    bd_cost, (bd_file, bd_data) = costume_entry("backdrop1", bd_svg, 240, 180)
    assets[bd_file] = bd_data
    targets.append({
        "isStage": True, "name": "Stage", "variables": {}, "lists": {}, "broadcasts": {},
        "blocks": {}, "comments": {}, "currentCostume": 0, "costumes": [bd_cost], "sounds": [],
        "volume": 100, "layerOrder": 0, "tempo": 60, "videoTransparency": 50,
        "videoState": "on", "textToSpeechLanguage": None,
    })

    # ----- Sprites -----
    task = ("Let's build: " + (sess.get("projectTitle") or sess.get("title") or "your project"))
    if len(task) > 60:
        task = task[:57] + "..."
    names_used = []
    for i, (asset, sname, x, y, size) in enumerate(sprites):
        svg, cx, cy = SPRITES[asset]
        cost, (afile, adata) = costume_entry(asset.lower(), svg, cx, cy)
        assets[afile] = adata
        blocks = main_blocks(i, task) if i == 0 else {}
        targets.append({
            "isStage": False, "name": sname, "variables": {}, "lists": {}, "broadcasts": {},
            "blocks": blocks, "comments": {}, "currentCostume": 0, "costumes": [cost], "sounds": [],
            "volume": 100, "layerOrder": i + 1, "visible": True,
            "x": x, "y": y, "size": size, "direction": 90,
            "draggable": False, "rotationStyle": "all around",
        })
        names_used.append(sname)

    project = {
        "targets": targets, "monitors": [], "extensions": [],
        "meta": {"semver": "3.0.0", "vm": "0.2.0",
                 "agent": "GradeNext Scratch Coding Academy starter generator"},
    }
    return project, assets, backdrop_name, names_used


def write_sb3(path, project, assets):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("project.json", json.dumps(project, separators=(",", ":")))
        for fname, data in assets.items():
            z.writestr(fname, data)
    raw = buf.getvalue()
    with open(path, "wb") as f:
        f.write(raw)
    return raw


def main():
    with open(os.path.join(HERE, "sessions.json"), encoding="utf-8") as f:
        sessions = json.load(f)

    manifest = {}
    b64data = {}
    total = 0
    for sess in sessions:
        key = sess["key"]
        project, assets, backdrop_name, names = build_project(sess)
        raw = write_sb3(os.path.join(STARTERS_DIR, key + ".sb3"), project, assets)
        total += len(raw)
        b64data[key] = base64.b64encode(raw).decode("ascii")
        manifest[key] = {
            "file": key + ".sb3",
            "title": sess.get("projectTitle") or sess.get("title"),
            "module": sess.get("module"),
            "backdrop": backdrop_name,
            "sprites": names,
        }

    with open(os.path.join(STARTERS_DIR, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1)

    js = ("/* AUTO-GENERATED by tools/generate_starters.py — do not edit by hand.\n"
          "   Maps each session key to its Scratch starter project metadata. */\n"
          "window.GN_STARTERS = " + json.dumps(manifest, separators=(",", ":")) + ";\n")
    with open(os.path.join(ROOT, "assets", "js", "starters-manifest.js"), "w", encoding="utf-8") as f:
        f.write(js)

    # embedded base64 of every .sb3 so downloads work with no server / single-file build
    jsdata = ("/* AUTO-GENERATED by tools/generate_starters.py — do not edit by hand.\n"
              "   Base64 of each starter .sb3 so the Download button works offline,\n"
              "   from file://, and in the single-file standalone build. */\n"
              "window.GN_STARTERS_DATA = " + json.dumps(b64data, separators=(",", ":")) + ";\n")
    with open(os.path.join(ROOT, "assets", "js", "starters-data.js"), "w", encoding="utf-8") as f:
        f.write(jsdata)

    print("Generated %d starter .sb3 files (%.0f KB total, avg %.1f KB)."
          % (len(sessions), total / 1024, total / 1024 / len(sessions)))
    print("Wrote starters/manifest.json, assets/js/starters-manifest.js, assets/js/starters-data.js")


if __name__ == "__main__":
    main()
