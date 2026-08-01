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


# =====================================================================
# USES — every practical way each block gets used in real projects.
# This is what turns "here is a block" into "here is what you can DO
# with it", and gives a tutor enough material to fill a full hour.
# =====================================================================
USES = {
 "move () steps": ["Walk a character across the stage", "Drive a car forwards", "Fire a bullet in the direction it faces", "Step an enemy along a patrol route", "Draw a line of a shape with the pen"],
 "turn right () degrees": ["Turn a corner when drawing shapes", "Spin a fan, wheel or coin", "Aim a turret step by step", "Make a compass needle rotate", "Rotate a pattern in spirograph art"],
 "turn left () degrees": ["Steer a car or boat left", "Undo a turn made the other way", "Make a character look around", "Create anticlockwise spiral art"],
 "turn () degrees": ["Spin continuously inside a loop", "Wobble a sprite back and forth", "Rotate a shape a little between draws", "Make a slow hand on a clock"],
 "point in direction ()": ["Reset a sprite to face right at the start", "Make a character face up to jump", "Point a rocket before launching", "Fix an upside-down sprite"],
 "point towards ()": ["Make an enemy chase the player", "Aim a cannon at a target", "Make a flower turn to follow the sun", "Have a pet follow its owner"],
 "point towards [mouse-pointer]": ["Eyes that follow the cursor", "A turret that aims where you point", "A magnifying glass that tracks the mouse", "A shark that swims towards the pointer"],
 "go to x: () y: ()": ["Send a sprite home at the start of a game", "Respawn the player after losing a life", "Place sprites exactly when setting a scene", "Reset a ball to the centre after a goal"],
 "go to [random position]": ["Make a target pop up somewhere new", "Scatter collectibles around the stage", "Move a ghost unpredictably", "Place stars randomly in a night sky"],
 "go to [mouse-pointer]": ["Make a paddle or cursor sprite", "Drag-and-drop feeling for a paint brush", "A net that follows your hand", "A spotlight that follows the mouse"],
 "glide () secs to x: () y: ()": ["A rocket flying across space", "A lift moving between floors", "A card sliding into place", "A fish drifting across a tank", "Cutscene movement in a story"],
 "glide () secs to [random position]": ["Bees or butterflies drifting about", "A ghost floating to a new spot", "Fish wandering an aquarium", "Snowflakes moving gently"],
 "change x by ()": ["Arrow-key left/right movement", "Scroll a background sideways", "Nudge a paddle along", "Push an object when it is hit"],
 "change y by ()": ["Jumping and falling with gravity", "Make objects rain down the screen", "Move a lift up and down", "Bob a boat on waves"],
 "set x to ()": ["A paddle that follows only the mouse's x", "Snap a sprite to a lane in a runner game", "Reset horizontal position without changing height"],
 "x position": ["Check if a sprite reached the right edge", "Score based on how far the player travelled", "Keep two sprites lined up", "Decide which way an enemy should face"],
 "y position": ["Ground checks for jumping", "Detect when a falling object is off the bottom", "Height-based scoring in a climbing game", "Depth in an underwater game"],
 "if on edge, bounce": ["A ball bouncing around the stage", "A patrolling enemy", "A screensaver-style logo", "Fish that turn at the tank wall"],
 "set rotation style ()": ["Keep a walking character upright", "Let a spaceship rotate fully", "Stop a bouncing sprite going upside-down", "Make a car face its driving direction"],

 "say () for () seconds": ["Character dialogue in a story", "Explaining the rules at the start", "Reacting to being clicked", "Announcing the score or a win"],
 "say ()": ["A permanent label above a sprite", "Showing a live value while debugging", "A sign that stays on screen", "Clearing a bubble by saying nothing"],
 "think () for () seconds": ["Showing what a character is feeling", "A hint bubble in a puzzle", "Comic-style inner thoughts", "A character deciding what to do"],
 "switch costume to ()": ["Show a hurt or happy face", "Change a character's outfit", "Show a door open or closed", "Display a specific number or letter card"],
 "next costume": ["Walk and run cycles", "Flapping wings", "A spinning coin", "Flicking through cards or slides"],
 "costume number": ["Check which state a sprite is in", "Score based on which card is showing", "Only allow an action when a door costume is open"],
 "switch backdrop to ()": ["Move to a new scene in a story", "Show a game-over screen", "Change level", "Switch between day and night"],
 "next backdrop": ["Step through a slideshow", "Move to the next level", "Cycle through story scenes"],
 "when backdrop switches to ()": ["Start enemies only when the game scene begins", "Play scene music", "Hide menu sprites when play starts"],
 "set size to () %": ["Reset size at the start of a game", "Make a boss bigger than normal enemies", "Shrink a sprite that is far away"],
 "change size by ()": ["A pop effect when collecting", "Growing a balloon until it bursts", "A pulsing heartbeat", "Zooming towards the player"],
 "show": ["Bring a sprite into play", "Reveal a hidden clue", "Respawn a collectible", "Reset visibility at the start"],
 "hide": ["Remove a collected item", "Hide menu sprites during play", "Make a clone's original invisible", "Hide an enemy that has been defeated"],
 "change [ghost] effect by ()": ["Fade an item out when collected", "Make a ghost semi-transparent", "Fade in a title", "Show a sprite is invincible by flashing"],
 "change () effect by ()": ["Rainbow colour cycling", "A damage flash", "A power-up glow", "Underwater colour shifts"],
 "clear graphic effects": ["Reset appearance at the start of a game", "End a power-up effect", "Remove a fade before showing again"],

 "start sound ()": ["A jump or coin sound", "A click on a button", "An explosion", "Footsteps while walking"],
 "play sound () until done": ["A voice line that must finish", "A countdown beep sequence", "Music that plays before the next scene"],
 "stop all sounds": ["Silence everything on game over", "Stop music when returning to the menu", "Cut a long sound short"],
 "change volume by ()": ["Fade music out at the end", "Make a sound quieter as a sprite moves away", "Volume controls in a settings screen"],

 "when green flag clicked": ["Start the game", "Reset all variables and positions", "Show the title screen", "Begin background music"],
 "when [] key pressed": ["Jump with space", "Fire a bullet", "Open a menu", "Cheat or debug keys for testing"],
 "when this sprite clicked": ["Buttons and menus", "Popping balloons", "Choosing a character", "Clicking a target for points"],
 "broadcast ()": ["Start the game from a menu button", "Tell every sprite the game is over", "Trigger the next scene of a story", "Signal that a level is complete"],
 "broadcast () and wait": ["Play an intro before the game starts", "Run a cutscene fully before resuming", "Make sure all sprites reset before play"],
 "when I receive ()": ["Hide menu sprites when play starts", "Make enemies start moving", "Show a game-over message", "Reset a sprite between rounds"],

 "wait () seconds": ["Pause between lines of dialogue", "Control animation speed", "Delay an enemy spawn", "Stop a collision firing repeatedly"],
 "wait until <>": ["Wait for the player to press start", "Hold until a sprite reaches a place", "Pause until the score reaches a target"],
 "repeat ()": ["Draw a shape with equal sides", "Flap wings a set number of times", "Spawn a wave of exactly 10 enemies", "Blink three times"],
 "forever": ["Constantly check for key presses", "Keep an enemy patrolling", "Run an animation for the whole game", "Continuously check collisions"],
 "repeat until <>": ["Chase until you catch the player", "Keep falling until you hit the ground", "Count down until time runs out", "Move until you touch a wall"],
 "if <> then": ["Score a point on collision", "Jump only when on the ground", "Play a sound when a key is pressed", "Show a message when the score is high"],
 "if <> then else": ["Right or wrong answer in a quiz", "Win or lose message", "Day or night behaviour", "Enough coins to buy, or not"],
 "stop [all]": ["End the game when you win or lose", "Stop everything on a game-over screen"],
 "stop [this script]": ["End one behaviour without stopping the game", "Stop a clone's loop before deleting it", "End a patrol when an enemy is defeated"],
 "when I start as a clone": ["Give each falling object its own behaviour", "Make each bullet fly independently", "Give each enemy its own speed"],
 "create clone of ()": ["Spawn falling objects", "Fire bullets", "Make a wave of enemies", "Scatter stars or snowflakes"],
 "delete this clone": ["Remove a bullet that left the screen", "Delete a collected coin", "Clear enemies at the end of a wave"],

 "touching ()?": ["Collect a coin", "Take damage from an enemy", "Reach the goal", "Detect a bullet hitting a target"],
 "touching color ()?": ["Stay on a race track", "Stand on a platform", "Detect walls in a maze", "Detect lava or water"],
 "key () pressed?": ["Smooth four-way movement", "Hold to charge a jump", "Run faster while shift is held", "Aim while a key is down"],
 "distance to ()": ["An enemy that notices you when close", "Proximity scoring", "A magnet that attracts coins", "Sound that gets louder as you approach"],
 "mouse x": ["A paddle that slides horizontally", "Aiming a shot", "Drawing where you point"],
 "mouse y": ["A lift controlled by the mouse", "Vertical aiming", "Following the pointer in both directions"],
 "ask () and wait": ["Ask the player's name", "Quiz questions", "Choose a difficulty", "Enter a password or code"],
 "answer": ["Greet the player by name", "Check a quiz answer", "Store a choice for later", "Use a typed number in a calculation"],
 "timer": ["Time how fast the player finished", "Give a time bonus", "Trigger events after a delay", "Measure reaction speed"],
 "reset timer": ["Start a fair countdown", "Restart timing for each round", "Begin a speedrun"],

 "() + ()": ["Add a bonus to the score", "Total two values", "Increase speed over time", "Add up collected coins"],
 "() - ()": ["Take damage off health", "Work out remaining time", "Find the gap between two positions"],
 "() * ()": ["Points per coin", "A score multiplier for a streak", "Scale a value up", "Double points in a bonus round"],
 "() / ()": ["Work out an average", "Convert a score into a percentage", "Halve the speed"],
 "() mod ()": ["Do something every 5th point", "Alternate between two behaviours", "Wrap a value around a range", "Detect even and odd numbers"],
 "round ()": ["Tidy a percentage score", "Snap a position to a whole number", "Show a clean time in seconds"],
 "() < ()": ["Game over when lives are low", "Speed up when time is short", "Check if a sprite is below the ground"],
 "() = ()": ["Check a quiz answer", "Detect an exact level number", "Match a password", "Check a costume number"],
 "() > ()": ["Win when the score passes a target", "Level up at a threshold", "Detect going past the edge"],
 "<> and <>": ["Win only if you reach the goal AND collect everything", "Jump only if on the ground AND space is pressed", "Unlock a door with the key AND enough coins"],
 "<> or <>": ["Take damage from either hazard", "End on win OR lose", "Accept two different answers as correct"],
 "not <>": ["Keep moving while NOT touching a wall", "Act only when the player is not hidden", "Invert a switch"],
 "join () ()": ["Greet the player by name", "Build a score message", "Show 'Level 3 of 5'", "Combine typed answers into a sentence"],
 "pick random () to ()": ["Random enemy positions", "Random wait between spawns", "Dice rolls", "Random colours or sizes", "Pick a random question"],

 "set () to ()": ["Reset the score to 0", "Start lives at 3", "Set a timer to 30", "Store a typed answer"],
 "change () by ()": ["Add a point", "Lose a life", "Count down a timer", "Increase speed each level"],
 "show variable ()": ["Display the score", "Show lives and time", "Reveal a debug value while testing"],
 "hide variable ()": ["Hide working values from the player", "Clean up the stage for a title screen"],
 "add () to []": ["Save a high score", "Record each player's name", "Build a list of questions", "Log the order of moves"],
 "delete () of []": ["Remove a used question", "Clear a list before refilling it", "Drop the lowest score"],
 "item () of []": ["Show question number 3", "Pick a random joke", "Step through a list one at a time"],
 "length of []": ["Count how many questions remain", "Pick a random item safely", "Show how many high scores are stored"],
 "[] contains ()?": ["Check an answer against many accepted spellings", "See if a name is already saved", "Check if an item has been collected"],

 "define ()": ["A 'reset game' block", "A 'lose a life' block", "A 'draw a shape' block", "A 'spawn enemy' block"],
 "custom block": ["Call your reset routine at the start", "Reuse a damage routine anywhere", "Keep the main script short and readable"],
 "define () with inputs": ["draw square (size)", "damage (amount)", "spawn enemy (speed)", "say line (text)"],
 "custom block with number input": ["Draw shapes of different sizes", "Apply different amounts of damage", "Spawn enemies at different speeds"],

 "pen down": ["Draw a trail behind a sprite", "Sign your name", "Draw shapes with loops", "Plot a graph"],
 "pen up": ["Move without drawing", "Lift between separate shapes", "Reposition before starting a new line"],
 "erase all": ["Clear the canvas at the start", "Reset a drawing app", "Clear between pattern attempts"],
 "set pen color to ()": ["Choose a brush colour", "Colour-code different data", "Match the pen to a theme"],
 "set pen size to ()": ["Thick brush for painting", "Thin lines for detail", "Vary thickness for effect"],
 "change pen color by ()": ["Rainbow spirographs", "Gradient trails", "Colour that shifts as a sprite moves"],

 "play drum () for () beats": ["Build a drum loop", "A metronome", "Rhythm-game beats", "Sound effects for footsteps"],
 "play note () for () beats": ["Play a melody", "A doorbell or jingle", "Musical scales for learning", "A piano you can click"],
 "set tempo to ()": ["Speed a song up as the level gets harder", "Slow music for a calm scene", "Match two parts to the same speed"],
 "rest for () beats": ["Gaps that make a rhythm groove", "Space between musical phrases", "Timing a call-and-response"],
}
