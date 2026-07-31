#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
templates.py — parameterised, playable "desired output" games.

Each template takes a `theme` (which real library sprites/backdrop to use) and
returns (targets, monitors). The same template + different art = a different
game, so a handful of verified templates covers many exercises.

Templates: collect, catch, dodge, clicker, quiz.
All are built with game_engine and auto-verified on write.
"""
from game_engine import (Factory, target_sprite, make_stage, var_monitor, write_project,
                         txt, num, whenflag, whenclicked, whenkey, setvar, changevar, gotoxy, sety,
                         changex, changey, pointdir, move, show, hide, sayfor, nextcostume,
                         changesize, wait, repeat, forever, if_, stop, pointtowards, askandwait,
                         bounce, turnright, turnleft, goto_sprite, repeatuntil, waituntil)

def _goto_random_top(f, y=175):
    r = f.random(-210, 210)
    return {"op": "motion_gotoxy", "inputs": {"X": [3, r, [4, "0"]], "Y": num(y)}}

def key_move(f, key, dx=0, dy=0):
    cond = f.key_pressed(key)
    sub = []
    if dx: sub.append(changex(dx))
    if dy: sub.append(changey(dy))
    return if_(cond, sub)

def four_dir(f, step=5):
    return [key_move(f, "right arrow", dx=step), key_move(f, "left arrow", dx=-step),
            key_move(f, "up arrow", dy=step), key_move(f, "down arrow", dy=-step)]

# ------------------------------------------------------------ COLLECT
def collect(theme):
    vid = "vsc"; vi = {"score": vid}
    wp = Factory("p", vi)
    ce = wp.touching(theme["enemy"])
    moves = four_dir(wp) + [if_(ce, [gotoxy(-195, -70)])]
    wp.stack([whenflag(), setvar("score", 0, vid), gotoxy(-195, -70), pointdir(90), forever(moves)])
    player = target_sprite(theme["player"], theme["player"], -195, -70, theme.get("psize", 75), wp, 6)

    crystals = []
    for i, (x, y) in enumerate([(-70, -120), (70, 10), (165, -120)]):
        cf = Factory("c%d" % i, vi)
        ct = cf.touching(theme["player"])
        cf.stack([whenflag(), show(), forever([if_(ct, [changevar("score", 1, vid), hide(), stop("this script")])])])
        crystals.append(target_sprite("Gem%d" % (i + 1), theme["collectible"], x, y, 55, cf, i + 1))

    ef = Factory("e", vi)
    ef.stack([whenflag(), gotoxy(0, 90), forever([pointtowards(theme["player"]), move(2)])])
    ef.stack([whenflag(), forever([nextcostume(), wait("0.25")])], top=True, y=220)
    enemy = target_sprite(theme["enemy"], theme["enemy"], 0, 90, 70, ef, 4)

    gf = Factory("g", vi)
    eq = gf.equals(gf.rvar("score"), txt("3"))
    gf.stack([whenflag(), gotoxy(185, 70), forever([if_(eq, [sayfor(theme.get("win", "You collected all 3 — YOU WIN!"), 4), stop("all")])])])
    gf.stack([whenflag(), forever([nextcostume(), wait("0.35")])], top=True, y=220)
    goal = target_sprite(theme["goal"], theme["goal"], 185, 70, 80, gf, 5)

    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage] + crystals + [enemy, goal, player], [var_monitor("score", vid)]

# ------------------------------------------------------------ CATCH
def catch(theme):
    vid = "vsc"; vlid = "vlv"; vi = {"score": vid, "lives": vlid}
    pf = Factory("p", vi)
    mx = pf.mousex()
    setx_mouse = {"op": "motion_setx", "inputs": {"X": [3, mx, [4, "0"]]}}
    eq0 = pf.equals(pf.rvar("lives"), txt("0"))
    pf.stack([whenflag(), setvar("score", 0, vid), setvar("lives", 3, vlid), sety(-140),
              forever([setx_mouse, if_(eq0, [sayfor("Game Over!", 3), stop("all")])])])
    player = target_sprite(theme["player"], theme["player"], 0, -140, theme.get("psize", 85), pf, 3)

    itf = Factory("i", vi)
    yb = itf.ypos(); lt = itf.lt([3, yb, [4, "0"]], num(-160)); tp = itf.touching(theme["player"])
    itf.stack([whenflag(), _goto_random_top(itf),
               forever([changey(-6),
                        if_(lt, [changevar("lives", -1, vlid), _goto_random_top(itf)]),
                        if_(tp, [changevar("score", 1, vid), _goto_random_top(itf)])])])
    item = target_sprite(theme["item"], theme["item"], 0, 170, 65, itf, 1)

    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage, item, player], [var_monitor("score", vid, 5, 5), var_monitor("lives", vlid, 5, 40)]

# ------------------------------------------------------------ DODGE
def dodge(theme):
    vid = "vsc"; vi = {"score": vid}
    pf = Factory("p", vi)
    pf.stack([whenflag(), setvar("score", 0, vid), gotoxy(0, -120), forever(four_dir(pf))])
    player = target_sprite(theme["player"], theme["player"], 0, -120, theme.get("psize", 70), pf, 5)

    enemies = []
    for i in range(3):
        ef = Factory("e%d" % i, vi)
        yb = ef.ypos(); lt = ef.lt([3, yb, [4, "0"]], num(-170)); tp = ef.touching(theme["player"])
        ef.stack([whenflag(), _goto_random_top(ef, 185), wait(str(round(i * 0.5, 2))),
                  forever([changey(-5),
                           if_(lt, [changevar("score", 1, vid), _goto_random_top(ef, 185)]),
                           if_(tp, [sayfor("You got hit — Game Over!", 3), stop("all")])])])
        enemies.append(target_sprite("Rock%d" % (i + 1), theme["enemy"], 0, 185, 65, ef, i + 1))

    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage] + enemies + [player], [var_monitor("score", vid)]

# ------------------------------------------------------------ CLICKER
def clicker(theme):
    vid = "vsc"; vi = {"score": vid}
    tf = Factory("t", vi)
    tf.stack([whenflag(), setvar("score", 0, vid), gotoxy(0, -10)])
    tf.stack([whenclicked(), changevar("score", 1, vid), changesize(10), wait("0.05"), changesize(-10)], top=True, y=220)
    eq = tf.equals(tf.rvar("score"), txt("25"))
    tf.stack([whenflag(), forever([if_(eq, [sayfor("You reached 25 — amazing!", 4), stop("all")])])], top=True, y=360)
    target = target_sprite(theme["target"], theme["target"], 0, -10, 120, tf, 1)
    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage, target], [var_monitor("score", vid)]

# ------------------------------------------------------------ QUIZ (Recall Test)
def quiz(theme):
    vid = "vsc"; vi = {"score": vid}
    hf = Factory("h", vi)
    seq = [whenflag(), setvar("score", 0, vid), sayfor("Recall Quiz — answer each question!", 2)]
    qs = theme["questions"]
    for q, a in qs:
        seq.append(askandwait(q))
        cond = hf.equals([3, hf.answer(), [10, ""]], txt(a))
        seq.append(if_(cond, [changevar("score", 1, vid)]))
    j1 = hf.join([1, [10, "You scored "]], hf.rvar("score"))
    j2 = hf.join([3, j1, [10, ""]], [1, [10, " / %d!" % len(qs)]])
    seq.append({"op": "looks_sayforsecs", "inputs": {"MESSAGE": [3, j2, [10, ""]], "SECS": num(6)}})
    hf.stack(seq)
    host = target_sprite(theme["host"], theme["host"], 0, -30, 95, hf, 1)
    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage, host], [var_monitor("score", vid)]

# ------------------------------------------------------------ FLAPPY
def flappy(theme):
    vid = "vsc"; vvy = "vvy"; vi = {"score": vid, "vy": vvy}
    pf = Factory("p", vi)
    ob = pf.touching(theme["obstacle"])
    yb = pf.ypos(); floor = pf.lt([3, yb, [4, "0"]], num(-170))
    change_y_by_vy = {"op": "motion_changeyby", "inputs": {"DY": [3, [12, "vy", vvy], [4, "0"]]}}
    pf.stack([whenflag(), setvar("score", 0, vid), setvar("vy", 0, vvy), gotoxy(-120, 0), pointdir(90),
              forever([{"op": "data_changevariableby", "inputs": {"VALUE": txt("-1")}, "fields": {"VARIABLE": ["vy", vvy]}},
                       change_y_by_vy,
                       if_(ob, [sayfor("Ouch! Game Over", 3), stop("all")]),
                       if_(floor, [sayfor("You fell — Game Over", 3), stop("all")])])])
    pf.stack([whenkey("space"), setvar("vy", 12, vvy)], top=True, y=240)
    player = target_sprite(theme["player"], theme["player"], -120, 0, theme.get("psize", 70), pf, 3, rot="left-right")

    of = Factory("o", vi)
    def g_edge(f):
        r = f.random(-110, 110)
        return {"op": "motion_gotoxy", "inputs": {"X": num(240), "Y": [3, r, [4, "0"]]}}
    xb = of.xpos(); off = of.lt([3, xb, [4, "0"]], num(-235))
    of.stack([whenflag(), g_edge(of),
              forever([changex(-4), if_(off, [g_edge(of), changevar("score", 1, vid)])])])
    obstacle = target_sprite(theme["obstacle"], theme["obstacle"], 240, 0, theme.get("osize", 80), of, 1)

    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage, obstacle, player], [var_monitor("score", vid)]

# ------------------------------------------------------------ WHACK
def whack(theme):
    vid = "vsc"; vtm = "vtm"; vi = {"score": vid, "time": vtm}
    tf = Factory("t", vi)
    def rgoto(f):
        rx = f.random(-200, 200); ry = f.random(-140, 140)
        return {"op": "motion_gotoxy", "inputs": {"X": [3, rx, [4, "0"]], "Y": [3, ry, [4, "0"]]}}
    def rwait(f, a, b):
        r = f.random(a, b)
        return {"op": "control_wait", "inputs": {"DURATION": [3, r, [5, "1"]]}}
    # pop-up loop
    tf.stack([whenflag(), setvar("score", 0, vid),
              forever([show(), rgoto(tf), rwait(tf, "0.6", "1.1"), hide(), rwait(tf, "0.3", "0.6")])])
    # click to score
    tf.stack([whenclicked(), changevar("score", 1, vid), hide()], top=True, y=240)
    # countdown then game over
    jscore = tf.join([1, [10, "Time up! Score: "]], tf.rvar("score"))
    tf.stack([whenflag(), setvar("time", 20, vtm),
              repeat(20, [wait("1"), changevar("time", -1, vtm)]),
              stop("other scripts in sprite"),
              {"op": "looks_sayforsecs", "inputs": {"MESSAGE": [3, jscore, [10, ""]], "SECS": num(5)}},
              stop("all")], top=True, y=440)
    target = target_sprite(theme["target"], theme["target"], 0, 0, theme.get("tsize", 90), tf, 1)
    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage, target], [var_monitor("score", vid, 5, 5), var_monitor("time", vtm, 5, 40)]

# ------------------------------------------------------------ PONG
def pong(theme):
    vid = "vsc"; vi = {"score": vid}
    pf = Factory("p", vi)
    mx = pf.mousex()
    setx_mouse = {"op": "motion_setx", "inputs": {"X": [3, mx, [4, "0"]]}}
    pf.stack([whenflag(), sety(-150), forever([setx_mouse])])
    paddle = target_sprite(theme["paddle"], theme["paddle"], 0, -150, theme.get("padsize", 100), pf, 1, rot="left-right")

    bf = Factory("b", vi)
    tp = bf.touching(theme["paddle"])
    yb = bf.ypos(); floor = bf.lt([3, yb, [4, "0"]], num(-165))
    flip = bf.minus(num(180), [3, bf.direction(), [4, "0"]])
    pdflip = {"op": "motion_pointindirection", "inputs": {"DIRECTION": [3, flip, [8, "90"]]}}
    bf.stack([whenflag(), setvar("score", 0, vid), gotoxy(0, 30), pointdir(45),
              forever([move(7), bounce(),
                       if_(tp, [pdflip, changevar("score", 1, vid), move(12)]),
                       if_(floor, [sayfor("Game Over!", 3), stop("all")])])])
    ball = target_sprite(theme["ball"], theme["ball"], 0, 30, theme.get("ballsize", 65), bf, 2)
    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage, paddle, ball], [var_monitor("score", vid)]

# ------------------------------------------------------------ RUNNER
def runner(theme):
    vid = "vsc"; vvy = "vvy"; vi = {"score": vid, "vy": vvy}
    gf = Factory("p", vi)
    ob = gf.touching(theme["obstacle"])
    yb = gf.ypos(); below = gf.lt([3, yb, [4, "0"]], num(-100))
    dyvy = {"op": "motion_changeyby", "inputs": {"DY": [3, [12, "vy", vvy], [4, "0"]]}}
    gf.stack([whenflag(), setvar("score", 0, vid), setvar("vy", 0, vvy), gotoxy(-150, -100),
              forever([changevar("vy", -1, vvy), dyvy,
                       if_(below, [{"op": "motion_sety", "inputs": {"Y": num(-100)}}, setvar("vy", 0, vvy)]),
                       if_(ob, [sayfor("Crash — Game Over!", 3), stop("all")])])])
    yb2 = gf.ypos(); near = gf.lt([3, yb2, [4, "0"]], num(-95))
    gf.stack([whenkey("space"), if_(near, [setvar("vy", 14, vvy)])], top=True, y=260)
    player = target_sprite(theme["player"], theme["player"], -150, -100, theme.get("psize", 70), gf, 2, rot="left-right")

    of = Factory("o", vi)
    xb = of.xpos(); off = of.lt([3, xb, [4, "0"]], num(-240))
    of.stack([whenflag(), gotoxy(240, -105),
              forever([changex(-6), if_(off, [gotoxy(240, -105), changevar("score", 1, vid)])])])
    obstacle = target_sprite(theme["obstacle"], theme["obstacle"], 240, -105, theme.get("osize", 65), of, 1)
    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage, obstacle, player], [var_monitor("score", vid)]

# ------------------------------------------------------------ SHOOTER (single bullet)
def shooter(theme):
    vid = "vsc"; vi = {"score": vid}
    pf = Factory("p", vi)
    kl = pf.key_pressed("left arrow"); kr = pf.key_pressed("right arrow")
    pf.stack([whenflag(), setvar("score", 0, vid), sety(-140),
              forever([if_(kl, [changex(-7)]), if_(kr, [changex(7)])])])
    player = target_sprite(theme["player"], theme["player"], 0, -140, theme.get("psize", 80), pf, 3)

    bf = Factory("b", vi)
    sp = bf.key_pressed("space")
    en = bf.touching(theme["enemy"]); yb = bf.ypos(); topedge = bf.gt([3, yb, [4, "0"]], num(170))
    done = bf.or_(en, topedge)
    bf.stack([whenflag(),
              forever([goto_sprite(theme["player"]), hide(), waituntil(sp), show(), repeatuntil(done, [changey(14)])])])
    bullet = target_sprite(theme["bullet"], theme["bullet"], 0, -120, theme.get("bsize", 55), bf, 2)

    ef = Factory("e", vi)
    def gtop(f):
        r = f.random(-200, 200); return {"op": "motion_gotoxy", "inputs": {"X": [3, r, [4, "0"]], "Y": num(170)}}
    yb2 = ef.ypos(); below = ef.lt([3, yb2, [4, "0"]], num(-175))
    tb = ef.touching(theme["bullet"]); tp = ef.touching(theme["player"])
    ef.stack([whenflag(), gtop(ef),
              forever([changey(-3), if_(below, [gtop(ef)]),
                       if_(tb, [changevar("score", 1, vid), gtop(ef)]),
                       if_(tp, [sayfor("The enemy got you — Game Over!", 3), stop("all")])])])
    enemy = target_sprite(theme["enemy"], theme["enemy"], 0, 170, theme.get("esize", 70), ef, 1)
    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage, enemy, bullet, player], [var_monitor("score", vid)]

# ------------------------------------------------------------ DRIVE (top-down racer)
def drive(theme):
    vi = {}
    cf = Factory("c", vi)
    ku = cf.key_pressed("up arrow"); kd = cf.key_pressed("down arrow")
    kl = cf.key_pressed("left arrow"); kr = cf.key_pressed("right arrow")
    gl = cf.touching(theme["goal"]); en = cf.touching(theme["enemy"])
    cf.stack([whenflag(), gotoxy(-200, -140), pointdir(90),
              forever([if_(ku, [move(5)]), if_(kd, [move(-5)]), if_(kl, [turnleft(8)]), if_(kr, [turnright(8)]),
                       if_(gl, [sayfor("You reached the finish — YOU WIN!", 4), stop("all")]),
                       if_(en, [gotoxy(-200, -140)])])])
    car = target_sprite(theme["player"], theme["player"], -200, -140, theme.get("psize", 60), cf, 3)

    ef = Factory("e", vi)
    ef.stack([whenflag(), gotoxy(0, 60), pointdir(90), forever([move(4), bounce()])])
    enemy = target_sprite(theme["enemy"], theme["enemy"], 0, 60, theme.get("esize", 60), ef, 2, rot="left-right")
    goal = target_sprite(theme["goal"], theme["goal"], 200, 150, theme.get("gsize", 80), Factory("g", vi), 1)
    stage = make_stage(theme["backdrop"])
    return [stage, goal, enemy, car], []

TEMPLATES = {"collect": collect, "catch": catch, "dodge": dodge, "clicker": clicker,
             "quiz": quiz, "flappy": flappy, "whack": whack,
             "pong": pong, "runner": runner, "shooter": shooter, "drive": drive}

def build(template, theme, out_path):
    targets, monitors = TEMPLATES[template](theme)
    return write_project(targets, monitors, out_path, agent="GradeNext desired-output (%s)" % template)
