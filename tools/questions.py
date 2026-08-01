#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
questions.py — the MULTIPLE-CHOICE QUESTION BANK.

At least 10 questions for every concept in the curriculum. Each question tests
understanding rather than recall of trivia, and every one carries an
explanation that teaches — shown after the child answers, right or wrong.

Format:  Q(concept, stem, "option|option|option|option", correct_index, why)

Recall Tests are built from this bank: 10 questions drawn per session, mixed
into a fresh order each attempt so a retake is never identical.
"""

BANK = []


def Q(concept, stem, options, correct, why):
    BANK.append({"concept": concept, "stem": stem,
                 "options": options.split("|"), "correct": correct, "why": why})


# =====================================================================
# LEVEL 1
# =====================================================================

# ---- tour ----
Q("tour", "Where do you find the blocks you drag into your code?", "The block palette on the left|The stage at the top right|The sprite list|The costumes tab", 0, "All the blocks live in the palette on the left, sorted into coloured groups.")
Q("tour", "What is a sprite?", "A character or object you can give code to|The background picture|A type of loop|The green flag", 0, "A sprite is a character or object. Each one has its own code, costumes and sounds.")
Q("tour", "What does the green flag do?", "Runs every 'when green flag clicked' script|Saves your project|Deletes the cat|Adds a new sprite", 0, "The green flag is the usual way to start a project running.")
Q("tour", "Where does your project actually appear when it runs?", "On the stage|In the block palette|In the sprite list|In the costumes tab", 0, "The stage is the screen where everything you make is shown.")
Q("tour", "You added blocks but clicking the flag does nothing. What is most likely wrong?", "There is no 'when green flag clicked' block on top|The computer is broken|Scratch needs reinstalling|The sprite is too small", 0, "Without a hat block listening for the flag, nothing tells the script to run.")
Q("tour", "What is a script?", "A stack of blocks joined together|A single sprite|A sound file|The name of the stage", 0, "A script is blocks snapped together so they run in order.")
Q("tour", "How do you know two blocks have joined properly?", "They snap together with no gap|They change colour|They start flashing|A sound plays", 0, "Blocks snap together — if there is a gap, they are not connected and will not run in order.")
Q("tour", "You are editing code but it affects the wrong character. What should you check?", "Which sprite is selected in the sprite list|The volume|The backdrop name|The zoom level", 0, "Code belongs to whichever sprite is selected, so always check the highlighted thumbnail.")
Q("tour", "What happens if you click a block on its own, without a hat block?", "It runs once straight away|Nothing ever happens|It is deleted|It becomes a sprite", 0, "Clicking a block or stack runs it immediately — a quick way to test an idea.")
Q("tour", "Which part of Scratch shows all your characters?", "The sprite list|The palette|The stage|The paint editor", 0, "The sprite list under the stage shows every sprite in your project.")

# ---- sequence ----
Q("sequence", "What is a sequence?", "Instructions carried out in order, one after another|Blocks that all run at the same time|A type of sprite|A sound effect", 0, "A sequence means the order matters — each step runs after the one before it.")
Q("sequence", "If you swap two blocks in a script, what usually happens?", "The result changes|Nothing changes|The project deletes itself|The sprite disappears", 0, "Order matters. Different order, different result.")
Q("sequence", "What is an algorithm?", "A set of steps in order to get a job done|A kind of sprite|A colour of block|A Scratch extension", 0, "An algorithm is just a precise set of steps — a recipe for the computer.")
Q("sequence", "Your sprite does everything instantly and you cannot see the steps. What helps?", "Add 'wait 1 seconds' between the blocks|Delete some blocks|Make the sprite bigger|Change the backdrop", 0, "Waits slow the sequence down so you can actually watch each step happen.")
Q("sequence", "The blocks are: move 10, turn 90, move 10. Where does the sprite end up?", "It moves, turns a quarter turn, then moves in the new direction|It moves 20 steps in a straight line|It spins in a circle|It stays still", 0, "It moves, changes direction by 90 degrees, then moves along the NEW direction.")
Q("sequence", "Why should you predict what code will do before running it?", "It helps you understand and spot mistakes|It makes Scratch run faster|It saves the project|It unlocks new blocks", 0, "Predicting first turns running the code into a test of your thinking.")
Q("sequence", "Can two different orders of blocks reach the same end point?", "Yes, often more than one algorithm works|No, only one order ever works|Only in Level 2|Only with loops", 0, "There is usually more than one way to solve a problem — that is real programming.")
Q("sequence", "Your sprite starts in the wrong place each time you run the project. What fixes it?", "Add 'go to x: y:' at the start|Add more move blocks|Change the costume|Delete the sprite", 0, "Sprites keep their last position, so send them home at the start of every run.")
Q("sequence", "Why must instructions for a computer be precise?", "The computer does exactly what you say, not what you mean|Computers guess well|Scratch fixes mistakes automatically|Precision is only needed in Level 2", 0, "A computer follows your instructions literally — vagueness produces bugs.")
Q("sequence", "Which is a sequence in real life?", "Following a recipe step by step|Choosing a favourite colour|Looking at a picture|Listening to music", 0, "A recipe is a sequence — the order of steps changes the result.")

# ---- motion-steps ----
Q("motion-steps", "How many degrees is a quarter turn?", "90|45|180|360", 0, "90 degrees is a quarter turn; 180 is half and 360 is a full circle.")
Q("motion-steps", "What does 'move 10 steps' do?", "Moves the sprite forwards in the direction it faces|Moves it 10 pixels to the right always|Turns it 10 degrees|Makes it 10 times bigger", 0, "It moves forwards along whatever direction the sprite is currently pointing.")
Q("motion-steps", "You change 'move 10 steps' to 'move 100 steps'. What happens?", "The sprite moves ten times further|The sprite moves slower|Nothing changes|The sprite turns", 0, "The number controls the distance — bigger number, bigger jump.")
Q("motion-steps", "How could you make a sprite move backwards?", "Use a negative number, like move -10 steps|Use turn left|Use 'hide'|You cannot", 0, "Negative steps move the sprite in the opposite direction to where it faces.")
Q("motion-steps", "To draw a square path, which turn do you need each corner?", "90 degrees|60 degrees|120 degrees|45 degrees", 0, "A square has four 90-degree corners: 4 x 90 = 360.")
Q("motion-steps", "To trace a triangle, what turn is needed at each corner?", "120 degrees|90 degrees|60 degrees|180 degrees", 0, "360 divided by 3 sides = 120 degrees per turn.")
Q("motion-steps", "Your sprite ends up upside-down after turning. What fixes it?", "Set the rotation style to left-right|Delete the turn blocks|Make the sprite smaller|Change the backdrop", 0, "Rotation style controls whether a sprite is allowed to rotate all the way round.")
Q("motion-steps", "'point in direction 90' makes the sprite face which way?", "Right|Left|Up|Down", 0, "In Scratch 90 is right, -90 is left, 0 is up and 180 is down.")
Q("motion-steps", "Your sprite has moved off the stage and vanished. What can you do?", "Drag it back, or add 'go to x: 0 y: 0'|Restart the computer|Delete the project|Add more move blocks", 0, "Sending it to 0,0 brings it back to the centre of the stage.")
Q("motion-steps", "Which pair of blocks together makes a sprite follow a path with corners?", "move and turn|say and think|show and hide|play sound and wait", 0, "Moving then turning, repeated, traces a path with corners.")

# ---- looks-say ----
Q("looks-say", "What is the difference between 'say Hello!' and 'say Hello! for 2 seconds'?", "The timed one clears itself, the plain one stays forever|There is no difference|The plain one is louder|The timed one is bigger text", 0, "'say for seconds' tidies up after itself; plain 'say' leaves the bubble on screen.")
Q("looks-say", "How do you clear a speech bubble that will not go away?", "Use a 'say' block with nothing in it|Delete the sprite|Press the green flag|Change the backdrop", 0, "An empty say block clears the bubble.")
Q("looks-say", "Two sprites talk over each other. What is the fix?", "Give each a wait as long as the other's speech|Make them bigger|Delete one sprite|Use think instead", 0, "Matching waits to speaking time makes the sprites take turns properly.")
Q("looks-say", "Which block shows a thought bubble instead of speech?", "think () for () seconds|say () for () seconds|switch costume|start sound", 0, "'think' shows a thought cloud — good for showing what a character feels.")
Q("looks-say", "Sprite A says something for 2 seconds. How long should sprite B wait before replying?", "About 2 seconds|No wait at all|10 seconds|0.1 seconds", 0, "Sprite B should wait roughly as long as sprite A speaks, so they alternate.")
Q("looks-say", "Why keep speech bubbles short?", "Long text overflows and is hard to read|Scratch only allows 8 words|Long text runs slower|It uses more memory", 0, "Bubbles are small — keeping text short keeps it readable.")
Q("looks-say", "Which block would you use for a character greeting the player at the start?", "say () for () seconds|hide|move () steps|erase all", 0, "A timed say shows a greeting and then clears itself automatically.")
Q("looks-say", "What happens if two sprites both use plain 'say' with no waits?", "Both bubbles appear at once and stay|They take turns automatically|Only one shows|Scratch shows an error", 0, "Without timing they speak simultaneously and neither bubble clears.")
Q("looks-say", "Where does a speech bubble appear?", "Next to the sprite that said it|At the top of the stage|In the block palette|In the sprite list", 0, "The bubble belongs to the sprite that ran the block.")
Q("looks-say", "Which is the best way to build a conversation between two sprites?", "Alternate say blocks with matching waits|Put all the says on one sprite|Use forever loops on both|Use hide and show", 0, "Alternating speech with matching waits is how dialogue is timed in Scratch.")

# ---- costumes ----
Q("costumes", "What is a costume?", "One of the pictures a sprite can wear|A sound a sprite plays|The stage background|A kind of loop", 0, "Costumes are the different pictures a sprite can switch between.")
Q("costumes", "How does switching costumes create animation?", "The pictures swap quickly, like a flip-book|The sprite moves faster|The stage changes|The sound loops", 0, "Animation is just pictures swapped fast enough to look like movement.")
Q("costumes", "Which block moves to the sprite's next picture?", "next costume|next backdrop|switch backdrop to|change size by", 0, "'next costume' steps to the following costume in the list.")
Q("costumes", "Your animation is a blur you cannot see. What is missing?", "A wait between costume changes|More costumes|A bigger sprite|A backdrop", 0, "Without a small wait the costumes change too fast to see.")
Q("costumes", "Which tab do you use to see and edit a sprite's pictures?", "The Costumes tab|The Code tab|The Sounds tab|The Stage tab", 0, "The Costumes tab holds all of a sprite's pictures.")
Q("costumes", "You want a sprite to look hurt when hit. What is a good approach?", "Switch to a 'hurt' costume|Make it invisible|Delete the sprite|Change the backdrop", 0, "Costumes are perfect for showing a sprite's state, like hurt or jumping.")
Q("costumes", "How many costumes does a sprite need to look like it is walking?", "At least two, swapped repeatedly|Exactly one|At least ten|None", 0, "Two alternating costumes already read as a walk cycle.")
Q("costumes", "What does the 'costume number' block report?", "Which costume the sprite is currently wearing|How many sprites there are|The sprite's size|The backdrop name", 0, "It tells you the current costume, useful for checking a sprite's state.")
Q("costumes", "A good wait between costume changes for a walk is about:", "0.2 seconds|5 seconds|1 minute|0 seconds", 0, "Around 0.1-0.3 seconds looks like natural movement.")
Q("costumes", "Which block picks one exact picture rather than moving to the next?", "switch costume to ()|next costume|change size by|show", 0, "'switch costume to' jumps straight to the costume you name.")

# ---- animation-loop ----
Q("animation-loop", "What does a 'repeat 10' block do?", "Runs the blocks inside it ten times|Runs the blocks below it ten times|Waits ten seconds|Makes ten sprites", 0, "A repeat loop runs whatever is INSIDE its C-shape, the set number of times.")
Q("animation-loop", "Why use a loop instead of copying the same blocks many times?", "Less code and much easier to change|Loops run faster than blocks|Copying is not allowed|Loops use less battery", 0, "One loop replaces many copies, so changing it means editing one number.")
Q("animation-loop", "Where must blocks go to be repeated?", "Inside the C-shaped mouth of the loop|Underneath the loop|Above the loop|In another sprite", 0, "Only blocks inside the loop's mouth are repeated.")
Q("animation-loop", "What is one pass through a loop called?", "An iteration|A sequence|A sprite|A costume", 0, "Each time round the loop is one iteration.")
Q("animation-loop", "'repeat 4 [move 100 steps, turn 90 degrees]' draws what path?", "A square|A triangle|A circle|A straight line", 0, "Four moves with four 90-degree turns traces a square.")
Q("animation-loop", "You want a walking animation to go on longer. What do you change?", "The repeat number|The sprite's size|The backdrop|The sound", 0, "The repeat count controls how many times the animation cycles.")
Q("animation-loop", "Blocks placed UNDER a repeat loop run when?", "After the loop has finished all its repeats|Never|At the same time as the loop|Before the loop", 0, "The script continues below the loop only once the loop is done.")
Q("animation-loop", "Which is the clearest sign you should use a loop?", "You are about to copy the same blocks again and again|Your sprite is too small|You have two sprites|You need a sound", 0, "Repetition in your code is the signal to reach for a loop.")
Q("animation-loop", "A loop inside another loop is called:", "A nested loop|A double sprite|A broadcast|A clone", 0, "Loops inside loops are nested — the inner one runs fully each time the outer repeats.")
Q("animation-loop", "'repeat 3' containing 'repeat 4' runs the innermost blocks how many times?", "12|7|3|4", 0, "3 x 4 = 12 — the inner loop runs fully on each of the outer loop's 3 passes.")

# ---- forever ----
Q("forever", "When should you use a forever loop instead of repeat?", "For behaviour that should always be running|When you know the exact number of repeats|Only for sounds|Only in Level 2", 0, "Forever suits continuous behaviour like checking, patrolling or animating.")
Q("forever", "What happens to blocks placed UNDER a forever loop?", "They never run|They run first|They run once at the end|They run twice", 0, "A forever loop never finishes, so nothing below it is ever reached.")
Q("forever", "How do you stop a forever loop?", "Press the red stop sign or use 'stop all'|Wait for it to finish|Delete the sprite|Press the green flag again", 0, "Forever never ends by itself — it needs stopping.")
Q("forever", "Which behaviour is best in a forever loop?", "Constantly checking if the player pressed a key|Setting the score to 0|Saying hello once at the start|Adding a sprite", 0, "Checking must repeat constantly, so it belongs in a forever loop.")
Q("forever", "Can two sprites each run their own forever loop at the same time?", "Yes, scripts run in parallel|No, only one at a time|Only in Level 2|Only with clones", 0, "Scratch runs many scripts at once, which is how games feel alive.")
Q("forever", "You put 'set score to 0' inside a forever loop. What goes wrong?", "The score resets constantly and never goes up|The score doubles|Nothing, it is correct|The sprite disappears", 0, "Resetting inside the loop wipes the score every frame — it belongs at the start.")
Q("forever", "Which is the better structure for a game?", "Several small scripts, each with one job|One giant forever loop containing everything|No loops at all|Only repeat loops", 0, "Separate scripts for separate behaviours are far easier to read and debug.")
Q("forever", "A patrolling enemy that moves back and forth all game should use:", "forever|repeat 1|wait|hide", 0, "Patrolling should continue for the whole game, so forever fits.")
Q("forever", "What is the difference between 'repeat 10' and 'forever'?", "Repeat runs a set number of times, forever never stops|They are identical|Forever is faster|Repeat only works on sprites", 0, "The key difference is whether the number of repeats is known.")
Q("forever", "Your project cannot be stopped by the red sign. What is most likely?", "A script is stuck in a loop with no screen refresh|Scratch is broken|The sprite is hidden|The backdrop is wrong", 0, "Tight loops can block stopping — adding a small wait inside usually helps.")

# ---- events-key ----
Q("events-key", "What is an event?", "Something that happens and starts a script|A kind of sprite|A maths block|A costume", 0, "Events are triggers — a key press, a click, the green flag.")
Q("events-key", "How many scripts do you need for four arrow keys?", "Four, one for each key|One|Two|None", 0, "Each key press event needs its own hat block and script.")
Q("events-key", "Which block moves a sprite left?", "change x by -10|change x by 10|change y by 10|change y by -10", 0, "Negative x moves left; positive x moves right.")
Q("events-key", "What is a hat block?", "The rounded block on top that listens for an event|The last block in a script|A block that plays sound|A loop", 0, "Hat blocks sit on top and start the script when their event happens.")
Q("events-key", "Which block moves a sprite up?", "change y by 10|change y by -10|change x by 10|move 10 steps", 0, "In Scratch, y increases upwards.")
Q("events-key", "You press a key and nothing happens. What is worth checking first?", "That you clicked the stage so it has focus|That the sprite is big enough|The backdrop colour|The volume", 0, "Scratch needs the stage focused to receive key presses.")
Q("events-key", "Which trigger suits a character that reacts when tapped?", "when this sprite clicked|when green flag clicked|when I receive|forever", 0, "'when this sprite clicked' fires when the player clicks that sprite.")
Q("events-key", "What makes an event-driven program different from a straight sequence?", "Scripts wait for something to happen before running|It runs faster|It uses fewer blocks|It needs no sprites", 0, "Event-driven code responds to triggers rather than running straight through.")
Q("events-key", "Only one arrow key works in your game. What is the likely cause?", "The other keys have no scripts of their own|The sprite is too small|The stage is wrong|The score is 0", 0, "Each key needs its own hat block; one script cannot cover them all.")
Q("events-key", "Which key event would make a sprite jump?", "when space key pressed|when green flag clicked|when backdrop switches|when I start as a clone", 0, "Space is the usual jump key, triggered by a key-press event.")

# ---- events-click ----
Q("events-click", "Where must you click to test 'when this sprite clicked'?", "On the sprite on the stage|On the sprite in the sprite list|On the green flag|On the palette", 0, "Clicking the thumbnail in the sprite list only selects it — you must click it on the stage.")
Q("events-click", "Which trigger starts the whole project?", "when green flag clicked|when this sprite clicked|when I receive|forever", 0, "The green flag is the standard project start.")
Q("events-click", "Your click reaction is too fast to notice. What helps?", "Add a wait or a longer effect|Delete the sprite|Make the stage bigger|Use a smaller sprite", 0, "Reactions need enough time on screen for the player to see them.")
Q("events-click", "What makes a project interactive?", "It responds to what the player does|It has many sprites|It uses lots of colours|It runs for a long time", 0, "Interactivity means the program reacts to the player's input.")
Q("events-click", "Three sprites should each do something different when clicked. What do you need?", "A separate click script on each sprite|One script on the stage|One script on one sprite|A broadcast only", 0, "Each sprite carries its own click script and its own reaction.")
Q("events-click", "Which trigger fires when the scene changes?", "when backdrop switches to ()|when this sprite clicked|when green flag clicked|when key pressed", 0, "It lets sprites react to a change of scene.")
Q("events-click", "Why give a click a sound as well as a visual change?", "Feedback makes the interaction feel satisfying|Sounds run faster|It saves blocks|It is required by Scratch", 0, "Multiple kinds of feedback make an action feel responsive and clear.")
Q("events-click", "Which is the best trigger for a start button on a title screen?", "when this sprite clicked|forever|when I start as a clone|wait 1 seconds", 0, "The player clicks the button, so a click event is right.")
Q("events-click", "You coded a click reaction but on the wrong sprite. What do you check?", "Which sprite was selected when you added the code|The backdrop|The volume|The score", 0, "Code always belongs to the selected sprite.")
Q("events-click", "What is a trigger?", "The thing that starts a script running|The last block in a script|A type of variable|A sprite costume", 0, "A trigger is the event that causes the script to run.")

# ---- coordinates ----
Q("coordinates", "What is at x: 0, y: 0?", "The centre of the stage|The top left corner|The bottom right corner|Off the stage", 0, "0,0 is the middle of the Scratch stage.")
Q("coordinates", "Which way does y increase?", "Upwards|Downwards|To the right|To the left", 0, "In Scratch, larger y values are higher up the stage.")
Q("coordinates", "What is the difference between 'set x to 10' and 'change x by 10'?", "Set jumps to 10; change moves 10 further|They are the same|Set is faster|Change only works in loops", 0, "Set gives an exact position; change adjusts relative to where the sprite already is.")
Q("coordinates", "What is the usual range of x on the stage?", "About -240 to 240|0 to 100|-180 to 180|-1000 to 1000", 0, "The stage is 480 wide, so x runs roughly -240 to 240.")
Q("coordinates", "What is the usual range of y?", "About -180 to 180|-240 to 240|0 to 360|-100 to 100", 0, "The stage is 360 tall, so y runs roughly -180 to 180.")
Q("coordinates", "Your sprite keeps disappearing off the edge. What is likely wrong?", "The coordinate values are outside the stage range|The sprite is too small|The backdrop is wrong|There are too many sprites", 0, "Values beyond the stage bounds put the sprite out of view.")
Q("coordinates", "Which block sends a sprite to an exact place instantly?", "go to x: () y: ()|glide () secs to x: () y: ()|move () steps|change x by ()", 0, "'go to' is an instant jump to exact coordinates.")
Q("coordinates", "Which block reports how far right a sprite is?", "x position|y position|direction|size", 0, "The x position block reports the sprite's left-right coordinate.")
Q("coordinates", "To move a sprite to the top right corner you would use roughly:", "x: 200 y: 150|x: -200 y: -150|x: 0 y: 0|x: -200 y: 150", 0, "Positive x is right and positive y is up, so both should be positive.")
Q("coordinates", "Why is x, y like Battleships?", "Both use two numbers to find an exact spot on a grid|Both use loops|Both need sprites|Both use colours", 0, "Coordinates are grid references — the same idea as a Battleships square.")

# ---- glide ----
Q("glide", "What does the seconds number in a glide block control?", "How long the movement takes|How far the sprite travels|The sprite's size|The sound volume", 0, "It sets the duration, which controls how fast the journey looks.")
Q("glide", "When would you choose glide over 'go to'?", "When the movement should be seen, not instant|When you want a teleport|When the sprite must hide|Never", 0, "Glide shows the journey; go to is an instant jump.")
Q("glide", "Your glide looks jumpy. What usually helps?", "Use a longer duration such as 1 second|Use 0 seconds|Make the sprite smaller|Delete the backdrop", 0, "Very short glides look like teleports; longer ones read as smooth travel.")
Q("glide", "Which block makes a sprite face the direction it is travelling?", "point towards ()|change x by ()|say ()|hide", 0, "Pointing towards the target makes the movement look natural.")
Q("glide", "A glide of 0.2 seconds compared with 3 seconds feels:", "Much faster|Much slower|Exactly the same|Backwards", 0, "Shorter duration over the same distance means faster movement.")
Q("glide", "Which is best for a rocket flying slowly across space?", "glide 3 secs to x: 200 y: 0|go to x: 200 y: 0|change x by 200|hide", 0, "A long glide shows a slow, visible journey.")
Q("glide", "Why might you combine glide with 'point towards'?", "So the sprite faces where it is going|To make it louder|To change its costume|To reset the score", 0, "Facing the direction of travel makes movement believable.")
Q("glide", "Your sprite arrives sideways after gliding. What fixes it?", "Set the rotation style or point in direction 90|Add more glides|Make it bigger|Use say", 0, "Rotation style controls how the sprite is allowed to turn.")
Q("glide", "Glide moves a sprite to:", "An exact x and y position over time|A random costume|The next backdrop|The sprite list", 0, "Glide targets exact coordinates, just spread over a duration.")
Q("glide", "Which gives the smoothest-looking movement?", "glide|go to|switch costume|hide then show", 0, "Glide interpolates the movement, which is what makes it look smooth.")

# ---- backdrops ----
Q("backdrops", "Where does backdrop code usually live?", "On the Stage|On the main sprite|In the palette|In the costumes tab", 0, "The Stage has its own code area for backdrop behaviour.")
Q("backdrops", "How can a sprite react when the scene changes?", "Use 'when backdrop switches to'|Use 'when green flag clicked'|Use 'move 10 steps'|It cannot", 0, "That hat block lets scenery drive character behaviour.")
Q("backdrops", "How do you stop a sprite appearing in the wrong scene?", "Use hide and show with the backdrop change|Delete it|Make it small|Move it off stage only", 0, "Hiding and showing per scene is the reliable way to manage visibility.")
Q("backdrops", "What is a backdrop?", "The picture behind everything on the stage|A sprite costume|A type of sound|A variable", 0, "The backdrop is the stage's background image.")
Q("backdrops", "Which block moves to the next background?", "next backdrop|next costume|switch costume to|change y by", 0, "'next backdrop' steps through the backdrop list.")
Q("backdrops", "Why add a wait after switching backdrops in a story?", "So the player has time to see the new scene|To save memory|To make sprites bigger|To reset the score", 0, "Instant changes give the player no time to read or absorb the scene.")
Q("backdrops", "In a film, how do you know the location changed?", "The background changes|The music stops|The credits roll|The screen goes black", 0, "Changing the background is exactly what a backdrop switch does.")
Q("backdrops", "You added backdrop code to a sprite by mistake. What should you do?", "Move it to the Stage|Delete the sprite|Add another backdrop|Change the costume", 0, "Backdrop logic belongs on the Stage.")
Q("backdrops", "Which is a good use of multiple backdrops?", "Showing different scenes in a story|Making a sprite jump|Adding a score|Playing a sound", 0, "Multiple backdrops let you build scenes and settings.")
Q("backdrops", "A title screen and a game screen are best built with:", "Two backdrops plus show/hide on sprites|One backdrop only|Two projects|No backdrops", 0, "Separate backdrops with managed sprite visibility create clean screens.")

# ---- size-effects ----
Q("size-effects", "Why should you set size at the start of a project?", "So it resets to the same size every run|To make it run faster|To add sound|To change the backdrop", 0, "Without a reset, size changes carry over into the next game.")
Q("size-effects", "What does the ghost effect do?", "Makes the sprite see-through|Makes it bigger|Changes its colour to white|Deletes it", 0, "Ghost controls transparency — 100 is fully invisible.")
Q("size-effects", "How do you make a collected item disappear?", "hide|show|change size by 10|say", 0, "Hiding removes it from view when it is picked up.")
Q("size-effects", "Your sprite is invisible when the game starts. What is the likely cause?", "It was hidden last game and never shown|It is too small|The backdrop is dark|The score is 0", 0, "A hidden sprite stays hidden until a 'show' block runs.")
Q("size-effects", "Your sprite grows bigger every time you play. What fixes it?", "Use 'set size to 100' at the start|Use 'change size by' at the start|Delete the sprite|Hide it", 0, "'Set' forces an exact size; 'change' just keeps adding.")
Q("size-effects", "What does 'set size to 50 %' do?", "Makes the sprite half its normal size|Doubles the size|Hides it|Makes it 50 pixels wide", 0, "Size is a percentage where 100% is the sprite's normal size.")
Q("size-effects", "Which block removes leftover colour or ghost effects?", "clear graphic effects|hide|erase all|stop all", 0, "'clear graphic effects' resets all visual effects on a sprite.")
Q("size-effects", "Which combination makes a satisfying 'collect' animation?", "Grow, fade with ghost, then hide|Just hide instantly|Change backdrop|Play a long sound", 0, "Layering a grow, a fade and a hide gives clear, pleasing feedback.")
Q("size-effects", "What three things should most projects reset at the start?", "Position, size and visibility|Sound, colour and score only|Nothing|Costume names", 0, "Resetting position, size and show/hide prevents a whole class of bugs.")
Q("size-effects", "A ghost effect of 100 means the sprite is:", "Completely invisible|Fully solid|Twice as big|Upside down", 0, "Ghost 100 is fully transparent; 0 is fully solid.")

# ---- sound-play ----
Q("sound-play", "What is the difference between 'start sound' and 'play sound until done'?", "Start carries straight on; until done waits for the sound to finish|They are identical|Start is louder|Until done repeats", 0, "It matters when the next block should run.")
Q("sound-play", "Where do a sprite's sounds live?", "In its Sounds tab|In the Costumes tab|On the Stage only|In the palette", 0, "Each sprite has its own Sounds tab.")
Q("sound-play", "Your sounds overlap into noise. What helps?", "Use 'play until done' or stop other sounds|Add more sounds|Make them louder|Delete the sprite", 0, "Overlapping starts pile sounds on top of each other.")
Q("sound-play", "Why does sound matter in a game?", "It gives feedback and makes actions feel real|It makes the game run faster|It is required|It saves blocks", 0, "Sound is cheap polish that communicates what just happened.")
Q("sound-play", "Which block would you use for a jump sound that should not pause the game?", "start sound|play sound until done|stop all sounds|wait", 0, "Start sound lets the action continue immediately.")
Q("sound-play", "Which block silences everything?", "stop all sounds|stop all|hide|erase all", 0, "'stop all sounds' silences audio without stopping the project.")
Q("sound-play", "You hear nothing at all. What should you check?", "The sprite has the sound and the volume is up|The backdrop|The score|The sprite's size", 0, "Check the sound is attached to the sprite and the system volume is on.")
Q("sound-play", "Which block makes the sound quieter?", "change volume by -10|change volume by 10|start sound|stop all sounds", 0, "A negative change reduces the volume.")
Q("sound-play", "When should you use 'play sound until done'?", "When the next action must wait for the sound|For rapid game effects|Never|Only on the Stage", 0, "It is right when timing depends on the sound finishing.")
Q("sound-play", "A good rule for game sounds is:", "Every important player action gets its own sound|One sound for everything|No sounds|Only music", 0, "Distinct sounds tell the player exactly what happened.")

# ---- wait-timing ----
Q("wait-timing", "What does 'wait 1 seconds' do?", "Pauses that script for one second|Pauses the whole computer|Repeats a block|Stops the project", 0, "It pauses only the script it is in; other scripts keep running.")
Q("wait-timing", "Which wait is better for smooth animation?", "0.1 seconds|5 seconds|1 minute|10 seconds", 0, "Short waits give smooth motion; long ones look like slideshow steps.")
Q("wait-timing", "Everything seems to happen at once. What is missing?", "Waits between the actions|More sprites|A backdrop|A variable", 0, "Without waits the steps run too fast to distinguish.")
Q("wait-timing", "How do two sprites take turns speaking?", "Match one sprite's wait to the other's speaking time|Use forever on both|Hide one sprite|Use random waits", 0, "Timing their waits to each other keeps a conversation in order.")
Q("wait-timing", "What does 'wait until' do?", "Pauses until a condition becomes true|Waits a fixed number of seconds|Repeats forever|Stops the script", 0, "It waits on a condition rather than a fixed time.")
Q("wait-timing", "Your animation is jerky. What should you try?", "Shorter waits between frames|Longer waits|Removing all waits|Adding more sprites", 0, "Shorter waits mean more frames per second, which looks smoother.")
Q("wait-timing", "Why can timing with waits drift out of sync over a long project?", "Small differences add up over time|Waits are random|Scratch has a bug|Sprites get tired", 0, "This is exactly why broadcasts are better for coordinating sprites later on.")
Q("wait-timing", "A sprite should pause until the player presses space. Best block?", "wait until <key space pressed?>|wait 1 seconds|forever|hide", 0, "Wait until responds to the player rather than guessing a time.")
Q("wait-timing", "In a 3-step scene, waits let you control:", "The order and pacing of the steps|The sprite's colour|The score|The backdrop size", 0, "Waits are how you choreograph when each thing happens.")
Q("wait-timing", "Which is true about waits?", "They pause only the script they are inside|They pause every sprite|They delete blocks|They reset variables", 0, "Other scripts continue running during a wait.")

# ---- if-basic ----
Q("if-basic", "What shape of block fits in an 'if' condition slot?", "A pointy (boolean) block|A round block|A stack block|A hat block", 0, "Boolean blocks are pointy and report true or false.")
Q("if-basic", "Why is an 'if' usually placed inside a forever loop?", "So it keeps checking again and again|To make it run faster|Because Scratch requires it|To save blocks", 0, "Checked once, an if only tests at that instant; games need constant checking.")
Q("if-basic", "What is a condition?", "Something that is either true or false|A type of sprite|A sound|A costume", 0, "Conditions are true/false tests that decide whether code runs.")
Q("if-basic", "'IF it rains THEN take an umbrella' is an example of:", "A conditional|A loop|A variable|A broadcast", 0, "It runs an action only when a condition is true.")
Q("if-basic", "Your if block never seems to do anything. What is a likely cause?", "It is not inside a loop, so it checked only once|The sprite is too small|The backdrop is wrong|There are too many sprites", 0, "A one-time check usually misses the moment the condition becomes true.")
Q("if-basic", "What is a boolean?", "A value that is either true or false|A number over 100|A kind of sprite|A sound", 0, "Booleans are the true/false values that conditions produce.")
Q("if-basic", "Which block reports whether a sprite is touching another?", "touching ()?|move () steps|say ()|change x by ()", 0, "It is a boolean sensing block that reports true or false.")
Q("if-basic", "An empty condition slot in an if block means:", "The if will not do anything useful|Scratch fills it automatically|The project crashes|It runs forever", 0, "Without a condition there is nothing to test.")
Q("if-basic", "What is the difference between 'if' and 'wait until'?", "If checks once and moves on; wait until pauses until true|They are identical|If is faster|Wait until repeats", 0, "One tests and continues, the other blocks the script until true.")
Q("if-basic", "Which structure detects a collision continuously?", "forever containing if <touching ...?>|if on its own|repeat 1 containing if|wait 1 seconds", 0, "Continuous detection needs the check repeated inside a forever loop.")

# ---- sensing-touch ----
Q("sensing-touch", "How does a game know two things collided?", "Touching sensing|The score|The backdrop|A costume", 0, "Sensing blocks detect when sprites touch.")
Q("sensing-touch", "Why might colour sensing fail?", "The colour picked is not an exact match|Colours never work|The sprite is too big|Sound is off", 0, "Colour sensing needs the exact shade — use the eyedropper on the real pixel.")
Q("sensing-touch", "A collision fires many times per second. How do you make it happen once?", "Hide the object or add a short wait|Delete the sprite|Use a bigger sprite|Add another loop", 0, "Removing the object or pausing stops repeated triggering.")
Q("sensing-touch", "Sprites look like they touch but nothing happens. What is a likely reason?", "Transparent edges in the costume|The score is 0|The music is off|The backdrop is wrong", 0, "Scratch senses the visible pixels, and costumes often have invisible padding.")
Q("sensing-touch", "Which block detects touching a coloured line, such as a race track?", "touching color ()?|touching ()?|distance to ()|key pressed?", 0, "Colour sensing is ideal for tracks, walls and platforms.")
Q("sensing-touch", "What does 'distance to' report?", "How far away another sprite or the mouse is|How fast a sprite moves|The score|The sprite's size", 0, "Useful for 'the enemy notices you when you get close'.")
Q("sensing-touch", "In a collect game, what should happen when the player touches a coin?", "Score up, sound, and the coin hides|Nothing|The game stops|The backdrop changes", 0, "Collision is a trigger for feedback and game logic.")
Q("sensing-touch", "Where should a touching check normally live?", "Inside a forever loop|Under a forever loop|On the Stage only|In the Sounds tab", 0, "Detection must repeat constantly, so it goes inside forever.")
Q("sensing-touch", "Which is a boolean sensing block?", "touching ()?|move () steps|change score by 1|say ()", 0, "It is pointy and reports true or false.")
Q("sensing-touch", "Why keep all your platforms exactly the same colour?", "So one colour check works for all of them|To look nicer|To save memory|Scratch requires it", 0, "A single consistent colour makes collision detection reliable.")

# ---- sensing-key ----
Q("sensing-key", "Why is 'key pressed?' sensing smoother than key-press events?", "It checks constantly with no key-repeat delay|It uses fewer blocks|It is newer|It makes sprites bigger", 0, "Polling avoids the pause before a held key starts repeating.")
Q("sensing-key", "How do you allow diagonal movement?", "Put all the ifs in the same forever loop|Use separate forever loops|Use key events instead|You cannot", 0, "In one loop, two conditions can both be true on the same pass.")
Q("sensing-key", "What does 'polling' mean?", "Checking something over and over|Voting|Playing a sound|Saving a project", 0, "Polling is repeatedly asking 'is this true yet?'.")
Q("sensing-key", "Your sprite moves far too fast. What do you change?", "Use a smaller change value like 3|Add more ifs|Remove the loop|Make the sprite bigger", 0, "The change amount per frame controls speed.")
Q("sensing-key", "Old key-event scripts still exist alongside new sensing scripts. What happens?", "They fight each other and movement feels odd|Nothing|The project speeds up|Scratch merges them", 0, "Two systems moving the same sprite cause conflicts — delete the old one.")
Q("sensing-key", "Which block reports true while a key is held down?", "key () pressed?|when key pressed|touching ()?|answer", 0, "It is a boolean that stays true for as long as the key is down.")
Q("sensing-key", "Which structure gives responsive four-way control?", "forever with four if blocks inside|four separate hat blocks|one repeat 10|wait until", 0, "One loop polling four keys is the standard responsive control pattern.")
Q("sensing-key", "Games usually prefer polling over events for movement because:", "It feels smoother and allows diagonals|It uses less memory|Events are broken|It is easier to type", 0, "Smoothness and simultaneous keys are why games poll.")
Q("sensing-key", "What is the trade-off with key events?", "Simple to build but movement stutters|They are always better|They cannot be used|They need clones", 0, "Events are simpler but have the key-repeat delay.")
Q("sensing-key", "How would you add a 'run faster while shift is held'?", "Nest another if checking the shift key|Add another sprite|Use a backdrop|Use a costume", 0, "Nesting conditions creates speed states.")

# ---- random ----
Q("random", "Why use random numbers in a game?", "Every play is different, so it stays interesting|It makes the game faster|It saves blocks|It is required", 0, "Unpredictability is what makes a game worth replaying.")
Q("random", "Which range keeps a sprite on stage horizontally?", "-200 to 200|-500 to 500|0 to 1000|-1000 to 0", 0, "The stage is about -240 to 240 wide, so -200 to 200 is safely inside.")
Q("random", "Your sprite is vibrating in place. What is the likely cause?", "A random position is being picked every frame|The sprite is too big|The sound is on|The score is high", 0, "Re-picking a random value constantly makes the sprite jitter.")
Q("random", "Which block gives a different number each time?", "pick random () to ()|set () to ()|x position|answer", 0, "Pick random returns a new value on each use.")
Q("random", "How can random make timing feel natural?", "wait (pick random 1 to 3) seconds|wait 1 seconds always|Never use waits|Use forever only", 0, "Varying the gaps stops events feeling mechanical.")
Q("random", "'pick random 1 to 6' is like:", "Rolling a dice|Flipping one coin|Counting to 6|Adding numbers", 0, "It gives a whole number from 1 to 6, exactly like a dice.")
Q("random", "Where should you pick a random value if the sprite should keep it for a while?", "Once, before the loop or after a wait|Every frame inside the loop|Never|On the Stage only", 0, "Picking once and keeping it avoids constant re-rolling.")
Q("random", "Which makes a target appear unpredictably?", "go to x: (pick random -200 to 200) y: (pick random -150 to 150)|go to x: 0 y: 0|move 10 steps|hide", 0, "Random coordinates place the target somewhere new each time.")
Q("random", "A range that keeps a sprite fully on stage vertically is about:", "-150 to 150|-300 to 300|0 to 500|-500 to 500", 0, "The stage is roughly -180 to 180 tall, so -150 to 150 stays safely inside.")
Q("random", "Combining random size, position and wait creates:", "A lively, varied scene|A slower project|An error|Fewer sprites", 0, "Layering randomness makes a scene feel alive rather than repetitive.")

# ---- variable-score ----
Q("variable-score", "What is a variable?", "A named box that stores a value you can change|A type of sprite|A sound|A costume", 0, "Think of it as a labelled box holding one value.")
Q("variable-score", "What is the difference between 'set' and 'change by'?", "Set puts an exact value in; change adds to what is there|They are the same|Set is faster|Change only works on scores", 0, "Set replaces the value; change adjusts it.")
Q("variable-score", "Why 'set score to 0' when the flag is clicked?", "So every game starts fresh|To make it run faster|To hide the score|Scratch requires it", 0, "Without a reset the previous game's score carries over.")
Q("variable-score", "Your score jumps up by many points at once. What is the cause?", "The change block is running every frame in a loop|The score is too big|The sprite is small|The sound is on", 0, "The collision fires repeatedly — hide the item or add a wait.")
Q("variable-score", "What makes a good variable name?", "score|thing|x|a", 0, "Clear names make code readable — a real programming habit.")
Q("variable-score", "Which block adds one point?", "change score by 1|set score to 1|show variable score|hide variable score", 0, "Change adds to the current value.")
Q("variable-score", "How do you let the player see their score?", "Show the variable on the stage|Hide the variable|Use a sound|Change the backdrop", 0, "Players need to see the score for it to matter.")
Q("variable-score", "A high-score variable should update when:", "The new score beats the old high score|Every frame|Never|At the start only", 0, "That comparison is what makes it a high score.")
Q("variable-score", "Which variable option gives every clone its own copy?", "For this sprite only|For all sprites|Global|Hidden", 0, "'For this sprite only' creates a local copy per sprite and per clone.")
Q("variable-score", "What is stored in a variable?", "One value at a time|Many values at once|Only numbers|Only words", 0, "One variable holds one value; lists hold many.")

# ---- if-else ----
Q("if-else", "When do you need 'if ... else'?", "When there are exactly two possible outcomes|When there is one outcome|Only in loops|Never", 0, "If-else picks between two paths.")
Q("if-else", "If the condition is false, which part runs?", "The else part|The if part|Both|Neither", 0, "Else is the path taken when the condition is false.")
Q("if-else", "Can both branches of an if-else run at the same time?", "No, only one|Yes, always|Only in Level 2|Only with clones", 0, "Exactly one branch runs each time.")
Q("if-else", "Both your win and lose messages appear. What went wrong?", "You used two separate ifs, or the conditions overlap|The sprite is too big|The sound is on|The backdrop is wrong", 0, "If-else guarantees only one path runs.")
Q("if-else", "'If you finish your homework, then you play, ELSE you keep working' is:", "An if-else|A loop|A variable|A broadcast", 0, "Two outcomes, chosen by one condition.")
Q("if-else", "Your else branch never runs. What should you check?", "Whether the condition is always true|The volume|The backdrop|The sprite size", 0, "If the condition can never be false, else is unreachable.")
Q("if-else", "How would you handle three outcomes such as win, draw and lose?", "Nest an if inside the else|Use one if only|Use a loop|Use a sound", 0, "Nesting conditionals handles more than two cases.")
Q("if-else", "A quiz answer check is best written as:", "if <answer = correct> then [point] else [try again]|two separate ifs|forever only|wait until", 0, "There are exactly two outcomes, which is what if-else is for.")
Q("if-else", "What does 'tracing' code mean?", "Following which branch runs, step by step|Drawing with the pen|Copying blocks|Deleting code", 0, "Tracing is a core debugging skill.")
Q("if-else", "Which is tidier than two ifs with opposite conditions?", "One if-else|Three ifs|A forever loop|A broadcast", 0, "If-else expresses the either/or clearly and cannot double-fire.")

# ---- repeat-until ----
Q("repeat-until", "Which loop suits 'keep going until you reach the goal'?", "repeat until|repeat 10|forever|wait", 0, "Repeat until runs while working towards a condition.")
Q("repeat-until", "Why might a repeat-until loop never stop?", "The condition can never become true|Loops always stop|The sprite is too small|The sound is off", 0, "If nothing can make the condition true, the loop runs forever.")
Q("repeat-until", "What does 'wait until' do?", "Pauses the script until a condition is true|Repeats blocks|Stops the project|Plays a sound", 0, "It is the pausing version of the same idea.")
Q("repeat-until", "Your repeat-until ends immediately. Why?", "The condition was already true at the start|The loop is broken|The sprite is hidden|The score is 0", 0, "If it is true before the loop begins, the loop body never runs.")
Q("repeat-until", "'Keep stirring until it is smooth' is like which loop?", "repeat until|repeat 10|forever|wait 1 seconds", 0, "The end is defined by a condition, not a count.")
Q("repeat-until", "Which loop should you use when you know the exact number of repeats?", "repeat ()|repeat until|forever|wait until", 0, "A fixed count means a plain repeat loop.")
Q("repeat-until", "Which loop never ends on its own?", "forever|repeat 10|repeat until|wait until", 0, "Forever continues until the project is stopped.")
Q("repeat-until", "How would you end a loop on two possible conditions?", "Use 'or' to combine them|Use two loops|Use forever|You cannot", 0, "Combining conditions with 'or' ends the loop when either happens.")
Q("repeat-until", "A chasing sprite should move until it catches the target. Best structure?", "repeat until <touching target?> [move 5 steps]|forever [move 5 steps]|repeat 10|wait until", 0, "The chase should end exactly when it catches the target.")
Q("repeat-until", "'stop this script' does what?", "Stops just this one script|Stops the whole project|Deletes the sprite|Clears variables", 0, "It ends only the script it is in, leaving others running.")

# ---- mouse-follow ----
Q("mouse-follow", "How do you make a sprite face the mouse?", "point towards mouse-pointer|go to x: 0 y: 0|say hello|hide", 0, "Point towards rotates the sprite to face the target.")
Q("mouse-follow", "How do you build a paddle that slides side to side only?", "set x to (mouse x)|go to mouse-pointer|change y by 10|point towards", 0, "Setting only x keeps the paddle on a fixed height.")
Q("mouse-follow", "Following code must sit inside which block?", "forever|repeat 1|wait|if on edge bounce", 0, "Following must be continuous, so it goes in a forever loop.")
Q("mouse-follow", "Your sprite sits exactly on the pointer and hides it. What helps?", "Offset it, for example change y by -20|Make it bigger|Delete it|Use say", 0, "An offset keeps the cursor visible.")
Q("mouse-follow", "Your following sprite spins wildly. What fixes it?", "Set an appropriate rotation style|Add more loops|Make it smaller|Change the backdrop", 0, "Rotation style controls whether it flips or spins fully.")
Q("mouse-follow", "Which blocks report where the mouse is?", "mouse x and mouse y|x position and y position|answer|timer", 0, "They give the pointer's coordinates.")
Q("mouse-follow", "How could a sprite follow only when the mouse is close?", "Check 'distance to mouse-pointer' first|Use a bigger sprite|Use a sound|Use a costume", 0, "Adding a distance condition makes the following conditional.")
Q("mouse-follow", "'go to mouse-pointer' makes the sprite:", "Sit exactly on the pointer|Face the pointer|Move away|Hide", 0, "It matches the pointer's position exactly.")
Q("mouse-follow", "For eyes that track the player, the best block is:", "point towards mouse-pointer|go to mouse-pointer|hide|change size by", 0, "Pointing rotates the eyes to look at the cursor without moving them.")
Q("mouse-follow", "In a Pong-style game, the paddle usually follows:", "The mouse on one axis|The mouse on both axes|A random position|The backdrop", 0, "Constraining to one axis keeps the paddle on its side of the court.")

# ---- bounce ----
Q("bounce", "Which block keeps a sprite on the stage by reversing it at the edge?", "if on edge, bounce|go to x: 0 y: 0|hide|wait", 0, "It flips the sprite's direction when it reaches the edge.")
Q("bounce", "Your bouncing sprite is upside-down. What fixes it?", "Set rotation style to left-right|Make it bigger|Add a sound|Change the backdrop", 0, "The default all-around rotation lets sprites flip over.")
Q("bounce", "Where must the bounce block go?", "Inside the forever loop with the move block|Under the loop|On the Stage|In the Sounds tab", 0, "It must run every frame alongside the movement.")
Q("bounce", "How do you make each run take a different path?", "point in direction (pick random 1 to 360) at the start|Use the same direction|Hide the sprite|Add a costume", 0, "A random starting direction makes each run unique.")
Q("bounce", "Your sprite gets stuck vibrating on the edge. What helps?", "Move it inward slightly or increase the step size|Delete it|Make it bigger|Add a sound", 0, "It is re-triggering the bounce every frame while still on the edge.")
Q("bounce", "A patrolling enemy is usually built from:", "move plus if on edge bounce inside forever|hide and show|say blocks|a single glide", 0, "That pairing creates continuous back-and-forth movement.")
Q("bounce", "What real-world idea does bouncing model?", "A ball rebounding off a wall|Gravity pulling down|Friction|Wind", 0, "The direction reverses on impact, just like a rebound.")
Q("bounce", "Rotation style 'left-right' means the sprite:", "Only flips horizontally, never upside-down|Spins fully|Cannot turn|Turns 90 degrees only", 0, "It keeps characters the right way up while still facing left or right.")
Q("bounce", "Two bouncing sprites should react when they hit each other. What do you add?", "An if with touching sensing|Another bounce block|A backdrop|A sound only", 0, "Sprite-to-sprite collision needs touching sensing.")
Q("bounce", "The bounce block works on which boundary?", "The edge of the stage|Other sprites|Coloured lines|Variables", 0, "It specifically handles the stage edge.")

# ---- debug-basics ----
Q("debug-basics", "What is a bug?", "A mistake that makes a program behave wrongly|A type of sprite|A sound|A loop", 0, "A bug is an error in the code causing unexpected behaviour.")
Q("debug-basics", "What is the first step when debugging?", "Say what it should do versus what it actually does|Delete the script|Restart the computer|Add more blocks", 0, "Naming the gap between expected and actual focuses the search.")
Q("debug-basics", "Why change only one thing at a time?", "So you know which change fixed it|To save time|Scratch requires it|To use fewer blocks", 0, "Changing many things at once hides which one mattered.")
Q("debug-basics", "How can you test one script on its own?", "Click just that stack of blocks|Press the green flag|Delete the others|Hide the sprite", 0, "Clicking a stack runs it in isolation.")
Q("debug-basics", "How can a 'say' block help you debug?", "It shows you what the code thinks is happening|It fixes bugs automatically|It deletes errors|It saves the project", 0, "Displaying a value reveals what is really going on inside the code.")
Q("debug-basics", "Your project runs too fast to see the problem. What helps?", "Add waits to slow it down|Make it faster|Delete blocks|Add sprites", 0, "Slowing execution makes the failure visible.")
Q("debug-basics", "After fixing a bug you should:", "Run it again to confirm the fix|Move on immediately|Delete the script|Add a new feature", 0, "Fixing without re-testing is how bugs come back.")
Q("debug-basics", "If the program does something strange, who is usually right?", "The computer — it does exactly what it was told|The programmer|Nobody|Scratch", 0, "The computer follows instructions literally; find what it was actually told.")
Q("debug-basics", "Why is debugging a normal part of programming?", "All programmers spend much of their time finding bugs|Only beginners get bugs|Bugs are rare|It means you failed", 0, "Debugging is the job, not a sign of failure.")
Q("debug-basics", "A good habit before making big changes is:", "Keep a copy so you can go back|Delete everything|Change many things at once|Ignore testing", 0, "A safe copy lets you experiment without losing working code.")

# ---- game-win-lose ----
Q("game-win-lose", "What is a win condition?", "The rule that decides the player has won|The starting score|A sprite costume|A backdrop", 0, "It is the test that ends the game in success.")
Q("game-win-lose", "Why use '>' rather than '=' when checking a score?", "The score might skip past the exact number|'=' does not work|'>' is faster|Scratch requires it", 0, "If the score jumps by 2 or 5, an exact match can be missed entirely.")
Q("game-win-lose", "Your win message flashes and disappears instantly. What is wrong?", "'stop all' ran before the message could be read|The text is too small|The sound is off|The sprite is hidden", 0, "Say the message first, give it time, then stop.")
Q("game-win-lose", "Your game ends the moment it starts. What is the likely cause?", "Variables were not reset, so the condition was already true|The sprite is too big|The backdrop is wrong|The sound is on", 0, "Resetting score and lives at the start prevents this.")
Q("game-win-lose", "How should the game tell the player they won?", "A message and a backdrop change|Nothing|By stopping silently|By hiding all sprites", 0, "Clear feedback is essential — a silent ending confuses players.")
Q("game-win-lose", "What is a lose condition?", "The rule that ends the game in failure|A high score|A sprite|A costume", 0, "For example, lives reaching zero or time running out.")
Q("game-win-lose", "Why write your rules in plain English before coding?", "It makes turning them into blocks much easier|It is required|It saves memory|It makes it faster", 0, "Designing before coding is what separates a planned game from a mess.")
Q("game-win-lose", "What is 'game state'?", "Whether the game is playing, won or lost|The sprite's size|The backdrop colour|The score only", 0, "Game state describes which part of the game is currently active.")
Q("game-win-lose", "You should test a game's endings by:", "Deliberately triggering both win and lose|Only playing normally|Never testing|Asking someone else", 0, "Both endings need testing on purpose, since they are easy to get wrong.")
Q("game-win-lose", "Which block ends the whole project?", "stop all|stop this script|hide|wait", 0, "'stop all' halts every script in the project.")

# ---- l1-capstone ----
Q("l1-capstone", "What should you do before building a big project?", "Plan it — goal, controls, rules, win and lose|Start coding immediately|Add every sprite first|Pick a backdrop", 0, "Ten minutes of planning saves thirty minutes of confusion.")
Q("l1-capstone", "What should you build and test first?", "The player controls|The ending|The title screen|The music", 0, "Get the core interaction working before layering features on it.")
Q("l1-capstone", "Why test after each layer instead of at the end?", "It is much easier to find what broke|It looks better|It is faster to type|Scratch requires it", 0, "Testing in layers isolates problems to the thing you just added.")
Q("l1-capstone", "Your project idea is far too big. What is the best response?", "Cut it down to one screen and one mechanic|Build it all anyway|Give up|Copy another project", 0, "A finished small game beats an unfinished ambitious one.")
Q("l1-capstone", "Which blocks should run at the start of your game?", "Reset score, position, size and show|Only the ending|None|Just the sound", 0, "Resetting state at the start prevents a whole class of bugs.")
Q("l1-capstone", "What is a capstone project?", "A project that brings together everything you have learned|A first lesson|A type of sprite|A backdrop", 0, "It is where all the separate skills combine into one build.")
Q("l1-capstone", "Presenting your project means:", "Demonstrating it and explaining your code choices|Only showing the title|Hiding the code|Deleting it", 0, "Explaining your decisions shows real understanding.")
Q("l1-capstone", "What is iteration?", "Improving a project through repeated testing|Copying a project|Deleting blocks|Adding sprites", 0, "Iteration means build, test, improve, repeat.")
Q("l1-capstone", "A good order for building a game is:", "Controls, objective, scoring, endings, polish|Polish, endings, controls|Endings first|Random order", 0, "Build the core first, then layer features, testing at each stage.")
Q("l1-capstone", "Why write instructions for your player?", "They cannot see your code or read your mind|It is required|It adds points|It makes it run faster", 0, "A game that needs explaining in person is not finished.")

# =====================================================================
# LEVEL 2
# =====================================================================

# ---- operators-math ----
Q("operators-math", "Where do green operator blocks go?", "Inside another block's slot|Underneath a block|On the Stage only|In the Sounds tab", 0, "Operators are values, so they slot inside other blocks.")
Q("operators-math", "What does 'mod' give you?", "The remainder after dividing|The total|The bigger number|A random number", 0, "10 mod 3 is 1, because 3 goes into 10 three times with 1 left over.")
Q("operators-math", "How would you double a score?", "(score) * (2)|(score) + (2)|(score) / (2)|(score) - (2)", 0, "Multiplying by 2 doubles the value.")
Q("operators-math", "Your division shows a long decimal. What tidies it?", "round ()|join ()|not ()|hide", 0, "Round gives the nearest whole number.")
Q("operators-math", "'set score to ((score) + (5))' does the same as:", "change score by 5|set score to 5|change score by -5|show variable score", 0, "Both add 5 to the current score.")
Q("operators-math", "How could you detect every 5th point?", "if ((score) mod (5)) = 0|if (score) = 5|if (score) > 5|if (score) < 5", 0, "Mod 5 equals 0 at 5, 10, 15 and so on.")
Q("operators-math", "7 coins worth 10 points each. Which expression gives the score?", "(coins) * (10)|(coins) + (10)|(coins) / (10)|(coins) mod (10)", 0, "Multiplication is repeated addition — 7 lots of 10.")
Q("operators-math", "What is an expression?", "Blocks combined to work out a value|A type of sprite|A loop|A sound", 0, "An expression calculates and reports a value.")
Q("operators-math", "Your nested expression is impossible to read. What helps?", "Build it in stages using a helper variable|Add more nesting|Delete it|Use a sound", 0, "Breaking a calculation into named steps makes it readable.")
Q("operators-math", "Which block subtracts?", "() - ()|() + ()|() * ()|() mod ()", 0, "The minus operator subtracts the second value from the first.")

# ---- operators-compare ----
Q("operators-compare", "What do comparison blocks report?", "True or false|A number|A sprite|A sound", 0, "Comparisons are booleans — they report true or false.")
Q("operators-compare", "Why is '>' safer than '=' for a score check?", "The score might skip the exact value|'=' is broken|'>' is faster|Scratch prefers it", 0, "If the score jumps by 2, it can step straight over the exact number.")
Q("operators-compare", "How do you check 'at least 10'?", "(score) > 9|(score) < 10|(score) = 10|(score) mod 10", 0, "Greater than 9 includes 10 and everything above.")
Q("operators-compare", "You put a comparison into a 'say' block and clicked it. What appears?", "true or false|The number|An error|Nothing", 0, "Seeing the boolean directly makes the idea concrete.")
Q("operators-compare", "Which block checks if lives have run out?", "(lives) < 1|(lives) > 1|(lives) = 3|(lives) + 1", 0, "Less than 1 catches 0 and any negative value.")
Q("operators-compare", "Your comparison compares text instead of numbers. What should you check?", "That the variable holds a number|The sprite size|The backdrop|The volume", 0, "A variable holding text will not compare numerically as expected.")
Q("operators-compare", "Comparison blocks are used most often inside:", "if blocks and loop conditions|say blocks only|sound blocks|costume blocks", 0, "Their true/false result drives decisions.")
Q("operators-compare", "Which reports true when the first value is smaller?", "() < ()|() > ()|() = ()|() + ()", 0, "The less-than operator.")
Q("operators-compare", "For a grade band 'over 90 is excellent', you would use:", "(score) > 90|(score) < 90|(score) = 90|(score) mod 90", 0, "Greater than 90 defines the top band.")
Q("operators-compare", "A boolean block is shaped:", "Pointy|Round|Rectangular|C-shaped", 0, "Pointy blocks report true or false and fit condition slots.")

# ---- operators-logic ----
Q("operators-logic", "When is 'A and B' true?", "Only when both are true|When either is true|When neither is true|Always", 0, "And requires both conditions.")
Q("operators-logic", "When is 'A or B' true?", "When either one is true|Only when both are true|Never|Always", 0, "Or needs just one condition to hold.")
Q("operators-logic", "What does 'not' do?", "Flips true to false and false to true|Adds numbers|Repeats blocks|Hides sprites", 0, "Not inverts a boolean.")
Q("operators-logic", "'You may have ice cream if you finish dinner AND it is not a school night' uses:", "and, plus not|or only|not only|and only", 0, "It combines two conditions with and, one of them negated.")
Q("operators-logic", "Which condition means 'hit by either hazard'?", "<touching Enemy?> or <touching Spike?>|<touching Enemy?> and <touching Spike?>|not <touching Enemy?>|<touching Enemy?>", 0, "Either hazard should count, so use or.")
Q("operators-logic", "'Keep moving while not touching a wall' uses which structure?", "repeat until, or not with a condition|and only|or only|a plain if", 0, "Not inverts the touching test so movement continues while free.")
Q("operators-logic", "Your combined condition behaves oddly. What is a good first step?", "Test each condition separately|Delete both|Add a third|Use a sound", 0, "Isolating each part shows which one misbehaves.")
Q("operators-logic", "How many rows does a truth table for two conditions have?", "4|2|3|8", 0, "Each condition can be true or false: 2 x 2 = 4 combinations.")
Q("operators-logic", "To win you must reach the goal AND collect all items. Which block?", "and|or|not|mod", 0, "Both requirements must be met.")
Q("operators-logic", "A very complex condition is easier to manage if you:", "Store part of it in a variable such as 'ready'|Add more nesting|Delete it|Use more sprites", 0, "Naming part of the logic makes it readable and testable.")

# ---- variable-timer ----
Q("variable-timer", "How do you count down?", "change the variable by -1 with a wait|change by 1|set it once|hide it", 0, "Negative change plus a wait produces a countdown.")
Q("variable-timer", "Your countdown races to zero instantly. What is missing?", "A 'wait 1 seconds' inside the loop|More variables|A backdrop|A sound", 0, "Without a wait, the loop runs many times per second.")
Q("variable-timer", "What does 'reset timer' do?", "Sets the built-in timer back to zero|Stops the project|Clears variables|Hides the timer", 0, "Reset it at the start so timing is fair.")
Q("variable-timer", "Why do timers make games more exciting?", "They add pressure and urgency|They make it run faster|They use fewer blocks|They add sprites", 0, "Time pressure changes how a game feels to play.")
Q("variable-timer", "Which structure builds a 30-second countdown?", "set time to 30, repeat until time = 0 [wait 1, change time by -1]|forever [change time by 1]|set time to 30 only|wait 30 seconds", 0, "Set, then decrease once per second until zero.")
Q("variable-timer", "Your timer keeps running after the game ends. What fixes it?", "Use 'stop all' or a game-state check|Add another timer|Hide the variable|Change the backdrop", 0, "The timer loop needs stopping when the game ends.")
Q("variable-timer", "The built-in 'timer' block reports:", "Seconds since it was last reset|The score|The number of sprites|The backdrop number", 0, "It counts elapsed time continuously.")
Q("variable-timer", "A timer that counts up instead of down means you used:", "change by 1 instead of -1|set instead of change|the wrong sprite|no loop", 0, "The sign of the change controls direction.")
Q("variable-timer", "How could a bonus give extra time?", "change time by 5 when collected|set time to 5|hide the timer|stop all", 0, "Change adds to the remaining time.")
Q("variable-timer", "Making the timer flash under 5 seconds is an example of:", "Feedback that builds tension|A bug|A variable reset|A broadcast", 0, "Visual urgency communicates the state of play.")

# ---- variable-lives ----
Q("variable-lives", "Why do games give three lives rather than one?", "Instant failure feels unfair and discouraging|It uses fewer blocks|It runs faster|Scratch requires it", 0, "Fairness is a deliberate design decision.")
Q("variable-lives", "One touch drains all three lives instantly. What is the fix?", "Add a brief wait or move the player away after a hit|Add more lives|Delete the enemy|Hide the player", 0, "The collision is firing every frame — pause or separate them.")
Q("variable-lives", "Which block takes a life away?", "change lives by -1|change lives by 1|set lives to 3|show variable lives", 0, "A negative change reduces the value.")
Q("variable-lives", "What should happen when lives reach zero?", "The game ends with a clear message|Nothing|The score resets only|A new sprite appears", 0, "Zero lives is the lose condition and needs feedback.")
Q("variable-lives", "What does 'respawn' mean?", "Returning the player to a safe start position|Deleting the player|Adding a life|Changing costume", 0, "Respawning puts the player back into play after a hit.")
Q("variable-lives", "Lives carry over between games. What is missing?", "'set lives to 3' at the start|A backdrop|A sound|More sprites", 0, "Variables must be reset when the game begins.")
Q("variable-lives", "Which check is safest for game over?", "lives < 1|lives = 0|lives > 0|lives = 3", 0, "Less than 1 also catches negative values if lives overshoot.")
Q("variable-lives", "How could you show health without a number?", "Use costumes or sprite size as a health bar|Hide it entirely|Use sound only|Use the backdrop", 0, "Visual health is easier for young players to read at a glance.")
Q("variable-lives", "A pick-up that restores health would use:", "change health by a positive number|change health by -1|set health to 0|hide", 0, "Adding to health restores it.")
Q("variable-lives", "Brief invincibility after a hit is used because:", "It stops one collision draining every life|It looks nicer|It is required|It saves blocks", 0, "It is the standard fix for repeated-collision damage.")

# ---- broadcast ----
Q("broadcast", "What does a broadcast do?", "Sends a message every sprite can hear|Moves a sprite|Plays a sound|Changes a costume", 0, "It is a one-to-many signal.")
Q("broadcast", "What is the difference from 'broadcast and wait'?", "And-wait pauses until all receivers finish|They are identical|And-wait is faster|And-wait only works on the Stage", 0, "Use and-wait when the next step depends on receivers completing.")
Q("broadcast", "Nothing reacts to your broadcast. What should you check?", "The receiver is listening for the same message name|The sprite size|The backdrop|The volume", 0, "Message names must match exactly.")
Q("broadcast", "Why are broadcasts better than waits for coordinating sprites?", "They stay in sync reliably|They use fewer blocks|They are newer|They are faster to type", 0, "Waits drift; messages are exact.")
Q("broadcast", "What is a good message name?", "game-over|message1|thing|a", 0, "Descriptive names keep bigger projects readable.")
Q("broadcast", "A referee's whistle starting eight runners is like:", "One broadcast, many receivers|Eight separate waits|A loop|A variable", 0, "One signal, everyone reacts — exactly a broadcast.")
Q("broadcast", "Broadcasting inside a forever loop causes:", "Hundreds of messages per second|Nothing|Better sync|Fewer blocks", 0, "Guard it or move it out, or receivers restart constantly.")
Q("broadcast", "Which hat block reacts to a message?", "when I receive ()|when green flag clicked|when this sprite clicked|when key pressed", 0, "It runs when that message is broadcast.")
Q("broadcast", "'Decoupling' with broadcasts means:", "Sprites cooperate without being directly connected|Sprites are deleted|Code runs faster|Fewer sprites are needed", 0, "Each sprite just listens for messages it cares about.")
Q("broadcast", "A broadcast chain is when:", "A receiver broadcasts another message|Two sprites collide|A loop repeats|A variable changes", 0, "Chains let you sequence complex behaviour across sprites.")

# ---- broadcast-scenes ----
Q("broadcast-scenes", "What are the three usual game states?", "Menu, playing, game over|Start, middle, end of a sprite|Small, medium, large|Red, green, blue", 0, "Most games move between these three screens.")
Q("broadcast-scenes", "How do you move between game states?", "Broadcast messages|Wait blocks only|Change costumes|Move sprites", 0, "Messages signal a state change to every sprite.")
Q("broadcast-scenes", "What must happen when a new game starts?", "Reset variables and sprite visibility|Nothing|Only change the backdrop|Add sprites", 0, "Without a reset the new game inherits the old game's state.")
Q("broadcast-scenes", "Menu sprites are still visible during play. What is missing?", "A 'hide' on each when the game starts|A backdrop|A sound|A variable", 0, "Every sprite must decide what to show or hide per state.")
Q("broadcast-scenes", "A start button on a title screen should:", "Broadcast 'start-game' when clicked|Move 10 steps|Hide immediately|Change size", 0, "The click triggers the state change.")
Q("broadcast-scenes", "What is a state machine?", "A design that moves between defined states on events|A kind of sprite|A loop block|A sound effect", 0, "Boxes and arrows: states and the events that move between them.")
Q("broadcast-scenes", "Two states seem to run at once. What is the likely cause?", "The old state's loops were never stopped|Too many sprites|The backdrop is wrong|The score is high", 0, "Stop the previous state's scripts or guard them with a state variable.")
Q("broadcast-scenes", "Why is a title screen worth adding?", "It tells the player what to do before they start|It is required|It saves blocks|It runs faster", 0, "It sets expectations and makes a project feel finished.")
Q("broadcast-scenes", "Restarting your game leaves the old score. What fixes it?", "Reset all variables on 'start-game'|Add another sprite|Change the backdrop|Use a longer wait", 0, "Every restart must clear game state.")
Q("broadcast-scenes", "A pause state would need:", "A way to stop game loops and resume them|Only a backdrop change|A new project|More sprites", 0, "Pausing means suspending the playing state cleanly.")

# ---- clones-basic ----
Q("clones-basic", "What is a clone?", "A copy of a sprite made while the project runs|A second project|A costume|A backdrop", 0, "Clones let one sprite become many at runtime.")
Q("clones-basic", "Which block runs for each new clone?", "when I start as a clone|when green flag clicked|when this sprite clicked|forever", 0, "Each clone runs that script separately.")
Q("clones-basic", "Why must you delete clones?", "They pile up and slow the project down|They look wrong|Scratch requires it|To save blocks", 0, "Undeleted clones accumulate and destroy performance.")
Q("clones-basic", "Your clones never appear. What is a common cause?", "The original is not hidden or the clones never show|Too few sprites|The backdrop|The score", 0, "Usually the original should hide and each clone should show.")
Q("clones-basic", "All your clones move identically and overlap. What helps?", "Give each a random position or wait when it starts|Delete some|Make them bigger|Use one clone", 0, "Randomising per clone makes them behave individually.")
Q("clones-basic", "A game with 50 falling asteroids is best built with:", "One sprite plus clones|50 separate sprites|One sprite moving fast|A backdrop", 0, "Cloning is the efficient approach.")
Q("clones-basic", "Which block makes a copy at runtime?", "create clone of ()|next costume|broadcast|change x by", 0, "It spawns a new clone.")
Q("clones-basic", "A spawner usually looks like:", "forever [create clone of myself, wait 1 seconds]|repeat 1 [hide]|forever [hide]|wait until", 0, "A loop with a wait produces a steady stream of clones.")
Q("clones-basic", "Each clone has its own copy of which variables?", "Ones made 'for this sprite only'|All variables|None|Only the score", 0, "Local variables are per-sprite and per-clone.")
Q("clones-basic", "When should a falling clone be deleted?", "When it goes off-screen or is caught|Never|At the start|Only at game over", 0, "Deleting when finished keeps the clone count under control.")

# ---- clones-advanced ----
Q("clones-advanced", "Why use a 'for this sprite only' variable with clones?", "So each clone has its own value, such as speed|To save memory|It is required|To make it global", 0, "Local variables give each clone individual properties.")
Q("clones-advanced", "How do you build a formation of clones?", "Calculate positions in a loop|Use random only|Use one clone|Use the backdrop", 0, "Calculated positions create deliberate patterns.")
Q("clones-advanced", "What is a wave of enemies?", "A group of clones spawned together|A single sprite|A sound|A backdrop", 0, "Waves are a design tool for pacing difficulty.")
Q("clones-advanced", "Your frame rate collapses. What should you do?", "Cap the clone count and delete off-screen clones|Add more clones|Make them bigger|Add sound", 0, "Performance depends on how many clones exist at once.")
Q("clones-advanced", "How do you make each wave harder?", "Increase speed or clone count each wave|Keep everything the same|Remove clones|Change the backdrop", 0, "Escalating difficulty keeps the player engaged.")
Q("clones-advanced", "All clones unexpectedly share one value. What went wrong?", "The variable was made 'for all sprites'|There are too many clones|The sprite is hidden|The score is high", 0, "Global variables are shared; local ones are per clone.")
Q("clones-advanced", "'repeat 10 [create clone, wait 0.2]' produces:", "A wave of 10 clones spread over time|10 clones at once|One clone|No clones", 0, "The wait staggers their arrival.")
Q("clones-advanced", "How can clones have different types, such as good and bad?", "Use a local variable to store the type|Use two projects|Use the backdrop|You cannot", 0, "A per-clone variable lets one sprite behave in several ways.")
Q("clones-advanced", "Clones spawning on top of each other is fixed by:", "Staggering with a wait or spreading positions|Adding more clones|Hiding them|Making them bigger", 0, "Spacing them out in time or position separates them.")
Q("clones-advanced", "Synchronised patterns work because:", "Each clone follows the same rule from a different start|They share one script instance|They are separate sprites|Of the backdrop", 0, "Identical rules with different starting values create formations.")

# ---- lists ----
Q("lists", "What number is the first item in a Scratch list?", "1|0|-1|It varies", 0, "Scratch lists start counting at 1.")
Q("lists", "What is the difference between a variable and a list?", "A variable holds one value, a list holds many|Lists are faster|Variables hold text only|There is none", 0, "Lists store a numbered collection.")
Q("lists", "How do you pick a random item safely?", "item (pick random 1 to (length of list)) of list|item 0 of list|item (length) of list|item random of list", 0, "The range must be 1 to the list's length.")
Q("lists", "Your list doubles in size every run. What is missing?", "'delete all' before adding items|A longer wait|More sprites|A backdrop", 0, "Without clearing, items are appended again each run.")
Q("lists", "What does 'length of list' report?", "How many items it holds|The longest word|The first item|The list name", 0, "It counts the items.")
Q("lists", "Which block checks whether a list holds a value?", "[] contains ()?|item () of []|add () to []|delete () of []", 0, "Contains reports true or false.")
Q("lists", "Two parallel lists for questions and answers must:", "Stay aligned, so item 3 matches item 3|Be different lengths|Be sorted|Be hidden", 0, "Their positions correspond, so alignment is essential.")
Q("lists", "A high-score table is best stored in:", "A list|A single variable|A costume|A backdrop", 0, "Lists hold multiple scores in order.")
Q("lists", "Which block adds an item to the end of a list?", "add () to []|delete () of []|item () of []|length of []", 0, "Add appends to the end.")
Q("lists", "A shopping list is a good real-world example of:", "A list holding many values|A variable holding one value|A loop|A broadcast", 0, "Many items stored together under one name.")

# ---- myblocks ----
Q("myblocks", "What is a custom block?", "A block you make that runs your own script|A block from the palette|A sprite|A sound", 0, "You define what it does, then use it like any other block.")
Q("myblocks", "Why use custom blocks?", "Less repetition and much clearer code|They run faster|Scratch requires them|They add sprites", 0, "They remove duplication and give code meaningful names.")
Q("myblocks", "What is abstraction?", "Hiding detail behind a simple name|Deleting code|Copying blocks|Adding sprites", 0, "'Make a cup of tea' hides twelve steps behind three words.")
Q("myblocks", "You made a custom block but nothing changed. What is likely?", "You defined it but never used it in a script|It is broken|It needs a sprite|It needs a sound", 0, "The definition must be called from your main script.")
Q("myblocks", "Which is a good custom block name?", "reset player|block1|thing|a", 0, "Names should say what the block does.")
Q("myblocks", "What goes under the 'define' hat?", "The blocks your custom block runs|Nothing|Only comments|Another define", 0, "The define script is the block's body.")
Q("myblocks", "When is a custom block most clearly needed?", "When the same blocks appear in several places|When you have one sprite|When using sound|Never", 0, "Repeated code is the signal to refactor.")
Q("myblocks", "Refactoring means:", "Restructuring code to be clearer without changing what it does|Adding features|Deleting a project|Fixing a bug", 0, "It improves the structure, not the behaviour.")
Q("myblocks", "One custom block should ideally:", "Do one clear job|Do everything|Be empty|Contain every script", 0, "Single-purpose blocks are readable and reusable.")
Q("myblocks", "After refactoring, your main script should:", "Read like a list of clear instructions|Be longer|Be empty|Be harder to read", 0, "That readability is the whole point of abstraction.")

# ---- myblocks-params ----
Q("myblocks-params", "What is a parameter?", "A value you pass into your block|A type of sprite|A sound|A backdrop", 0, "Parameters make one block work for many situations.")
Q("myblocks-params", "Where do you use the parameter?", "Inside the define, dragged from the hat|Outside the define|On the Stage|In the Sounds tab", 0, "Drag the orange oval from the define hat into the blocks inside.")
Q("myblocks-params", "Why is one block with an input better than five similar blocks?", "It works for every value|It is prettier|It runs faster|It uses more memory", 0, "One definition covers all cases.")
Q("myblocks-params", "Your block ignores the number you give it. What went wrong?", "The parameter was not dragged into the blocks inside|The block is broken|The sprite is hidden|The score is 0", 0, "Without dragging it in, a fixed value is used instead.")
Q("myblocks-params", "Which is a good input name?", "size|a|x1|input1", 0, "Descriptive names make the block self-explaining.")
Q("myblocks-params", "'draw square (size)' called with 50 and 100 draws:", "Two squares of different sizes|Two identical squares|Nothing|An error", 0, "The argument changes what the definition draws.")
Q("myblocks-params", "What is an argument?", "The actual value given when the block is used|The block's name|A sprite|A costume", 0, "The parameter is the placeholder; the argument is the real value.")
Q("myblocks-params", "A block with two inputs might be:", "draw shape (size) (colour)|draw shape|hide|move", 0, "Multiple parameters allow richer reuse.")
Q("myblocks-params", "Creating many nearly identical blocks instead of one with an input is:", "A sign you should use a parameter|Good practice|Faster|Required", 0, "Duplication is the signal to parameterise.")
Q("myblocks-params", "Parameters make code more:", "Reusable|Colourful|Random|Hidden", 0, "Reuse is the main benefit.")

# ---- ask-answer ----
Q("ask-answer", "Which block holds what the player typed?", "answer|ask|join|say", 0, "The answer block stores the most recent reply.")
Q("ask-answer", "Why store the answer in a variable straight away?", "The next ask overwrites it|It looks tidier|It runs faster|Scratch requires it", 0, "Only the most recent answer is kept.")
Q("ask-answer", "Which block builds a sentence from words and an answer?", "join () ()|say ()|ask ()|not ()", 0, "Join concatenates text.")
Q("ask-answer", "Your reply reads 'HelloSam'. What is missing?", "A space at the end of 'Hello '|A new sprite|A wait|A backdrop", 0, "Join does not add spaces for you.")
Q("ask-answer", "What makes a chatbot feel alive?", "Using the player's own words back to them|Long speeches|Loud sounds|Many sprites", 0, "Personalised responses create the illusion of understanding.")
Q("ask-answer", "The correct block to ask a question is:", "ask () and wait|say ()|think ()|answer", 0, "It shows an input box and waits for the reply.")
Q("ask-answer", "To remember three facts you need:", "Three variables, one per answer|One variable|No variables|Three sprites", 0, "Each answer must be saved before the next ask.")
Q("ask-answer", "What does 'input' mean?", "Information the user gives the program|Output on screen|A sprite|A sound", 0, "Input comes from the user into the program.")
Q("ask-answer", "After 'ask' runs, the program:", "Waits for the player to type and press enter|Carries straight on|Stops|Restarts", 0, "'Ask and wait' pauses for the reply.")
Q("ask-answer", "Which shows a personalised greeting?", "say (join [Hello ] (name))|say [Hello]|say (name)|ask [Hello]", 0, "Joining fixed text with a stored value personalises it.")

# ---- quiz-logic ----
Q("quiz-logic", "How do you check an answer?", "Compare 'answer' with the correct value|Use a loop|Use a costume|Use a sound", 0, "An equality comparison drives the decision.")
Q("quiz-logic", "Where do you add the point for a correct answer?", "In the 'then' branch of the if|In the else branch|Before the question|At the end only", 0, "Points are awarded on the correct path.")
Q("quiz-logic", "Does Scratch's '=' care about capital letters for words?", "No, 'paris' matches 'Paris'|Yes, always|Only in Level 2|Only for numbers", 0, "Text comparison ignores case, which is helpful for quizzes.")
Q("quiz-logic", "Your answer is always marked wrong. What should you check?", "Extra spaces, or comparing the wrong variable|The backdrop|The volume|The sprite size", 0, "A stray space stops the values matching.")
Q("quiz-logic", "Only the last question scores. What is missing?", "Each question needs its own check|A backdrop|More sprites|A sound", 0, "Every question needs its own comparison and scoring.")
Q("quiz-logic", "How do you grade at the end?", "Compare the score with thresholds|Hide the score|Use a costume|Use a broadcast", 0, "Comparisons turn a score into a grade band.")
Q("quiz-logic", "Using lists for questions lets you:", "Randomise so questions never repeat|Use fewer sprites|Play sounds|Change backdrops", 0, "Lists plus random selection make quizzes replayable.")
Q("quiz-logic", "What is validation?", "Checking whether an answer is correct|Adding a sprite|Saving a project|Playing a sound", 0, "Validation compares input against what is expected.")
Q("quiz-logic", "Good feedback for a wrong answer includes:", "Telling the player the correct answer|Nothing|Just a buzzer|Ending the quiz", 0, "Feedback that teaches is better than feedback that only judges.")
Q("quiz-logic", "Your quiz score is not reset between runs. What is missing?", "'set score to 0' at the start|A backdrop|A wait|More questions", 0, "Score must be reset when the quiz begins.")

# ---- gravity ----
Q("gravity", "What does a velocity variable do?", "Controls how fast and which way the sprite moves vertically|Sets the sprite size|Changes the costume|Plays a sound", 0, "Velocity is added to the position each frame.")
Q("gravity", "What does gravity do to velocity?", "Reduces it a little every frame|Increases it forever|Leaves it unchanged|Resets it", 0, "Constantly reducing velocity creates acceleration downwards.")
Q("gravity", "Which pair models falling?", "change y by (velocity), change velocity by -1|change y by -1 only|glide down|hide", 0, "Position changes by velocity; velocity changes by gravity.")
Q("gravity", "How do you make a sprite jump?", "Set velocity to a positive number on the key press|Change y by 100 instantly|Hide then show|Use a costume", 0, "A single upward velocity gives a natural arc as gravity takes over.")
Q("gravity", "Your sprite falls through the floor. What is missing?", "A ground check that stops it|More gravity|A backdrop|A sound", 0, "Without a boundary test nothing stops the fall.")
Q("gravity", "Your jump has no arc and looks instant. What is wrong?", "Velocity is being set every frame instead of once|Gravity is too weak|The sprite is too big|The backdrop is wrong", 0, "Set velocity once on the press, then let gravity act.")
Q("gravity", "How do you stop endless mid-air jumping?", "Only allow a jump when the sprite is on the ground|Remove the jump|Add more gravity|Hide the sprite", 0, "Checking the ground state gates the jump.")
Q("gravity", "Dropping a pen shows that real gravity:", "Makes things speed up as they fall|Keeps speed constant|Slows things down|Has no effect", 0, "Acceleration is exactly what the velocity model reproduces.")
Q("gravity", "Changing gravity from -1 to -0.5 makes the game feel:", "Floatier, with slower falling|Heavier|Exactly the same|Faster", 0, "Tuning these numbers is game feel design.")
Q("gravity", "A double jump would need:", "A counter tracking how many jumps have been used|More gravity|A bigger sprite|A backdrop", 0, "Counting jumps lets you allow exactly two.")

# ---- platformer ----
Q("platformer", "How does a game know you are standing on something?", "It senses the platform below the player|It checks the score|It uses the backdrop|It uses sound", 0, "Colour or sprite sensing below the player detects ground.")
Q("platformer", "Why use one colour for all platforms?", "So a single check works everywhere|It looks nicer|It saves memory|Scratch requires it", 0, "Consistency makes collision reliable.")
Q("platformer", "Your player sinks into the ground. What is missing?", "A push-out loop that moves them up until free|More gravity|A sound|A backdrop", 0, "Resolve the overlap by stepping out of the platform.")
Q("platformer", "Which pattern climbs a player out of the ground?", "repeat until <not <touching colour?>> [change y by 1]|change y by 100|hide|glide", 0, "Moving out one step at a time avoids teleporting.")
Q("platformer", "Your player sticks to walls. What helps?", "Handle x and y collision separately|Add more gravity|Make the sprite bigger|Use one loop for both", 0, "Separating the axes prevents sticking.")
Q("platformer", "What is a hitbox?", "The area used to detect collisions|The sprite's costume name|The backdrop|A variable", 0, "It is the region the game treats as solid.")
Q("platformer", "Collision is unreliable across your level. Likely cause?", "Platforms are slightly different shades|Too many sprites|The score is high|The sound is off", 0, "Colour sensing needs an exact match.")
Q("platformer", "What is collision resolution?", "Pushing the player out of a solid object|Detecting a collision only|Deleting the sprite|Adding a point", 0, "Detection finds the overlap; resolution fixes it.")
Q("platformer", "A one-way platform lets the player:", "Jump up through it but land on top|Never pass|Always fall through|Move sideways only", 0, "It is a collision rule applied only when falling.")
Q("platformer", "Moving platforms require the player to:", "Move along with the platform while standing on it|Ignore the platform|Jump constantly|Hide", 0, "The player's position must follow the platform.")

# ---- pen ----
Q("pen", "What does 'pen down' do?", "Makes the sprite draw as it moves|Deletes drawings|Changes costume|Plays a sound", 0, "The sprite leaves a trail while the pen is down.")
Q("pen", "What should every pen project start with?", "erase all and pen up|pen down only|A sound|A costume change", 0, "Otherwise old drawings pile up between runs.")
Q("pen", "How do you draw a square with a loop?", "repeat 4 [move 100 steps, turn 90 degrees]|repeat 3 [move, turn 120]|forever [move]|repeat 4 [turn 45]", 0, "Four equal sides with four 90-degree turns.")
Q("pen", "Where do you find the pen blocks?", "Add the Pen extension from the bottom-left button|In the Motion palette|In the Sounds tab|They are always there", 0, "Pen is an extension you must add.")
Q("pen", "Your sprite draws a stray line moving into position. What fixes it?", "Use 'pen up' before moving|Use pen down|Erase at the end|Hide the sprite", 0, "Lift the pen while repositioning.")
Q("pen", "To draw a hexagon, the turn should be:", "60 degrees|90 degrees|120 degrees|45 degrees", 0, "360 divided by 6 sides = 60 degrees.")
Q("pen", "Which block changes line thickness?", "set pen size to ()|set pen color to ()|pen down|erase all", 0, "Pen size controls thickness.")
Q("pen", "For any regular polygon the turn angle is:", "360 divided by the number of sides|90 always|180 divided by sides|The number of sides", 0, "The turns must total one full rotation.")
Q("pen", "'erase all' does what?", "Clears everything drawn on the stage|Deletes sprites|Clears variables|Stops the project", 0, "It clears only pen drawings.")
Q("pen", "A triangle needs a turn of:", "120 degrees|90 degrees|60 degrees|45 degrees", 0, "360 divided by 3 = 120.")

# ---- pen-art ----
Q("pen-art", "In 'repeat 36 [shape, turn 10]', why 36 and 10?", "36 x 10 = 360, a full circle|They are random|36 sides|10 colours", 0, "The repeats times the turn must total 360 to close the pattern.")
Q("pen-art", "What does the inner loop of a spirograph draw?", "One shape|The whole pattern|A single line|Nothing", 0, "The inner loop draws one shape; the outer rotates and repeats it.")
Q("pen-art", "How do you get a rainbow effect?", "change pen color by a small amount in the outer loop|Use one colour|Change the backdrop|Use a sound", 0, "Shifting the colour each repetition creates the gradient.")
Q("pen-art", "Your pattern does not close into a circle. What is wrong?", "Repeats times turn does not equal 360|Too few colours|The sprite is too big|The pen is up", 0, "The maths must total a full rotation.")
Q("pen-art", "What is a nested loop?", "A loop inside another loop|Two loops side by side|A broken loop|A loop with sound", 0, "The inner loop runs fully on each pass of the outer.")
Q("pen-art", "Your drawing runs off the stage. What helps?", "Reduce the move distance|Add more repeats|Change colour|Hide the sprite", 0, "Smaller shapes keep the pattern on screen.")
Q("pen-art", "The colour never changes in your pattern. Likely cause?", "The colour block is in the wrong loop|The pen is up|Too few repeats|The sprite is hidden", 0, "It must be in the loop that repeats for each shape.")
Q("pen-art", "'repeat 18 [square, turn 20]' closes because:", "18 x 20 = 360|18 is even|20 is small|Squares always close", 0, "The rotations complete exactly one full turn.")
Q("pen-art", "Geometric art in Scratch mainly demonstrates:", "Loops and angle maths working together|Sound design|Variables|Broadcasts", 0, "It is maths made visible through code.")
Q("pen-art", "To make a denser pattern you would:", "Increase repeats and decrease the turn angle|Decrease both|Increase both|Change the backdrop", 0, "More shapes at smaller angles fill the circle more densely.")

# ---- music-blocks ----
Q("music-blocks", "What is a beat?", "The basic unit of musical time|A type of sprite|A drum sound only|A backdrop", 0, "Beats measure musical time, like steps measure distance.")
Q("music-blocks", "What does tempo change?", "How fast the music plays|How loud it is|The instrument|The pitch", 0, "Higher tempo means faster playback.")
Q("music-blocks", "Which note number is middle C?", "60|1|100|40", 0, "In Scratch, 60 is middle C; higher numbers are higher notes.")
Q("music-blocks", "How do you make two musical parts start together?", "Trigger both with one broadcast|Use two green flags|Use separate waits|Play them one after another", 0, "A single message keeps parts in sync.")
Q("music-blocks", "Your two parts drift out of time. What is the cause?", "They were started separately with waits|The tempo is too slow|Too few notes|The sprite is hidden", 0, "Independent waits drift; broadcasts do not.")
Q("music-blocks", "Where do the music blocks come from?", "The Music extension|The Sound palette|The Motion palette|They are built in", 0, "Music is an extension you add.")
Q("music-blocks", "What does 'rest for 0.25 beats' do?", "Creates a short silence|Plays a quiet note|Stops the project|Repeats a note", 0, "Silence is part of rhythm.")
Q("music-blocks", "A repeating drum pattern is best built with:", "A loop|A single block|A broadcast only|A variable", 0, "Rhythms are repetition, which is exactly what loops do.")
Q("music-blocks", "Playing a drum 'for 0.25 beats' compared with 1 beat is:", "Four times shorter|Longer|The same|Louder", 0, "The beat value sets the duration.")
Q("music-blocks", "A three-layer piece usually means:", "Three parts playing together, such as drums, bass and melody|Three projects|Three sprites moving|Three backdrops", 0, "Layering parts creates fuller music.")

# ---- game-polish ----
Q("game-polish", "What is 'game feel'?", "How satisfying a game is to play|How it looks in screenshots|The file size|The number of sprites", 0, "Feel is the moment-to-moment satisfaction of playing.")
Q("game-polish", "Why should every player action have feedback?", "It tells the player what happened|It uses more blocks|It is required|It runs faster", 0, "Feedback is communication, not decoration.")
Q("game-polish", "During a playtest, what should you do?", "Watch silently and note every confusion|Explain how to play|Play it yourself|Fix bugs while they play", 0, "A real player will have nobody to explain it to them.")
Q("game-polish", "Your game has effects on everything and feels chaotic. What is the fix?", "One clear effect per action|More effects|No effects|Louder sounds", 0, "Restraint keeps feedback readable.")
Q("game-polish", "What is 'juice' in game design?", "Small effects that make actions feel good|A bug|A variable|A backdrop", 0, "Juice is the layer of feedback that makes actions satisfying.")
Q("game-polish", "After a playtest you should:", "Fix the most common confusion first|Ignore the feedback|Change everything|Start again", 0, "Prioritising by impact is how real teams iterate.")
Q("game-polish", "A satisfying collect effect might combine:", "A sound, a quick grow and a fade|Only a score change|Nothing|A backdrop change", 0, "Layered feedback across senses feels best.")
Q("game-polish", "If a playtester is confused, it usually means:", "The game needs clearer feedback or instructions|The tester is wrong|Nothing needs changing|The game is too easy", 0, "Confusion is information about your design.")
Q("game-polish", "Why not explain your game while someone tests it?", "Because the game must speak for itself|To be unfriendly|To save time|It is a rule of Scratch", 0, "Explaining hides exactly the problems you are looking for.")
Q("game-polish", "Polish is best described as:", "Communication with the player|Decoration only|Extra sprites|More levels", 0, "Good polish tells the player what is happening.")

# ---- publish-share ----
Q("publish-share", "What three things do good instructions include?", "The goal, the controls and how to win|Your name and age|The block count|The file size", 0, "Players need to know what to do, how to do it and what success is.")
Q("publish-share", "Why credit others' work?", "It is honest and respectful|It is optional decoration|It adds points|It makes it faster", 0, "Attribution is basic ethics in creative and technical work.")
Q("publish-share", "What should never go in a public project?", "Personal details like your full name or school|A title|Instructions|Credits", 0, "Online safety comes first.")
Q("publish-share", "How do you know if your instructions are clear?", "Test them on someone who has never played|Read them yourself|Make them longer|Add pictures only", 0, "Fresh eyes reveal assumptions you did not notice.")
Q("publish-share", "What is a remix?", "Building on someone else's shared project|Copying with no changes|Deleting a project|A type of sprite", 0, "Remixing is encouraged in Scratch — with credit.")
Q("publish-share", "Instructions that assume the player already knows the game are:", "Not good enough|Ideal|Shorter|Required", 0, "They must work for a complete newcomer.")
Q("publish-share", "Why does sharing your project matter?", "Others can play it and give you feedback|It saves space|It runs faster|It is required", 0, "Feedback from real players is how projects improve.")
Q("publish-share", "Where do you write how to play in Scratch?", "The Instructions field on the project page|In the code only|In a sprite name|Nowhere", 0, "The project page has fields for instructions and credits.")
Q("publish-share", "If you used someone's sprite or sound you should:", "Credit them in the notes|Say nothing|Rename it|Delete it", 0, "Credit whatever you did not make yourself.")
Q("publish-share", "A finished project usually includes:", "Clear instructions, credits and no personal details|Only code|Only a title|Only sprites", 0, "Presentation is part of finishing the work.")

# ---- l2-capstone ----
Q("l2-capstone", "What is a specification?", "A written description of what you will build|A type of sprite|A bug|A backdrop", 0, "Agreeing the spec before coding prevents drifting scope.")
Q("l2-capstone", "What is a milestone?", "A checkpoint in a bigger build|A type of block|A sprite|A sound", 0, "Milestones break a big project into testable stages.")
Q("l2-capstone", "Which should you build first?", "The core mechanic|The title screen|The credits|The music", 0, "If the core is not fun, nothing else will save it.")
Q("l2-capstone", "Your code has become an unreadable tangle. What should you do?", "Refactor it into well-named custom blocks|Delete it|Add more sprites|Ignore it", 0, "Refactoring restores readability without changing behaviour.")
Q("l2-capstone", "Your project is far too ambitious. Best response?", "Cut to three features and finish them well|Build everything|Give up|Copy another project", 0, "A finished focused project beats an unfinished sprawling one.")
Q("l2-capstone", "When should you test during a long build?", "After every milestone|Only at the end|Never|Only at the start", 0, "Testing per milestone isolates problems to recent work.")
Q("l2-capstone", "Which counts as a Level 2 technique?", "Clones, broadcasts, custom blocks, lists or physics|Move and turn|Say blocks|Costumes", 0, "These are the advanced techniques Level 2 teaches.")
Q("l2-capstone", "A portfolio is:", "A collection of work that shows your skill|A single sprite|A backdrop|A bug list", 0, "It is what you show people to demonstrate what you can do.")
Q("l2-capstone", "When presenting, you should be able to explain:", "One clever piece of code and what was hardest|Only the title|Nothing|The file size", 0, "Explaining your engineering decisions demonstrates real understanding.")
Q("l2-capstone", "Writing a spec before coding helps because:", "You know what 'finished' means|It is required|It runs faster|It uses fewer blocks", 0, "A defined target is what makes finishing possible.")
