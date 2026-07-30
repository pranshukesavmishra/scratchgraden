#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a Scratch .sb3 starter that references the REAL Scratch sprite/backdrop
library by md5 (professional art). Assets are NOT bundled — Scratch / TurboWarp
fetch them from the Scratch asset servers when the project opens, so the file
stays tiny and the sprites look exactly like the real library.

This is the new starter engine (replaces the hand-drawn SVGs) once the sample
is approved. For now it builds one sample game.
"""
import json, io, zipfile, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SPRITES = {s["name"]: s for s in json.load(open(os.path.join(HERE, "scratch_sprites.json")))}
BACKDROPS = {b["name"]: b for b in json.load(open(os.path.join(HERE, "scratch_backdrops.json")))}


def costume_from(entry, name=None):
    """Turn a library costume/backdrop metadata entry into an sb3 costume dict."""
    c = {
        "assetId": entry["assetId"],
        "name": name or entry["name"],
        "bitmapResolution": entry.get("bitmapResolution", 1),
        "md5ext": entry["md5ext"],
        "dataFormat": entry["dataFormat"],
        "rotationCenterX": entry["rotationCenterX"],
        "rotationCenterY": entry["rotationCenterY"],
    }
    return c


def player_blocks(task):
    return {
        "hat": {"opcode": "event_whenflagclicked", "next": "say", "parent": None,
                "inputs": {}, "fields": {}, "shadow": False, "topLevel": True, "x": 40, "y": 40},
        "say": {"opcode": "looks_sayforsecs", "next": None, "parent": "hat",
                "inputs": {"MESSAGE": [1, [10, task]], "SECS": [1, [4, "3"]]},
                "fields": {}, "shadow": False, "topLevel": False},
    }


def build(spec, out_path):
    targets = []
    # ---- Stage / backdrop ----
    bd = BACKDROPS[spec["backdrop"]]
    targets.append({
        "isStage": True, "name": "Stage", "variables": {}, "lists": {}, "broadcasts": {},
        "blocks": {}, "comments": {}, "currentCostume": 0,
        "costumes": [costume_from(bd, spec["backdrop"])], "sounds": [],
        "volume": 100, "layerOrder": 0, "tempo": 60, "videoTransparency": 50,
        "videoState": "on", "textToSpeechLanguage": None,
    })
    # ---- Sprites (all costumes referenced by md5, unbundled) ----
    for i, sp in enumerate(spec["sprites"]):
        lib = SPRITES[sp["lib"]]
        costumes = [costume_from(c) for c in lib["costumes"]]
        blocks = player_blocks(spec["task"]) if sp.get("player") else {}
        targets.append({
            "isStage": False, "name": sp["name"], "variables": {}, "lists": {},
            "broadcasts": {}, "blocks": blocks, "comments": {}, "currentCostume": 0,
            "costumes": costumes, "sounds": [], "volume": 100, "layerOrder": i + 1,
            "visible": True, "x": sp["x"], "y": sp["y"], "size": sp["size"], "direction": 90,
            "draggable": False, "rotationStyle": "all around",
        })
    project = {"targets": targets, "monitors": [], "extensions": [],
               "meta": {"semver": "3.0.0", "vm": "0.2.0", "agent": "GradeNext starter (library art)"}}

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("project.json", json.dumps(project, separators=(",", ":")))
    open(out_path, "wb").write(buf.getvalue())
    return len(buf.getvalue()), [t["name"] for t in targets]


SAMPLE = {
    "title": "Dragon's Keep",
    "backdrop": "Castle 3",
    "task": "Grab all 3 crystals, dodge the ghost, and reach the Dragon!",
    "sprites": [
        {"lib": "Crystal", "name": "Crystal1", "x": -70, "y": -120, "size": 55},
        {"lib": "Crystal", "name": "Crystal2", "x": 70, "y": 10, "size": 55},
        {"lib": "Crystal", "name": "Crystal3", "x": 165, "y": -120, "size": 55},
        {"lib": "Ghost", "name": "Ghost", "x": 0, "y": 90, "size": 70},
        {"lib": "Dragon", "name": "Dragon", "x": 185, "y": 70, "size": 80},
        {"lib": "Wizard", "name": "Wizard", "x": -195, "y": -70, "size": 75, "player": True},
    ],
}

if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "starters"), exist_ok=True)
    out = os.path.join(ROOT, "starters", "SAMPLE-dragons-keep.sb3")
    size, names = build(SAMPLE, out)
    print("Built %s (%d bytes)" % (out, size))
    print("Targets:", names)
