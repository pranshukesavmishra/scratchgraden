#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
game_engine.py — a small, verified Scratch-3 (.sb3) code generator.

It builds real, playable Scratch projects using the REAL Scratch sprite/backdrop
library (referenced by md5, so Scratch/TurboWarp fetch the professional art).
Every project is auto-verified three ways before it is written:
  1. block wiring (next/parent/input references all resolve)
  2. opcode input/field names match the Scratch spec
  3. (callers may also run scratch-parser, the official validator)

Used to produce the "desired output" finished games and the starters.
"""
import json, os, io, zipfile, itertools, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SPRITES = {s["name"]: s for s in json.load(open(os.path.join(HERE, "scratch_sprites.json")))}
BACKDROPS = {b["name"]: b for b in json.load(open(os.path.join(HERE, "scratch_backdrops.json")))}

# ---------------------------------------------------------------- library art
def costume_from(entry, name=None):
    return {"assetId": entry["assetId"], "name": name or entry["name"],
            "bitmapResolution": entry.get("bitmapResolution", 1), "md5ext": entry["md5ext"],
            "dataFormat": entry["dataFormat"], "rotationCenterX": entry["rotationCenterX"],
            "rotationCenterY": entry["rotationCenterY"]}

def sprite_costumes(lib):
    return [costume_from(c) for c in SPRITES[lib]["costumes"]]

def backdrop_costume(name):
    return costume_from(BACKDROPS[name], name)

# ---------------------------------------------------------------- input encoders
def num(v):  return [1, [4, str(v)]]
def pos(v):  return [1, [5, str(v)]]
def ang(v):  return [1, [8, str(v)]]
def txt(v):  return [1, [10, str(v)]]

# ---------------------------------------------------------------- block factory
class Factory:
    def __init__(self, prefix, var_index=None):
        self.blocks = {}
        self.c = itertools.count(1)
        self.prefix = prefix
        self.vars = var_index or {}   # name -> id
    def nid(self):
        return "%s%d" % (self.prefix, next(self.c))
    def add(self, opcode, inputs=None, fields=None, mutation=None, shadow=False):
        bid = self.nid()
        b = {"opcode": opcode, "next": None, "parent": None,
             "inputs": inputs or {}, "fields": fields or {}, "shadow": shadow, "topLevel": False}
        if mutation: b["mutation"] = mutation
        self.blocks[bid] = b
        return bid
    # ---- reporters / booleans (return a block id to embed in inputs) ----
    def var_ref(self, name):
        return [12, name, self.vars[name]]
    def rvar(self, name):
        return [3, self.var_ref(name), [10, ""]]
    def touching(self, sprite):
        menu = self.add("sensing_touchingobjectmenu", fields={"TOUCHINGOBJECTMENU": [sprite, None]}, shadow=True)
        return self.add("sensing_touchingobject", inputs={"TOUCHINGOBJECTMENU": [1, menu]})
    def touching_color(self, hexcolor):
        return self.add("sensing_touchingcolor", inputs={"COLOR": [1, [9, hexcolor]]})
    def key_pressed(self, key):
        menu = self.add("sensing_keyoptions", fields={"KEY_OPTION": [key, None]}, shadow=True)
        return self.add("sensing_keypressed", inputs={"KEY_OPTION": [1, menu]})
    def mouse_down(self):
        return self.add("sensing_mousedown")
    def equals(self, a, b):
        return self.add("operator_equals", inputs={"OPERAND1": a, "OPERAND2": b})
    def gt(self, a, b):
        return self.add("operator_gt", inputs={"OPERAND1": a, "OPERAND2": b})
    def lt(self, a, b):
        return self.add("operator_lt", inputs={"OPERAND1": a, "OPERAND2": b})
    def and_(self, a, b):
        return self.add("operator_and", inputs={"OPERAND1": [2, a], "OPERAND2": [2, b]})
    def random(self, a, b):
        return self.add("operator_random", inputs={"FROM": num(a), "TO": num(b)})
    def answer(self):
        return self.add("sensing_answer")
    def mousex(self):
        return self.add("sensing_mousex")
    def xpos(self):
        return self.add("motion_xposition")
    def ypos(self):
        return self.add("motion_yposition")
    def direction(self):
        return self.add("motion_direction")
    def minus(self, a, b):
        return self.add("operator_subtract", inputs={"NUM1": a, "NUM2": b})
    def plus(self, a, b):
        return self.add("operator_add", inputs={"NUM1": a, "NUM2": b})
    def times(self, a, b):
        return self.add("operator_multiply", inputs={"NUM1": a, "NUM2": b})
    def mousey(self):
        return self.add("sensing_mousey")
    def timer(self):
        return self.add("sensing_timer")
    def not_(self, a):
        return self.add("operator_not", inputs={"OPERAND": [2, a]})
    def or_(self, a, b):
        return self.add("operator_or", inputs={"OPERAND1": [2, a], "OPERAND2": [2, b]})
    def join(self, a, b):
        return self.add("operator_join", inputs={"STRING1": a, "STRING2": b})
    def reporter_input(self, block_id, shadow=None):
        """wrap a reporter block id for use in an input slot"""
        return [3, block_id, shadow or [4, "0"]]
    # ---- stack builder (DSL) ----
    def stack(self, specs, top=True, x=40, y=40):
        first = prev = None
        for i, s in enumerate(specs):
            bid = self.add(s["op"], dict(s.get("inputs", {})), dict(s.get("fields", {})), s.get("mutation"))
            b = self.blocks[bid]
            if top and i == 0:
                b["topLevel"] = True; b["x"] = x; b["y"] = y
            if "substack" in s and s["substack"]:
                sub = self.stack(s["substack"], top=False)
                b["inputs"]["SUBSTACK"] = [2, sub]
            if "substack2" in s and s["substack2"]:
                sub2 = self.stack(s["substack2"], top=False)
                b["inputs"]["SUBSTACK2"] = [2, sub2]
            if first is None: first = bid
            if prev is not None:
                self.blocks[prev]["next"] = bid
            prev = bid
        return first

# ---- statement shorthands (return DSL dicts) ----
def whenflag(): return {"op": "event_whenflagclicked"}
def whenclicked(): return {"op": "event_whenthisspriteclicked"}
def whenkey(key): return {"op": "event_whenkeypressed", "fields": {"KEY_OPTION": [key, None]}}
def whenclone(): return {"op": "control_start_as_clone"}
def whenreceive(msg, mid): return {"op": "event_whenbroadcastreceived", "fields": {"BROADCAST_OPTION": [msg, mid]}}
def setvar(name, val, vid): return {"op": "data_setvariableto", "inputs": {"VALUE": txt(val)}, "fields": {"VARIABLE": [name, vid]}}
def changevar(name, val, vid): return {"op": "data_changevariableby", "inputs": {"VALUE": txt(val)}, "fields": {"VARIABLE": [name, vid]}}
def gotoxy(x, y): return {"op": "motion_gotoxy", "inputs": {"X": num(x), "Y": num(y)}}
def glidexy(sec, x, y): return {"op": "motion_glidesecstoxy", "inputs": {"SECS": num(sec), "X": num(x), "Y": num(y)}}
def changex(v): return {"op": "motion_changexby", "inputs": {"DX": num(v)}}
def changey(v): return {"op": "motion_changeyby", "inputs": {"DY": num(v)}}
def setx(v): return {"op": "motion_setx", "inputs": {"X": num(v)}}
def sety(v): return {"op": "motion_sety", "inputs": {"Y": num(v)}}
def pointdir(v): return {"op": "motion_pointindirection", "inputs": {"DIRECTION": ang(v)}}
def move(v): return {"op": "motion_movesteps", "inputs": {"STEPS": num(v)}}
def bounce(): return {"op": "motion_ifonedgebounce"}
def show(): return {"op": "looks_show"}
def hide(): return {"op": "looks_hide"}
def sayfor(msg, sec): return {"op": "looks_sayforsecs", "inputs": {"MESSAGE": txt(msg), "SECS": num(sec)}}
def say(msg): return {"op": "looks_say", "inputs": {"MESSAGE": txt(msg)}}
def nextcostume(): return {"op": "looks_nextcostume"}
def changesize(v): return {"op": "looks_changesizeby", "inputs": {"CHANGE": num(v)}}
def setsize(v): return {"op": "looks_setsizeto", "inputs": {"SIZE": num(v)}}
def switchbackdrop(name): return {"op": "looks_switchbackdropto", "inputs": {"BACKDROP": [1, ("__bd__", name)]}}  # patched in builder
def wait(sec): return {"op": "control_wait", "inputs": {"DURATION": pos(sec)}}
def forever(sub): return {"op": "control_forever", "substack": sub}
def repeat(n, sub): return {"op": "control_repeat", "inputs": {"TIMES": num(n)}, "substack": sub}
def if_(cond_id, sub): return {"op": "control_if", "inputs": {"CONDITION": [2, cond_id]}, "substack": sub}
def ifelse(cond_id, sub, sub2): return {"op": "control_if_else", "inputs": {"CONDITION": [2, cond_id]}, "substack": sub, "substack2": sub2}
def waituntil(cond_id): return {"op": "control_wait_until", "inputs": {"CONDITION": [2, cond_id]}}
def stop(opt): return {"op": "control_stop", "fields": {"STOP_OPTION": [opt, None]},
                       "mutation": {"tagName": "mutation", "children": [], "hasnext": "false" if opt != "other scripts in sprite" else "true"}}
def createclone_self(): return {"op": "control_create_clone_of", "inputs": {"CLONE_OPTION": [1, ("__clonemenu__",)]}}
def deleteclone(): return {"op": "control_delete_this_clone"}
def pointtowards(sprite): return {"op": "motion_pointtowards", "inputs": {"TOWARDS": [1, ("__ptmenu__", sprite)]}}
def askandwait(q): return {"op": "sensing_askandwait", "inputs": {"QUESTION": txt(q)}}
def broadcast(msg, mid): return {"op": "event_broadcast", "inputs": {"BROADCAST_INPUT": [1, [11, msg, mid]]}}
def turnright(d): return {"op": "motion_turnright", "inputs": {"DEGREES": num(d)}}
def turnleft(d): return {"op": "motion_turnleft", "inputs": {"DEGREES": num(d)}}
def bounce(): return {"op": "motion_ifonedgebounce"}
def goto_sprite(sprite): return {"op": "motion_goto", "inputs": {"TO": [1, ("__gotomenu__", sprite)]}}
def repeatuntil(cond_id, sub): return {"op": "control_repeat_until", "inputs": {"CONDITION": [2, cond_id]}, "substack": sub}

# ---------------------------------------------------------------- post-processing
def _patch_menus(f):
    """Replace placeholder menu tuples with real shadow menu blocks."""
    for bid, b in list(f.blocks.items()):
        for inp, val in list(b["inputs"].items()):
            if isinstance(val, list) and len(val) >= 2 and isinstance(val[1], tuple):
                tag = val[1][0]
                if tag == "__ptmenu__":
                    m = f.add("motion_pointtowards_menu", fields={"TOWARDS": [val[1][1], None]}, shadow=True)
                elif tag == "__clonemenu__":
                    m = f.add("control_create_clone_of_menu", fields={"CLONE_OPTION": ["_myself_", None]}, shadow=True)
                elif tag == "__bd__":
                    m = f.add("looks_backdrops", fields={"BACKDROP": [val[1][1], None]}, shadow=True)
                elif tag == "__gotomenu__":
                    m = f.add("motion_goto_menu", fields={"TO": [val[1][1], None]}, shadow=True)
                else:
                    continue
                b["inputs"][inp] = [1, m]

def fix_parents(blocks):
    for bid, b in blocks.items():
        for inp, val in b.get("inputs", {}).items():
            if not isinstance(val, list): continue
            for slot in val[1:]:
                if isinstance(slot, str) and slot in blocks:
                    blocks[slot]["parent"] = bid
        nxt = b.get("next")
        if nxt and nxt in blocks:
            blocks[nxt]["parent"] = bid
    # top-level chain parents (first block parent stays None)
    return blocks

# ---------------------------------------------------------------- verification
OPSPEC = {
 "event_whenflagclicked":(set(),set()),"event_whenthisspriteclicked":(set(),set()),
 "event_whenkeypressed":(set(),{"KEY_OPTION"}),"control_start_as_clone":(set(),set()),
 "event_whenbroadcastreceived":(set(),{"BROADCAST_OPTION"}),
 "event_broadcast":({"BROADCAST_INPUT"},set()),
 "data_setvariableto":({"VALUE"},{"VARIABLE"}),"data_changevariableby":({"VALUE"},{"VARIABLE"}),
 "motion_gotoxy":({"X","Y"},set()),"motion_glidesecstoxy":({"SECS","X","Y"},set()),
 "motion_changexby":({"DX"},set()),"motion_changeyby":({"DY"},set()),
 "motion_setx":({"X"},set()),"motion_sety":({"Y"},set()),
 "motion_pointindirection":({"DIRECTION"},set()),"motion_movesteps":({"STEPS"},set()),
 "motion_ifonedgebounce":(set(),set()),"motion_pointtowards":({"TOWARDS"},set()),
 "motion_pointtowards_menu":(set(),{"TOWARDS"}),
 "looks_show":(set(),set()),"looks_hide":(set(),set()),"looks_nextcostume":(set(),set()),
 "looks_sayforsecs":({"MESSAGE","SECS"},set()),"looks_say":({"MESSAGE"},set()),
 "looks_changesizeby":({"CHANGE"},set()),"looks_setsizeto":({"SIZE"},set()),
 "looks_switchbackdropto":({"BACKDROP"},set()),"looks_backdrops":(set(),{"BACKDROP"}),
 "control_wait":({"DURATION"},set()),"control_forever":({"SUBSTACK"},set()),
 "control_repeat":({"TIMES","SUBSTACK"},set()),"control_if":({"CONDITION","SUBSTACK"},set()),
 "control_if_else":({"CONDITION","SUBSTACK","SUBSTACK2"},set()),"control_wait_until":({"CONDITION"},set()),
 "control_stop":(set(),{"STOP_OPTION"}),"control_create_clone_of":({"CLONE_OPTION"},set()),
 "control_create_clone_of_menu":(set(),{"CLONE_OPTION"}),"control_delete_this_clone":(set(),set()),
 "sensing_touchingobject":({"TOUCHINGOBJECTMENU"},set()),"sensing_touchingobjectmenu":(set(),{"TOUCHINGOBJECTMENU"}),
 "sensing_touchingcolor":({"COLOR"},set()),"sensing_keypressed":({"KEY_OPTION"},set()),
 "sensing_keyoptions":(set(),{"KEY_OPTION"}),"sensing_mousedown":(set(),set()),
 "sensing_askandwait":({"QUESTION"},set()),"sensing_answer":(set(),set()),
 "operator_equals":({"OPERAND1","OPERAND2"},set()),"operator_gt":({"OPERAND1","OPERAND2"},set()),
 "operator_lt":({"OPERAND1","OPERAND2"},set()),"operator_and":({"OPERAND1","OPERAND2"},set()),
 "operator_or":({"OPERAND1","OPERAND2"},set()),"operator_not":({"OPERAND"},set()),
 "operator_random":({"FROM","TO"},set()),"operator_join":({"STRING1","STRING2"},set()),
 "sensing_mousex":(set(),set()),"sensing_mousey":(set(),set()),"sensing_timer":(set(),set()),
 "motion_xposition":(set(),set()),"motion_yposition":(set(),set()),"motion_direction":(set(),set()),
 "motion_turnright":({"DEGREES"},set()),"motion_turnleft":({"DEGREES"},set()),
 "motion_goto":({"TO"},set()),"motion_goto_menu":(set(),{"TO"}),
 "operator_add":({"NUM1","NUM2"},set()),"operator_subtract":({"NUM1","NUM2"},set()),
 "operator_multiply":({"NUM1","NUM2"},set()),"control_repeat_until":({"CONDITION","SUBSTACK"},set()),
}

def verify(project):
    problems = []
    for t in project["targets"]:
        blocks = t["blocks"]; ids = set(blocks)
        for bid, b in blocks.items():
            op = b["opcode"]
            if op not in OPSPEC:
                problems.append(f"{t['name']}:{op} unknown opcode"); continue
            ein, efi = OPSPEC[op]
            gin = set(b["inputs"]); gfi = set(b["fields"])
            # SUBSTACK/SUBSTACK2 optional if empty
            missing = ein - gin - {"SUBSTACK", "SUBSTACK2"}
            if missing: problems.append(f"{t['name']}:{op} missing inputs {missing}")
            extra = gin - ein
            if extra: problems.append(f"{t['name']}:{op} extra inputs {extra}")
            if gfi != efi: problems.append(f"{t['name']}:{op} fields {gfi}!={efi}")
            # reference integrity
            nxt = b.get("next")
            if nxt and (nxt not in ids or blocks[nxt]["parent"] != bid):
                problems.append(f"{t['name']}:{bid} bad next")
            for inp, val in b["inputs"].items():
                if not isinstance(val, list): continue
                for slot in val[1:]:
                    if isinstance(slot, str):
                        if slot not in ids: problems.append(f"{t['name']}:{bid} input {inp} dangling")
                        elif blocks[slot]["parent"] != bid: problems.append(f"{t['name']}:{bid} input {inp} child parent")
    return problems

# ---------------------------------------------------------------- assembly
def target_sprite(name, lib, x, y, size, factory, layer, direction=90, rot="all around", current=0):
    _patch_menus(factory); fix_parents(factory.blocks)
    return {"isStage": False, "name": name, "variables": {}, "lists": {}, "broadcasts": {},
            "blocks": factory.blocks, "comments": {}, "currentCostume": current,
            "costumes": sprite_costumes(lib), "sounds": [], "volume": 100, "layerOrder": layer,
            "visible": True, "x": x, "y": y, "size": size, "direction": direction,
            "draggable": False, "rotationStyle": rot}

def make_stage(backdrop, variables=None, broadcasts=None):
    return {"isStage": True, "name": "Stage",
            "variables": {vid: [nm, 0] for nm, vid in (variables or {}).items()},
            "lists": {}, "broadcasts": broadcasts or {}, "blocks": {}, "comments": {},
            "currentCostume": 0, "costumes": [backdrop_costume(backdrop)], "sounds": [],
            "volume": 100, "layerOrder": 0, "tempo": 60, "videoTransparency": 50,
            "videoState": "on", "textToSpeechLanguage": None}

def var_monitor(name, vid, x=5, y=5):
    return {"id": vid, "mode": "default", "opcode": "data_variable", "params": {"VARIABLE": name},
            "spriteName": None, "value": 0, "width": 0, "height": 0, "x": x, "y": y,
            "visible": True, "sliderMin": 0, "sliderMax": 100, "isDiscrete": True}

def write_project(targets, monitors, out_path, agent="GradeNext game engine"):
    project = {"targets": targets, "monitors": monitors, "extensions": [],
               "meta": {"semver": "3.0.0", "vm": "0.2.0", "agent": agent}}
    problems = verify(project)
    if problems:
        raise SystemExit("VERIFY FAILED for %s:\n  " % out_path + "\n  ".join(problems[:20]))
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("project.json", json.dumps(project, separators=(",", ":")))
    raw = buf.getvalue()
    if out_path:
        open(out_path, "wb").write(raw)
    return raw
