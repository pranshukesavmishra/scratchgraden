#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
briefs.py — MULTI-STAGE BUILD BRIEFS (long form).

A real 60-minute session needs a build that fills the hour. Every exercise
gets an 8-stage brief (~50 minutes, ~45 concrete tasks):

    1  Set the scene         sprites, backdrop, reset scripts
    2  Core mechanic         the thing the player does
    3  The challenge         what makes it a game
    4  Score & consequences  variables, lives, collisions done right
    5  Level 2 of your game  a second wave/level with rising difficulty
    6  Win and lose          endings, restart button
    7  Feedback and polish   sound, effects, title
    8  Make it yours         extensions so fast finishers never idle

Each stage ends in a CHECKPOINT ("it works when …") so the student always
knows whether they are done and a tutor can see progress at a glance.

Every task is written to be executable exactly as read: real block names,
real numbers, real positions.
"""


def S(title, goal, tasks, check, minutes):
    return {"title": title, "goal": goal, "tasks": tasks,
            "check": check, "minutes": minutes}


# ---------------------------------------------------------------------------
# Shared stages
# ---------------------------------------------------------------------------
def stage_scene(sprites, backdrop):
    names = ", ".join(sprites[:5]) if sprites else "your sprites"
    return S("Set the scene",
             "Get everything on the stage and reset properly, so the game starts identically every time.",
             ["Add the backdrop%s." % ((" (" + backdrop + ")") if backdrop else " that fits your game's world"),
              "Add these sprites: %s." % names,
              "Rename every sprite so its job is obvious — 'Player', 'Coin 1', 'Enemy' — never 'Sprite1'.",
              "Size each sprite sensibly: player around 70–90%, collectibles 45–60%, enemies 60–80%.",
              "Place each sprite at its starting position by dragging, then read off its x and y.",
              "On EVERY sprite add: when green flag clicked → go to x: (its start x) y: (its start y), show, set size, clear graphic effects.",
              "Set the player's rotation style to left-right so it never goes upside-down.",
              "Test: press the green flag three times in a row. Everything must snap back to exactly the same place every time."],
             "Pressing the flag three times puts every sprite back in exactly the same starting state.", 6)


def stage_score(collect_verb="collect a coin", hurt_verb="touch a hazard"):
    return S("Score and consequences",
             "Wire up the variables that make the game matter — correctly, with none of the classic bugs.",
             ["Make TWO variables: 'score' and 'lives'. Name them exactly that.",
              "At the very top of the player's flag script add: set score to 0, set lives to 3.",
              "Add 1 to the score each time you %s — and hide the object or add a wait so one touch scores exactly once." % collect_verb,
              "Take 1 life each time you %s — then send the player back to the start and 'wait 1 seconds' so a single hit costs a single life." % hurt_verb,
              "Show 'score' and 'lives' on the stage; drag their readouts to a top corner where they don't cover the action.",
              "Deliberately try to cheat your own game: hold the player against the hazard. If lives drain instantly, your wait is missing.",
              "Test: play one full round watching only the variables — every change must have exactly one cause."],
             "Score rises by exactly 1 per collect, one hit costs exactly one life, and both readouts are visible.", 7)


def stage_level2(extra):
    return S("Level 2 of your game",
             "One level is a demo; two levels is a game. Add a second, harder stage.",
             ["Make a variable called 'level' and set it to 1 when the flag is clicked.",
              "Add a second backdrop for level 2 — pick one that looks clearly different.",
              "When the score reaches 10: change level to 2, switch to the level-2 backdrop, and broadcast 'level-up'.",
              "When sprites receive 'level-up', make the game harder: " + extra,
              "Show a 'LEVEL 2!' message for 2 seconds when it happens — the player must notice the change.",
              "Play from the start to level 2 without dying. If you can't, level 1 is too hard; tune it.",
              "Test: the difficulty visibly steps up the moment the backdrop changes."],
             "Reaching 10 points switches the backdrop, announces LEVEL 2 and makes the game noticeably harder.", 8)


def stage_endings(win, lose):
    return S("Win and lose",
             "Give the game clear endings the player always understands.",
             ["Write your rules in plain English first: 'You win when %s. You lose when %s.'" % (win, lose),
              "Add the win check with an if inside a forever loop — use '>' not '=' so a jumping score can't skip past it.",
              "On winning: say 'You win!' for 2 seconds, switch to a win backdrop, THEN stop all — in that order.",
              "Add the lose check the same way: message first, then backdrop, then stop all.",
              "Add a Restart button sprite: show it on the end screens; when clicked it broadcasts 'start-game'.",
              "Make every sprite reset itself when it receives 'start-game' — variables, position, visibility.",
              "Test BOTH endings on purpose, then restart twice. No leftover score, no ghost sprites."],
             "You have deliberately triggered win, lose and restart — all three work with nothing left over.", 7)


def stage_polish():
    return S("Feedback and polish",
             "Make every action feel good. This is what separates a finished game from a demo.",
             ["Give every important action its own sound: collect, hit, win, lose. Use 'start sound' so the game never pauses.",
              "Add a collect effect: repeat 3 [change size by 6] then repeat 3 [change size by -6] — a satisfying pop.",
              "Add a damage flash: repeat 3 [change color effect by 50, wait 0.05, clear graphic effects, wait 0.05].",
              "Add looping background music: forever [play sound (a music loop) until done] on the Stage.",
              "Give the game a title: a sprite that shows the name for 2 seconds at the start, then fades out with the ghost effect.",
              "Hide any variables the player doesn't need to watch.",
              "Test: play for 30 seconds with your eyes half-closed. You should still know what's happening just from sound and motion."],
             "Every action produces sound or visual feedback, and the game has a title and music.", 7)


def stage_yours(ideas):
    return S("Make it yours",
             "Add something nobody told you to add. This is the part you'll want to show people.",
             ideas + ["Invent a power-up: something collectable that changes the rules for 5 seconds.",
                      "Tune the numbers until the difficulty feels right to YOU — speed, sizes, timings.",
                      "Ask someone else to play while you watch silently. Write down every confusion you see.",
                      "Fix the single most common confusion before anything else."],
             "Your game has at least one feature that was entirely your own idea — and someone else has played it.", 6)


# ---------------------------------------------------------------------------
# Per-template core stages
# ---------------------------------------------------------------------------
def _collect():
    return [
        S("Move the player", "Give the player smooth, professional-feeling control.",
          ["On the player add: when green flag clicked → forever.",
           "Inside the forever put four separate 'if <key pressed?>' checks — right, left, up, down.",
           "Right: change x by 4 · Left: change x by -4 · Up: change y by 4 · Down: change y by -4.",
           "All four ifs must live in the SAME forever loop — that is what makes diagonals work.",
           "Add a costume flip: inside the right/left ifs, 'point in direction 90' / '-90' (rotation style left-right).",
           "Make a 'speed' variable set to 4, and use it in all four change blocks instead of the raw number.",
           "Test: drive a full lap of the stage — smooth in all 8 directions, no stutter, never upside-down."],
          "The player moves smoothly in eight directions using a speed variable.", 7),
        S("Collect the items", "Make the collectibles behave like real pickups.",
          ["On each collectible: when green flag clicked → show, go to its own fixed position.",
           "Add: forever → if <touching Player?> then [start sound pop, hide].",
           "Hiding on touch is what stops the score firing 30 times a second — never skip it.",
           "Give each collectible a gentle idle animation: forever [change size by 2, wait .3, change size by -2, wait .3].",
           "Add a 'collected' count: change it by 1 inside the touch-if, right before the hide.",
           "Test: walk over every item once — each disappears with a pop and counts exactly once."],
          "Every item can be collected exactly once, with sound, and the count is correct.", 6),
        S("The hazard and the goal", "Add danger and a destination.",
          ["Add a moving hazard: forever [move 6 steps, if on edge bounce], rotation style left-right.",
           "Start the hazard with 'point in direction (pick random 1 to 360)' so every run differs.",
           "Add the goal sprite at the far corner from the player's start.",
           "On the goal: forever → if <<touching Player?> and <collected = (number of items)>> then broadcast 'reached-goal'.",
           "If the player touches the goal too early, have it say 'Collect them all first!' for 1 second.",
           "Test: the goal refuses you until everything is collected, then triggers."],
          "The goal only accepts the player after every item is collected; the hazard patrols unpredictably.", 6),
    ]


def _catch():
    return [
        S("Move the catcher", "Control the catcher with the mouse — one axis only.",
          ["On the catcher: when green flag clicked → forever → set x to (mouse x).",
           "Do NOT use 'go to mouse-pointer' — the catcher must stay at the bottom (y around -140).",
           "Clamp it: after 'set x', add 'if <(x position) > 220> then set x to 220' and the same for -220.",
           "Test: the catcher glides left–right under your mouse and never leaves the stage or rises."],
          "The catcher tracks the mouse horizontally only, clamped to the stage.", 5),
        S("Make things fall", "Real falling-object behaviour with clones.",
          ["On the falling item: when flag clicked → hide, then forever [create clone of myself, wait (pick random 0.6 to 1.4) seconds].",
           "On 'when I start as a clone': go to x: (pick random -200 to 200) y: 180, show.",
           "Then: repeat until <(y position) < -160> [change y by -6].",
           "After the repeat: delete this clone — clones you never delete pile up and kill the frame rate.",
           "Make a 'fallspeed' variable (start 6) and use it in 'change y by (0 - fallspeed)'.",
           "Test: items rain from random positions at a steady rhythm and vanish at the bottom."],
          "A continuous, random rain of clones falls and cleans itself up.", 7),
        S("Catch, miss and the bad one", "Consequences for every outcome.",
          ["Inside the clone's fall loop add: if <touching Catcher?> then [start sound pop, change score by 1, delete this clone].",
           "When a clone reaches the bottom uncaught: change lives by -1 before deleting it.",
           "Add a BAD item sprite with the same clone pattern but rarer (wait 3 to 5 seconds).",
           "Catching the bad item costs a life — colour it clearly differently so players learn to dodge it.",
           "Every 5 points, change fallspeed by 1 — the rain gets faster as you improve.",
           "Test: catch scores, miss costs, bad item punishes, and it speeds up at 5, 10, 15…"],
          "All three outcomes work and the game accelerates every 5 points.", 7),
    ]


def _dodge():
    return [
        S("Move the player", "Responsive eight-way control.",
          ["when green flag clicked → forever with four 'if <key pressed?>' checks inside, ±4 on x and y.",
           "All four ifs in ONE forever loop; rotation style left-right.",
           "Add a dash: if <key space pressed?> then set speed to 8, else set speed to 4 — use 'speed' in every move.",
           "Test: smooth in 8 directions, and space visibly doubles your speed."],
          "Eight-way movement with a working dash on space.", 6),
        S("Send in the hazards", "Three different threats, not one.",
          ["Hazard 1: forever [move 7 steps, if on edge bounce], random start direction.",
           "Hazard 2: same pattern, speed 5, start it in the opposite corner.",
           "Hazard 3 (the hunter): forever [point towards Player, move 2.5 steps] — slow but relentless.",
           "Set all three to rotation style left-right and sizes 60–75%.",
           "Test: three visibly different behaviours share the stage; the hunter always creeps toward you."],
          "Two bouncers and a hunter patrol the stage with distinct behaviour.", 7),
        S("Survive and score", "Time is your score; contact is your enemy.",
          ["Player damage: forever → if touching ANY hazard (use 'or') then [change lives by -1, go to start, wait 1 seconds].",
           "Survival score: forever [wait 1 seconds, change score by 1].",
           "Every 10 seconds broadcast 'speed-up'; hazards receive it and change their own speed variable by 1.",
           "Add a star that appears at a random spot every ~8 seconds; touching it gives +5.",
           "Test: score climbs each second, hazards genuinely accelerate at 10 and 20, star pays out +5."],
          "You score for surviving, lose lives fairly, and the pressure rises every 10 seconds.", 7),
    ]


def _clicker():
    return [
        S("Make it clickable", "A target worth chasing.",
          ["On the target: when this sprite clicked → change score by 1, start sound pop.",
           "After each click: go to x: (pick random -200 to 200) y: (pick random -140 to 140).",
           "Add the pop: repeat 3 [change size by 6] then repeat 3 [change size by -6].",
           "Shrink it as you score: also 'change size by -1' per click (harder every time).",
           "Test: every click scores once, the target jumps away and slowly shrinks."],
          "Clicking scores, relocates and shrinks the target.", 6),
        S("The countdown", "Pressure turns clicking into a game.",
          ["Make a 'time' variable; set it to 30 on the flag.",
           "Add: repeat until <(time) = 0> [wait 1 seconds, change time by -1] — the wait is what makes it real seconds.",
           "When time hits 0: say the final score for 2 seconds, then stop all.",
           "Under 6 seconds, make the timer flash: if <(time) < 6> then [change color effect by 40, wait .1, clear graphic effects].",
           "Test: time a full run against a real clock — it must take 30 actual seconds."],
          "A genuine 30-second countdown that flashes in the final 5 seconds and ends the game.", 6),
        S("Three targets, three rules", "Depth comes from choices.",
          ["Add a GOLD target: worth +5, visible for only 1.5 seconds at a time (show, wait 1.5, hide, wait random 3–6).",
           "Add a BOMB: clicking it costs -3 and shakes the screen (repeat 6 [change x by 6, change x by -6]).",
           "Colour the three targets so their rules are instantly readable.",
           "Track 'best combo': clicks within 1 second of each other add to a combo variable; missing resets it.",
           "Test: gold pays +5, bomb costs 3, and quick strings of clicks build a combo."],
          "Three targets with different rules and a combo bonus for fast play.", 8),
    ]


def _quiz():
    return [
        S("Play the recall quiz", "The Scratch quiz on this page IS today's warm-up — play it first.",
          ["Press the green flag on the embedded quiz and answer every question by typing.",
           "Play it twice: second time, try to beat your first score.",
           "Write down any question you got wrong — that's your revision list for today.",
           "Test: you've finished two full runs and know your best score."],
          "You have played the quiz twice and can say which questions caught you out.", 6),
        S("Design your own quiz", "Now build one — starting from a plan, not from blocks.",
          ["Open a BLANK Scratch editor (button above) — your quiz, your rules.",
           "Pick a topic you love and write 5 questions with exact answers on paper first.",
           "Add a quizmaster sprite and a backdrop that fits your topic.",
           "Give it an intro: say 'Welcome to my quiz! 5 questions — type your answers.' for 3 seconds.",
           "Test: flag click shows your intro on your chosen backdrop."],
          "Five questions are written down and your quizmaster introduces the quiz.", 6),
        S("Ask, check, respond", "The ask–check–respond pattern, five times.",
          ["Question 1: ask [your question] and wait → if <(answer) = [right answer]> then [change score by 1, say Correct! for 1] else [say (join 'It was ' [answer]) for 2].",
           "Set score to 0 BEFORE question 1 — on the flag, at the top.",
           "Build all 5 questions as one long script, testing after each one.",
           "Mix types: one number question, one word question, one trick question.",
           "For a word answer, test wrong capitalisation — Scratch's = ignores case, so 'paris' still passes.",
           "Test: a full run with all-right answers scores exactly 5; all-wrong scores 0 and teaches the right answers."],
          "Five questions score correctly and wrong answers teach the right one.", 9),
    ]


def _flappy():
    return [
        S("Flap and fall", "Real gravity, real arcs.",
          ["Make a 'velocity' variable, set it to 0 on the flag.",
           "Add: forever [change y by (velocity), change velocity by -1] — position changes by velocity, velocity by gravity.",
           "On space: set velocity to 10 — set it ONCE per press; setting it every frame makes floaty nonsense.",
           "If y position < -160 or > 175: that's a crash — broadcast 'game-over'.",
           "Tilt the bird with its speed: point in direction (90 - (velocity * 3)).",
           "Test: the fall accelerates, each tap gives a clean arc, and the bird noses up and down."],
          "The bird falls with real acceleration, flaps in arcs and tilts with its motion.", 8),
        S("The obstacle stream", "An endless, fair obstacle course.",
          ["On the obstacle: hide, then forever [create clone of myself, wait 2.2 seconds].",
           "Clone: go to x: 240 y: (pick random -80 to 120), show, then repeat until <(x position) < -235> [change x by -4], delete this clone.",
           "Add a SECOND obstacle sprite with a different costume, offset its first wait by 1.1 seconds so the stream alternates.",
           "Bird collision: if touching either obstacle → broadcast 'game-over'.",
           "Test: an even, alternating stream you can genuinely fly through."],
          "Two alternating obstacle streams cross the screen and crashes register.", 7),
        S("Score the gaps", "Score, coins and rising speed.",
          ["Score +1 when an obstacle's x position passes the bird's x (check once per clone with a 'scored' flag).",
           "Add a coin between obstacles: same clone pattern, +5 and a sparkle sound when touched.",
           "Every 5 points broadcast 'faster'; obstacle clones move -5 then -6 as it stacks.",
           "On 'game-over': show the score, stop all — and your restart button from the endings stage replays it.",
           "Test: passing scores exactly once each, coins pay +5, and it genuinely gets faster."],
          "Passing scores once, coins pay bonus, and speed rises every 5 points.", 7),
    ]


def _pong():
    return [
        S("Paddle and ball", "The core rally.",
          ["Paddle: forever → set x to (mouse x); keep y at -140; clamp x to ±200.",
           "Ball: on flag go to 0,0, point in direction (pick random 100 to 170), then forever [move 9 steps, if on edge bounce].",
           "Test: the ball ricochets around; the paddle glides under your mouse."],
          "The ball bounces and the paddle tracks the mouse smoothly.", 5),
        S("The rally", "Bounce physics that feel fair.",
          ["Ball: if <touching Paddle?> then point in direction ((180 - direction) + pick random -10 to 10), move 10 steps, start sound boing.",
           "Add 'wait 0.15 seconds' after the bounce so one touch can't double-bounce.",
           "Speed up every hit: make a 'ballspeed' variable (start 9), use it in the move, +0.3 per paddle hit.",
           "The random ±10 stops the ball looping in one boring path forever.",
           "Test: rally ten hits — angles vary, pace rises, no double-bounces."],
          "Ten-hit rallies work with varied angles and rising speed.", 7),
        S("Bricks and lives", "Turn the rally into Breakout.",
          ["Lay a wall: 6 bricks along the top (two rows of 3, or clone a brick 6 times at calculated x positions).",
           "Each brick: if <touching Ball?> then [change score by 1, hide, broadcast 'brick-hit'].",
           "Ball receives 'brick-hit': point in direction (180 - direction) — it rebounds off the brick.",
           "Below the paddle (y < -170): lose a life, reset the ball to 0,0 pointing downward at random.",
           "Win when score = 6 (all bricks gone); lose at 0 lives.",
           "Test: clear the whole wall once and drop the ball three times — both endings fire."],
          "Six breakable bricks, rebounds, ball-drop lives — a complete Breakout loop.", 8),
    ]


def _generic():
    return [
        S("Build the core mechanic", "Make the ONE main action work perfectly before anything else.",
          ["Name the single action the player does most — moving, clicking, typing, aiming — and build only that.",
           "Give it real control values: movement ±4 per frame, glide 1s, or ask-and-wait for typing.",
           "Wire it to a forever loop so it responds constantly, not once.",
           "Add instant feedback to the action — a sound or a size pop on every use.",
           "Test the action 20 times in a row. It must work all 20 — that is what 'reliable' means."],
          "The core action works 20 times out of 20 with feedback each time.", 8),
        S("Add the challenge", "Something to overcome, different every run.",
          ["Add the obstacle/opponent/target that resists the player.",
           "Randomise it with 'pick random' — position, timing or speed — so no two runs match.",
           "Add a SECOND challenger with clearly different behaviour (speed, path or size).",
           "Give each challenger rotation style left-right and a sensible size.",
           "Test: play three runs — they must all feel different."],
          "Two distinct challengers make every run different.", 7),
        S("React and progress", "The world answers the player.",
          ["Use touching/sensing so the challenge and the player genuinely interact.",
           "Add progression: a variable that rises with success and makes something faster, bigger or more frequent.",
           "Handle the repeat-collision bug: hide, move away or wait so each event counts once.",
           "Test: cause each interaction deliberately and watch its variable change exactly once."],
          "Every interaction fires exactly once and success visibly raises the stakes.", 7),
    ]


MIDDLE = {
    "collect": _collect, "catch": _catch, "dodge": _dodge, "clicker": _clicker,
    "quiz": _quiz, "flappy": _flappy, "pong": _pong,
    "whack": _clicker, "runner": _flappy, "shooter": _dodge,
    "drive": _dodge, "animation": _generic, "chatbot": _quiz,
    "art": _generic, "music": _generic,
}

WIN_LOSE = {
    "collect": ("every item is collected and you reach the goal", "lives reach 0"),
    "catch":   ("the score reaches 20", "lives reach 0 from misses or bad items"),
    "dodge":   ("you survive 60 seconds", "lives reach 0"),
    "clicker": ("the score beats 25 before time runs out", "the timer reaches 0 first"),
    "quiz":    ("your quiz scores 4 or more out of 5", "fewer than 4 — revise and replay"),
    "flappy":  ("the score reaches 15", "you crash into an obstacle or the ground"),
    "pong":    ("all 6 bricks are broken", "you drop the ball three times"),
}

LEVEL2_TWIST = {
    "collect": "make the hazard 2 steps faster and add one more collectible in a hard-to-reach corner.",
    "catch":   "raise fallspeed by 2 and spawn the bad item twice as often.",
    "dodge":   "give every hazard +2 speed and spawn a fourth bouncing hazard.",
    "clicker": "shrink the target 20% and shorten the gold target's visit to 1 second.",
    "quiz":    "add 3 harder bonus questions worth 2 points each.",
    "flappy":  "narrow the safe gap by moving obstacle spawn heights closer together and add +1 speed.",
    "pong":    "add a second row of bricks worth 2 points each and +1 ball speed.",
}
DEFAULT_TWIST = "increase every speed variable by 2 and add one brand-new obstacle."

EXTRAS = {
    "collect": ["Add a key that must be found before the goal's door 'opens' (switch costume).",
                "Add a moving collectible that glides between two points."],
    "catch":   ["Add a golden item worth 5 that falls 1.5x faster.",
                "Give the catcher 3 costumes that change as lives drop."],
    "dodge":   ["Add a shield power-up: 3 seconds of invincibility with a ghost-effect flicker.",
                "Add a safe zone that heals 1 life if you stand in it for 3 seconds."],
    "clicker": ["Add an auto-clicker power-up: +1 per second for 5 seconds.",
                "Show 'best combo' on a results screen at the end."],
    "quiz":    ["Move your questions into LISTS so they shuffle every play.",
                "Accept two spellings of one answer using 'or'."],
    "flappy":  ["Add a day/night backdrop switch every 10 points.",
                "Add a ghost replay: a second bird that mimics your last run (advanced!)."],
    "pong":    ["Add a power-up brick that widens the paddle for 10 seconds.",
                "Add a second ball at level 2 (clone the ball!)."],
}
DEFAULT_EXTRAS = ["Add a title screen with a start button that broadcasts 'start-game'.",
                  "Add a high-score variable that only updates when beaten."]


def build_brief(template, title, sprites, backdrop):
    """Return the full staged brief for one exercise (~50 minutes)."""
    mid = MIDDLE.get(template, _generic)()
    win, lose = WIN_LOSE.get(template, ("you reach your target score", "you run out of lives or time"))
    twist = LEVEL2_TWIST.get(template, DEFAULT_TWIST)
    if template in ("quiz", "chatbot"):
        # a quiz build has its own arc: play → design → build → polish → yours
        stages = [mid[0], mid[1], mid[2],
                  stage_endings(win, lose), stage_polish(),
                  stage_yours(EXTRAS.get(template, DEFAULT_EXTRAS))]
    else:
        stages = [stage_scene(sprites, backdrop)] + mid + \
                 [stage_score(), stage_level2(twist),
                  stage_endings(win, lose), stage_polish(),
                  stage_yours(EXTRAS.get(template, DEFAULT_EXTRAS))]
    total = sum(s["minutes"] for s in stages)
    return {"stages": stages, "minutes": total,
            "taskCount": sum(len(s["tasks"]) for s in stages)}
