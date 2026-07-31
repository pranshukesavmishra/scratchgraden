#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
templates.py — parameterised, playable "desired output" projects.

Each template is a fuller, multi-sprite build (several sprites, score/lives,
win/lose) so exercises are substantial. The generated project is the DESIRED
OUTPUT; the starter is the same sprites with the code stripped out, so students
build the solution themselves from the hints + desired output.

All templates are auto-verified (wiring + opcode names) on write.
"""
from game_engine import (Factory, target_sprite, make_stage, var_monitor, write_project,
                         txt, num, whenflag, whenclicked, whenkey, setvar, changevar, gotoxy, sety,
                         changex, changey, pointdir, move, show, hide, sayfor, nextcostume,
                         changesize, wait, repeat, forever, if_, stop, pointtowards, askandwait,
                         bounce, turnright, turnleft, goto_sprite, repeatuntil, waituntil,
                         pen_clear, pen_down, pen_up, pen_color, pen_size, pen_rainbow, drum)


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

def nm(base, i):
    return base if i == 0 else base + " " + str(i + 1)

# ------------------------------------------------------------ COLLECT
def collect(theme):
    vid = "vsc"; vi = {"score": vid}
    wp = Factory("p", vi)
    ce = wp.touching(theme["enemy"])
    wp.stack([whenflag(), setvar("score", 0, vid), gotoxy(-195, -70), pointdir(90),
              forever(four_dir(wp) + [if_(ce, [gotoxy(-195, -70)])])])
    player = target_sprite(theme["player"], theme["player"], -195, -70, theme.get("psize", 75), wp, 7)
    gems = []
    for i, (x, y) in enumerate([(-70, -120), (70, 10), (165, -120)]):
        cf = Factory("c%d" % i, vi)
        ct = cf.touching(theme["player"])
        cf.stack([whenflag(), show(), forever([if_(ct, [changevar("score", 1, vid), hide(), stop("this script")])])])
        gems.append(target_sprite(nm("Gem", i), theme["collectible"], x, y, 55, cf, i + 1))
    ef = Factory("e", vi)
    ef.stack([whenflag(), gotoxy(0, 90), forever([pointtowards(theme["player"]), move(2)])])
    ef.stack([whenflag(), forever([nextcostume(), wait("0.25")])], top=True, y=220)
    enemy = target_sprite(theme["enemy"], theme["enemy"], 0, 90, 70, ef, 5)
    gf = Factory("g", vi)
    eq = gf.equals(gf.rvar("score"), txt("3"))
    gf.stack([whenflag(), gotoxy(185, 70), forever([if_(eq, [sayfor(theme.get("win", "You collected all 3 — YOU WIN!"), 4), stop("all")])])])
    gf.stack([whenflag(), forever([nextcostume(), wait("0.35")])], top=True, y=220)
    goal = target_sprite(theme["goal"], theme["goal"], 185, 70, 80, gf, 6)
    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage] + gems + [enemy, goal, player], [var_monitor("score", vid)]

# ------------------------------------------------------------ CATCH (bowl + 3 fruit + bomb + lives)
def catch(theme):
    vid = "vsc"; vlid = "vlv"; vi = {"score": vid, "lives": vlid}
    pf = Factory("p", vi)
    mx = pf.mousex()
    setx_mouse = {"op": "motion_setx", "inputs": {"X": [3, mx, [4, "0"]]}}
    eq0 = pf.equals(pf.rvar("lives"), txt("0"))
    pf.stack([whenflag(), setvar("score", 0, vid), setvar("lives", 3, vlid), sety(-140),
              forever([setx_mouse, if_(eq0, [sayfor("Game Over!", 3), stop("all")])])])
    player = target_sprite(theme["player"], theme["player"], 0, -140, theme.get("psize", 85), pf, 6)
    fruits = []
    for i in range(3):
        itf = Factory("f%d" % i, vi)
        yb = itf.ypos(); lt = itf.lt([3, yb, [4, "0"]], num(-160)); tp = itf.touching(theme["player"])
        itf.stack([whenflag(), _goto_random_top(itf), wait(str(round(i * 0.6, 2))),
                   forever([changey(-6),
                            if_(lt, [_goto_random_top(itf)]),
                            if_(tp, [changevar("score", 1, vid), _goto_random_top(itf)])])])
        fruits.append(target_sprite(nm(theme["item"], i), theme["item"], -120 + i * 120, 150, 60, itf, i + 1))
    bf = Factory("bm", vi)
    yb2 = bf.ypos(); lt2 = bf.lt([3, yb2, [4, "0"]], num(-160)); tp2 = bf.touching(theme["player"])
    bf.stack([whenflag(), _goto_random_top(bf),
              forever([changey(-5),
                       if_(lt2, [_goto_random_top(bf)]),
                       if_(tp2, [changevar("lives", -1, vlid), _goto_random_top(bf)])])])
    bomb = target_sprite(theme.get("bomb", "Beetle"), theme.get("bomb", "Beetle"), 180, 150, 55, bf, 5)
    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage] + fruits + [bomb, player], [var_monitor("score", vid, 5, 5), var_monitor("lives", vlid, 5, 40)]

# ------------------------------------------------------------ DODGE (player + 3 hazards + bonus coin)
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
        enemies.append(target_sprite(nm(theme["enemy"], i), theme["enemy"], -120 + i * 120, 185, 65, ef, i + 1))
    cf = Factory("cn", vi)
    yb2 = cf.ypos(); lt2 = cf.lt([3, yb2, [4, "0"]], num(-170)); tpc = cf.touching(theme["player"])
    cf.stack([whenflag(), _goto_random_top(cf, 185),
              forever([changey(-3),
                       if_(lt2, [_goto_random_top(cf, 185)]),
                       if_(tpc, [changevar("score", 1, vid), _goto_random_top(cf, 185)])])])
    coin = target_sprite(theme.get("coin", "Star"), theme.get("coin", "Star"), 180, 185, 45, cf, 4)
    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage] + enemies + [coin, player], [var_monitor("score", vid)]

# ------------------------------------------------------------ CLICKER (target + 2 auto-helpers)
def clicker(theme):
    vid = "vsc"; vi = {"score": vid}
    tf = Factory("t", vi)
    tf.stack([whenflag(), setvar("score", 0, vid), gotoxy(0, 20)])
    tf.stack([whenclicked(), changevar("score", 1, vid), changesize(12), wait("0.05"), changesize(-12)], top=True, y=220)
    eq = tf.equals(tf.rvar("score"), txt("50"))
    tf.stack([whenflag(), forever([if_(eq, [sayfor("You reached 50 — amazing!", 4), stop("all")])])], top=True, y=380)
    target = target_sprite(theme["target"], theme["target"], 0, 20, 110, tf, 1)
    helpers = []
    hpos = [(-175, -95), (175, -95)]
    for i in range(2):
        hf = Factory("h%d" % i, vi)
        hf.stack([whenflag(), gotoxy(hpos[i][0], hpos[i][1]),
                  forever([wait("2"), changevar("score", 1, vid), changesize(8), wait("0.1"), changesize(-8)])])
        helpers.append(target_sprite(nm("Helper", i), theme.get("helper", "Cat 2"), hpos[i][0], hpos[i][1], 70, hf, i + 2))
    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage, target] + helpers, [var_monitor("score", vid)]

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

# ------------------------------------------------------------ FLAPPY (bird + 2 obstacles + coin)
def flappy(theme):
    vid = "vsc"; vvy = "vvy"; vi = {"score": vid, "vy": vvy}
    pf = Factory("p", vi)
    ob = pf.touching(theme["obstacle"])
    yb = pf.ypos(); floor = pf.lt([3, yb, [4, "0"]], num(-170))
    dyvy = {"op": "motion_changeyby", "inputs": {"DY": [3, [12, "vy", vvy], [4, "0"]]}}
    pf.stack([whenflag(), setvar("score", 0, vid), setvar("vy", 0, vvy), gotoxy(-120, 0), pointdir(90),
              forever([{"op": "data_changevariableby", "inputs": {"VALUE": txt("-1")}, "fields": {"VARIABLE": ["vy", vvy]}}, dyvy,
                       if_(ob, [sayfor("Ouch! Game Over", 3), stop("all")]),
                       if_(floor, [sayfor("You fell — Game Over", 3), stop("all")])])])
    pf.stack([whenkey("space"), setvar("vy", 12, vvy)], top=True, y=240)
    player = target_sprite(theme["player"], theme["player"], -120, 0, theme.get("psize", 65), pf, 4, rot="left-right")
    obs = []
    for i in range(2):
        of = Factory("o%d" % i, vi)
        def g_edge(f):
            r = f.random(-110, 110)
            return {"op": "motion_gotoxy", "inputs": {"X": num(240), "Y": [3, r, [4, "0"]]}}
        xb = of.xpos(); off = of.lt([3, xb, [4, "0"]], num(-235))
        of.stack([whenflag(), g_edge(of), wait(str(i * 1.5)),
                  forever([changex(-4), if_(off, [g_edge(of), changevar("score", 1, vid)])])])
        obs.append(target_sprite(nm(theme["obstacle"], i), theme["obstacle"], 180 + i * 60, 0, 70, of, i + 1))
    cf = Factory("cn", vi)
    def g_edge2(f):
        r = f.random(-120, 120)
        return {"op": "motion_gotoxy", "inputs": {"X": num(240), "Y": [3, r, [4, "0"]]}}
    xb2 = cf.xpos(); off2 = cf.lt([3, xb2, [4, "0"]], num(-235)); tpc = cf.touching(theme["player"])
    cf.stack([whenflag(), g_edge2(cf), wait("0.8"),
              forever([changex(-3), if_(off2, [g_edge2(cf)]), if_(tpc, [changevar("score", 1, vid), g_edge2(cf)])])])
    coin = target_sprite(theme.get("coin", "Star"), theme.get("coin", "Star"), 240, 80, 45, cf, 3)
    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage] + obs + [coin, player], [var_monitor("score", vid)]

# ------------------------------------------------------------ WHACK (3 moles + a bad one + timer)
def whack(theme):
    vid = "vsc"; vtm = "vtm"; vi = {"score": vid, "time": vtm}
    def rgoto(ff):
        rx = ff.random(-200, 200); ry = ff.random(-140, 140)
        return {"op": "motion_gotoxy", "inputs": {"X": [3, rx, [4, "0"]], "Y": [3, ry, [4, "0"]]}}
    def rwait(ff, a, b):
        r = ff.random(a, b)
        return {"op": "control_wait", "inputs": {"DURATION": [3, r, [5, "1"]]}}
    def pop_scripts(f, good=True):
        f.stack([whenflag(), forever([show(), rgoto(f), rwait(f, "0.6", "1.1"), hide(), rwait(f, "0.3", "0.6")])])
        f.stack([whenclicked(), changevar("score", 1 if good else -2, vid), hide()], top=True, y=240)
    targets = [make_stage(theme["backdrop"], variables=vi)]
    holes = [(-120, -30), (0, -30), (120, -30)]
    for i in range(3):
        mf = Factory("m%d" % i, vi)
        pop_scripts(mf, good=True)
        if i == 0:
            j = mf.join([1, [10, "Time up! Score: "]], mf.rvar("score"))
            mf.stack([whenflag(), setvar("score", 0, vid), setvar("time", 20, vtm),
                      repeat(20, [wait("1"), changevar("time", -1, vtm)]),
                      stop("other scripts in sprite"),
                      {"op": "looks_sayforsecs", "inputs": {"MESSAGE": [3, j, [10, ""]], "SECS": num(5)}},
                      stop("all")], top=True, y=440)
        targets.append(target_sprite(nm(theme["target"], i), theme["target"], holes[i][0], holes[i][1], 85, mf, i + 1))
    bf = Factory("bad", vi)
    pop_scripts(bf, good=False)
    targets.append(target_sprite(theme.get("bad", "Ghost"), theme.get("bad", "Ghost"), 0, 90, 80, bf, 4))
    return targets, [var_monitor("score", vid, 5, 5), var_monitor("time", vtm, 5, 40)]

# ------------------------------------------------------------ PONG / BREAKOUT (paddle + ball + 4 bricks)
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
    bf.stack([whenflag(), setvar("score", 0, vid), gotoxy(0, -60), pointdir(45),
              forever([move(7), bounce(),
                       if_(tp, [pdflip, move(12)]),
                       if_(floor, [sayfor("Game Over!", 3), stop("all")])])])
    ball = target_sprite(theme["ball"], theme["ball"], 0, -60, 65, bf, 2)
    bricks = []
    bx = [-120, -40, 40, 120]
    for i in range(4):
        kf = Factory("k%d" % i, vi)
        tb = kf.touching(theme["ball"])
        kf.stack([whenflag(), show(), gotoxy(bx[i], 130),
                  forever([if_(tb, [changevar("score", 1, vid), hide(), stop("this script")])])])
        bricks.append(target_sprite(nm("Brick", i), theme.get("brick", "Button2"), bx[i], 130, 70, kf, i + 3))
    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage, paddle, ball] + bricks, [var_monitor("score", vid)]

# ------------------------------------------------------------ RUNNER (player + 2 obstacles + coin)
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
    player = target_sprite(theme["player"], theme["player"], -150, -100, theme.get("psize", 70), gf, 4, rot="left-right")
    obs = []
    for i in range(2):
        of = Factory("o%d" % i, vi)
        xb = of.xpos(); off = of.lt([3, xb, [4, "0"]], num(-240))
        of.stack([whenflag(), gotoxy(240, -105), wait(str(round(i * 1.3, 2))),
                  forever([changex(-6), if_(off, [gotoxy(240, -105), changevar("score", 1, vid)])])])
        obs.append(target_sprite(nm(theme["obstacle"], i), theme["obstacle"], 140 + i * 60, -105, 65, of, i + 1))
    cf = Factory("cn", vi)
    xb2 = cf.xpos(); off2 = cf.lt([3, xb2, [4, "0"]], num(-240)); tpc = cf.touching(theme["player"])
    cf.stack([whenflag(), gotoxy(240, -60), wait("0.7"),
              forever([changex(-6), if_(off2, [gotoxy(240, -60)]), if_(tpc, [changevar("score", 1, vid), gotoxy(240, -60)])])])
    coin = target_sprite(theme.get("coin", "Star"), theme.get("coin", "Star"), 60, -60, 45, cf, 3)
    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage] + obs + [coin, player], [var_monitor("score", vid)]

# ------------------------------------------------------------ SHOOTER (ship + bullet + 2 enemies)
def shooter(theme):
    vid = "vsc"; vi = {"score": vid}
    pf = Factory("p", vi)
    kl = pf.key_pressed("left arrow"); kr = pf.key_pressed("right arrow")
    pf.stack([whenflag(), setvar("score", 0, vid), sety(-140),
              forever([if_(kl, [changex(-7)]), if_(kr, [changex(7)])])])
    player = target_sprite(theme["player"], theme["player"], 0, -140, theme.get("psize", 80), pf, 4)
    bf = Factory("b", vi)
    sp = bf.key_pressed("space")
    en = bf.touching(theme["enemy"]); yb = bf.ypos(); topedge = bf.gt([3, yb, [4, "0"]], num(170))
    done = bf.or_(en, topedge)
    bf.stack([whenflag(),
              forever([goto_sprite(theme["player"]), hide(), waituntil(sp), show(), repeatuntil(done, [changey(14)])])])
    bullet = target_sprite(theme["bullet"], theme["bullet"], 0, -120, theme.get("bsize", 55), bf, 3)
    enemies = []
    for i in range(2):
        ef = Factory("e%d" % i, vi)
        def gtop(f):
            r = f.random(-200, 200)
            return {"op": "motion_gotoxy", "inputs": {"X": [3, r, [4, "0"]], "Y": num(170)}}
        yb2 = ef.ypos(); below = ef.lt([3, yb2, [4, "0"]], num(-175))
        tb = ef.touching(theme["bullet"]); tp = ef.touching(theme["player"])
        ef.stack([whenflag(), gtop(ef), wait(str(i * 0.8)),
                  forever([changey(-3), if_(below, [gtop(ef)]),
                           if_(tb, [changevar("score", 1, vid), gtop(ef)]),
                           if_(tp, [sayfor("The enemy got you — Game Over!", 3), stop("all")])])])
        enemies.append(target_sprite(nm(theme["enemy"], i), theme["enemy"], -80 + i * 160, 170, 70, ef, i + 1))
    stage = make_stage(theme["backdrop"], variables=vi)
    return [stage] + enemies + [bullet, player], [var_monitor("score", vid)]

# ------------------------------------------------------------ DRIVE (car + finish + 2 traffic cars)
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
    car = target_sprite(theme["player"], theme["player"], -200, -140, theme.get("psize", 60), cf, 4)
    traffic = []
    tpos = [(0, 60), (60, -20)]
    for i in range(2):
        ef = Factory("e%d" % i, vi)
        ef.stack([whenflag(), gotoxy(tpos[i][0], tpos[i][1]), pointdir(90 if i == 0 else -90), forever([move(4), bounce()])])
        traffic.append(target_sprite(nm(theme["enemy"], i), theme["enemy"], tpos[i][0], tpos[i][1], 60, ef, i + 2))
    goal = target_sprite(theme["goal"], theme["goal"], 200, 150, theme.get("gsize", 80), Factory("g", vi), 1)
    stage = make_stage(theme["backdrop"])
    return [stage, goal] + traffic + [car], []

# ------------------------------------------------------------ ANIMATION
def animation(theme):
    mf = Factory("m")
    mf.stack([whenflag(), gotoxy(-210, theme.get("my", -40)), show(), pointdir(90),
              sayfor(theme.get("line1", "Off we go!"), 1.8),
              repeat(22, [nextcostume(), changex(19), wait("0.12")]),
              sayfor(theme.get("line2", "We made it!"), 2.5)])
    mover = target_sprite(theme["mover"], theme["mover"], -210, theme.get("my", -40), theme.get("msize", 90), mf, 2, rot="left-right")
    sf = Factory("s")
    sf.stack([whenflag(), forever([changey(6), wait("0.5"), changey(-6), wait("0.5")])])
    scenery = target_sprite(theme["scenery"], theme["scenery"], theme.get("sx", 150), theme.get("sy", 90), theme.get("ssize", 80), sf, 1)
    stage = make_stage(theme["backdrop"])
    return [stage, scenery, mover], []

# ------------------------------------------------------------ CHATBOT
def chatbot(theme):
    bf = Factory("b"); name = theme.get("name", "Robo")
    def sayjoin(a, b, secs):
        return {"op": "looks_sayforsecs", "inputs": {"MESSAGE": [3, bf.join(a, b), [10, ""]], "SECS": num(secs)}}
    ans = lambda: [3, bf.answer(), [10, ""]]
    bf.stack([whenflag(), sayfor("Hi! I'm " + name + " the robot.", 1.5),
              askandwait("What is your name?"),
              sayjoin([1, [10, "Nice to meet you, "]], ans(), 2),
              askandwait("What is your favourite animal?"),
              sayjoin(ans(), [1, [10, "s are awesome!"]], 2),
              askandwait("What makes you smile?"),
              sayfor("That makes me smile too!", 2),
              sayfor("Thanks for chatting with me!", 2)])
    bot = target_sprite(theme["bot"], theme["bot"], 0, -20, theme.get("bsize", 100), bf, 1)
    stage = make_stage(theme["backdrop"])
    return [stage, bot], []

# ------------------------------------------------------------ ART (pen)
def art(theme):
    pf = Factory("a")
    pf.stack([whenflag(), pen_clear(), hide(), gotoxy(0, 0), pointdir(90), pen_size(2),
              pen_color(theme.get("color", "#ff2d55")), pen_down(),
              repeat(theme.get("points", 72), [move(theme.get("arm", 120)), turnright(theme.get("angle", 175)), pen_rainbow(6)]),
              pen_up()])
    drawer = target_sprite(theme.get("pen", "Ball"), theme.get("pen", "Ball"), 0, 0, 40, pf, 1)
    stage = make_stage(theme["backdrop"])
    return [stage, drawer], []

# ------------------------------------------------------------ MUSIC (drums)
def music(theme):
    targets = [make_stage(theme["backdrop"])]
    seen = {}
    for i, pad in enumerate(theme["pads"]):
        lib, drumn, x, y = pad
        name = lib if seen.get(lib, 0) == 0 else lib + " " + str(seen[lib] + 1)
        seen[lib] = seen.get(lib, 0) + 1
        pf = Factory("m%d" % i)
        pf.stack([whenflag(), gotoxy(x, y)])
        pf.stack([whenclicked(), changesize(18), drum(drumn, 0.25), changesize(-18)], top=True, y=220)
        targets.append(target_sprite(name, lib, x, y, theme.get("size", 90), pf, i + 1))
    return targets, []

TEMPLATES = {"collect": collect, "catch": catch, "dodge": dodge, "clicker": clicker,
             "quiz": quiz, "flappy": flappy, "whack": whack,
             "pong": pong, "runner": runner, "shooter": shooter, "drive": drive,
             "animation": animation, "chatbot": chatbot, "art": art, "music": music}

TEMPLATE_EXT = {"art": ["pen"], "music": ["music"]}

def build(template, theme, out_path):
    targets, monitors = TEMPLATES[template](theme)
    return write_project(targets, monitors, out_path, agent="GradeNext desired-output (%s)" % template,
                         extensions=TEMPLATE_EXT.get(template))
