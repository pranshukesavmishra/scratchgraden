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
                         txt, num, whenflag, whenclicked, setvar, changevar, gotoxy, sety,
                         changex, changey, pointdir, move, show, hide, sayfor, nextcostume,
                         changesize, wait, forever, if_, stop, pointtowards, askandwait)

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

TEMPLATES = {"collect": collect, "catch": catch, "dodge": dodge, "clicker": clicker, "quiz": quiz}

def build(template, theme, out_path):
    targets, monitors = TEMPLATES[template](theme)
    return write_project(targets, monitors, out_path, agent="GradeNext desired-output (%s)" % template)
