#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a FINISHED, playable Scratch example (the "desired output") for the
sample game, using the real Scratch library art (referenced by md5). Students
open this to see the goal and can look inside to predict how it's coded.

Keeps the game logic deliberately simple/standard (top-down move + collect +
respawn + win) so it is robust. Structure is validated with scratch-parser.
"""
import json, io, zipfile, os, itertools

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SPRITES = {s["name"]: s for s in json.load(open(os.path.join(HERE, "scratch_sprites.json")))}
BACKDROPS = {b["name"]: b for b in json.load(open(os.path.join(HERE, "scratch_backdrops.json")))}

SCORE_ID = "scoreVar1234567890ab"

def costume_from(entry, name=None):
    return {"assetId": entry["assetId"], "name": name or entry["name"],
            "bitmapResolution": entry.get("bitmapResolution", 1), "md5ext": entry["md5ext"],
            "dataFormat": entry["dataFormat"], "rotationCenterX": entry["rotationCenterX"],
            "rotationCenterY": entry["rotationCenterY"]}

# ---- input helpers ----
def num(v):  return [1, [4, str(v)]]
def ang(v):  return [1, [8, str(v)]]
def pos(v):  return [1, [5, str(v)]]
def txt(v):  return [1, [10, str(v)]]
def rvar():  return [3, [12, "score", SCORE_ID], [10, ""]]

class Factory:
    def __init__(self, prefix):
        self.blocks = {}
        self.counter = itertools.count(1)
        self.prefix = prefix
    def nid(self):
        return "%s%d" % (self.prefix, next(self.counter))
    def add(self, opcode, inputs=None, fields=None, mutation=None, shadow=False, top=False):
        bid = self.nid()
        b = {"opcode": opcode, "next": None, "parent": None,
             "inputs": inputs or {}, "fields": fields or {},
             "shadow": shadow, "topLevel": top}
        if top:
            b["x"] = 40; b["y"] = 40
        if mutation:
            b["mutation"] = mutation
        self.blocks[bid] = b
        return bid
    def menu(self, opcode, field, value):
        return self.add(opcode, fields={field: [value, None]}, shadow=True)
    def stack(self, specs, top=True):
        """specs: list of dicts {op, inputs, fields, mutation, substack:[...]}. Links next/parent."""
        first = None
        prev = None
        for i, s in enumerate(specs):
            bid = self.add(s["op"], dict(s.get("inputs", {})), dict(s.get("fields", {})),
                           s.get("mutation"), top=(top and i == 0))
            if s.get("substack"):
                sub_first = self.stack(s["substack"], top=False)
                self.blocks[bid]["inputs"]["SUBSTACK"] = [2, sub_first]
                self._reparent(sub_first, bid)
            if first is None:
                first = bid
            if prev is not None:
                self.blocks[prev]["next"] = bid
                self.blocks[bid]["parent"] = prev
            prev = bid
        return first
    def _reparent(self, child, parent):
        self.blocks[child]["parent"] = parent
    def link_menu(self, host_id, input_name, menu_id):
        self.blocks[host_id]["inputs"][input_name] = [1, menu_id]
        self.blocks[menu_id]["parent"] = host_id
    def cond(self, bool_id):
        return [2, bool_id]

def key_if(f, key, dx=None, dy=None):
    """if <key pressed> then change x/y"""
    menu = f.menu("sensing_keyoptions", "KEY_OPTION", key)
    cond = f.add("sensing_keypressed", inputs={"KEY_OPTION": [1, menu]})
    f.blocks[menu]["parent"] = cond
    inner = []
    if dx is not None:
        inner.append({"op": "motion_changexby", "inputs": {"DX": num(dx)}})
    if dy is not None:
        inner.append({"op": "motion_changeyby", "inputs": {"DY": num(dy)}})
    return {"op": "control_if", "inputs": {"CONDITION": [2, cond]}, "substack": inner}, cond

def touching(f, sprite):
    menu = f.menu("sensing_touchingobjectmenu", "TOUCHINGOBJECTMENU", sprite)
    b = f.add("sensing_touchingobject", inputs={"TOUCHINGOBJECTMENU": [1, menu]})
    f.blocks[menu]["parent"] = b
    return b

# ---------------- Build the four sprites' scripts ----------------
def wizard_blocks():
    f = Factory("w")
    # movement ifs
    if_r, _ = key_if(f, "right arrow", dx=5)
    if_l, _ = key_if(f, "left arrow", dx=-5)
    if_u, _ = key_if(f, "up arrow", dy=5)
    if_d, _ = key_if(f, "down arrow", dy=-5)
    ghost_cond = touching(f, "Ghost")
    if_ghost = {"op": "control_if", "inputs": {"CONDITION": [2, ghost_cond]},
                "substack": [{"op": "motion_gotoxy", "inputs": {"X": num(-195), "Y": num(-70)}}]}
    forever = {"op": "control_forever", "substack": [if_r, if_l, if_u, if_d, if_ghost]}
    f.stack([
        {"op": "event_whenflagclicked"},
        {"op": "data_setvariableto", "inputs": {"VALUE": txt("0")}, "fields": {"VARIABLE": ["score", SCORE_ID]}},
        {"op": "motion_gotoxy", "inputs": {"X": num(-195), "Y": num(-70)}},
        {"op": "motion_pointindirection", "inputs": {"DIRECTION": ang(90)}},
        forever,
    ])
    return f.blocks

def crystal_blocks():
    f = Factory("c")
    tw = touching(f, "Wizard")
    collect = {"op": "control_if", "inputs": {"CONDITION": [2, tw]}, "substack": [
        {"op": "data_changevariableby", "inputs": {"VALUE": txt("1")}, "fields": {"VARIABLE": ["score", SCORE_ID]}},
        {"op": "looks_hide"},
        {"op": "control_stop", "fields": {"STOP_OPTION": ["this script", None]},
         "mutation": {"tagName": "mutation", "children": [], "hasnext": "false"}},
    ]}
    f.stack([
        {"op": "event_whenflagclicked"},
        {"op": "looks_show"},
        {"op": "control_forever", "substack": [collect]},
    ])
    return f.blocks

def ghost_blocks2(x, y):
    f = Factory("g")
    # chase: forever [ point towards Wizard -> move 2 ]
    menu = f.menu("motion_pointtowards_menu", "TOWARDS", "Wizard")
    f.stack([
        {"op": "event_whenflagclicked"},
        {"op": "motion_gotoxy", "inputs": {"X": num(x), "Y": num(y)}},
        {"op": "control_forever", "substack": [
            {"op": "motion_pointtowards", "inputs": {"TOWARDS": [1, menu]}},
            {"op": "motion_movesteps", "inputs": {"STEPS": num(2)}},
        ]},
    ])
    # animation script (separate top-level)
    f.stack([
        {"op": "event_whenflagclicked"},
        {"op": "control_forever", "substack": [
            {"op": "looks_nextcostume"},
            {"op": "control_wait", "inputs": {"DURATION": pos("0.25")}},
        ]},
    ], top=True)
    return f.blocks

def dragon_blocks(x, y):
    f = Factory("d")
    eq = f.add("operator_equals", inputs={"OPERAND1": rvar(), "OPERAND2": txt("3")})
    win_if = {"op": "control_if", "inputs": {"CONDITION": [2, eq]}, "substack": [
        {"op": "looks_sayforsecs", "inputs": {"MESSAGE": txt("You collected all 3 crystals — YOU WIN!"), "SECS": num(4)}},
        {"op": "control_stop", "fields": {"STOP_OPTION": ["all", None]},
         "mutation": {"tagName": "mutation", "children": [], "hasnext": "false"}},
    ]}
    f.stack([
        {"op": "event_whenflagclicked"},
        {"op": "motion_gotoxy", "inputs": {"X": num(x), "Y": num(y)}},
        {"op": "control_forever", "substack": [win_if]},
    ])
    # animation
    f.stack([
        {"op": "event_whenflagclicked"},
        {"op": "control_forever", "substack": [
            {"op": "looks_nextcostume"},
            {"op": "control_wait", "inputs": {"DURATION": pos("0.35")}},
        ]},
    ], top=True)
    return f.blocks

def fix_parents(blocks):
    """Ensure every block referenced inside another block's inputs (conditions,
    menus, reporters, substack first-child) has its parent set correctly."""
    for bid, b in blocks.items():
        for inp, val in b.get("inputs", {}).items():
            if not isinstance(val, list):
                continue
            for slot in val[1:]:
                if isinstance(slot, str) and slot in blocks:
                    blocks[slot]["parent"] = bid
    return blocks

def target(name, lib, x, y, size, blocks, layer):
    fix_parents(blocks)
    costumes = [costume_from(c) for c in SPRITES[lib]["costumes"]]
    return {"isStage": False, "name": name, "variables": {}, "lists": {}, "broadcasts": {},
            "blocks": blocks, "comments": {}, "currentCostume": 0, "costumes": costumes, "sounds": [],
            "volume": 100, "layerOrder": layer, "visible": True, "x": x, "y": y, "size": size,
            "direction": 90, "draggable": False, "rotationStyle": "all around"}

def build(out):
    bd = BACKDROPS["Castle 3"]
    stage = {"isStage": True, "name": "Stage",
             "variables": {SCORE_ID: ["score", 0]}, "lists": {}, "broadcasts": {},
             "blocks": {}, "comments": {}, "currentCostume": 0,
             "costumes": [costume_from(bd, "Castle 3")], "sounds": [], "volume": 100,
             "layerOrder": 0, "tempo": 60, "videoTransparency": 50, "videoState": "on",
             "textToSpeechLanguage": None}
    targets = [stage,
               target("Crystal1", "Crystal", -70, -120, 55, crystal_blocks(), 1),
               target("Crystal2", "Crystal", 70, 10, 55, crystal_blocks(), 2),
               target("Crystal3", "Crystal", 165, -120, 55, crystal_blocks(), 3),
               target("Ghost", "Ghost", 0, 90, 70, ghost_blocks2(0, 90), 4),
               target("Dragon", "Dragon", 185, 70, 80, dragon_blocks(185, 70), 5),
               target("Wizard", "Wizard", -195, -70, 75, wizard_blocks(), 6)]
    monitors = [{"id": SCORE_ID, "mode": "default", "opcode": "data_variable",
                 "params": {"VARIABLE": "score"}, "spriteName": None, "value": 0,
                 "width": 0, "height": 0, "x": 5, "y": 5, "visible": True,
                 "sliderMin": 0, "sliderMax": 100, "isDiscrete": True}]
    project = {"targets": targets, "monitors": monitors, "extensions": [],
               "meta": {"semver": "3.0.0", "vm": "0.2.0", "agent": "GradeNext finished example"}}
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("project.json", json.dumps(project, separators=(",", ":")))
    open(out, "wb").write(buf.getvalue())
    return len(buf.getvalue())

if __name__ == "__main__":
    out = os.path.join(ROOT, "starters", "SAMPLE-dragons-keep-FINISHED.sb3")
    print("Built", out, build(out), "bytes")
