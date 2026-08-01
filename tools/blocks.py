#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
blocks.py — the BLOCK REFERENCE.

Every Scratch block taught across the 100 sessions, with a plain-English
meaning a 7-12 year old can read, a worked example, and the gotcha that
catches children out.

This powers:
  • the Learn stage of each session (the blocks introduced today)
  • the Block Lab (browse every block by category, see what you've unlocked)

Fields: category, what (plain English), example, tip.
"""

CATEGORIES = {
    "Motion":    {"color": "#4c97ff", "emoji": "\U0001F3C3", "blurb": "Move, turn and position your sprite."},
    "Looks":     {"color": "#9966ff", "emoji": "\U0001F3A8", "blurb": "Costumes, size, effects and speech."},
    "Sound":     {"color": "#cf63cf", "emoji": "\U0001F50A", "blurb": "Play sounds and control volume."},
    "Events":    {"color": "#ffbf00", "emoji": "⚡",     "blurb": "Start scripts when something happens."},
    "Control":   {"color": "#ffab19", "emoji": "\U0001F501", "blurb": "Loops, waits, conditions and clones."},
    "Sensing":   {"color": "#5cb1d6", "emoji": "\U0001F441️", "blurb": "Detect touching, keys, the mouse and input."},
    "Operators": {"color": "#59c059", "emoji": "➕",     "blurb": "Maths, comparisons, logic and text."},
    "Variables": {"color": "#ff8c1a", "emoji": "\U0001F4E6", "blurb": "Store scores, lives, timers and lists."},
    "MyBlocks":  {"color": "#ff6680", "emoji": "\U0001F9E9", "blurb": "Build your own blocks."},
    "Pen":       {"color": "#0fbd8c", "emoji": "\U0001F58A️", "blurb": "Draw on the stage as your sprite moves."},
    "Music":     {"color": "#d65cd6", "emoji": "\U0001F3B5", "blurb": "Play drums and notes."},
}


def B(cat, what, example, tip):
    return {"category": cat, "what": what, "example": example, "tip": tip}


BLOCKS = {
 # ---------------- Motion ----------------
 "move () steps": B("Motion", "Moves the sprite forwards in the direction it is facing.", "move 10 steps", "One step is about one dot on the screen — 10 is small, 100 is a big jump."),
 "turn right () degrees": B("Motion", "Turns the sprite clockwise.", "turn right 90 degrees", "90 is a quarter turn, 180 is half, 360 is all the way round."),
 "turn left () degrees": B("Motion", "Turns the sprite anticlockwise.", "turn left 90 degrees", "Turning left 90 is the same as turning right 270."),
 "turn () degrees": B("Motion", "Turns the sprite by the number of degrees you choose.", "turn 15 degrees", "Small turns inside a loop make smooth spinning."),
 "point in direction ()": B("Motion", "Faces the sprite in an exact direction.", "point in direction 90", "90 is right, -90 is left, 0 is up, 180 is down."),
 "point towards ()": B("Motion", "Turns the sprite so it faces another sprite or the mouse.", "point towards Earth", "Put it in a forever loop to keep watching a moving target."),
 "point towards [mouse-pointer]": B("Motion", "Makes the sprite face wherever the mouse is.", "point towards mouse-pointer", "Great for eyes that follow you, or a turret that aims."),
 "go to x: () y: ()": B("Motion", "Jumps the sprite instantly to an exact spot.", "go to x: 0 y: 0", "x 0, y 0 is the middle of the stage."),
 "go to [random position]": B("Motion", "Jumps the sprite to a random spot on the stage.", "go to random position", "Perfect for making targets appear unpredictably."),
 "go to [mouse-pointer]": B("Motion", "Makes the sprite sit exactly on the mouse.", "go to mouse-pointer", "The sprite will cover your pointer — offset it if that's a problem."),
 "glide () secs to x: () y: ()": B("Motion", "Moves the sprite smoothly to a spot over a set time.", "glide 1 secs to x: 100 y: 50", "Use glide when you want the movement to be SEEN, not a teleport."),
 "glide () secs to [random position]": B("Motion", "Glides smoothly to a random spot.", "glide 1 secs to random position", "Nice for fish, bees or ghosts drifting around."),
 "change x by ()": B("Motion", "Moves the sprite left or right by an amount.", "change x by 10", "Negative numbers move left. This is how arrow-key movement works."),
 "change y by ()": B("Motion", "Moves the sprite up or down by an amount.", "change y by -10", "Negative moves down — that's how falling works."),
 "set x to ()": B("Motion", "Puts the sprite at an exact left/right position.", "set x to 0", "'set' jumps there; 'change' moves by an amount. Very different!"),
 "x position": B("Motion", "Reports how far left or right the sprite is.", "if (x position) > 200", "Use it to check if a sprite has reached the edge."),
 "y position": B("Motion", "Reports how far up or down the sprite is.", "if (y position) < -120", "Used for ground checks in jumping games."),
 "if on edge, bounce": B("Motion", "Turns the sprite around when it hits the edge of the stage.", "forever [move 10 steps, if on edge bounce]", "Your sprite may go upside-down — fix it with rotation style left-right."),
 "set rotation style ()": B("Motion", "Chooses how the sprite is allowed to rotate.", "set rotation style [left-right]", "Use left-right to stop characters standing on their head."),

 # ---------------- Looks ----------------
 "say () for () seconds": B("Looks", "Shows a speech bubble for a set time, then clears it.", "say Hello! for 2 seconds", "Use this one for conversations — it tidies up after itself."),
 "say ()": B("Looks", "Shows a speech bubble that stays until you change it.", "say Hello!", "It never disappears on its own — clear it with an empty say."),
 "think () for () seconds": B("Looks", "Shows a thought bubble for a set time.", "think Hmm... for 2 seconds", "Handy for showing what a character is feeling."),
 "switch costume to ()": B("Looks", "Changes the sprite to a chosen picture.", "switch costume to [jump]", "Great for showing a state — walking, jumping, hurt."),
 "next costume": B("Looks", "Moves to the sprite's next picture.", "forever [next costume, wait 0.2 seconds]", "Without a wait it's a blur — animation needs timing."),
 "costume number": B("Looks", "Reports which costume the sprite is wearing.", "if (costume number) = 2", "Useful for checking which state a sprite is in."),
 "switch backdrop to ()": B("Looks", "Changes the stage background.", "switch backdrop to [forest]", "Backdrop code usually lives on the Stage, not a sprite."),
 "next backdrop": B("Looks", "Moves to the next background.", "next backdrop", "Good for flicking through scenes in a story."),
 "when backdrop switches to ()": B("Events", "Starts a script when the scene changes.", "when backdrop switches to [forest]", "Lets scenery drive your characters."),
 "set size to () %": B("Looks", "Sets the sprite's size, where 100% is normal.", "set size to 50 %", "Always set size at the start so it resets every game."),
 "change size by ()": B("Looks", "Makes the sprite bigger or smaller by an amount.", "repeat 5 [change size by 10]", "Grow-then-shrink makes a satisfying 'pop' effect."),
 "show": B("Looks", "Makes the sprite visible.", "show", "Put this at the start — otherwise a hidden sprite stays invisible."),
 "hide": B("Looks", "Makes the sprite invisible.", "hide", "The classic bug: hiding a sprite and forgetting to show it next game."),
 "change [ghost] effect by ()": B("Looks", "Makes the sprite more or less see-through.", "repeat 10 [change ghost effect by 10]", "100 ghost = fully invisible. Great for fading out."),
 "change () effect by ()": B("Looks", "Changes a visual effect such as colour or ghost.", "change color effect by 25", "Fun for power-ups and flashing damage."),
 "clear graphic effects": B("Looks", "Removes all visual effects.", "clear graphic effects", "Add it at the start or last game's effects stay stuck on."),

 # ---------------- Sound ----------------
 "start sound ()": B("Sound", "Plays a sound and carries straight on with the code.", "start sound [pop]", "Use this for game effects so the action isn't paused."),
 "play sound () until done": B("Sound", "Plays a sound and waits for it to finish.", "play sound [cheer] until done", "Use it when the next thing must not start too early."),
 "stop all sounds": B("Sound", "Stops every sound playing.", "stop all sounds", "Handy when the game ends or restarts."),
 "change volume by ()": B("Sound", "Makes the sound louder or quieter.", "change volume by -10", "Negative numbers make it quieter."),

 # ---------------- Events ----------------
 "when green flag clicked": B("Events", "Starts the script when the green flag is pressed.", "when green flag clicked", "Every project needs one — it's how everything begins."),
 "when [] key pressed": B("Events", "Starts the script when a key is pressed.", "when [space] key pressed", "Each key needs its own script."),
 "when this sprite clicked": B("Events", "Starts the script when the player clicks this sprite.", "when this sprite clicked", "Test by clicking the sprite on the STAGE, not in the sprite list."),
 "broadcast ()": B("Events", "Sends a message that every sprite can hear.", "broadcast [game-over]", "Name messages properly — 'game-over', never 'message1'."),
 "broadcast () and wait": B("Events", "Sends a message and waits until all receivers finish.", "broadcast [intro] and wait", "Use it when the next step must not start too soon."),
 "when I receive ()": B("Events", "Starts the script when a message is sent.", "when I receive [game-over]", "One broadcast can start many sprites at once."),

 # ---------------- Control ----------------
 "wait () seconds": B("Control", "Pauses this script for a time.", "wait 1 seconds", "Use 0.1 or 0.2 for smooth animation, 1 for conversations."),
 "wait until <>": B("Control", "Pauses until something becomes true.", "wait until <touching goal?>", "Great for 'don't start until the player is ready'."),
 "repeat ()": B("Control", "Repeats the blocks inside a set number of times.", "repeat 4 [move 100 steps, turn 90 degrees]", "Blocks must go INSIDE the C-shape, not underneath."),
 "forever": B("Control", "Repeats the blocks inside for ever.", "forever [if <key pressed?> then ...]", "Nothing placed under a forever loop will ever run."),
 "repeat until <>": B("Control", "Repeats until something becomes true.", "repeat until <touching goal?> [move 5 steps]", "If the condition can never be true, the loop never stops."),
 "if <> then": B("Control", "Runs the blocks inside only when something is true.", "if <touching Enemy?> then [change lives by -1]", "Usually needs a forever loop around it so it keeps checking."),
 "if <> then else": B("Control", "Does one thing when true, a different thing when false.", "if <(answer) = Paris> then [correct] else [wrong]", "Use it when there are exactly two outcomes."),
 "stop [all]": B("Control", "Stops the whole project.", "stop all", "Say your message BEFORE stopping, or nobody can read it."),
 "stop [this script]": B("Control", "Stops just this one script.", "stop this script", "Useful for ending one behaviour without ending the game."),
 "when I start as a clone": B("Control", "Runs for each new clone that is made.", "when I start as a clone [show, glide...]", "Each clone runs this separately with its own position."),
 "create clone of ()": B("Control", "Makes a copy of a sprite while the game runs.", "create clone of [myself]", "One sprite plus clones beats making 50 sprites by hand."),
 "delete this clone": B("Control", "Removes this clone.", "delete this clone", "Always delete clones when done or the project slows to a crawl."),

 # ---------------- Sensing ----------------
 "touching ()?": B("Sensing", "Reports true when this sprite is touching another.", "if <touching Enemy?> then ...", "Collision often fires many times a second — hide or wait to stop repeats."),
 "touching color ()?": B("Sensing", "Reports true when the sprite touches a colour.", "if <touching color #00ff00?> then ...", "Pick the colour with the eyedropper — it must match exactly."),
 "key () pressed?": B("Sensing", "Reports true while a key is held down.", "forever [if <key [right arrow] pressed?> then change x by 4]", "Smoother than key events — no delay before it repeats."),
 "distance to ()": B("Sensing", "Reports how far away another sprite or the mouse is.", "if <(distance to [Player]) < 50> then ...", "Great for 'enemy notices you when you get close'."),
 "mouse x": B("Sensing", "Reports the mouse's left/right position.", "set x to (mouse x)", "Use it for a paddle that slides side to side only."),
 "mouse y": B("Sensing", "Reports the mouse's up/down position.", "set y to (mouse y)", "Combine with mouse x to follow the pointer exactly."),
 "ask () and wait": B("Sensing", "Asks the player a question and waits for them to type.", "ask [What's your name?] and wait", "The reply goes into the 'answer' block."),
 "answer": B("Sensing", "Holds whatever the player last typed.", "say (join [Hello ] (answer))", "The NEXT ask overwrites it — store it in a variable straight away."),
 "timer": B("Sensing", "Reports how many seconds since the timer was reset.", "if (timer) > 30 then [stop all]", "Reset it at the start or it counts from when Scratch opened."),
 "reset timer": B("Sensing", "Sets the timer back to zero.", "reset timer", "Do this when the game starts so timing is fair."),

 # ---------------- Operators ----------------
 "() + ()": B("Operators", "Adds two numbers together.", "set score to ((score) + (5))", "Green blocks go INSIDE other blocks' slots."),
 "() - ()": B("Operators", "Takes one number away from another.", "set lives to ((lives) - (1))", "Or use 'change lives by -1', which is shorter."),
 "() * ()": B("Operators", "Multiplies two numbers.", "set score to ((coins) * (10))", "Perfect for 'each coin is worth 10 points'."),
 "() / ()": B("Operators", "Divides one number by another.", "set half to ((score) / (2))", "Can give long decimals — wrap it in 'round'."),
 "() mod ()": B("Operators", "Gives the remainder after dividing.", "if ((score) mod (5)) = 0 then [speed up]", "Brilliant for 'every 5th point, do something'."),
 "round ()": B("Operators", "Rounds a number to the nearest whole number.", "round (3.7)", "Gives 4. Keeps scores looking tidy."),
 "() < ()": B("Operators", "Reports true when the first number is smaller.", "if <(lives) < 1> then [game over]", "Safer than '=' because values can skip past."),
 "() = ()": B("Operators", "Reports true when two values are the same.", "if <(answer) = [Paris]> then ...", "For letters it ignores capitals, so 'paris' still matches."),
 "() > ()": B("Operators", "Reports true when the first number is bigger.", "if <(score) > 9> then [you win]", "Use > instead of = for scores that jump by 2 or 5."),
 "<> and <>": B("Operators", "True only when BOTH conditions are true.", "<touching goal?> and <(score) > 9>", "Both must be true — like 'finish dinner AND tidy up'."),
 "<> or <>": B("Operators", "True when EITHER condition is true.", "<touching Enemy?> or <touching Spike?>", "Only one needs to be true."),
 "not <>": B("Operators", "Flips true into false and false into true.", "repeat until <not <touching ground?>>", "Reads as 'while NOT touching'."),
 "join () ()": B("Operators", "Sticks two pieces of text together.", "join [Hello ] (answer)", "Remember the space at the end of 'Hello ' or words run together."),
 "pick random () to ()": B("Operators", "Gives a different random number each time.", "go to x: (pick random -200 to 200) y: 150", "Keep x within -200..200 or your sprite lands off the stage."),

 # ---------------- Variables ----------------
 "set () to ()": B("Variables", "Puts an exact value into a variable.", "set score to 0", "Always reset score, lives and timers at the start of a game."),
 "change () by ()": B("Variables", "Adds to what a variable already holds.", "change score by 1", "Use a negative number to take away."),
 "show variable ()": B("Variables", "Shows the variable on the stage.", "show variable [score]", "Players need to see the score to care about it."),
 "hide variable ()": B("Variables", "Hides the variable from the stage.", "hide variable [score]", "Hide working variables the player doesn't need to see."),
 "add () to []": B("Variables", "Adds an item to the end of a list.", "add (answer) to [names]", "Lists hold many values; a variable holds only one."),
 "delete () of []": B("Variables", "Removes one item from a list.", "delete 1 of [names]", "'delete all' clears the list — do that before refilling it."),
 "item () of []": B("Variables", "Reads the item at a position in a list.", "item 1 of [questions]", "Lists start at 1 in Scratch, not 0."),
 "length of []": B("Variables", "Reports how many items a list holds.", "item (pick random 1 to (length of [questions])) of [questions]", "This pattern picks a random item safely."),
 "[] contains ()?": B("Variables", "Reports true if the list holds a value.", "if <[answers] contains (answer)?> then ...", "Handy for checking an answer against many possibilities."),

 # ---------------- My Blocks ----------------
 "define ()": B("MyBlocks", "The script that says what your own block does.", "define [reset player]", "Name it in plain English — 'reset player', not 'block1'."),
 "custom block": B("MyBlocks", "A block you invented, used like any other block.", "reset player", "Move repeated code here and your main script gets much clearer."),
 "define () with inputs": B("MyBlocks", "Your own block that takes a value.", "define [draw square (size)]", "Drag the orange input from the hat into the blocks inside."),
 "custom block with number input": B("MyBlocks", "Uses your block with a value you choose.", "draw square (100)", "One block with an input beats five nearly identical blocks."),

 # ---------------- Pen ----------------
 "pen down": B("Pen", "Starts drawing a line as the sprite moves.", "pen down", "Needs the Pen extension, added from the bottom-left button."),
 "pen up": B("Pen", "Stops drawing.", "pen up", "Lift the pen before moving into position, or you draw a stray line."),
 "erase all": B("Pen", "Clears everything drawn on the stage.", "erase all", "Start every pen project with this or old drawings pile up."),
 "set pen color to ()": B("Pen", "Chooses the colour to draw with.", "set pen color to [#ff0000]", "Change it inside a loop for rainbow patterns."),
 "set pen size to ()": B("Pen", "Chooses how thick the line is.", "set pen size to 5", "Thick lines for bold art, thin for detail."),
 "change pen color by ()": B("Pen", "Shifts the pen colour a little.", "repeat 36 [change pen color by 5, ...]", "This is how rainbow spirographs are made."),

 # ---------------- Music ----------------
 "play drum () for () beats": B("Music", "Plays a drum sound for a number of beats.", "play drum (1) for 0.25 beats", "Needs the Music extension. Put it in a loop to make a rhythm."),
 "play note () for () beats": B("Music", "Plays a musical note for a number of beats.", "play note (60) for 0.5 beats", "60 is middle C. Higher numbers are higher notes."),
 "set tempo to ()": B("Music", "Sets how fast the music plays.", "set tempo to 100", "Bigger number = faster music."),
 "rest for () beats": B("Music", "A silent gap in the music.", "rest for 0.25 beats", "Silence is part of rhythm — it's what makes a beat groove."),
}

# Short aliases used in a few concept lists.
ALIASES = {
    "move": "move () steps",
    "turn": "turn right () degrees",
    "wait": "wait () seconds",
}

# Placeholders that are not real blocks (used by capstone concepts).
PLACEHOLDERS = {"all Level 1 blocks", "all Level 2 blocks", "project notes", "share"}


def resolve(label):
    """Map a concept's block label to a real block key, or None."""
    if label in BLOCKS:
        return label
    if label in ALIASES:
        return ALIASES[label]
    return None
