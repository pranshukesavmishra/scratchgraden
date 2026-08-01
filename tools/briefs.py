#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
briefs.py — MULTI-STAGE BUILD BRIEFS.

An exercise used to be a short list of hints — about five minutes of work.
A real 60-minute session needs a build the student can work at for 20-30
minutes, in stages, with something testable at the end of each one.

Every exercise now gets a staged brief:

    Stage 1  Set the scene      place sprites and backdrop, reset state
    Stage 2  Core mechanic      the thing the player does
    Stage 3  The challenge      what makes it a game
    Stage 4  Score and feedback variables, sound, effects
    Stage 5  Win and lose       endings the player understands
    Stage 6  Make it yours      extensions, so fast finishers never idle

Each stage has concrete tasks and a CHECKPOINT — "it works when ..." — so a
student always knows whether they are done, and a tutor can see progress at a
glance. Stages are generated per game template, so a catch game and a quiz get
genuinely different briefs rather than the same generic text.
"""


def S(title, goal, tasks, check, minutes):
    return {"title": title, "goal": goal, "tasks": tasks,
            "check": check, "minutes": minutes}


# ---------------------------------------------------------------------------
# Shared opening and closing stages
# ---------------------------------------------------------------------------
def stage_scene(sprites, backdrop):
    names = ", ".join(sprites[:5]) if sprites else "your sprites"
    return S("Set the scene",
             "Get everything on the stage and reset properly, so the game starts the same way every time.",
             ["Add the backdrop%s." % ((" (" + backdrop + ")") if backdrop else ""),
              "Add these sprites: %s." % names,
              "Give each sprite a sensible size and starting position.",
              "On every sprite add: when green flag clicked -> go to its start position, show, set size to 100%.",
              "Test: press the green flag twice. Everything must return to exactly the same place."],
             "Pressing the flag twice puts every sprite back in its starting place.", 5)


def stage_polish():
    return S("Feedback and polish",
             "Make every action feel good. This is what separates a finished game from a demo.",
             ["Add a sound to every important action (collect, hit, win, lose).",
              "Add a visual effect for one action — a grow, a fade or a colour flash.",
              "Show the score and any other variables the player needs.",
              "Hide any variables the player does not need to see.",
              "Test: play for 30 seconds. Can you tell what is happening without anyone explaining?"],
             "Every action gives the player sound or visual feedback.", 4)


def stage_endings(win, lose):
    return S("Win and lose",
             "Give the game clear endings, so the player always knows how they did.",
             ["Write your rules in plain English first: 'You win when ...' and 'You lose when ...'.",
              "Add the win check: %s" % win,
              "Add the lose check: %s" % lose,
              "Say a message FIRST, wait 2 seconds, and only THEN use 'stop all'.",
              "Switch to a win or lose backdrop so the ending is obvious.",
              "Test BOTH endings deliberately — do not assume they work."],
             "You have triggered the win ending and the lose ending on purpose, and both work.", 5)


def stage_yours(ideas):
    return S("Make it yours",
             "Add something nobody told you to add. This is the part you will want to show people.",
             ideas + ["Change the numbers until the difficulty feels right to YOU.",
                      "Ask someone else to play it and watch them silently."],
             "Your game has at least one feature that was your own idea.", 4)


# ---------------------------------------------------------------------------
# Per-template middle stages (the actual game mechanics)
# ---------------------------------------------------------------------------
def _collect():
    return [
        S("Move the player", "Give the player smooth control.",
          ["Add: when green flag clicked -> forever.",
           "Inside the forever, add four 'if <key pressed?>' checks — one per arrow key.",
           "Right: change x by 4. Left: change x by -4. Up: change y by 4. Down: change y by -4.",
           "Keep ALL FOUR ifs inside the SAME forever loop so diagonal movement works.",
           "Test: can you move in eight directions smoothly, including diagonally?"],
          "The player moves smoothly in all directions, including diagonals.", 6),
        S("Collect the items", "Make the collectibles actually collectable.",
          ["On each collectible: when green flag clicked -> show, go to a random position.",
           "Add a forever loop with 'if <touching Player?>'.",
           "Inside the if: play a sound, hide, and change score by 1.",
           "Hiding the item is what stops the score jumping up 30 times a second.",
           "Test: collect every item. The score must go up by exactly 1 each time."],
          "Each item can be collected once and adds exactly one point.", 6),
        S("Add a hazard", "Make it a game, not a shopping trip.",
          ["Add a hazard sprite that moves — use 'forever [move 6 steps, if on edge bounce]'.",
           "Set its rotation style to left-right so it does not go upside-down.",
           "On the player: if touching the hazard, lose a life and return to the start.",
           "Add 'wait 1 seconds' after losing a life so one touch costs only one life.",
           "Test: touch the hazard once. You should lose exactly one life."],
          "Touching the hazard costs exactly one life and moves you back to the start.", 6),
    ]


def _catch():
    return [
        S("Move the catcher", "Control the catcher with the mouse.",
          ["On the catcher: when green flag clicked -> forever.",
           "Inside: 'set x to (mouse x)'. Do NOT use 'go to mouse-pointer'.",
           "Using only x keeps the catcher at the bottom where it belongs.",
           "Test: the catcher follows your mouse left and right but never moves up."],
          "The catcher slides side to side with the mouse and stays at the bottom.", 5),
        S("Make things fall", "Give the falling objects their behaviour.",
          ["On a falling item: when green flag clicked -> forever.",
           "Inside: go to x: (pick random -200 to 200) y: 180.",
           "Then 'repeat until <(y position) < -150>' containing 'change y by -6'.",
           "Test: items fall from random places at the top, all the way to the bottom."],
          "Items fall from random positions at the top down to the bottom.", 6),
        S("Catch and miss", "Score catches and punish misses.",
          ["Inside the falling loop add 'if <touching Catcher?>' -> sound, change score by 1, and restart from the top.",
           "When an item reaches the bottom without being caught, lose a life.",
           "Add a second and third falling item with different speeds so it gets busy.",
           "Add one BAD item that costs a life if you catch it.",
           "Test: catching scores, missing costs a life, and the bad item punishes you."],
          "Catching scores a point, missing costs a life, and the bad item is dangerous.", 7),
    ]


def _dodge():
    return [
        S("Move the player", "Give the player responsive control.",
          ["when green flag clicked -> forever, with four 'if <key pressed?>' checks inside.",
           "Use 'change x by 4' / 'change y by 4' and their negatives.",
           "Keep all four ifs in the same forever loop.",
           "Test: movement is smooth and diagonals work."],
          "The player moves smoothly in eight directions.", 5),
        S("Send in the hazards", "Make the hazards move and threaten.",
          ["On each hazard: forever [move 7 steps, if on edge bounce].",
           "Set rotation style to left-right.",
           "Start each hazard with 'point in direction (pick random 1 to 360)' so runs differ.",
           "Add at least THREE hazards, each with a different speed.",
           "Test: the hazards never leave the stage and each run looks different."],
          "Three hazards patrol the stage at different speeds and never escape.", 6),
        S("Survive", "Add damage, survival scoring and rising difficulty.",
          ["On the player: forever [if <touching any hazard?> then change lives by -1, go to start, wait 1 seconds].",
           "Add a survival score: forever [wait 1 seconds, change score by 1].",
           "Every 10 points, speed the hazards up by 1 — use a speed variable.",
           "Test: the game gets noticeably harder the longer you survive."],
          "You take damage fairly, score for surviving, and the game speeds up over time.", 7),
    ]


def _clicker():
    return [
        S("Make it clickable", "Turn the target into something worth clicking.",
          ["On the target: when this sprite clicked -> change score by 1, play a sound.",
           "Add a pop effect: repeat 3 [change size by 6] then repeat 3 [change size by -6].",
           "After each click, jump to a random position so it must be chased.",
           "Test: every click scores exactly one point and the target moves."],
          "Clicking scores a point, plays a sound and moves the target.", 6),
        S("Add the pressure", "Add a timer so the game has a shape.",
          ["Create a 'time' variable and set it to 30 at the start.",
           "Add: repeat until <(time) = 0> [wait 1 seconds, change time by -1].",
           "The 'wait 1 seconds' is essential — without it the timer empties instantly.",
           "When time hits 0, say the final score and stop all.",
           "Test: the countdown takes exactly 30 real seconds."],
          "A 30-second countdown runs at the right speed and ends the game.", 6),
        S("Helpers and bonuses", "Add depth so it is not just one button.",
          ["Add a bonus target worth 5 points that appears only sometimes.",
           "Add a penalty target that costs 3 points if clicked.",
           "Make the main target shrink slightly each time it is clicked, so it gets harder.",
           "Test: all three targets behave differently and scoring is correct."],
          "Three different targets each affect the score in their own way.", 7),
    ]


def _quiz():
    return [
        S("Ask the first question", "Build the ask-check-respond pattern once, properly.",
          ["Add 'ask [your question] and wait'.",
           "Add 'if <(answer) = [correct answer]> then ... else ...'.",
           "In the 'then': change score by 1 and say 'Correct!'.",
           "In the 'else': say the right answer so the player learns something.",
           "Test: try a right answer AND a wrong answer."],
          "One question scores correctly and gives useful feedback either way.", 6),
        S("Build the full quiz", "Turn one question into a real quiz.",
          ["Set score to 0 at the very start — before the first question.",
           "Add at least FIVE questions, each with its own check.",
           "Vary the question types: numbers, words, and one trick question.",
           "Test: answer everything correctly and check the score is exactly 5."],
          "Five questions each score correctly and the total is right.", 8),
        S("Grade the player", "Give a meaningful result, not just a number.",
          ["At the end, compare the score with thresholds using '>'.",
           "Over 4: 'Excellent!'  Over 2: 'Good work.'  Otherwise: 'Practise and try again.'",
           "Show the score out of the total, not just the raw number.",
           "Test: deliberately score high, medium and low, and check each message."],
          "The quiz gives a different, sensible message for high, medium and low scores.", 6),
    ]


def _flappy():
    return [
        S("Flap and fall", "Build the physics that make this game feel right.",
          ["Create a 'velocity' variable and set it to 0 at the start.",
           "Add: forever [change y by (velocity), change velocity by -1].",
           "Add: when space key pressed -> set velocity to 10.",
           "Set velocity ONCE on the press — do not set it every frame or it will float.",
           "Test: the bird falls faster and faster, and each tap gives a proper arc."],
          "The bird accelerates as it falls and arcs upward on each flap.", 7),
        S("Obstacles to fly through", "Make something to avoid.",
          ["Each obstacle: forever [set x to 240, glide to x: -240 at a random height].",
           "Give each obstacle a different starting delay so they are spread out.",
           "Add at least TWO obstacles for a steady stream.",
           "Test: obstacles cross the screen continuously at varying heights."],
          "A steady stream of obstacles crosses the screen at different heights.", 6),
        S("Crash and score", "Add the consequences.",
          ["On the bird: if touching an obstacle, or y position < -170, then game over.",
           "Score 1 point each time an obstacle passes the bird without hitting it.",
           "Add a collectible coin worth 5 points that appears between obstacles.",
           "Test: crashing ends the game and passing an obstacle scores."],
          "Crashing ends the game, surviving an obstacle scores a point.", 7),
    ]


def _pong():
    return [
        S("Paddle and ball", "Get the core moving.",
          ["Paddle: forever [set x to (mouse x)].",
           "Ball: point in direction (pick random 45 to 135), then forever [move 8 steps, if on edge bounce].",
           "Test: the paddle follows the mouse and the ball bounces off the walls."],
          "The paddle tracks the mouse and the ball bounces around the stage.", 6),
        S("Hit the ball", "Make the paddle matter.",
          ["On the ball: if <touching Paddle?> then turn 180 degrees (plus a small random turn) and play a sound.",
           "Add 'wait 0.2 seconds' after the bounce so it cannot trigger twice.",
           "Speed the ball up slightly on every hit.",
           "Test: the ball bounces off the paddle and gets gradually faster."],
          "The ball bounces off the paddle reliably and speeds up as you rally.", 7),
        S("Bricks and lives", "Turn it into a full game.",
          ["Add at least FOUR bricks across the top.",
           "Each brick: if touching the ball, hide, score 1, and make the ball turn 180.",
           "If the ball goes below the paddle, lose a life and reset the ball.",
           "Win when every brick is hidden.",
           "Test: clearing all bricks wins, dropping the ball three times loses."],
          "Breaking every brick wins the game; missing three times loses it.", 8),
    ]


def _generic(title):
    return [
        S("Build the core mechanic", "Make the main thing the player does actually work.",
          ["Decide the ONE action the player performs most — moving, clicking, typing or aiming.",
           "Build just that, with nothing else, and test it on its own.",
           "Make it feel good before adding anything else: right speed, instant response.",
           "Test: the main action works every single time you try it."],
          "The main player action works reliably and feels responsive.", 7),
        S("Add the challenge", "Give the player something to overcome.",
          ["Add the obstacle, opponent or target that makes this a challenge.",
           "Use 'pick random' so it is different on every play.",
           "Add a SECOND one with different behaviour or speed.",
           "Test: two runs of the game should not look identical."],
          "There is a real challenge, and each play is different.", 7),
        S("Score and progress", "Let the player see how they are doing.",
          ["Create a score variable and set it to 0 at the start.",
           "Change the score at the right moment — and stop it firing repeatedly.",
           "Show the score on the stage.",
           "Make the game get harder as the score rises.",
           "Test: the score only changes when it should."],
          "The score is accurate, visible, and the game gets harder as it rises.", 6),
    ]


MIDDLE = {
    "collect": _collect, "catch": _catch, "dodge": _dodge, "clicker": _clicker,
    "quiz": _quiz, "flappy": _flappy, "pong": _pong,
    "whack": _clicker, "runner": _flappy, "shooter": _dodge,
    "drive": _dodge, "animation": _generic, "chatbot": _quiz,
    "art": _generic, "music": _generic,
}

WIN_LOSE = {
    "collect": ("all items collected and the player reaches the goal", "lives reach 0"),
    "catch":   ("the score passes your target", "lives reach 0 after too many misses"),
    "dodge":   ("you survive until the timer ends", "lives reach 0"),
    "clicker": ("the score passes your target before time runs out", "the timer reaches 0 first"),
    "quiz":    ("the score is above your pass mark", "the score is below the pass mark"),
    "flappy":  ("the score passes your target", "you crash or fall off the bottom"),
    "pong":    ("every brick is broken", "you miss the ball three times"),
}

EXTRAS = {
    "collect": ["Add a second level with a new backdrop and more items.",
                "Add a power-up that makes the player faster for 5 seconds."],
    "catch":   ["Add a golden item worth 5 points that falls faster.",
                "Make items fall faster every 10 points."],
    "dodge":   ["Add a shield power-up that protects you for 3 seconds.",
                "Add a hazard that chases the player instead of bouncing."],
    "clicker": ["Add a combo bonus for clicking several times quickly.",
                "Add a target that must be avoided completely."],
    "quiz":    ["Use a list so questions are asked in a random order.",
                "Accept two different spellings as correct."],
    "flappy":  ["Add a moving obstacle that goes up and down.",
                "Add a high score that survives between games."],
    "pong":    ["Add a second row of bricks worth double points.",
                "Add a power-up brick that makes the paddle wider."],
}

DEFAULT_EXTRAS = ["Add a title screen with a start button.",
                  "Add a second level that is harder than the first.",
                  "Add a high-score variable that only updates when beaten."]


def build_brief(template, title, sprites, backdrop):
    """Return the full staged brief for one exercise."""
    mid = MIDDLE.get(template, _generic)(*([] if template in MIDDLE and MIDDLE[template] is not _generic else [title]))
    win, lose = WIN_LOSE.get(template, ("you reach your target score", "you run out of lives or time"))
    stages = [stage_scene(sprites, backdrop)] + mid + \
             [stage_endings(win, lose), stage_polish(),
              stage_yours(EXTRAS.get(template, DEFAULT_EXTRAS))]
    total = sum(s["minutes"] for s in stages)
    return {"stages": stages, "minutes": total,
            "taskCount": sum(len(s["tasks"]) for s in stages)}
