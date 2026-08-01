#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
spine.py — the CURRICULUM SPINE.

One coherent scope & sequence: 2 levels x 50 sessions = 100 sessions.
Each session pairs a teaching concept (from concepts.py) with the single best
piece of real content we have:

  project   one of the 28 imported Raspberry Pi / Code Club projects
  exercise  one of the 90 generated game exercises
  build     an open build/consolidation session using the concept only

Each session also carries its own homework and a recall focus, so a tutor can
run the session and set work afterwards without inventing anything.

Run nothing here directly — build_platform.py consumes it.
"""

# (concept_key, title, content_kind, content_ref, homework)
# content_kind: "project" | "exercise" | "build"

LEVEL1 = [
 ("tour",           "Welcome to Scratch",              "build",   None,               "Open Scratch at home and make the cat say your name."),
 ("sequence",       "Steps in order",                  "exercise","S1E1",             "Put 4 blocks in an order that draws a path; screenshot it."),
 ("motion-steps",   "Move and turn",                   "exercise","S1E2",             "Make your sprite walk a square path."),
 ("looks-say",      "Say hello",                       "project", "space-talk",       "Add one more line of dialogue to your space scene."),
 ("looks-say",      "Two sprites talking",             "exercise","S1E3",             "Write a 4-line conversation between two sprites."),
 ("costumes",       "Costumes and characters",         "exercise","S2E1",             "Give your sprite 3 costumes and switch between them."),
 ("animation-loop", "Your first loop",                 "project", "lost-in-space",    "Change the repeat number and describe what changed."),
 ("animation-loop", "Animate a walk",                  "exercise","S2E2",             "Animate a sprite walking across the stage."),
 ("forever",        "Forever loops",                   "exercise","S2E3",             "Make a sprite that spins forever."),
 ("events-key",     "Press a key",                     "exercise","S3E1",             "Add a key that makes your sprite say something."),
 ("events-key",     "Arrow key controls",              "exercise","S3E2",             "Drive your sprite with all four arrow keys."),
 ("events-click",   "Click to interact",               "project", "surprise-animation","Add a second clickable sprite with its own surprise."),
 ("events-click",   "An interactive scene",            "exercise","S3E3",             "Make 3 sprites that each react differently to a click."),
 ("coordinates",    "X and Y coordinates",             "exercise","S4E1",             "Place 4 sprites at 4 exact coordinates."),
 ("coordinates",    "Coordinate challenge",            "exercise","S4E2",             "Move a sprite in a diamond using go-to blocks."),
 ("glide",          "Smooth gliding",                  "exercise","S4E3",             "Make a rocket glide across the stage."),
 ("glide",          "Journeys and timing",             "project", "silly-eyes",       "Make your character follow the mouse smoothly."),
 ("backdrops",      "Backdrops and scenes",            "exercise","S5E1",             "Build a 2-scene story."),
 ("size-effects",   "Size, show and hide",             "exercise","S5E2",             "Make an item fade out and disappear."),
 ("sound-play",     "Adding sound",                    "project", "rock-band",        "Add one more instrument to your band."),
 ("sound-play",     "Sound effects everywhere",        "exercise","S5E3",             "Give every action in your project a sound."),
 ("wait-timing",    "Timing and waits",                "exercise","S6E1",             "Choreograph 3 things happening in order."),
 ("if-basic",       "If ... then",                     "exercise","S6E2",             "Make a sprite react when it touches another."),
 ("sensing-touch",  "Sensing a touch",                 "project", "catch-the-bus",    "Make the bus react differently when caught."),
 ("sensing-touch",  "Collect and avoid",               "exercise","S6E3",             "Build a scene with one good and one bad object."),
 ("sensing-touch",  "Colour sensing",                  "project", "boat-race",        "Draw your own track and race it."),
 ("sensing-key",    "Smooth controls",                 "exercise","S7E1",             "Convert your player to smooth 4-way control."),
 ("random",         "Random numbers",                  "exercise","S7E2",             "Make a target appear in a random place."),
 ("random",         "Unpredictable games",             "project", "catch-the-dots",   "Change the speed and describe how it feels."),
 ("variable-score", "Keeping score",                   "project", "balloons",         "Add a bonus balloon worth 5 points."),
 ("variable-score", "Score in your game",              "exercise","S7E3",             "Add a working score to a collecting game."),
 ("variable-score", "Score and targets",               "project", "beat-the-goalie",  "Change the goal target and test it."),
 ("if-else",        "If ... else",                     "exercise","S8E1",             "Give your game a win message and a lose message."),
 ("repeat-until",   "Repeat until",                    "exercise","S8E2",             "Make a sprite chase until it catches the target."),
 ("mouse-follow",   "Follow the mouse",                "exercise","S8E3",             "Build a paddle that follows the mouse."),
 ("mouse-follow",   "Aim and shoot",                   "project", "archery",          "Add a moving target for extra difficulty."),
 ("bounce",         "Bouncing and edges",              "exercise","S9E1",             "Build a bouncing ball that never leaves the stage."),
 ("bounce",         "Patrolling enemies",              "exercise","S9E2",             "Make an enemy patrol back and forth."),
 ("debug-basics",   "Finding bugs",                    "project", "find-the-bug",     "Break a project on purpose, then fix it."),
 ("debug-basics",   "Debug detective",                 "exercise","S9E3",             "Fix 2 bugs and write down what you tried."),
 ("game-win-lose",  "Winning and losing",              "exercise","S10E1",            "Write your win and lose rules in English, then code them."),
 ("game-win-lose",  "Game over screens",               "exercise","S10E2",            "Add a game-over backdrop and message."),
 ("sensing-touch",  "Dodge and survive",               "project", "dodgeball",        "Add a second dodgeball with a different speed."),
 ("variable-score", "Score, time and challenge",       "exercise","S10E3",            "Add a score and a target to beat."),
 ("game-win-lose",  "Balancing your game",             "exercise","S11E1",            "Make your game easier, then harder. Which is more fun?"),
 ("l1-capstone",    "Capstone: plan your game",        "build",   None,               "Write your game plan: goal, controls, rules."),
 ("l1-capstone",    "Capstone: build the controls",    "build",   None,               "Build and test your player controls."),
 ("l1-capstone",    "Capstone: objective and score",   "build",   None,               "Add your objective and scoring."),
 ("l1-capstone",    "Capstone: endings and polish",    "build",   None,               "Add win/lose endings and sounds."),
 ("l1-capstone",    "Capstone: present your game",     "build",   None,               "Show your game to your family and note their feedback."),
]

LEVEL2 = [
 ("operators-math",    "Maths in code",                "exercise","S12E1",            "Make a bonus that doubles your points."),
 ("operators-compare", "Comparing values",             "exercise","S12E2",            "Trigger a level-up when the score passes 10."),
 ("operators-logic",   "and, or, not",                 "exercise","S12E3",            "Write a truth table for two conditions."),
 ("operators-logic",   "Two conditions to win",        "exercise","S13E1",            "Require the goal AND all items to win."),
 ("variable-timer",    "Timers and countdowns",        "project", "ghostbusters",     "Change the time limit and test the difficulty."),
 ("variable-timer",    "Beat the clock",               "exercise","S13E2",            "Add a 30-second limit to your game."),
 ("variable-lives",    "Lives and health",             "exercise","S13E3",            "Add a 3-life system with respawn."),
 ("variable-lives",    "Health bars",                  "exercise","S14E1",            "Show health with costumes or size."),
 ("ask-answer",        "Ask and answer",               "project", "chatbot",          "Teach your chatbot 2 new questions."),
 ("ask-answer",        "Remembering answers",          "exercise","S14E2",            "Build a chatbot that remembers 3 facts."),
 ("quiz-logic",        "Checking answers",             "project", "brain-game",       "Add 3 more questions to your quiz."),
 ("quiz-logic",        "Scoring a quiz",               "project", "guess-the-flag",   "Add a percentage score at the end."),
 ("quiz-logic",        "Your own quiz",                "exercise","S14E3",            "Make a 5-question quiz on a topic you love."),
 ("broadcast",         "Broadcast and receive",        "project", "broadcasting-spells","Add a third spell with its own message."),
 ("broadcast",         "Coordinating sprites",         "exercise","S15E1",            "Replace waits with broadcasts in an old project."),
 ("broadcast-scenes",  "Game states",                  "project", "create-your-own-world","Add a third area to your world."),
 ("broadcast-scenes",  "Title and game-over screens",  "exercise","S15E2",            "Wrap your game in a title screen."),
 ("broadcast-scenes",  "Restart without bugs",         "exercise","S15E3",            "Make your game restart cleanly every time."),
 ("clones-basic",      "Clones: many from one",        "project", "clone-wars",       "Change the spawn rate and observe."),
 ("clones-basic",      "Falling objects",              "exercise","S16E1",            "Build falling objects using clones."),
 ("clones-advanced",   "Clone waves",                  "project", "space-junk",       "Add a second type of space junk."),
 ("clones-advanced",   "Patterns with clones",         "project", "synchronised-swimming","Design your own formation."),
 ("clones-advanced",   "Difficulty waves",             "exercise","S16E2",            "Make each wave faster than the last."),
 ("lists",             "Lists: storing many values",   "project", "memory",           "Make the sequence longer each round."),
 ("lists",             "List-driven quizzes",          "exercise","S16E3",            "Use lists so questions never repeat."),
 ("lists",             "High score tables",            "exercise","S17E1",            "Store the top 3 scores in a list."),
 ("myblocks",          "Make your own blocks",         "exercise","S17E2",            "Move repeated code into a named block."),
 ("myblocks",          "Refactor a project",           "exercise","S17E3",            "Refactor an old project into 3 custom blocks."),
 ("myblocks-params",   "Blocks with inputs",           "exercise","S18E1",            "Build a 'draw square (size)' block."),
 ("myblocks-params",   "Reusable tools",               "exercise","S18E2",            "Make a block with 2 inputs."),
 ("gravity",           "Gravity and jumping",          "project", "flappy-parrot",    "Tune gravity and jump height; describe the feel."),
 ("gravity",           "Jump physics",                 "exercise","S18E3",            "Add a jump with a proper arc."),
 ("platformer",        "Platform collision",           "exercise","S19E1",            "Stop your player falling through the floor."),
 ("platformer",        "Build a level",                "exercise","S19E2",            "Design a 3-platform level."),
 ("pen",               "Drawing with the pen",         "project", "paint-box",        "Add a new colour and brush size."),
 ("pen",               "Shapes with loops",            "exercise","S19E3",            "Draw a triangle, square and hexagon."),
 ("pen-art",           "Geometric art",                "project", "butterfly-garden", "Invent your own pattern."),
 ("pen-art",           "Spirograph patterns",          "exercise","S20E1",            "Design a pattern and explain the maths."),
 ("music-blocks",      "Music with code",              "project", "music-maker",      "Compose an 8-beat rhythm."),
 ("music-blocks",      "Rhythm and melody",            "project", "binary-hero",      "Add a second musical part."),
 ("music-blocks",      "Compose a piece",              "exercise","S20E2",            "Build a 3-layer piece with a broadcast start."),
 ("game-polish",       "Game feel and juice",          "exercise","S20E3",            "Add feedback to every player action."),
 ("game-polish",       "Playtesting",                  "build",   None,               "Watch someone play your game silently. Write 3 notes."),
 ("debug-basics",      "Advanced debugging",           "build",   None,               "Fix a bug and write down how you found it."),
 ("publish-share",     "Publishing your work",         "build",   None,               "Write instructions and credits for your project."),
 ("l2-capstone",       "Capstone: write the spec",     "build",   None,               "Write a one-page spec for your final project."),
 ("l2-capstone",       "Capstone: core mechanic",      "build",   None,               "Build and test your core mechanic."),
 ("l2-capstone",       "Capstone: features",           "build",   None,               "Add your 3 features, testing each."),
 ("l2-capstone",       "Capstone: polish and test",    "build",   None,               "Polish, playtest and fix the top 2 issues."),
 ("l2-capstone",       "Capstone: present and publish","build",   None,               "Present your project and share it safely."),
]

LEVELS = [
    {"level": 1, "title": "Level 1 — Foundations",
     "blurb": "From first block to a complete game a child designs themselves. "
              "Motion, looks, events, loops, sensing, conditionals and variables.",
     "emoji": "\U0001F331", "color": "#34d399", "sessions": LEVEL1},
    {"level": 2, "title": "Level 2 — Logic, Data and Game Engineering",
     "blurb": "Real programming: operators, lists, broadcasts, clones, custom blocks, "
              "physics, pen, music, debugging and publishing.",
     "emoji": "\U0001F680", "color": "#818cf8", "sessions": LEVEL2},
]


def build_sessions():
    """Flatten the spine into 100 numbered session records."""
    out = []
    for lv in LEVELS:
        for i, (ck, title, kind, ref, hw) in enumerate(lv["sessions"], start=1):
            out.append({
                "id": "L%dS%d" % (lv["level"], i),
                "level": lv["level"], "n": i, "title": title,
                "conceptKey": ck, "contentKind": kind, "contentRef": ref,
                "homework": hw,
            })
    return out
