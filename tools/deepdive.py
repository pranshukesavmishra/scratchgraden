#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deepdive.py — the SUBJECT CONTENT for each topic.

concepts.py answers "how do I teach this?".
This file answers "what IS this?" — the actual material a tutor teaches and a
student reads: a proper explanation, worked code examples, why it matters, the
real-world link, and where the idea goes next.

Together they give a tutor enough substance to fill a full hour instead of
running out of things to say after fifteen minutes.

Fields per concept:
  explain  : 2-4 short teaching paragraphs (the actual subject matter)
  examples : worked code examples  {title, code, note}
  why      : why this matters in programming
  real     : where children have already met this idea in real life
  extend   : further possibilities to explore if there is time
"""


def D(explain, examples, why, real, extend):
    return {"explain": explain, "examples": examples, "why": why,
            "real": real, "extend": extend}


def E(title, code, note):
    return {"title": title, "code": code, "note": note}


DEEP = {}

DEEP["tour"] = D(
 ["Scratch is made of four areas. The **stage** is the screen where your project happens. The **sprite list** below it holds every character. The **block palette** on the left holds the instructions, sorted by colour. The **code area** in the middle is where you build.",
  "Every sprite carries its own code, its own costumes and its own sounds. That is important: if you click the wrong sprite, you will write code in the wrong place. Professional programmers call this 'scope' — where a piece of code belongs.",
  "Blocks only run when something tells them to. Clicking a block runs it once. A hat block on top makes it run whenever an event happens. Nothing in Scratch happens by accident."],
 [E("Your first script", "when green flag clicked\nsay [Hello!] for 2 seconds\nmove 50 steps",
    "The hat block listens for the flag. Everything below runs in order."),
  E("Testing one block", "move 10 steps",
    "Click a block on its own to run it immediately — the fastest way to find out what it does.")],
 "Knowing where code lives is the difference between fixing a bug in ten seconds and hunting for it for ten minutes.",
 "A TV remote only works when you press a button — the press is the event, the channel change is the code.",
 ["Add a second sprite and give it its own code", "Try the same script on the Stage and see what changes", "Rename sprites so you can tell them apart"])

DEEP["sequence"] = D(
 ["A sequence is instructions carried out in order, one after another. The computer never skips ahead and never guesses what you meant — it does exactly what you wrote, in the order you wrote it.",
  "This is why the same blocks in a different order give a different result. 'Move then turn' draws a different path from 'turn then move'.",
  "A set of ordered steps that solves a problem has a name: an **algorithm**. Children already write algorithms every day — getting dressed, making toast, walking to school."],
 [E("Order changes everything", "move 100 steps\nturn right 90 degrees\nmove 100 steps",
    "An L-shaped path. Swap the first two blocks and the shape changes completely."),
  E("Slow it down to see the order", "move 100 steps\nwait 1 seconds\nturn right 90 degrees\nwait 1 seconds\nmove 100 steps",
    "Waits make an invisible sequence visible. This is a debugging technique, not just a slowdown.")],
 "Sequence is the foundation of every program ever written. Loops, conditions and functions are all built on top of ordered steps.",
 "A recipe: add eggs before you bake, not after. Same ingredients, wrong order, ruined cake.",
 ["Reach the same point using a different order", "Write the algorithm on paper first, then code it", "Act the steps out physically before coding"])

DEEP["motion-steps"] = D(
 ["Scratch measures movement in **steps**. One step is roughly one dot on the screen, so 'move 10 steps' is a small nudge and 'move 100 steps' is a big jump. The number is a control you own — changing it changes the behaviour.",
  "Sprites always move in the direction they are **facing**, not simply rightwards. That is why turning matters: turn first, then move, and the sprite travels somewhere new.",
  "Turns are measured in **degrees**. 90 is a quarter turn, 180 is a half turn and 360 brings you back where you started. Every closed shape needs turns that add up to 360."],
 [E("A square path", "repeat 4\n  move 100 steps\n  turn right 90 degrees\nend",
    "4 turns of 90 = 360, so the path closes exactly."),
  E("A triangle path", "repeat 3\n  move 100 steps\n  turn right 120 degrees\nend",
    "3 turns of 120 = 360. Fewer sides means a bigger turn."),
  E("Going backwards", "move -50 steps",
    "A negative number moves the sprite backwards without turning it round.")],
 "Movement plus rotation is how every character, vehicle and projectile in every game gets around.",
 "Turning a quarter turn to face a different wall in your room — you have been doing 90-degree turns your whole life.",
 ["Work out the turn for a pentagon (360/5)", "Draw a shape with the pen attached", "Make the step size a variable so speed can change"])

DEEP["animation-loop"] = D(
 ["A **loop** repeats the blocks inside it. Instead of dragging out 'next costume' twenty times, you say 'repeat 20' once. Less code, and changing 20 to 50 is a one-second edit.",
  "The blocks must go **inside** the loop's C-shaped mouth. Anything placed underneath runs only after the loop has finished all its repeats.",
  "Animation itself is a loop: swap the picture, wait a moment, swap again. Without the wait the costumes change faster than the eye can follow and it looks like a blur.",
  "One pass through a loop is called an **iteration**. A loop inside another loop is **nested**: the inner loop runs fully on every pass of the outer one, so 3 outer x 4 inner = 12 runs."],
 [E("Walking animation", "repeat 10\n  next costume\n  move 10 steps\n  wait 0.2 seconds\nend",
    "Costume change plus movement plus timing — the three ingredients of a walk cycle."),
  E("Nested loops", "repeat 3\n  repeat 4\n    move 50 steps\n    turn right 90 degrees\n  end\n  turn right 120 degrees\nend",
    "Draws three squares rotated around a point. The inner loop draws a square, the outer rotates it.")],
 "Loops are how programmers avoid repeating themselves. Almost every program you use is running loops thousands of times a second.",
 "A chorus in a song repeats. A washing machine cycle repeats. You do not write the instructions out again each time.",
 ["Change the repeat count and predict the result first", "Nest a loop and work out the total iterations", "Use a loop to draw a pattern with the pen"])

DEEP["if-basic"] = D(
 ["An **if** block runs the code inside it only when a condition is true. The condition slot is **pointy**, and only pointy (boolean) blocks fit — they report true or false, nothing else.",
  "A condition is checked at the moment the if runs. That is the single biggest source of confusion: if you check once, you only find out about that instant. Games need to check constantly, which is why an if usually lives inside a **forever** loop.",
  "You can see a boolean directly: drop 'touching Sprite1?' into a 'say' block and click it. It reports true or false. Making the invisible visible is a genuinely useful teaching move."],
 [E("Check once — usually wrong", "when green flag clicked\nif <touching [Enemy]?> then\n  say [Ouch!]\nend",
    "This tests once, the instant the flag is clicked, then never again."),
  E("Check constantly — right", "when green flag clicked\nforever\n  if <touching [Enemy]?> then\n    say [Ouch!] for 1 seconds\n  end\nend",
    "Now the game keeps watching for the whole game."),
  E("Seeing a boolean", "say <touching [Enemy]?>",
    "Reports 'true' or 'false' — proof that conditions are just values.")],
 "Conditionals are how programs make decisions. Without them software could only ever do one fixed thing.",
 "'If it is raining, take an umbrella.' Children already reason in conditions long before they meet code.",
 ["Combine two conditions with and/or", "Compare if with wait-until", "Trigger different reactions for different sprites"])

DEEP["variable-score"] = D(
 ["A **variable** is a named box that stores one value you can change while the program runs. Give it a clear name — 'score', not 'thing'. Naming well is a real programming habit worth starting immediately.",
  "There are two ways to put something in the box. **set** puts an exact value in ('set score to 0'). **change by** adds to whatever is already there ('change score by 1'). Mixing these up causes a lot of bugs.",
  "Every variable must be **reset** at the start of the game, or the last game's score carries into the new one. Show the bug first: play, score points, run again, and watch the score continue from where it was.",
  "Variables can be **for all sprites** (shared, like a score) or **for this sprite only** (private, so each sprite and each clone has its own copy). That distinction becomes essential once cloning starts."],
 [E("A working score", "when green flag clicked\nset [score] to 0\nforever\n  if <touching [Coin]?> then\n    change [score] by 1\n  end\nend",
    "Reset at the start, add during play. The reset is the part beginners forget."),
  E("Stopping a repeated score", "if <touching [Coin]?> then\n  change [score] by 1\n  hide\nend",
    "Hiding the coin stops the collision firing 30 times a second."),
  E("A high score", "if <(score) > (highscore)> then\n  set [highscore] to (score)\nend",
    "Only overwrite when the new score is genuinely better.")],
 "Variables are how a program remembers. Scores, lives, health, timers, levels and settings are all variables.",
 "The scoreboard at a cricket match: one number that changes as the game goes on.",
 ["Add a high score that survives the round", "Use a variable to control speed", "Try a for-this-sprite-only variable and see the difference"])

DEEP["clones-basic"] = D(
 ["A **clone** is a copy of a sprite created while the project is running. One asteroid sprite plus clones can become fifty asteroids on screen — without you making fifty sprites by hand.",
  "Cloning has three parts and all three matter. A **spawner** creates clones. A **'when I start as a clone'** script says what each clone does — it runs separately for every clone. And **'delete this clone'** cleans up, because clones that are never deleted pile up and grind the project to a halt.",
  "Each clone can behave differently if you give it its own values. A variable made **for this sprite only** gives every clone a private copy, so one can be fast and another slow.",
  "Clones inherit the original's position, size and costume at the moment they are created — so set those before cloning if you want variety."],
 [E("The spawner", "when green flag clicked\nhide\nforever\n  create clone of [myself]\n  wait 1 seconds\nend",
    "The original hides; only the clones are seen."),
  E("What each clone does", "when I start as a clone\ngo to x: (pick random -200 to 200) y: 180\nshow\nrepeat until <(y position) < -170>\n  change y by -5\nend\ndelete this clone",
    "Random x gives every clone a different path. The delete keeps performance healthy."),
  E("Clones with their own speed", "when I start as a clone\nset [speed] to (pick random 3 to 8)\nforever\n  change y by (0 - (speed))\nend",
    "'speed' must be a for-this-sprite-only variable or every clone shares one value.")],
 "Cloning is the first taste of creating objects at runtime — the same idea behind every enemy, bullet and particle in real games.",
 "One cookie cutter making hundreds of biscuits: one shape, many copies, each going its own way.",
 ["Two clone types — one good, one harmful", "Waves that get faster each round", "Formations built by calculating positions"])

DEEP["broadcast"] = D(
 ["A **broadcast** sends a message that every sprite can hear. Any sprite with a matching 'when I receive' script reacts. One signal, many reactions.",
  "This solves a real problem. Timing sprites with waits works for a few seconds but drifts over a long project. Messages are exact: everyone reacts at the same instant, however long the game has been running.",
  "Name messages properly — 'game-over' or 'start-game', never 'message1'. In a project with fifteen messages, good names are the difference between readable and hopeless.",
  "'broadcast and wait' is different from plain 'broadcast': it pauses the sending script until every receiver has finished. Use it when the next step must not begin too early, such as after a cutscene."],
 [E("Starting the game from a button", "when this sprite clicked\nbroadcast [start-game]",
    "The button does not need to know anything about the other sprites."),
  E("A sprite reacting", "when I receive [start-game]\nshow\nset [score] to 0\ngo to x: 0 y: -100",
    "Every sprite decides for itself what 'start-game' means."),
  E("Waiting for a cutscene", "broadcast [intro] and wait\nbroadcast [start-game]",
    "The game only begins once the intro has completely finished.")],
 "Broadcasting is message passing — how separate parts of large software systems talk without being tangled together.",
 "A referee's whistle: one sound, and every player on the pitch reacts at once.",
 ["Chain broadcasts so one triggers another", "Use messages to manage menu, play and game-over states", "Reset every sprite with a single message"])

DEEP["gravity"] = D(
 ["Real gravity does not move things at a constant speed — it makes them **speed up** as they fall. To model that you need two variables working together: **position** and **velocity**.",
  "The pattern is short but powerful. Every frame, velocity changes the position ('change y by velocity'), and gravity changes the velocity ('change velocity by -1'). Because velocity keeps growing more negative, the fall accelerates — exactly like a dropped pen.",
  "Jumping is simply setting velocity to a positive number **once**. Gravity then takes over automatically and produces a natural arc. If a child sets velocity every frame, the sprite floats instead of arcing.",
  "You always need a **ground check**, or the sprite falls forever. When it reaches the floor, snap it to floor level and set velocity back to 0."],
 [E("Gravity", "when green flag clicked\nset [velocity] to 0\nforever\n  change y by (velocity)\n  change [velocity] by -1\nend",
    "Two lines produce real accelerating motion."),
  E("Jumping", "when [space] key pressed\nif <(y position) < -119> then\n  set [velocity] to 12\nend",
    "Set velocity once, and only when standing on the ground — that also prevents mid-air jumping."),
  E("The ground check", "if <(y position) < -120> then\n  set y to -120\n  set [velocity] to 0\nend",
    "Stops the fall and resets velocity so the next jump works.")],
 "This is a real physics simulation — the same velocity-and-acceleration model used in professional game engines.",
 "Drop a pen and watch: it starts slow and speeds up. It does not fall at one constant speed.",
 ["Tune gravity and jump height for different feels", "Add a double jump with a counter", "Make jump height depend on how long space is held"])

DEEP["lists"] = D(
 ["A variable holds **one** value. A **list** holds many, numbered from 1. In Scratch the first item is item 1, not item 0 — worth saying out loud, because most programming languages start at 0 and this trips people up later.",
  "Lists unlock whole categories of project: quizzes with many questions, high-score tables, word games, inventories, and anything that stores a history.",
  "The most useful pattern is picking a random item safely: 'item (pick random 1 to (length of list)) of list'. Using the length rather than a fixed number means the code still works when you add more items.",
  "**Parallel lists** are two lists kept in step, so item 3 of 'questions' matches item 3 of 'answers'. Keeping them aligned is the programmer's responsibility — nothing enforces it for you."],
 [E("Filling a list once", "when green flag clicked\ndelete all of [questions]\nadd [What is 2+2?] to [questions]\nadd [What is 5x3?] to [questions]",
    "Clear before adding, or the list doubles in length every run."),
  E("Picking a random item", "set [n] to (pick random 1 to (length of [questions]))\nask (item (n) of [questions]) and wait",
    "Using length means the code adapts as the list grows."),
  E("Parallel lists", "if <(answer) = (item (n) of [answers])> then\n  change [score] by 1\nend",
    "Question n and answer n line up, so one index checks both.")],
 "Lists are the first data structure. Databases, spreadsheets and search engines are all built on the idea of ordered, indexed data.",
 "A shopping list, a register, a playlist — all numbered collections you already use.",
 ["Store a top-three high score table", "Remove questions as they are used so none repeat", "Use 'contains' to accept several correct spellings"])

DEEP["myblocks"] = D(
 ["A **custom block** is a block you invent. You give it a name, define what it does, and then use it exactly like any built-in block.",
  "The motivation is real duplication. When the same six blocks appear in three places, that is three places to fix when something changes. Move them into 'reset player' and there is one.",
  "This is **abstraction** — hiding detail behind a meaningful name. 'Make a cup of tea' is one instruction that hides twelve steps. Good code reads like a list of intentions, not a wall of blocks.",
  "Adding an **input** makes one block serve many cases. 'draw square (size)' replaces separate blocks for every size you might want."],
 [E("Before: repeated everywhere", "go to x: 0 y: -100\nset [lives] to 3\nset [score] to 0\nshow\nset size to 100 %",
    "Now imagine this same stack copied into three different scripts."),
  E("After: one named block", "define [reset player]\ngo to x: 0 y: -100\nset [lives] to 3\nset [score] to 0\nshow\nset size to 100 %",
    "The main script becomes simply 'reset player'."),
  E("With an input", "define [draw square (size)]\nrepeat 4\n  move (size) steps\n  turn right 90 degrees\nend",
    "'draw square (50)' and 'draw square (200)' now both work from one definition.")],
 "Custom blocks are functions. Every serious programming language has them, and they are the main tool for keeping large programs understandable.",
 "'Tidy your room' is one instruction that hides a dozen jobs everyone already understands.",
 ["Refactor an old project into three named blocks", "Add a second input", "Give every block exactly one job"])

DEEP["quiz-logic"] = D(
 ["A quiz has four parts: **ask** the question, **store** the answer, **compare** it with the right one, and **respond** with feedback and a score.",
  "The 'answer' block only ever holds the **most recent** reply. The next 'ask' overwrites it, so if you need it later, store it in a variable straight away.",
  "Scratch's '=' ignores capital letters for words, so 'paris' matches 'Paris'. That is helpful for children's quizzes. It does not ignore extra spaces, which is a common invisible bug.",
  "Good feedback teaches. 'Wrong' tells the child nothing; 'Not quite — the capital of France is Paris' turns a mistake into a lesson. That principle applies to your own quiz design as much as theirs."],
 [E("One question", "ask [What is the capital of France?] and wait\nif <(answer) = [Paris]> then\n  change [score] by 1\n  say [Correct!] for 1 seconds\nelse\n  say (join [The answer was Paris. You said: ] (answer)) for 2 seconds\nend",
    "One ask, one comparison, two clear outcomes."),
  E("Grading at the end", "if <(score) > 3> then\n  say [Excellent!]\nelse\n  say [Good try — practise and go again]\nend",
    "Thresholds turn a raw score into meaningful feedback.")],
 "Checking input against expected values is called **validation**, and it happens every time you log in anywhere.",
 "A spelling test: the teacher compares your answer with the correct one and gives feedback.",
 ["Use lists so questions never repeat", "Accept more than one correct spelling", "Show a percentage and a grade at the end"])

DEEP["pen"] = D(
 ["The **pen** turns a sprite into a paintbrush: while the pen is down, the sprite leaves a line wherever it moves.",
  "Pen blocks are an **extension** — they are not in the palette until you add them from the button at the bottom left. Children need to know extensions exist, because Music, Video Sensing and Text to Speech all work the same way.",
  "Every pen project should start with 'erase all' and 'pen up'. Without them, drawings from the previous run stay on the stage and stray lines appear as the sprite moves into position.",
  "Pen plus loops is where maths becomes visible. Any regular shape needs turns totalling 360, so the turn is always 360 divided by the number of sides."],
 [E("A clean start", "when green flag clicked\nerase all\npen up\ngo to x: 0 y: 0\npen down",
    "Clear, lift, position, then start drawing. This order prevents stray lines."),
  E("Any regular polygon", "set [sides] to 6\nrepeat (sides)\n  move 60 steps\n  turn right ((360) / (sides)) degrees\nend",
    "Change 'sides' to 3, 5 or 8 and the same code draws a triangle, pentagon or octagon."),
  E("A rainbow spiral", "repeat 36\n  repeat 4\n    move 100 steps\n    turn right 90 degrees\n  end\n  turn right 10 degrees\n  change pen color by 5\nend",
    "36 x 10 = 360, so the pattern closes perfectly into a circle.")],
 "Drawing with code is how data visualisation, computer graphics and CAD software all begin.",
 "A spirograph toy, or drawing round and round on paper without lifting your pencil.",
 ["Derive the turn for any polygon", "Draw a graph of a variable", "Build a paint program with pen size and colour controls"])

# --- remaining topics -------------------------------------------------

DEEP["looks-say"] = D(
 ["Speech is how sprites become characters. 'say () for () seconds' shows a bubble then clears itself; plain 'say ()' leaves the bubble on screen until you change it. That difference causes a lot of stuck bubbles.",
  "Two sprites talking need **timing**. If both speak at once they talk over each other. Sprite B must wait roughly as long as sprite A speaks. This is a child's first experience of coordinating two independent programs.",
  "'think' shows a thought cloud instead — useful for inner feelings, hints and comic effects."],
 [E("A timed conversation", "when green flag clicked\nsay [Hi, who are you?] for 2 seconds\nwait 2 seconds\nsay [Nice to meet you!] for 2 seconds",
    "The wait matches the other sprite's speaking time."),
  E("Clearing a stuck bubble", "say [Loading...]\nwait 1 seconds\nsay []",
    "An empty say removes the bubble.")],
 "Communicating state to the user is a core job of every interface, not just games.",
 "Speech bubbles in comics — you read them in order, one at a time.",
 ["Time a three-sprite conversation", "Use think for a character's private thoughts", "Build a branching story with choices"])

DEEP["costumes"] = D(
 ["A **costume** is one of the pictures a sprite can wear. Switching costumes quickly is literally all animation is — a flip-book made of code.",
  "Costumes are also a great way to show **state**: a character that is normal, hurt or celebrating; a door open or closed; a traffic light on red, amber or green.",
  "Timing matters as much as the pictures. Without a wait between switches, the costumes change faster than the eye can see."],
 [E("A walk cycle", "forever\n  next costume\n  wait 0.2 seconds\nend",
    "0.1-0.3 seconds reads as natural movement."),
  E("Costume as state", "if <(lives) < 1> then\n  switch costume to [sad]\nelse\n  switch costume to [happy]\nend",
    "The picture communicates the game state instantly.")],
 "Separating what something looks like from what it does is a key idea in software design.",
 "A flip-book, or the frames of a cartoon.",
 ["Different speeds for walking and running", "Costume changes that react to the score", "Draw your own costume in the paint editor"])

DEEP["forever"] = D(
 ["A **forever** loop never ends. It suits behaviour that should always be on: checking for key presses, patrolling, animating, watching for collisions.",
  "Nothing placed **under** a forever loop will ever run, because the loop never finishes. Demonstrating that deliberately saves hours of confusion later.",
  "Several forever loops can run at the same time, on different sprites or even the same sprite. That parallelism is what makes a Scratch game feel alive."],
 [E("Constant checking", "forever\n  if <key [right arrow] pressed?> then\n    change x by 4\n  end\nend",
    "The check repeats every frame, so control feels instant."),
  E("The classic trap", "forever\n  move 10 steps\nend\nsay [Done!]",
    "The 'say' never runs — the loop never ends.")],
 "Real programs run event loops constantly; your phone is running one right now.",
 "Your heartbeat: it does not run ten times and stop.",
 ["Run two forever loops at once and explain it", "Compare forever with repeat-until", "Split one big loop into separate behaviours"])

DEEP["events-key"] = D(
 ["An **event** is something that happens which starts a script. Hat blocks are the listeners: the green flag, a key press, a click, a message.",
  "Each key needs its **own** script. Four arrow keys means four hat blocks, each independent — they can even run at the same time.",
  "Key events have one weakness: holding a key gives a short pause before it repeats, which makes movement stutter. That is why games usually prefer sensing (covered soon)."],
 [E("Four-way control with events", "when [right arrow] key pressed\nchange x by 10",
    "Repeat this pattern for each of the four keys, changing x or y."),
  E("An action key", "when [space] key pressed\nstart sound [pop]\nchange size by 10",
    "Events are perfect for one-off actions like jumping or firing.")],
 "Event-driven programming is how nearly all modern software works — apps sit idle until you do something.",
 "A doorbell: nothing happens until someone presses it.",
 ["Add a key that changes costume", "Compare event control with sensing control", "Design your own control scheme"])

DEEP["events-click"] = D(
 ["'when this sprite clicked' turns any sprite into a button. This is where projects stop being animations and start being **interactive**.",
  "Choosing the right trigger is a design decision: the flag starts the project, keys control it, clicks interact with it.",
  "Test by clicking the sprite **on the stage** — clicking its thumbnail in the sprite list only selects it, which confuses almost every beginner once."],
 [E("A clickable character", "when this sprite clicked\nstart sound [meow]\nnext costume",
    "Instant feedback makes the sprite feel alive."),
  E("A start button", "when this sprite clicked\nbroadcast [start-game]\nhide",
    "The button starts the game and gets out of the way.")],
 "Buttons, menus and touch targets are the backbone of every app interface.",
 "Every icon on a phone: tap it, something happens.",
 ["Build a three-button menu", "Make a click change the backdrop", "Add a hover effect using sensing"])

DEEP["coordinates"] = D(
 ["The Scratch stage is a grid. **x** runs left to right from about -240 to 240; **y** runs bottom to top from about -180 to 180. The centre is x 0, y 0.",
  "'go to x y' jumps instantly to an exact place. 'change x by' moves relative to where the sprite already is. Confusing **set** with **change** is one of the most common bugs at this stage.",
  "Coordinates are how you place things precisely: resetting the player, laying out a level, or checking whether a sprite has gone past an edge."],
 [E("Reset to a known place", "when green flag clicked\ngo to x: 0 y: -120",
    "Sprites keep their last position, so always send them home at the start."),
  E("Set versus change", "set x to 100\nchange x by 100",
    "The first jumps to 100; the second moves 100 further from wherever it is."),
  E("Detecting an edge", "if <(x position) > 230> then\n  set x to -230\nend",
    "Wraps the sprite around to the other side of the stage.")],
 "Coordinate systems underpin graphics, mapping, robotics and every screen you have ever used.",
 "Battleships, or a grid reference on a map.",
 ["Place five sprites without dragging them", "Wrap a sprite around the screen edges", "Plot a shape from a list of coordinates"])

DEEP["glide"] = D(
 ["'glide' moves a sprite smoothly to a position over a chosen time, instead of teleporting. The seconds value controls how fast the journey looks.",
  "Timing is expressive. The same journey in 0.2 seconds feels panicked; in 3 seconds it feels calm. Children discover that pacing communicates mood.",
  "Combine glide with 'point towards' so the sprite faces where it is travelling — otherwise it slides sideways like a ghost."],
 [E("A smooth journey", "point towards [Earth]\nglide 2 secs to x: 0 y: 0",
    "Faces the destination, then travels there believably."),
  E("Comparing feel", "glide 0.2 secs to x: 200 y: 0\nglide 3 secs to x: -200 y: 0",
    "Same distance, completely different mood.")],
 "Smooth interpolation between two states is the basis of all animation and UI transitions.",
 "A lift gliding between floors rather than blinking from one to the other.",
 ["A three-leg journey at different speeds", "Glide to a random position repeatedly", "Combine glide with costume changes"])

DEEP["backdrops"] = D(
 ["The **backdrop** is the picture behind everything. Changing it is how a project moves between scenes — the same trick films use.",
  "Backdrop code usually lives on the **Stage**, not on a sprite. Sprites can react to a scene change with 'when backdrop switches to'.",
  "Managing which sprites are visible in each scene is the real skill. Every sprite needs to know what to do when the scene changes: show, hide, or move."],
 [E("Changing scene", "switch backdrop to [forest]\nwait 2 seconds\nswitch backdrop to [castle]",
    "Waits give the player time to take in each scene."),
  E("A sprite reacting to scene", "when backdrop switches to [castle]\nshow\ngo to x: -150 y: -50",
    "Scenery drives the characters — the seed of broadcasting.")],
 "Separating scenes is how any large interactive experience is structured.",
 "Changing the set between acts of a play.",
 ["A three-scene story", "Sprites that appear in only one scene", "Day and night versions of the same level"])

DEEP["size-effects"] = D(
 ["Size is a percentage: 100% is normal, 50% is half, 200% is double. **Always set size at the start**, or changes carry over between runs.",
  "'show' and 'hide' control visibility. The classic bug is hiding a sprite at the end of a game and never showing it again, so it is invisible next time.",
  "Graphic effects such as **ghost** (transparency) and **colour** give feedback: a fade when an item is collected, a flash when taking damage, a glow for a power-up. 'clear graphic effects' resets them."],
 [E("The reset habit", "when green flag clicked\nshow\nset size to 100 %\nclear graphic effects\ngo to x: 0 y: 0",
    "Five blocks that prevent a whole category of bugs."),
  E("A collect effect", "repeat 5\n  change size by 8\n  change [ghost] effect by 20\nend\nhide",
    "Grow and fade together, then vanish — satisfying feedback.")],
 "Resetting state at startup is a principle that applies to all software, not just games.",
 "A balloon growing then popping.",
 ["Fade a title in at the start", "Flash a sprite when it takes damage", "Shrink distant sprites to fake depth"])

DEEP["sound-play"] = D(
 ["Sounds belong to a sprite and live in its **Sounds** tab. 'start sound' plays and carries on immediately; 'play sound until done' waits for it to finish.",
  "That distinction is a real timing decision. Game effects should use 'start sound' so the action never pauses; a voice line that must finish should use 'until done'.",
  "Sound is the cheapest polish available. Adding a distinct sound to every important action makes a project feel dramatically more finished."],
 [E("A game effect", "when this sprite clicked\nstart sound [pop]\nchange [score] by 1",
    "The score changes instantly; the sound does not block it."),
  E("A sequence that must not overlap", "play sound [three] until done\nplay sound [two] until done\nplay sound [one] until done",
    "Each sound finishes before the next begins.")],
 "Audio feedback is a serious part of interface design — it confirms actions without using the screen.",
 "The click of a light switch tells you it worked.",
 ["Give every action its own sound", "Build a countdown with until-done", "Fade music with change volume"])

DEEP["wait-timing"] = D(
 ["'wait' pauses **only the script it is in** — other scripts keep running. That is worth stating clearly, because children often assume it freezes everything.",
  "Short waits (0.1-0.2 seconds) smooth animation; long waits (1-2 seconds) pace dialogue and scenes.",
  "'wait until' is the conditional version: pause until something becomes true, such as the player pressing start."],
 [E("Pacing a scene", "say [Ready...] for 1 seconds\nwait 0.5 seconds\nsay [Go!] for 1 seconds",
    "Waits choreograph when each thing happens."),
  E("Waiting for the player", "wait until <key [space] pressed?>\nbroadcast [start-game]",
    "Responds to the player instead of guessing a delay.")],
 "Controlling timing is essential in animation, music, robotics and networking.",
 "The gaps in music: silence is what makes rhythm.",
 ["Choreograph three sprites to a beat", "Replace waits with broadcasts and compare", "Use wait-until for a start gate"])

DEEP["sensing-touch"] = D(
 ["Sensing gives sprites **senses**. 'touching Sprite?' reports true whenever two sprites overlap; 'touching colour?' detects a specific colour, which is how tracks, walls and platforms are usually built.",
  "Collision is only the trigger — you then decide what happens: score, sound, hide, bounce, lose a life. That design decision is the interesting part.",
  "Two problems appear immediately. Collisions fire many times per second, so a single touch can score 30 points — fix it by hiding the object or adding a wait. And colour sensing needs an **exact** match, so all platforms should share one colour."],
 [E("Collecting safely", "forever\n  if <touching [Coin]?> then\n    change [score] by 1\n    start sound [pop]\n    hide\n  end\nend",
    "Hiding the coin stops the collision repeating."),
  E("Staying on a track", "if <not <touching color [#444444]?>> then\n  say [Off track!]\n  go to x: 0 y: 0\nend",
    "Colour sensing turns a drawn backdrop into game logic.")],
 "Collision detection is one of the fundamental problems in game programming and robotics.",
 "A reversing sensor that beeps when your car gets close to something.",
 ["Good and bad objects with different reactions", "Colour-sensed maze walls", "Use distance-to for proximity"])

DEEP["sensing-key"] = D(
 ["'key pressed?' is a **boolean** that stays true while the key is held. Checking it inside a forever loop is called **polling**.",
  "Polling is smoother than key events because there is no key-repeat delay, and it allows **diagonal** movement: two conditions can both be true on the same pass of the loop.",
  "All four checks must live in the **same** forever loop for diagonals to work. Separate loops fight each other."],
 [E("Smooth four-way control", "forever\n  if <key [right arrow] pressed?> then\n    change x by 4\n  end\n  if <key [left arrow] pressed?> then\n    change x by -4\n  end\nend",
    "Add up and down the same way, all inside this one loop."),
  E("A speed state", "if <key [shift] pressed?> then\n  set [speed] to 8\nelse\n  set [speed] to 4\nend",
    "Nested conditions create walking and running.")],
 "Input polling is exactly how real game engines read controllers every frame.",
 "Holding a button on a games controller — it keeps working while held.",
 ["Convert an old project from events to sensing", "Add a run key", "Restrict movement to the stage edges"])

DEEP["random"] = D(
 ["'pick random a to b' gives a different whole number each time. It is what makes a game worth playing twice.",
  "Randomness is used for **position** (where a target appears), **timing** (how long before the next enemy), **appearance** (size, colour) and **choice** (which question to ask).",
  "Ranges must respect the stage: roughly -200 to 200 for x and -150 to 150 for y keeps a sprite fully visible. And a random value re-picked every frame makes a sprite vibrate — pick once, then use it."],
 [E("Unpredictable spawning", "go to x: (pick random -200 to 200) y: 150\nwait (pick random 1 to 3) seconds",
    "Random position and random timing together feel natural."),
  E("Random variety", "set size to (pick random 50 to 150) %\nchange [color] effect by (pick random 0 to 200)",
    "One sprite becomes a crowd of different-looking ones.")],
 "Randomness drives simulations, procedural game worlds, cryptography and statistics.",
 "Rolling a dice or shuffling a pack of cards.",
 ["Random size, position and timing together", "A dice-rolling game", "Random questions that never repeat"])

DEEP["if-else"] = D(
 ["'if ... else' chooses between **exactly two** paths. One of them always runs, and never both — that guarantee is what makes it better than two separate ifs.",
  "Two ifs with opposite conditions usually work, but they can both fire if the conditions overlap, producing two messages at once. If-else cannot do that.",
  "**Tracing** — following which branch runs and why — is one of the most valuable debugging skills a child can build."],
 [E("Win or lose", "if <(score) > 9> then\n  say [You win!] for 2 seconds\nelse\n  say [Try again] for 2 seconds\nend",
    "Exactly one message, every time."),
  E("Three outcomes by nesting", "if <(score) > 9> then\n  say [Gold]\nelse\n  if <(score) > 5> then\n    say [Silver]\n  else\n    say [Bronze]\n  end\nend",
    "Nesting handles more than two cases.")],
 "Branching is how programs handle the messiness of the real world.",
 "'If you finish your homework you can play, otherwise you keep working.'",
 ["Nest for three grade bands", "Use if-else for a quiz check", "Trace which branch runs and why"])

DEEP["repeat-until"] = D(
 ["Scratch has three loops and choosing the right one is a real skill. **repeat n** for a known number of times, **forever** for behaviour that never stops, and **repeat until** for working towards a goal.",
  "'repeat until' checks its condition **before** each pass. If the condition is already true, the loop body never runs at all.",
  "A loop whose condition can never become true never stops — the most common cause of an apparently frozen project."],
 [E("Chase until caught", "repeat until <touching [Player]?>\n  point towards [Player]\n  move 3 steps\nend\nsay [Caught you!]",
    "The chase ends exactly when it should, not after a guessed number of steps."),
  E("Wait for a condition", "wait until <(score) > 9>\nbroadcast [level-up]",
    "The pausing version of the same idea.")],
 "Condition-controlled loops appear in every language as 'while' loops.",
 "'Keep stirring until it is smooth' — not a fixed number of stirs.",
 ["End a loop on two conditions with or", "Compare all three loop types", "Debug a loop that never ends"])

DEEP["mouse-follow"] = D(
 ["Two blocks make a sprite follow the mouse: 'point towards mouse-pointer' turns it to face the pointer, and 'go to mouse-pointer' moves it onto the pointer.",
  "Constraining the following is often better than copying it exactly. 'set x to mouse x' makes a paddle that slides horizontally but stays at its own height — the standard Pong paddle.",
  "Following must be continuous, so it always lives inside a forever loop."],
 [E("Eyes that watch you", "forever\n  point towards [mouse-pointer]\nend",
    "Delightful, and only two blocks."),
  E("A Pong paddle", "forever\n  set x to (mouse x)\nend",
    "Horizontal only — the paddle stays on its side of the court."),
  E("Follow only when close", "if <(distance to [mouse-pointer]) < 100> then\n  point towards [mouse-pointer]\nend",
    "Conditional following makes an enemy feel aware.")],
 "Cursor tracking is the basis of every drawing tool and drag interaction.",
 "A guard dog turning its head to watch you cross the room.",
 ["A paddle for a bat-and-ball game", "A sprite that follows only when near", "A drawing brush that follows the mouse"])

DEEP["bounce"] = D(
 ["'if on edge, bounce' reverses a sprite's direction when it reaches the stage edge. With 'move' inside a forever loop, that is a complete patrolling or bouncing behaviour in three blocks.",
  "The sprite will often end up **upside-down**, because the default rotation style lets it rotate all the way round. Setting rotation style to left-right fixes it.",
  "Starting at a random direction makes every run different, which turns one simple behaviour into an unpredictable game element."],
 [E("A bouncing ball", "when green flag clicked\npoint in direction (pick random 1 to 360)\nforever\n  move 8 steps\n  if on edge, bounce\nend",
    "Random start direction means no two games look the same."),
  E("An upright patrol", "set rotation style [left-right]\nforever\n  move 4 steps\n  if on edge, bounce\nend",
    "The character stays the right way up.")],
 "Reflecting off a boundary is a simple physics simulation used in countless games.",
 "A ball rebounding off a wall.",
 ["Two bouncing sprites that react to each other", "Speed that increases over time", "Bounce off a drawn colour instead of the edge"])

DEEP["debug-basics"] = D(
 ["A **bug** is a mistake that makes a program behave differently from what you intended. Debugging is finding and fixing it — and it is most of what programmers actually do.",
  "The method matters more than luck. First state clearly what it **should** do versus what it **does**. Then narrow the search: run a single script on its own, add a 'say' to reveal a value, or add waits to slow it down enough to watch.",
  "Change **one** thing at a time and re-test. Changing three things and finding it works tells you nothing about which one mattered.",
  "The computer is always doing exactly what it was told. The question is never 'why is it wrong?' but 'what did I actually tell it?'"],
 [E("Reveal what the code thinks", "forever\n  say (join [score is ] (score))\nend",
    "Making an invisible value visible often solves the bug immediately."),
  E("Slow it down to watch", "forever\n  move 10 steps\n  wait 0.5 seconds\nend",
    "If it fails too fast to see, make it slower.")],
 "Debugging is the single most transferable skill in programming — and it teaches persistence.",
 "Finding out why a torch will not switch on: batteries, bulb, or switch. You test one at a time.",
 ["Fix a project with two separate bugs", "Keep a log of what you tried", "Break a project deliberately, then swap and fix"])

DEEP["game-win-lose"] = D(
 ["A game needs rules the player can understand. A **win condition** is the test that means success; a **lose condition** means failure. Write both in plain English before writing any blocks.",
  "Use '>' rather than '=' for score checks. If the score can jump by 2 or 5, an exact equality test can be skipped straight over and the game never ends.",
  "Always tell the player what happened. Say the message first, give it time to be read, and only then 'stop all' — otherwise the message flashes and vanishes.",
  "Reset every variable at the start, or a condition may already be true when the game begins and it ends instantly."],
 [E("A safe win check", "forever\n  if <(score) > 9> then\n    say [You win!] for 2 seconds\n    switch backdrop to [win]\n    stop all\n  end\nend",
    "Message, then scene, then stop — in that order."),
  E("A lose condition", "if <(lives) < 1> then\n  say [Game over] for 2 seconds\n  stop all\nend",
    "'< 1' is safer than '= 0' if lives could overshoot.")],
 "Defining success and failure precisely is what turns an activity into a game.",
 "Any sport: you cannot play without knowing how to win.",
 ["Add a draw or time-out state", "Test both endings deliberately", "Balance the game so it is winnable but not easy"])

DEEP["operators-math"] = D(
 ["Green **operator** blocks calculate a value. They are not commands — they slot **inside** other blocks wherever a number is expected.",
  "'set score to (score) + (5)' and 'change score by 5' do the same job. Understanding both matters, because the first pattern generalises to any calculation.",
  "**mod** gives the remainder after dividing, which is how you detect 'every 5th point' or 'every other one' — surprisingly useful in games."],
 [E("Points per coin", "set [score] to ((coins) * (10))",
    "Nesting an operator inside a set block."),
  E("Every fifth point", "if <((score) mod (5)) = 0> then\n  change [speed] by 1\nend",
    "mod 5 = 0 happens at 5, 10, 15 — a clean way to escalate difficulty."),
  E("Tidy division", "set [percent] to (round (((score) / (total)) * (100)))",
    "Round keeps the display clean.")],
 "Expressions are how programs compute anything at all.",
 "Working out a total at the shop: price times quantity.",
 ["A combo multiplier that grows with a streak", "A percentage score", "Speed that increases with level"])

DEEP["operators-compare"] = D(
 ["Comparison blocks report **true or false** — they are booleans, and they fit the pointy slots in if blocks and loop conditions.",
  "You can see this directly: drop '(score) > 5' into a say block and click it. It reports true or false. Booleans stop being mysterious once you can see one.",
  "Prefer '>' or '<' over '=' for anything that can change by more than one. Exact equality is fragile whenever values can skip."],
 [E("Making a boolean visible", "say <(score) > (5)>",
    "Reports 'true' or 'false' — proof that conditions are values."),
  E("A robust threshold", "if <(score) > 9> then\n  broadcast [level-up]\nend",
    "Catches 10 and everything above, even if the score jumps.")],
 "Comparison drives every decision a program makes.",
 "Deciding whether you are tall enough for a ride.",
 ["Grade bands with several thresholds", "Compare two sprites' positions", "Check 'at least' correctly"])

DEEP["operators-logic"] = D(
 ["**and** is true only when both conditions are true. **or** is true when either is. **not** flips true and false.",
  "A **truth table** makes this concrete: with two conditions there are exactly four combinations. Working through all four on paper is genuine computer science and children enjoy it.",
  "When a condition becomes hard to read, store part of it in a well-named variable such as 'ready' — the same technique professionals use."],
 [E("Two requirements to win", "if <<touching [Goal]?> and <(coins) > 4>> then\n  say [Level complete!]\nend",
    "Both must be true — reaching the goal is not enough on its own."),
  E("Either hazard hurts", "if <<touching [Spike]?> or <touching [Lava]?>> then\n  change [lives] by -1\nend",
    "One condition is enough to trigger damage."),
  E("Keep going while free", "repeat until <not <touching color [#000000]?>>\n  change y by 1\nend",
    "'not' reads naturally as 'while NOT touching'.")],
 "Boolean logic is the mathematical foundation computers are physically built on.",
 "'You can go out if your homework is done AND it is not raining.'",
 ["Draw the truth table for two conditions", "Simplify a messy condition with a variable", "Combine three conditions"])

DEEP["variable-timer"] = D(
 ["A countdown is a variable that decreases. The pattern is: set it to a start value, then repeatedly wait one second and change it by **-1** until it reaches zero.",
  "The 'wait 1 seconds' is essential. Without it the loop runs dozens of times a second and the timer empties instantly.",
  "Scratch also has a built-in 'timer' that counts **up** in seconds. 'reset timer' zeroes it — do that at the start so timing is fair.",
  "Timers change how a game feels. The same game with a 30-second limit is a completely different experience."],
 [E("A 30-second countdown", "set [time] to 30\nrepeat until <(time) = 0>\n  wait 1 seconds\n  change [time] by -1\nend\nsay [Time up!]\nstop all",
    "Wait, decrease, repeat — the standard countdown."),
  E("Using the built-in timer", "reset timer\nwait until <touching [Goal]?>\nsay (join [You took ] (round (timer)))",
    "Perfect for speedruns and reaction games."),
  E("A time bonus", "if <touching [Clock]?> then\n  change [time] by 5\n  hide\nend",
    "Bonuses give the player a way to fight back against the clock.")],
 "Timing and scheduling appear everywhere in software, from animations to network timeouts.",
 "A kitchen timer, or the clock in a football match.",
 ["Flash the timer under five seconds", "Add time bonuses", "Score based on time remaining"])

DEEP["variable-lives"] = D(
 ["Lives give the player room to fail. Three lives is a **fairness** decision: instant failure is discouraging, especially for younger children.",
  "The classic bug is losing all three lives from one collision, because the check runs every frame while the sprites overlap. Fix it with a brief invincibility wait, or by moving the player away immediately.",
  "**Respawning** — returning the player to a safe start position — is what makes losing a life feel survivable rather than final."],
 [E("Losing a life safely", "if <touching [Enemy]?> then\n  change [lives] by -1\n  go to x: 0 y: -120\n  wait 1 seconds\nend",
    "Move away and pause, so one touch costs exactly one life."),
  E("Game over", "if <(lives) < 1> then\n  say [Game over] for 2 seconds\n  stop all\nend",
    "'< 1' catches zero and any negative value.")],
 "Managing state safely against repeated events is a real engineering problem, not just a game one.",
 "Three attempts at a penalty shootout.",
 ["A health bar using costumes", "A pick-up that restores health", "Invincibility frames after a hit"])

DEEP["broadcast-scenes"] = D(
 ["Real games are several small programs that hand over to each other: a **menu**, the **game**, and a **game-over** screen. Each is a **state**.",
  "Drawing the state diagram on paper first — three boxes and arrows between them — makes the code obvious before any blocks are dragged.",
  "Each state change is a broadcast, and **every sprite decides for itself** what to show or hide on each message. Missing one is why menu sprites float over the gameplay.",
  "Restarting must reset everything: variables, positions, visibility. A restart that inherits the old score is the commonest bug at this level."],
 [E("The state change", "when this sprite clicked\nbroadcast [start-game]\nhide",
    "The menu button hands over to the game."),
  E("Every sprite responds", "when I receive [start-game]\nshow\nset [score] to 0\ngo to x: 0 y: -100",
    "Reset variables and visibility together."),
  E("Ending cleanly", "when I receive [game-over]\nhide\nstop [other scripts in sprite]",
    "Stopping old loops prevents two states running at once.")],
 "This is a **state machine** — a formal idea used throughout professional software.",
 "A board game: setup, play, then declaring a winner.",
 ["Add a pause state", "A settings screen", "Restart with no leftover state"])

DEEP["clones-advanced"] = D(
 ["Waves are a design tool. 'repeat 10 [create clone, wait 0.2]' produces a burst of ten enemies rather than an endless stream, which lets you pace difficulty.",
  "Giving each clone its own **for this sprite only** variable is what makes cloning powerful: one sprite can produce fast enemies, slow enemies, and bonus items.",
  "Formations come from **calculating** positions in a loop rather than randomising them — that is how synchronised patterns and enemy grids are built.",
  "Performance is a genuine constraint. Cap the number of clones and delete them when they leave the screen."],
 [E("A wave", "repeat 10\n  create clone of [myself]\n  wait 0.2 seconds\nend",
    "A burst, not a stream — you control the pacing."),
  E("Per-clone speed", "when I start as a clone\nset [speed] to (pick random 3 to 9)\nrepeat until <(y position) < -170>\n  change y by (0 - (speed))\nend\ndelete this clone",
    "'speed' must be for-this-sprite-only or all clones share one value."),
  E("A formation", "set [i] to 0\nrepeat 8\n  set x to ((i) * 50)\n  create clone of [myself]\n  change [i] by 1\nend",
    "Calculated positions make a neat row instead of a random scatter.")],
 "Managing many independent objects efficiently is a core problem in real game engines.",
 "A flock of birds: same rules, each bird slightly different.",
 ["Waves that get harder", "Two clone types with different behaviour", "A boss clone that takes several hits"])

DEEP["myblocks-params"] = D(
 ["An **input** (parameter) lets one custom block handle many situations. Instead of 'jump small' and 'jump big', you build 'jump (height)'.",
  "The step children miss is **dragging the orange parameter** from the define hat into the blocks inside. Without that the block ignores its input and always uses a fixed number.",
  "Name inputs meaningfully — 'size' and 'amount', not 'a' and 'b'. The name is what makes the block readable when you use it later."],
 [E("A parameterised block", "define [draw square (size)]\nrepeat 4\n  move (size) steps\n  turn right 90 degrees\nend",
    "The orange 'size' must be dragged into the move block."),
  E("Using it", "draw square (50)\ndraw square (100)\ndraw square (150)",
    "One definition, three different results."),
  E("Two inputs", "define [damage (amount) to (target)]",
    "Multiple parameters make a block genuinely reusable.")],
 "This is exactly how functions with arguments work in every programming language.",
 "A recipe that says 'serves N' — the same method scaled to a number you choose.",
 ["Add a second input", "Rewrite three similar blocks as one", "Build a shape block that takes sides and size"])

DEEP["ask-answer"] = D(
 ["'ask () and wait' shows an input box and pauses until the player types something. Their reply lands in the **answer** block.",
  "'answer' only holds the **most recent** reply. Ask a second question and the first answer is gone — so store anything you need later in a variable straight away.",
  "'join' sticks text together, which is what makes a program feel personal: 'Hello Sam!' rather than 'Hello'. Remember the trailing space in 'Hello ' or the words run together."],
 [E("Remembering a name", "ask [What is your name?] and wait\nset [name] to (answer)\nsay (join [Hello ] (name)) for 2 seconds",
    "Store immediately, then reuse as often as you like."),
  E("The overwrite trap", "ask [Name?] and wait\nask [Age?] and wait\nsay (answer)",
    "This shows the age, not the name — the second ask overwrote it.")],
 "Handling user input safely is a fundamental part of every application.",
 "A form that asks your name, then greets you by it.",
 ["A chatbot that remembers three facts", "Use the answer in a calculation", "Validate that the input is sensible"])

DEEP["platformer"] = D(
 ["A platform game needs the player to **stand on** solid ground. The usual approach is colour sensing: make every platform exactly the same colour and check for it.",
  "Detection is only half the job. **Collision resolution** is what happens next: if the player has sunk into a platform, move them up one step at a time until they are free. Teleporting them looks wrong; stepping out looks right.",
  "Handle horizontal and vertical collision **separately**, or the player sticks to walls. This is the same approach real 2D engines use."],
 [E("Standing on ground", "repeat until <not <touching color [#7f7f7f]?>>\n  change y by 1\nend\nset [velocity] to 0",
    "Climb out of the platform one pixel at a time."),
  E("Blocking a wall", "change x by 4\nif <touching color [#7f7f7f]?> then\n  change x by -4\nend",
    "Move, test, and undo the move if it was invalid.")],
 "Separating detection from resolution is exactly how professional physics engines are structured.",
 "You cannot walk through a wall — something has to push you back.",
 ["Moving platforms", "One-way platforms you can jump up through", "A level with three platforms and a goal"])

DEEP["pen-art"] = D(
 ["Nested loops plus rotation produce spirograph art. The inner loop draws one shape; the outer loop rotates and repeats it.",
  "The maths must agree: repeats multiplied by the turn angle should total 360, or the pattern will not close into a circle. 36 x 10 = 360; 18 x 20 = 360.",
  "Changing the pen colour in the **outer** loop gives a rainbow across the whole pattern. Putting it in the inner loop changes colour within each shape instead — both are valid, and comparing them is a good experiment."],
 [E("A classic spirograph", "repeat 36\n  repeat 4\n    move 100 steps\n    turn right 90 degrees\n  end\n  turn right 10 degrees\n  change pen color by 5\nend",
    "Square, rotate 10 degrees, repeat 36 times — a full circle of squares."),
  E("Any shape, any rotation", "set [sides] to 6\nrepeat 24\n  repeat (sides)\n    move 60 steps\n    turn right ((360) / (sides)) degrees\n  end\n  turn right 15 degrees\nend",
    "24 x 15 = 360, and the shape is controlled by one variable.")],
 "Generative art is a real creative field, and it is pure loops and maths.",
 "A spirograph toy, or the patterns in a kaleidoscope.",
 ["Design a pattern to a specification", "Make it denser or sparser and explain why", "Randomise colours and sizes"])

DEEP["music-blocks"] = D(
 ["The Music extension adds drums and notes. A **beat** is the unit of musical time; **tempo** controls how fast beats go; notes are numbered, with 60 as middle C.",
  "Rhythm is repetition, so loops are the natural tool. A one-bar drum pattern in a repeat loop becomes a groove.",
  "Two parts must start together or they drift. Trigger both with the **same broadcast** rather than two separate flag clicks — a genuine reason to use messages.",
  "Silence matters: 'rest' is what gives a rhythm its shape."],
 [E("A drum loop", "set tempo to 100\nforever\n  play drum (1) for 0.25 beats\n  rest for 0.25 beats\n  play drum (2) for 0.25 beats\n  rest for 0.25 beats\nend",
    "Rests are as important as the hits."),
  E("A melody", "play note (60) for 0.5 beats\nplay note (62) for 0.5 beats\nplay note (64) for 1 beats",
    "60, 62, 64 walks up the scale."),
  E("Two parts in sync", "when I receive [play-music]\nforever\n  play drum (1) for 0.5 beats\nend",
    "Both sprites receive the same message, so they start together.")],
 "Music software is built on exactly these ideas: timing, loops and synchronisation.",
 "Clapping a rhythm together — everyone has to start on the same beat.",
 ["A three-layer piece", "Tempo that speeds up with difficulty", "A clickable piano"])

DEEP["game-polish"] = D(
 ["**Game feel** is how satisfying a game is to play, moment to moment. It is mostly feedback: every action the player takes should produce a visible or audible response.",
  "'Juice' means the small effects — a pop, a shake, a sound, a flash — that make an action feel good. They are cheap to add and transform how finished a project seems.",
  "**Playtesting** is the real skill. Let someone else play while you watch **silently** and write down every confusion. Not explaining is the hard part, and it is exactly the point: a published game has nobody to explain it.",
  "Then prioritise. Fix the most common confusion first rather than the one that annoys you most."],
 [E("A satisfying collect", "start sound [pop]\nrepeat 4\n  change size by 6\n  change [ghost] effect by 25\nend\nhide\nchange [score] by 1",
    "Sound, animation and score together — the action feels real."),
  E("Damage feedback", "repeat 3\n  change [color] effect by 50\n  wait 0.05 seconds\n  clear graphic effects\n  wait 0.05 seconds\nend",
    "A flash tells the player they were hit without any words.")],
 "User feedback and usability testing are central to all product design, not just games.",
 "A cash machine that beeps when you press a key — you know it worked.",
 ["Give every action feedback", "Run two playtests and compare notes", "Write a prioritised fix list"])

DEEP["publish-share"] = D(
 ["A project is not finished when the code works — it is finished when someone else can enjoy it without you sitting beside them.",
  "**Instructions** need three things: the goal, the controls, and how to win. Test them on someone who has never seen the project.",
  "**Credits** matter. If you used someone's sprite, sound or idea, say so. Attribution is basic honesty, and Scratch's remix culture depends on it.",
  "**Safety** comes first: never put your full name, school, address or contact details in a public project."],
 [E("Good instructions", "Goal: collect all 10 coins before the timer runs out.\nControls: arrow keys to move, space to jump.\nWin: reach the flag with all coins collected.",
    "Three lines, no jargon, nothing assumed."),
  E("Credits", "Sprites from the Scratch library. Bounce sound by [name].\nBased on an idea from Code Club's Ghostbusters project.",
    "Say what you used and where it came from.")],
 "Documentation and attribution are professional obligations in software and in research.",
 "Board game instructions: without them, nobody can play.",
 ["Test your instructions on a newcomer", "Remix a shared project and credit it", "Write a short 'what I learned' note"])

DEEP["l1-capstone"] = D(
 ["A capstone is where separate skills become one project. The change is that **you** decide what to build — nobody is giving you steps to follow.",
  "Plan on paper first: the goal, the player, the rules, and how you win and lose. Ten minutes of planning genuinely saves thirty minutes of confusion.",
  "Build in **layers**, testing each: controls first, then the objective, then scoring, then the endings, then polish. Building everything before testing anything is how projects become unfixable.",
  "Scope is the hardest lesson. A small finished game is worth far more than a big unfinished one."],
 [E("Start-of-game reset", "when green flag clicked\nset [score] to 0\nset [lives] to 3\ngo to x: 0 y: -120\nshow\nset size to 100 %",
    "Every capstone should start with a block like this."),
  E("Test as you build", "when [1] key pressed\nset [score] to 9",
    "A debug key that jumps you near the win condition, so you can test the ending quickly.")],
 "Planning, building in increments and testing continuously is how all real software is made.",
 "Building a model: base first, test it stands, then add detail.",
 ["Write instructions for a new player", "Add one original rule of your own", "Present it and explain one code decision"])

DEEP["l2-capstone"] = D(
 ["A Level 2 capstone is a **specified** project: before coding, write one page saying what it is, how it is played, and the three features it will have.",
  "Break it into **milestones** and build one at a time, testing each. Managing a build across several sessions is the real Level 2 skill.",
  "Use at least three Level 2 techniques — clones, broadcasts, custom blocks, lists or physics — deliberately, because they suit the problem.",
  "Refactor as you go. If the code becomes a tangle, move sections into well-named custom blocks so the main script reads like a plan."],
 [E("A spec", "Title: Cave Escape\nGoal: reach the exit before the air runs out\nControls: arrows to move, space to jump\nFeatures: 1) gravity + platforms  2) cloned falling rocks  3) air timer\nWin: reach the exit.  Lose: air = 0 or crushed.",
    "Agree this before writing any blocks."),
  E("A readable main script", "when green flag clicked\nreset game\nbuild level\nstart timer\nforever\n  handle input\n  check collisions\nend",
    "Every one of those is a custom block. The main script reads like the plan.")],
 "Specification, milestones and refactoring are exactly how professional software teams work.",
 "Building a house: plans, then foundations, then walls — checked at every stage.",
 ["Add a saved high score with a list", "Add a second level", "Present it and explain the hardest bug you fixed"])
