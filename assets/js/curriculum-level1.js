/* =====================================================================
   GRADE NEXT — SCRATCH CODING ACADEMY
   Curriculum data — LEVEL 1 "Coder Cadet" (50 sessions, ages 7–12)
   ---------------------------------------------------------------------
   Each session teaches Scratch topic-wise through exercises + a game
   project. Games are themed on what kids already love (Minecraft,
   Roblox, Flappy Bird, Mario, Pong) so motivation stays high.

   Data shape (see README for the full contract):
     module     grouping this session belongs to
     title      session title
     emoji      quick visual tag
     theme      the game/interest this session leans on
     minutes    suggested class length
     concept    the one big idea
     blocks     Scratch blocks introduced/used (with palette category)
     objective  what the student can DO after the session
     warmup     unplugged / quick starter (screens optional)
     exercises  ordered, do-able steps
     project    the build for the session (usually a game)
     challenge  extension for fast finishers
     vocab      key words to say and reuse
     checklist  "I can…" self-check the student ticks off
   ===================================================================== */
(function () {
  window.GN_LEVELS = window.GN_LEVELS || [];

  window.GN_LEVELS.push({
    level: 1,
    codename: "Coder Cadet",
    tagline: "From your first block to your first real games.",
    emoji: "🚀",
    ageNote: "Best for ages 7–12 who are new to coding.",
    color: "#4C97FF",
    modules: [
      "Welcome to Scratch",
      "Move & Look",
      "Loops & Repetition",
      "Events & Control",
      "Decisions & Sensing",
      "Variables & Scoring",
      "Level 1 Game Builds"
    ],
    sessions: [
      /* ---------- MODULE A: Welcome to Scratch (1–5) ---------- */
      {
        module: "Welcome to Scratch",
        title: "Meet Scratch",
        emoji: "👋",
        theme: "Getting started",
        minutes: 60,
        concept: "Scratch is a place where you give a character (a 'sprite') instructions by snapping coloured blocks together.",
        blocks: [
          "Stage & Sprite (the parts of Scratch)",
          "Blocks palette (the coloured categories)",
          "when green flag clicked — Events (yellow)"
        ],
        objective: "Find your way around Scratch: the Stage, the sprite list, the blocks palette, and the code area.",
        warmup: "Robot Teacher: give the teacher three commands only (forward, turn, stop) to reach a chair. The teacher obeys EXACTLY — walking into the chair if told to. Big laughs, and the lesson lands: the computer does what you SAY, not what you MEAN.",
        exercises: [
          { t: "Tour the screen", d: "Point to and name out loud: the Stage (top-right, where the show happens), the Sprite (the cat), the Blocks palette (left), and the Code area (middle)." },
          { t: "Find the colours", d: "Click each palette category. Say the colour and the name: Motion=blue, Looks=purple, Sound=pink, Events=yellow, Control=orange. You'll use these colours forever." },
          { t: "First block", d: "Drag a 'when green flag clicked' hat block into the code area. Nothing happens yet — that's normal. It's a 'hat' that waits for the flag." }
        ],
        project: {
          title: "Name Tag",
          brief: "Make the cat say YOUR name when the green flag is clicked.",
          must: ["when green flag clicked", "say [your name] block"],
          stretch: "Change the cat to a different sprite you like from the sprite library."
        },
        challenge: "Give the cat a two-part greeting: say your name, then say your favourite game.",
        vocab: ["sprite", "stage", "block", "palette", "green flag"],
        checklist: ["I can name the Stage, Sprite, and palette", "I can drag a block into the code area", "I can press the green flag to run my code"]
      },
      {
        module: "Welcome to Scratch",
        title: "Sprites, Stage & the Green Flag",
        emoji: "🐱",
        theme: "Getting started",
        minutes: 60,
        concept: "A project can have many sprites. Each sprite has its own code. The green flag starts everything at once.",
        blocks: [
          "when green flag clicked — Events",
          "when this sprite clicked — Events",
          "choose a sprite / choose a backdrop"
        ],
        objective: "Add and delete sprites, add a backdrop, and start code with the green flag or a click.",
        warmup: "Everyone is a 'sprite'. Teacher calls 'green flag!' and everyone does their one chosen action (wave, spin). This is what 'when green flag clicked' means — all sprites hear it at once.",
        exercises: [
          { t: "Add a sprite", d: "Use the 'Choose a Sprite' button (bottom-right cat icon) to add a second character. Delete a sprite by clicking the trash on its thumbnail." },
          { t: "Add a backdrop", d: "Use 'Choose a Backdrop' (bottom-right, far side) to set a scene behind your sprites." },
          { t: "Click to react", d: "On one sprite add 'when this sprite clicked → say Hi!'. Now clicking it (not the flag) runs the code." }
        ],
        project: {
          title: "Meet the Crew",
          brief: "Two sprites on a backdrop. Click each one and it introduces itself.",
          must: ["2 sprites", "a backdrop", "when this sprite clicked", "say"],
          stretch: "When the green flag is clicked, both sprites say hello at the same time."
        },
        challenge: "Make one sprite reply to the other so it looks like a tiny conversation.",
        vocab: ["backdrop", "sprite list", "event"],
        checklist: ["I can add and delete a sprite", "I can add a backdrop", "I can start code by clicking a sprite"]
      },
      {
        module: "Welcome to Scratch",
        title: "Motion Basics",
        emoji: "🏃",
        theme: "Character control",
        minutes: 60,
        concept: "Motion blocks (blue) move and turn your sprite around the Stage.",
        blocks: [
          "move (10) steps — Motion",
          "turn ↻ (15) degrees / turn ↺ (15) degrees — Motion",
          "point in direction (90) — Motion"
        ],
        objective: "Move and turn a sprite, and understand that a 'step' is one pixel.",
        warmup: "Face the Door: 'point to forward'. Turn left. 'Point to forward' again — half the room is now wrong. Forward changes when YOU change direction. This is why sprites need turn blocks.",
        exercises: [
          { t: "Take some steps", d: "Add 'when green flag clicked → move 10 steps'. Click flag. Change 10 to 100. See the difference. A step = 1 pixel, so numbers are bigger than in real life." },
          { t: "Turn and move", d: "Build: move 50 → turn ↻ 90 → move 50. Your sprite walks an L-shape." },
          { t: "Point first", d: "Use 'point in direction 90' (right) then 'point in direction -90' (left). Direction sets which way 'move' goes." }
        ],
        project: {
          title: "Square Walk",
          brief: "Make your sprite walk a full square and end facing where it started.",
          must: ["move", "turn 90 degrees (four times)"],
          stretch: "Add 'go to x:0 y:0' at the very start so it always begins in the middle."
        },
        challenge: "Walk a rectangle (two long sides, two short sides) instead of a square.",
        vocab: ["step (pixel)", "degrees", "direction"],
        checklist: ["I can move a sprite a set number of steps", "I can turn a sprite by degrees", "I can point a sprite in a direction"]
      },
      {
        module: "Welcome to Scratch",
        title: "The Stage Grid (x and y)",
        emoji: "📐",
        theme: "Character control",
        minutes: 60,
        concept: "The Stage is a grid. x = left/right (−240 to 240), y = up/down (−180 to 180). The middle is x:0 y:0.",
        blocks: [
          "go to x: () y: () — Motion",
          "glide (1) secs to x: () y: () — Motion",
          "change x by / change y by — Motion",
          "set x to / set y to — Motion"
        ],
        objective: "Place a sprite anywhere using coordinates and glide it smoothly between points.",
        warmup: "Battleship on the floor: tape an x/y cross on the ground. Call out 'x:2, y:-1' and a student stands there. Coordinates = an exact address for every spot.",
        exercises: [
          { t: "Read the address", d: "Drag your sprite around the Stage with the mouse and watch the x and y numbers change (bottom of the code area / sprite info)." },
          { t: "Teleport", d: "Use 'go to x:0 y:0' to snap to the middle. Try the four corners: (240,180), (−240,180), (−240,−180), (240,−180)." },
          { t: "Glide", d: "Use 'glide 1 secs to x:100 y:100' for smooth movement. Compare it to 'go to' (instant)." }
        ],
        project: {
          title: "Treasure Hop",
          brief: "Place a gem sprite somewhere, then make the cat glide to it and say 'Found it!'.",
          must: ["go to x y", "glide to x y", "say"],
          stretch: "Make the cat visit three gems in order, one glide each."
        },
        challenge: "Make your sprite bounce corner-to-corner forever using four glide blocks (we'll add 'forever' properly next module).",
        vocab: ["coordinate", "x-axis", "y-axis", "glide"],
        checklist: ["I know where x:0 y:0 is", "I can send a sprite to exact coordinates", "I can glide a sprite smoothly"]
      },
      {
        module: "Welcome to Scratch",
        title: "Looks Basics",
        emoji: "💬",
        theme: "Character control",
        minutes: 60,
        concept: "Looks blocks (purple) change how a sprite appears: speech, size, show/hide, and effects.",
        blocks: [
          "say () for (2) seconds / think () — Looks",
          "show / hide — Looks",
          "change size by / set size to (%) — Looks",
          "switch costume to / next costume — Looks"
        ],
        objective: "Make a sprite talk, resize, appear and disappear, and change costume.",
        warmup: "Silent charades: act 'I'm happy' with no words. Hard! Programs need Looks blocks to TELL us things, not just do things.",
        exercises: [
          { t: "Speak", d: "Try 'say Hello for 2 seconds' vs plain 'say Hello' (stays up). Try 'think ...' for a thought bubble." },
          { t: "Resize", d: "Use 'set size to 50%' (small) and 'set size to 150%' (big). Then 'change size by 10' a few times." },
          { t: "Now you see me", d: "Use hide then show with a wait between. Great for popping things in and out." }
        ],
        project: {
          title: "Magic Trick",
          brief: "A sprite grows, shrinks, disappears, then reappears and says 'Ta-da!'.",
          must: ["set size to", "hide", "show", "say"],
          stretch: "Add 'next costume' so it changes look during the trick."
        },
        challenge: "Make the sprite whisper (small + think) then shout (big + say in CAPITALS).",
        vocab: ["costume", "size (%)", "show/hide"],
        checklist: ["I can make a sprite say and think", "I can change a sprite's size", "I can show and hide a sprite"]
      },

      /* ---------- MODULE B: Move & Look (6–12) ---------- */
      {
        module: "Move & Look",
        title: "Costumes",
        emoji: "🎭",
        theme: "Animation",
        minutes: 60,
        concept: "A sprite can have several costumes (pictures). Switching costumes is how we draw animation.",
        blocks: [
          "switch costume to () — Looks",
          "next costume — Looks",
          "costume number/name — Looks (reporter)"
        ],
        objective: "Add costumes to a sprite and switch between them.",
        warmup: "Flipbook: flick a stack of sticky notes with a slightly-different doodle on each. That's animation — many still pictures shown fast.",
        exercises: [
          { t: "Meet the costumes", d: "Click a sprite → Costumes tab. The cat has 'costume1' and 'costume2' (walking legs). Click each to see the difference." },
          { t: "Switch by name", d: "Use 'switch costume to costume2'. The cat's legs move once." },
          { t: "Next costume", d: "Press 'next costume' repeatedly — it cycles through all costumes and wraps back to the first." }
        ],
        project: {
          title: "Two-Face",
          brief: "Add a second sprite with two costumes (e.g. happy/sad face). Click it to toggle its mood.",
          must: ["a sprite with 2+ costumes", "when this sprite clicked", "next costume"],
          stretch: "Add a third costume and cycle through all three."
        },
        challenge: "Duplicate a costume in the paint editor and change one small thing to make a smooth cycle.",
        vocab: ["costume", "cycle", "animation frame"],
        checklist: ["I can see a sprite's costumes", "I can switch to a named costume", "I can use next costume"]
      },
      {
        module: "Move & Look",
        title: "Animation = Costumes + Wait",
        emoji: "🚶",
        theme: "Animation",
        minutes: 60,
        concept: "Animation is 'next costume' inside a loop with a small wait. No wait = too fast to see.",
        blocks: [
          "next costume — Looks",
          "wait (0.2) seconds — Control",
          "repeat () / forever — Control (preview of loops)"
        ],
        objective: "Create a smooth walking animation by combining costumes, movement, and waits.",
        warmup: "Human flipbook: two students pose 'mid-step', switch on a clap. Speed up the claps — it looks like walking.",
        exercises: [
          { t: "Too fast", d: "Build 'forever → next costume'. Run it. The cat blurs — too fast! This is a great bug to see." },
          { t: "Add a wait", d: "Put 'wait 0.2 seconds' after 'next costume'. Now the legs move at a nice pace." },
          { t: "Walk", d: "Add 'move 10 steps' inside the loop too. The cat now walks across the Stage while its legs move." }
        ],
        project: {
          title: "Walk Cycle",
          brief: "A character walks across the screen with moving legs at a believable speed.",
          must: ["forever (or repeat)", "next costume", "wait", "move"],
          stretch: "Add 'if on edge, bounce' so it turns around at the wall."
        },
        challenge: "Make a bird flap: two wing costumes + a wait, and glide it upward as it flaps.",
        vocab: ["frame rate", "loop", "wait"],
        checklist: ["I know why animation needs a wait", "I can loop next costume", "I can walk a sprite with animated legs"]
      },
      {
        module: "Move & Look",
        title: "Backdrops & Scenes",
        emoji: "🏞️",
        theme: "World building",
        minutes: 60,
        concept: "The Stage can have many backdrops. Switching backdrops changes the scene — like changing rooms or levels.",
        blocks: [
          "switch backdrop to () — Looks",
          "next backdrop — Looks",
          "when backdrop switches to () — Events"
        ],
        objective: "Add multiple backdrops and switch scenes.",
        warmup: "Stage crew: describe three 'scenes' of a story (home → forest → castle). Each scene = one backdrop.",
        exercises: [
          { t: "Collect backdrops", d: "Add three backdrops from the library (e.g. a room, a forest, a castle)." },
          { t: "Switch scenes", d: "On the Stage's code, use 'switch backdrop to forest'. Try 'next backdrop' too." },
          { t: "React to a scene", d: "On a sprite, use 'when backdrop switches to castle → say We made it!'." }
        ],
        project: {
          title: "Mini Adventure",
          brief: "Click the sprite to travel: each click switches to the next backdrop and the sprite reacts to where it is.",
          must: ["3 backdrops", "next backdrop", "when backdrop switches to"],
          stretch: "Give each scene its own sound (add in the Sound module later, or hum it now)."
        },
        challenge: "Loop the scenes so after the last backdrop it returns to the first.",
        vocab: ["backdrop", "scene", "level"],
        checklist: ["I can add several backdrops", "I can switch backdrops", "I can make a sprite react to a backdrop change"]
      },
      {
        module: "Move & Look",
        title: "Looks Effects",
        emoji: "🌈",
        theme: "Game feel",
        minutes: 60,
        concept: "Graphic effects (colour, ghost, brightness) change how a sprite looks without changing its costume.",
        blocks: [
          "change [color] effect by () — Looks",
          "set [ghost] effect to () — Looks",
          "clear graphic effects — Looks"
        ],
        objective: "Apply and clear graphic effects like colour cycling and fading.",
        warmup: "Coloured cellophane over the eyes (or imagine it): the world changes colour but the objects are the same. That's an 'effect' — a filter, not a new costume.",
        exercises: [
          { t: "Colour cycle", d: "Loop 'change color effect by 25 → wait 0.1'. The sprite rainbows through colours." },
          { t: "Fade out", d: "Loop 'change ghost effect by 5' ten times. The sprite fades to invisible. 'set ghost to 0' brings it back." },
          { t: "Reset", d: "Always finish with 'clear graphic effects' so effects don't stick between runs." }
        ],
        project: {
          title: "Power-Up Glow",
          brief: "Click a sprite and it flashes rainbow for a second (a power-up effect), then returns to normal.",
          must: ["change color effect", "wait", "clear graphic effects"],
          stretch: "Make it fade in from invisible when the green flag is clicked."
        },
        challenge: "Combine a size pulse with a colour cycle for a 'charging up' effect.",
        vocab: ["effect", "ghost (transparency)", "reset"],
        checklist: ["I can cycle a sprite's colour", "I can fade a sprite with the ghost effect", "I remember to clear effects"]
      },
      {
        module: "Move & Look",
        title: "Design Your Own Sprite",
        emoji: "🎨",
        theme: "World building",
        minutes: 60,
        concept: "The Paint Editor lets you draw your own sprites and costumes — your game can look however you want.",
        blocks: [
          "Paint editor: brush, fill, shapes, eraser",
          "vector vs bitmap (just the idea)",
          "duplicate costume (for animation frames)"
        ],
        objective: "Draw a simple original sprite with at least two costumes.",
        warmup: "On paper, sketch a game character in two poses (still, and one leg forward). You're about to draw it in Scratch.",
        exercises: [
          { t: "Paint a sprite", d: "Click 'Paint' (brush icon) in the sprite menu. Draw a simple blob character. Name it." },
          { t: "Centre it", d: "Use the crosshair to set the costume centre — this is the point the sprite rotates and positions around. Important for games!" },
          { t: "Second costume", d: "Duplicate the costume, then nudge an arm/leg so you have a 2-frame animation." }
        ],
        project: {
          title: "My Character",
          brief: "Draw an original character with a walk cycle (2 costumes) and walk it across a backdrop you like.",
          must: ["a hand-drawn sprite", "2 costumes", "walk animation from earlier"],
          stretch: "Draw a matching collectible (coin/gem) as a second sprite."
        },
        challenge: "Draw a 3-frame animation (e.g. a jumping pose in the middle).",
        vocab: ["paint editor", "costume centre", "duplicate"],
        checklist: ["I can draw a sprite in the paint editor", "I can set the costume centre", "I can make a 2-frame animation"]
      },
      {
        module: "Move & Look",
        title: "Talking Sprites (Dialogue)",
        emoji: "🗨️",
        theme: "Storytelling",
        minutes: 60,
        concept: "Timed 'say' blocks plus waits let two sprites take turns talking — the start of cutscenes.",
        blocks: [
          "say () for () seconds — Looks",
          "wait () seconds — Control",
          "broadcast () / when I receive () — Events (preview)"
        ],
        objective: "Coordinate two sprites so they hold a short conversation without talking over each other.",
        warmup: "Puppet show with two hands: they must NOT talk at the same time. How do they know whose turn it is? (Timing — and soon, messages.)",
        exercises: [
          { t: "One speaks", d: "Sprite A: 'say Hi! for 2 seconds'." },
          { t: "Take turns with waits", d: "Sprite B: 'wait 2 seconds → say Hello! for 2 seconds'. Now they alternate." },
          { t: "Peek at messages", d: "Try A: 'say Hi → broadcast go'. B: 'when I receive go → say Hello'. Cleaner than counting waits (full lesson soon)." }
        ],
        project: {
          title: "Two-Character Scene",
          brief: "Two characters meet on a backdrop and have a 4-line conversation that reads smoothly.",
          must: ["2 sprites", "say for seconds", "waits (or broadcasts)"],
          stretch: "Switch the backdrop mid-scene for a scene change."
        },
        challenge: "Add a joke: one sprite sets up, the other delivers the punchline with good timing.",
        vocab: ["dialogue", "cutscene", "timing"],
        checklist: ["I can time two sprites talking in turns", "I can use say-for-seconds", "I've seen how broadcast helps timing"]
      },
      {
        module: "Move & Look",
        title: "Mini Project — Animated Postcard",
        emoji: "💌",
        theme: "Storytelling",
        minutes: 60,
        concept: "Combine everything so far into one polished little scene. This is your first 'ship it' moment.",
        blocks: ["Everything from sessions 1–11 (motion, costumes, backdrops, effects, dialogue)"],
        objective: "Plan and build a short animated scene that runs start-to-finish on the green flag.",
        warmup: "Storyboard: fold paper into 4 boxes and sketch the 4 beats of your scene before touching a screen.",
        exercises: [
          { t: "Plan on paper", d: "Answer: Where is it? Who's in it? What happens in 4 steps? What does it say?" },
          { t: "Build the beats", d: "Turn each storyboard box into blocks: set positions/backdrop, then animate the action, then the dialogue." },
          { t: "Green-flag reset", d: "Add a 'when green flag clicked' that resets all positions/sizes/backdrop so it plays the same every time." }
        ],
        project: {
          title: "Animated Postcard",
          brief: "A 15–20 second scene: a character does something on a backdrop, with movement, a costume change, and a line of dialogue. Plays cleanly from the green flag.",
          must: ["reset on green flag", "movement", "costume/animation", "at least one say"],
          stretch: "Add a title card backdrop at the start and an end card that says 'The End'."
        },
        challenge: "Make the postcard 'about' a game you love — a Minecraft sunrise, a Roblox obby start line, etc.",
        vocab: ["storyboard", "reset", "polish"],
        checklist: ["I planned before building", "I reset state on the green flag", "I combined motion, looks, and dialogue"]
      },

      /* ---------- MODULE C: Loops & Repetition (13–18) ---------- */
      {
        module: "Loops & Repetition",
        title: "Repeat — The Big Idea",
        emoji: "🔁",
        theme: "Core concept",
        minutes: 60,
        concept: "A loop tells the computer to do something several times without you writing it out over and over.",
        blocks: [
          "repeat () — Control (orange, C-shaped)",
          "how to drop blocks INSIDE the C-shape"
        ],
        objective: "Replace repeated blocks with a single repeat loop and see the code get shorter.",
        warmup: "The Boring List: write 'clap, stamp, clap, stamp…' until the class complains. Ask for a shorter way. Someone says 'do it 4 times'. They just invented the loop.",
        exercises: [
          { t: "The long way", d: "Make a square with 8 blocks: move, turn, move, turn, move, turn, move, turn. Count them." },
          { t: "The loop way", d: "Wrap 'move 50 → turn 90' in 'repeat 4'. Same square, 3 blocks. Watch the block count drop." },
          { t: "Change the number", d: "Change 'repeat 4' to 'repeat 3' and the turn to 120. What shape do you get? (A triangle.)" }
        ],
        project: {
          title: "Shape Stamper",
          brief: "Use a repeat loop to draw a square, then a triangle, then a hexagon (change repeat count and turn angle).",
          must: ["repeat", "move", "turn"],
          stretch: "Use the Pen extension 'pen down' so the sprite leaves a trail as it draws."
        },
        challenge: "Find the rule: for any regular shape, turn = 360 ÷ number of sides. Test it with a pentagon.",
        vocab: ["loop", "repeat", "iteration"],
        checklist: ["I can wrap blocks in a repeat loop", "I can put blocks inside the C-shape", "I know a loop makes code shorter"]
      },
      {
        module: "Loops & Repetition",
        title: "Forever Loops",
        emoji: "♾️",
        theme: "Core concept",
        minutes: 60,
        concept: "A 'forever' loop runs until you stop the project. It's how games keep checking and moving all the time.",
        blocks: [
          "forever — Control",
          "if on edge, bounce — Motion",
          "stop [all] — Control"
        ],
        objective: "Use forever for continuous behaviour and know how to stop it.",
        warmup: "Keep clapping until I say stop. That's 'forever' — no fixed number, it just keeps going until something ends it.",
        exercises: [
          { t: "Bounce forever", d: "Build 'forever → move 10 → if on edge, bounce'. The sprite ping-pongs across the Stage." },
          { t: "Fix upside-down", d: "Set the sprite's rotation style to 'left-right' so it doesn't flip upside down when bouncing." },
          { t: "Stop it", d: "Add 'when this sprite clicked → stop all' so you can end the madness on command." }
        ],
        project: {
          title: "Screensaver",
          brief: "One or more sprites bounce around forever with colour effects — a hypnotic screensaver.",
          must: ["forever", "move", "if on edge bounce"],
          stretch: "Add a colour effect inside the loop, and a second bouncing sprite at a different speed."
        },
        challenge: "Make the sprite speed up over time (increase the move number gradually — hint: you'll want a variable soon).",
        vocab: ["forever", "continuous", "stop all"],
        checklist: ["I can use a forever loop", "I can bounce a sprite off edges", "I can stop a running project"]
      },
      {
        module: "Loops & Repetition",
        title: "Loops for Animation",
        emoji: "🎞️",
        theme: "Animation",
        minutes: 60,
        concept: "Loops make animation effortless: one small loop can animate forever or for a set number of frames.",
        blocks: [
          "forever / repeat — Control",
          "next costume + wait — Looks/Control",
          "repeat until () — Control (preview)"
        ],
        objective: "Build reusable animation loops for idle, walk, and a one-time action.",
        warmup: "Idle vs action: stand still and 'breathe' (tiny idle animation) vs a big wave (one-time action). Games need both.",
        exercises: [
          { t: "Idle loop", d: "'forever → next costume → wait 0.3' for a gentle idle bob." },
          { t: "Timed action", d: "'repeat 6 → next costume → wait 0.05' for a quick one-time animation (like a spin) that then stops." },
          { t: "Walk on key", d: "Peek ahead: 'forever → if key right arrow pressed → next costume + move'. Legs only move when walking (full events lesson next)." }
        ],
        project: {
          title: "Living Character",
          brief: "A character that gently idles forever, and plays a special animation when you click it.",
          must: ["forever idle loop", "repeat action loop", "when this sprite clicked"],
          stretch: "Add a second special animation on a different trigger."
        },
        challenge: "Make a torch/flame flicker convincingly using two costumes and a random-ish wait.",
        vocab: ["idle animation", "action animation", "trigger"],
        checklist: ["I can build an idle animation loop", "I can build a one-time animation with repeat", "I can trigger an animation on click"]
      },
      {
        module: "Loops & Repetition",
        title: "Loops + Pen = Art",
        emoji: "🖊️",
        theme: "Creative coding",
        minutes: 60,
        concept: "The Pen extension makes the sprite draw. Loops + pen create patterns you could never draw by hand.",
        blocks: [
          "pen down / pen up — Pen (extension)",
          "erase all / set pen color / change pen color — Pen",
          "set pen size — Pen"
        ],
        objective: "Add the Pen extension and draw looped patterns like stars and spirals.",
        warmup: "Spirograph or a hand-drawn spiral: talk about how a small repeated move + a small turn makes a big pattern.",
        exercises: [
          { t: "Add Pen", d: "Click 'Add Extension' (bottom-left) → Pen. Start every drawing with 'erase all' and 'pen down'." },
          { t: "Draw a star", d: "'repeat 5 → move 100 → turn 144'. A perfect star." },
          { t: "Spiral", d: "Peek ahead with variables: 'repeat 50 → move (a number that grows) → turn 20'. For now, hardcode a few growing moves." }
        ],
        project: {
          title: "Pattern Machine",
          brief: "Use loops + pen to draw at least two different patterns (e.g. a star burst and a nested squares pattern).",
          must: ["pen down", "repeat", "move", "turn", "change pen color"],
          stretch: "Change pen colour inside the loop for a rainbow pattern."
        },
        challenge: "Draw a 'flower' by repeating a shape while turning a little each time (nested loops — next lesson!).",
        vocab: ["pen", "pattern", "extension"],
        checklist: ["I can add and use the Pen extension", "I can draw a shape with a loop", "I can make a repeating pattern"]
      },
      {
        module: "Loops & Repetition",
        title: "Nested Loops",
        emoji: "🪆",
        theme: "Core concept",
        minutes: 60,
        concept: "A loop inside a loop. The inner loop finishes fully for each single run of the outer loop.",
        blocks: [
          "repeat inside repeat — Control",
          "pen blocks (to see it clearly) — Pen"
        ],
        objective: "Read and build a nested loop and predict how many times the inside runs.",
        warmup: "Human loop: a row of 4 kids. Each claps twice (inner loop), and we go down the whole row (outer loop). Total claps? 4 × 2 = 8.",
        exercises: [
          { t: "Count it", d: "Predict: 'repeat 3 [ repeat 4 [ say hi ] ]' says hi how many times? (12.) Test it." },
          { t: "Grid of stamps", d: "Outer loop moves down a row, inner loop stamps across a column — a grid of sprites." },
          { t: "Flower", d: "Inner loop draws a shape; outer loop turns a bit and draws it again — a flower/mandala." }
        ],
        project: {
          title: "Mandala Maker",
          brief: "Use a nested loop to draw a symmetrical flower or mandala with the pen.",
          must: ["nested repeat", "pen", "turn in the outer loop"],
          stretch: "Change pen colour on each petal for a rainbow mandala."
        },
        challenge: "Draw a full grid of coins (like a Mario level) using two nested loops and stamp.",
        vocab: ["nested loop", "inner/outer loop"],
        checklist: ["I can put a loop inside a loop", "I can predict how many times the inner loop runs", "I built a pattern with nested loops"]
      },
      {
        module: "Loops & Repetition",
        title: "Mini Project — Dance Battle",
        emoji: "🕺",
        theme: "Just Dance",
        minutes: 60,
        concept: "Loops drive rhythm. Combine costume loops, movement, and repeats into a dance to a beat.",
        blocks: ["forever / repeat", "next costume", "move / glide", "wait (as the beat)"],
        objective: "Choreograph a looping dance for two sprites that stays on a beat.",
        warmup: "Clap a steady beat. Everyone does a 2-move dance ON the beat. The 'wait' is the beat length.",
        exercises: [
          { t: "One dancer", d: "'forever → next costume → move a bit → wait 0.3 (the beat)'." },
          { t: "Side to side", d: "Use a repeat to step right 4 times, then left 4 times, looping forever." },
          { t: "Add a partner", d: "Second sprite dances on the same beat but with a different move for contrast." }
        ],
        project: {
          title: "Dance Battle",
          brief: "Two characters dance on the same beat with different moves and colour effects. Add a backdrop with a stage vibe.",
          must: ["2 dancing sprites", "forever/repeat", "next costume", "wait on beat"],
          stretch: "Add a real drum sound each beat (Sound module next) and a spotlight colour effect."
        },
        challenge: "Make the dancers switch moves every 8 beats (hint: nested loops — 8 beats inside a forever).",
        vocab: ["beat", "choreography", "loop"],
        checklist: ["I can loop a dance on a beat", "I coordinated two dancers", "I used costume + movement loops together"]
      },

      /* ---------- MODULE D: Events & Control (19–24) ---------- */
      {
        module: "Events & Control",
        title: "Events — Making Things Happen",
        emoji: "⚡",
        theme: "Core concept",
        minutes: 60,
        concept: "Events (yellow hat blocks) start scripts. Different events = different ways to trigger code.",
        blocks: [
          "when green flag clicked — Events",
          "when () key pressed — Events",
          "when this sprite clicked — Events",
          "when [space] key pressed"
        ],
        objective: "Trigger scripts from the flag, a key press, and a click, all in one project.",
        warmup: "Doorbell / alarm / phone: each sound triggers a different reaction. Events are triggers — 'when X happens, do Y'.",
        exercises: [
          { t: "Flag", d: "'when green flag clicked → go to x:0 y:0' (a reset)." },
          { t: "Key", d: "'when space key pressed → say Jump!'. Press space to test." },
          { t: "Click", d: "'when this sprite clicked → play a sound / grow'." }
        ],
        project: {
          title: "Reaction Board",
          brief: "One sprite that does three different things depending on the trigger: flag resets it, space makes it jump-say, clicking makes it spin.",
          must: ["when green flag", "when key pressed", "when this sprite clicked"],
          stretch: "Add two more keys (arrow up/down) with their own reactions."
        },
        challenge: "Make a tiny 'piano': three sprites, each a key, each plays a different note when clicked.",
        vocab: ["event", "trigger", "hat block"],
        checklist: ["I can start code with a key press", "I can start code with a click", "I understand events are triggers"]
      },
      {
        module: "Events & Control",
        title: "Keyboard Control",
        emoji: "⌨️",
        theme: "Character control",
        minutes: 60,
        concept: "Arrow keys + change x/y = you can drive a character around. This is the heart of nearly every game.",
        blocks: [
          "when () key pressed — Events",
          "change x by () / change y by () — Motion",
          "point in direction () — Motion"
        ],
        objective: "Drive a sprite with all four arrow keys.",
        warmup: "Remote-control human: call left/right/up/down and a student steps that way. That's what the arrow keys will do.",
        exercises: [
          { t: "Left & right", d: "'when right arrow pressed → change x by 10' and 'when left arrow pressed → change x by -10'." },
          { t: "Up & down", d: "Add up (change y by 10) and down (change y by -10)." },
          { t: "Face the way you move", d: "Add 'point in direction 90/-90' so the sprite faces its movement direction." }
        ],
        project: {
          title: "Free Roam",
          brief: "Drive a character around a backdrop with all four arrow keys, facing the way it moves.",
          must: ["4 arrow-key scripts", "change x/y", "a backdrop"],
          stretch: "Keep the sprite on screen with 'if on edge, bounce' or by clamping position."
        },
        challenge: "Make movement smoother by putting the checks inside a forever loop with 'if key pressed' (compare the feel).",
        vocab: ["input", "arrow keys", "clamp"],
        checklist: ["I can move a sprite with all four arrows", "I can make it face the way it moves", "I understand keyboard input drives games"]
      },
      {
        module: "Events & Control",
        title: "Mouse Control",
        emoji: "🖱️",
        theme: "Character control",
        minutes: 60,
        concept: "Sprites can follow the mouse or react to clicks — perfect for aiming, dragging, and pointing games.",
        blocks: [
          "go to [mouse-pointer] / point towards [mouse-pointer] — Motion",
          "mouse x / mouse y — Sensing",
          "mouse down? — Sensing"
        ],
        objective: "Make a sprite follow and point at the mouse, and react to clicks.",
        warmup: "Follow my finger with your eyes. Now imagine a sprite doing that with the mouse. That's 'point towards mouse'.",
        exercises: [
          { t: "Follow", d: "'forever → go to mouse-pointer'. The sprite becomes the cursor." },
          { t: "Aim", d: "'forever → point towards mouse-pointer'. The sprite rotates to face the mouse (like a turret)." },
          { t: "Shoot on click", d: "'forever → if mouse down? → say Pew!'. React while the button is held." }
        ],
        project: {
          title: "Turret Aim",
          brief: "A cannon/turret that always points at the mouse and does something when you click.",
          must: ["point towards mouse", "if mouse down?", "a reaction on click"],
          stretch: "Add a crosshair sprite that follows the mouse exactly."
        },
        challenge: "Make a bug that runs AWAY from the mouse (point towards, then move backwards).",
        vocab: ["mouse-pointer", "aim", "cursor"],
        checklist: ["I can make a sprite follow the mouse", "I can make a sprite point at the mouse", "I can react to mouse clicks"]
      },
      {
        module: "Events & Control",
        title: "Broadcasting — Sprites Talking to Each Other",
        emoji: "📡",
        theme: "Core concept",
        minutes: 60,
        concept: "A broadcast is a message ALL sprites can hear. It's how one sprite tells others 'now do your thing'.",
        blocks: [
          "broadcast () — Events",
          "broadcast () and wait — Events",
          "when I receive () — Events"
        ],
        objective: "Coordinate multiple sprites with broadcast messages.",
        warmup: "Referee's whistle: one whistle, everyone reacts at once. That's a broadcast — one message, many listeners.",
        exercises: [
          { t: "Make a message", d: "Create a new message called 'start-game'. Broadcast it from the Stage on the green flag." },
          { t: "Everyone reacts", d: "Each sprite: 'when I receive start-game → show and go to its spot'." },
          { t: "Wait for it", d: "Use 'broadcast intro and wait' so the next line only runs AFTER all receivers finish. Great for cutscenes." }
        ],
        project: {
          title: "Countdown Start",
          brief: "Green flag → a '3-2-1-GO!' countdown → broadcast 'go' → all characters spring into action at once.",
          must: ["broadcast", "when I receive", "a countdown"],
          stretch: "Use 'broadcast and wait' to chain scenes: intro → gameplay → win screen."
        },
        challenge: "Build a domino chain: sprite A finishes then broadcasts to B, B to C, and so on.",
        vocab: ["broadcast", "message", "receiver"],
        checklist: ["I can create and send a broadcast", "I can make sprites react with 'when I receive'", "I know when to use 'broadcast and wait'"]
      },
      {
        module: "Events & Control",
        title: "Wait, Timing & Sequencing",
        emoji: "⏱️",
        theme: "Core concept",
        minutes: 60,
        concept: "Control the flow of time in your game with waits and 'wait until' so events happen in the right order.",
        blocks: [
          "wait () seconds — Control",
          "wait until () — Control",
          "repeat until () — Control"
        ],
        objective: "Sequence events with precise timing and wait for a condition to be true.",
        warmup: "Traffic lights: red (wait) → green (go). 'Wait until the light is green' is exactly 'wait until'.",
        exercises: [
          { t: "Fixed wait", d: "Make a light change: red backdrop → wait 2 → green backdrop." },
          { t: "Wait until", d: "'wait until key space pressed → say Go!'. The script pauses right there until you press space." },
          { t: "Repeat until", d: "'repeat until touching edge → move 10'. It moves until it hits the wall, then stops." }
        ],
        project: {
          title: "Traffic Light Crossing",
          brief: "A crossing where a character waits until the light is green (space press or backdrop) before walking across.",
          must: ["wait until", "backdrop or key trigger", "movement"],
          stretch: "Add a beeping sound while the light is red (Sound module)."
        },
        challenge: "Make a 'ready-set-go' race start: two racers wait until 'go', then both dash — first to the edge wins the say.",
        vocab: ["wait until", "sequence", "condition"],
        checklist: ["I can pause with a fixed wait", "I can wait until a condition is true", "I can loop until something happens"]
      },
      {
        module: "Events & Control",
        title: "Mini Project — Character Controller",
        emoji: "🎮",
        theme: "Minecraft-style movement",
        minutes: 60,
        concept: "Put motion + keyboard + animation + events together into a smooth, reusable character controller.",
        blocks: ["arrow key events", "change x/y", "next costume / walk animation", "point in direction"],
        objective: "Build a polished top-down character you can walk around a world — the base for many future games.",
        warmup: "Name three games where you walk a character around a top-down world (Minecraft, Zelda, Pokémon, Stardew). You're building that base today.",
        exercises: [
          { t: "Walk + animate", d: "Combine arrow-key movement with the walk animation from Module B — legs move only while walking." },
          { t: "Face direction", d: "Make the sprite face the way it's walking (up/down/left/right)." },
          { t: "World feel", d: "Add a top-down backdrop (a map/ground) and start the sprite in the centre on the green flag." }
        ],
        project: {
          title: "Explorer",
          brief: "A character that walks around a top-down world map with animated movement, facing the right way, staying on screen.",
          must: ["4-direction movement", "walk animation", "facing", "reset on green flag"],
          stretch: "Add a second area: walking to the edge switches to a new backdrop (a new 'room')."
        },
        challenge: "Add a 'sprint' — holding shift makes the character move faster.",
        vocab: ["controller", "top-down", "reusable"],
        checklist: ["I built a walking, animated character", "It faces the way it moves", "I can reuse this controller in future games"]
      },

      /* ---------- MODULE E: Decisions & Sensing (25–32) ---------- */
      {
        module: "Decisions & Sensing",
        title: "If / Then — Making Decisions",
        emoji: "🤔",
        theme: "Core concept",
        minutes: 60,
        concept: "'if <something is true> then …' lets your program make decisions instead of always doing the same thing.",
        blocks: [
          "if <> then — Control (C-shape)",
          "key () pressed? — Sensing (boolean, hexagon)"
        ],
        objective: "Run code only when a condition is true.",
        warmup: "'If you're wearing something blue, stand up.' Only some people react. That's an 'if' — the action depends on a condition.",
        exercises: [
          { t: "First if", d: "'forever → if key space pressed? then say Jump!'. It only speaks WHEN space is down." },
          { t: "Move on key", d: "'forever → if key right arrow pressed? then change x by 10'. Smoother than separate key hats." },
          { t: "Two ifs", d: "Add left arrow with 'change x by -10'. Two independent decisions in one loop." }
        ],
        project: {
          title: "Smooth Mover",
          brief: "Move a sprite left/right using 'if key pressed?' inside a forever loop (compare the feel to arrow-key hats).",
          must: ["forever", "if <> then", "key pressed?"],
          stretch: "Add up/down and a jump that only works when space is pressed."
        },
        challenge: "Add a boundary: 'if x position > 200 then set x to 200' so the sprite can't leave the screen.",
        vocab: ["condition", "if/then", "boolean"],
        checklist: ["I can run code only when a condition is true", "I can use 'key pressed?'", "I put ifs inside a forever loop"]
      },
      {
        module: "Decisions & Sensing",
        title: "If / Else",
        emoji: "🔀",
        theme: "Core concept",
        minutes: 60,
        concept: "'if…else' does one thing when true and a DIFFERENT thing when false — never both.",
        blocks: [
          "if <> then … else … — Control",
          "() > () / () < () / () = () — Operators (green)"
        ],
        objective: "Choose between two actions based on a condition.",
        warmup: "'If it's raining, take an umbrella, ELSE wear sunglasses.' You pick exactly one path.",
        exercises: [
          { t: "Door check", d: "'if key space pressed? then say Open else say Closed'. Exactly one shows." },
          { t: "Compare numbers", d: "Use an operator: 'if (x position) > 0 then say Right side else say Left side'." },
          { t: "Colour swap", d: "'if touching edge? then set colour effect to 100 else clear graphic effects'." }
        ],
        project: {
          title: "Mood Ring",
          brief: "A sprite that shows one look/message if a condition is true and a different one if false (e.g. left half vs right half of the screen).",
          must: ["if/else", "a comparison operator", "two clearly different outcomes"],
          stretch: "Nest an if inside the else for a third option (three zones)."
        },
        challenge: "Make a day/night toggle: space flips between a bright and a dark scene using if/else on a variable (preview).",
        vocab: ["if/else", "operator", "compare"],
        checklist: ["I can choose between two actions", "I can compare numbers with > < =", "I understand only one branch runs"]
      },
      {
        module: "Decisions & Sensing",
        title: "Sensing — Touching",
        emoji: "👉",
        theme: "Collision (game core)",
        minutes: 60,
        concept: "Collision detection = 'is this sprite touching that one?'. It's the beating heart of almost every game.",
        blocks: [
          "touching ()? — Sensing",
          "touching color ()? — Sensing",
          "if <> then — Control"
        ],
        objective: "Detect when sprites touch each other or touch a colour.",
        warmup: "Tag: 'if you're touched, you're it'. That single rule IS collision detection.",
        exercises: [
          { t: "Touch a sprite", d: "'forever → if touching Apple? then say Yum! and hide the apple'." },
          { t: "Touch a colour", d: "Draw a red wall. 'if touching color red? then go back to start'. (Maze games use this!)" },
          { t: "Touch the edge", d: "'if touching edge? then say Wall!'. Useful for boundaries." }
        ],
        project: {
          title: "Don't Touch the Lava",
          brief: "Walk a character across a backdrop. Touching the red 'lava' colour sends you back to the start; reaching the goal wins.",
          must: ["touching color?", "if/then", "go to start", "a goal"],
          stretch: "Add a moving hazard sprite and check 'touching' it too."
        },
        challenge: "Make the goal only count if you're ALSO touching a certain colour (a key + a door — hint: 'and' next lesson).",
        vocab: ["collision", "touching", "hazard"],
        checklist: ["I can detect touching a sprite", "I can detect touching a colour", "I built a touch-based game rule"]
      },
      {
        module: "Decisions & Sensing",
        title: "Sensing — Keys, Mouse & Distance",
        emoji: "📏",
        theme: "Collision (game core)",
        minutes: 60,
        concept: "Sensing blocks report what's happening: which keys are down, where the mouse is, and how far apart things are.",
        blocks: [
          "distance to () — Sensing",
          "mouse down? / key () pressed? — Sensing",
          "timer / reset timer — Sensing"
        ],
        objective: "Use distance and other sensing values to drive game logic.",
        warmup: "Hot-and-cold: hide an object; call 'hotter/colder' as someone nears it. 'Distance to' is the exact hot-and-cold number.",
        exercises: [
          { t: "Distance", d: "'forever → if distance to mouse-pointer < 50 then say Close!'. Reacts only when the mouse is near." },
          { t: "Timer", d: "Show the 'timer' value on the Stage. It counts seconds since the flag. 'reset timer' zeroes it." },
          { t: "Proximity glow", d: "Grow the sprite the closer the mouse is (change size based on distance)." }
        ],
        project: {
          title: "Proximity Alarm",
          brief: "A sprite that reacts (glows/beeps/warns) as the mouse gets closer, and relaxes when it's far.",
          must: ["distance to", "if/else", "a clear near vs far reaction"],
          stretch: "Show a live timer and challenge the player to reach the sprite within 5 seconds."
        },
        challenge: "Make a stealth game: a guard says 'I see you!' only if you come within a set distance.",
        vocab: ["distance", "timer", "sensing"],
        checklist: ["I can use 'distance to'", "I can read and reset the timer", "I drove behaviour from a sensed value"]
      },
      {
        module: "Decisions & Sensing",
        title: "Boolean Logic — And / Or / Not",
        emoji: "🧮",
        theme: "Core concept",
        minutes: 60,
        concept: "Combine conditions: AND (both true), OR (either true), NOT (flip true/false) for smarter rules.",
        blocks: [
          "<> and <> — Operators",
          "<> or <> — Operators",
          "not <> — Operators"
        ],
        objective: "Build rules that depend on more than one condition.",
        warmup: "'Stand if you have a pet AND a sibling.' Then 'OR'. Then 'NOT wearing trainers.' Feel how few/many stand each time.",
        exercises: [
          { t: "AND", d: "'if <touching goal?> and <key space pressed?> then say You win!'. Both must be true." },
          { t: "OR", d: "'if <touching lava?> or <touching spikes?> then lose a life'. Either hazard triggers it." },
          { t: "NOT", d: "'if not <touching ground?> then fall'. Reacts when something is NOT true." }
        ],
        project: {
          title: "Locked Door",
          brief: "A door that only opens if the player has the key (touching key sprite) AND presses space at the door.",
          must: ["and", "touching?", "key pressed?"],
          stretch: "Add a trap that hurts if you touch spikes OR fall off the edge."
        },
        challenge: "Make a rule that only fires the FIRST time both conditions are true (hint: use a flag variable — coming soon).",
        vocab: ["and", "or", "not", "boolean"],
        checklist: ["I can combine two conditions with AND", "I can use OR for alternatives", "I can flip a condition with NOT"]
      },
      {
        module: "Decisions & Sensing",
        title: "Ask & Answer (Input)",
        emoji: "❓",
        theme: "Quiz games",
        minutes: 60,
        concept: "'ask and wait' pauses the game and lets the player TYPE an answer, which you can then check.",
        blocks: [
          "ask () and wait — Sensing",
          "answer — Sensing (reporter)",
          "() = () — Operators"
        ],
        objective: "Collect typed input and respond differently based on the answer.",
        warmup: "Quiz-master: ask the class a question, wait for the answer, then say right/wrong. You'll code exactly that.",
        exercises: [
          { t: "Ask a name", d: "'ask What is your name? and wait → say (join Hello, answer)'." },
          { t: "Check an answer", d: "'ask 2+2? and wait → if answer = 4 then say Correct! else say Try again.'" },
          { t: "Join text", d: "Use the 'join' operator to build sentences from the answer." }
        ],
        project: {
          title: "Two-Question Quiz",
          brief: "Ask two questions, check each answer, and give feedback. Say the final result at the end.",
          must: ["ask and wait", "answer", "= comparison", "if/else feedback"],
          stretch: "Keep a score (preview of variables) and show the total out of 2."
        },
        challenge: "Accept more than one correct spelling (use OR: answer = 'red' or answer = 'Red').",
        vocab: ["input", "answer", "join"],
        checklist: ["I can ask the player a question", "I can check their typed answer", "I can join text into a sentence"]
      },
      {
        module: "Decisions & Sensing",
        title: "Collision Detection Deep Dive",
        emoji: "💥",
        theme: "Collision (game core)",
        minutes: 60,
        concept: "Reliable collisions make games feel fair. Small sprites, clear colours, and checking every frame are the tricks.",
        blocks: [
          "touching ()? / touching color ()? — Sensing",
          "forever + if — Control",
          "go to / set x/y (respond to a hit) — Motion"
        ],
        objective: "Make collisions that feel fair and respond correctly (bounce back, stop, or trigger an event).",
        warmup: "Bumper cars: what should happen the instant two cars touch? Stop? Bounce? Score? Design the response, not just the detection.",
        exercises: [
          { t: "Check every frame", d: "Collisions live inside 'forever' so they're checked constantly, not once." },
          { t: "Respond to the hit", d: "On touching a wall: 'set x to (last safe x)' or 'change x by -10' to push back out." },
          { t: "Small & distinct", d: "Shrink the player to ~40% and use one thick wall colour — this fixes most 'it went through the wall' bugs." }
        ],
        project: {
          title: "Bumper Arena",
          brief: "A sprite you drive that bounces back when it hits walls (a coloured border) and scores a 'ding' when it touches a target.",
          must: ["forever collision check", "push-back response", "touching color / touching sprite"],
          stretch: "Add two targets worth different points (preview variables)."
        },
        challenge: "Make a wall you can pass through only while holding space (a secret passage).",
        vocab: ["collision response", "frame", "push-back"],
        checklist: ["I check collisions every frame", "I respond to a hit, not just detect it", "I know tricks for fair collisions"]
      },
      {
        module: "Decisions & Sensing",
        title: "Mini Project — Collect the Coins",
        emoji: "🪙",
        theme: "Super Mario",
        minutes: 60,
        concept: "Combine movement + collision into the classic collect-em-up loop that powers Mario, Sonic, and more.",
        blocks: ["arrow movement", "touching?", "hide/show", "if/then", "broadcast (optional)"],
        objective: "Build a game where a character collects coins that disappear when touched.",
        warmup: "Name games where you collect things (Mario coins, Minecraft ores, Roblox candy). The rule is always: touch → collect → it's gone.",
        exercises: [
          { t: "Place coins", d: "Add 3–5 coin sprites around a backdrop (duplicate one coin)." },
          { t: "Collect", d: "Each coin: 'forever → if touching player? then hide'. Walk into it and it vanishes." },
          { t: "Win check", d: "When all coins are hidden, broadcast 'win' and show a 'You collected them all!' message." }
        ],
        project: {
          title: "Coin Rush",
          brief: "Drive a character to collect every coin on the screen; a win message appears when they're all gone.",
          must: ["player movement", "coins that hide on touch", "a win condition"],
          stretch: "Add a coin sound and reset all coins to visible on the green flag."
        },
        challenge: "Add a moving enemy — touching it sends you back to start (real stakes!).",
        vocab: ["collect", "win condition", "reset"],
        checklist: ["I built a collectible game", "Coins disappear on touch", "I detect when the level is complete"]
      },

      /* ---------- MODULE F: Variables & Scoring (33–38) ---------- */
      {
        module: "Variables & Scoring",
        title: "Variables — The Labelled Box",
        emoji: "📦",
        theme: "Core concept",
        minutes: 60,
        concept: "A variable is a labelled box that holds a value you can read and change while the game runs.",
        blocks: [
          "Make a Variable — Variables",
          "set () to () — Variables",
          "change () by () — Variables"
        ],
        objective: "Create a variable, set it, change it, and show it on the Stage.",
        warmup: "Paper cup labelled 'score' + counters. Add a counter = 'change score by 1'. Empty it = 'set score to 0'. That's a variable.",
        exercises: [
          { t: "Make it", d: "Variables category → 'Make a Variable' → name it 'score'. Tick its box to show it on the Stage." },
          { t: "Set & change", d: "'set score to 0' then 'change score by 1' a few times. Watch the number on the Stage." },
          { t: "Use it", d: "'if score = 5 then say Level up!'. The variable drives a decision." }
        ],
        project: {
          title: "Click Counter",
          brief: "Click a sprite to add 1 to a score; a button resets it to 0. Say a message when it reaches 10.",
          must: ["a variable", "set to 0", "change by 1", "an if check on the value"],
          stretch: "Add a second variable 'clicks needed' and count DOWN from 10 to 0 instead."
        },
        challenge: "Make a two-variable game: 'coins' and 'gems', each with its own button.",
        vocab: ["variable", "set", "change"],
        checklist: ["I can make a variable", "I can set and change it", "I can use a variable in an if"]
      },
      {
        module: "Variables & Scoring",
        title: "Score & Points",
        emoji: "🏆",
        theme: "Every game",
        minutes: 60,
        concept: "Scoring turns actions into progress. Always reset the score at the start or it carries over between games.",
        blocks: [
          "set [score] to 0 — Variables",
          "change [score] by () — Variables",
          "broadcast (game over) — Events"
        ],
        objective: "Add proper scoring to a game, including a reset and a target.",
        warmup: "The classic bug: a game where the score never resets, so it climbs to a million. Why? (No 'set score to 0'.)",
        exercises: [
          { t: "Reset first", d: "On the green flag: 'set score to 0' BEFORE anything else. This is the #1 scoring rule." },
          { t: "Award points", d: "On collecting a coin: 'change score by 1' (or by 5 for a rare gem)." },
          { t: "Reach the target", d: "'if score = 10 then broadcast win'." }
        ],
        project: {
          title: "Scored Coin Rush",
          brief: "Upgrade your Coin Rush: coins add to a score, rare gems add more, and reaching a target wins.",
          must: ["set score to 0 on start", "change score by (different amounts)", "win at a target"],
          stretch: "Add a 'high score' variable that only updates when you beat it."
        },
        challenge: "Add negative points: touching a bomb does 'change score by -3' (but not below 0).",
        vocab: ["score", "points", "reset"],
        checklist: ["I reset the score at the start", "I award different points for different things", "I win at a score target"]
      },
      {
        module: "Variables & Scoring",
        title: "Timer & Countdown",
        emoji: "⏳",
        theme: "Arcade pressure",
        minutes: 60,
        concept: "A countdown adds pressure and a clear end. Build one with a variable that ticks down each second.",
        blocks: [
          "set [time] to () / change [time] by -1 — Variables",
          "wait 1 seconds — Control",
          "repeat until (time = 0) — Control"
        ],
        objective: "Build a countdown timer that ends the game at zero.",
        warmup: "'You have 10 seconds to tidy your desk!' Countdown pressure changes everything. That's what a timer adds.",
        exercises: [
          { t: "Count down", d: "'set time to 30 → repeat until time = 0 [ wait 1 → change time by -1 ]'." },
          { t: "End the game", d: "After the countdown loop: 'broadcast game-over'." },
          { t: "Show it", d: "Display 'time' on the Stage so the player feels the pressure." }
        ],
        project: {
          title: "Beat the Clock",
          brief: "Collect as many coins as you can before a 30-second countdown reaches zero, then show the final score.",
          must: ["countdown variable", "score variable", "game-over broadcast at 0"],
          stretch: "Flash the timer red in the last 5 seconds for tension."
        },
        challenge: "Add time bonuses: certain coins give '+3 seconds' (change time by 3).",
        vocab: ["countdown", "pressure", "game over"],
        checklist: ["I can build a countdown", "I end the game at zero", "I show the timer to the player"]
      },
      {
        module: "Variables & Scoring",
        title: "Lives & Health",
        emoji: "❤️",
        theme: "Action games",
        minutes: 60,
        concept: "Lives/health let players fail without instantly losing. Game over happens when they hit zero.",
        blocks: [
          "set [lives] to 3 — Variables",
          "change [lives] by -1 — Variables",
          "if (lives = 0) then broadcast game-over — Control/Events"
        ],
        objective: "Add a lives/health system with damage, invulnerability, and game over.",
        warmup: "Video-game hearts: why not just die on the first hit? (No fun, no learning.) Lives give second chances.",
        exercises: [
          { t: "Start with lives", d: "'set lives to 3' on the green flag; show it on the Stage." },
          { t: "Take damage", d: "On touching an enemy: 'change lives by -1' then 'wait 1' (so one touch = one hit, not fifty)." },
          { t: "Game over", d: "'if lives = 0 then broadcast game-over and stop this script'." }
        ],
        project: {
          title: "Survive the Hazards",
          brief: "A character with 3 lives dodging hazards; each hit costs a life, and zero lives ends the game.",
          must: ["lives variable", "damage with a brief wait", "game over at 0"],
          stretch: "Flash the player (ghost effect) briefly after a hit to show invulnerability."
        },
        challenge: "Add a health bar using a costume that changes with the health value (full/half/low).",
        vocab: ["lives", "health", "invulnerability"],
        checklist: ["I can track lives", "I apply damage without draining all lives at once", "I trigger game over at zero"]
      },
      {
        module: "Variables & Scoring",
        title: "Variables Control Everything",
        emoji: "🎚️",
        theme: "Game design",
        minutes: 60,
        concept: "Variables can control speed, difficulty, position — not just score. Change the variable, change the game.",
        blocks: [
          "set/change (any variable) — Variables",
          "using a variable inside move/glide/wait — Motion/Control",
          "() * () , () + () — Operators"
        ],
        objective: "Use variables to control game behaviour like speed and difficulty.",
        warmup: "A volume knob controls loudness with one dial. A variable is a knob for your game — turn it and everything using it changes.",
        exercises: [
          { t: "Speed variable", d: "Make 'speed'. Use 'change x by speed' instead of a fixed number. Now one variable controls how fast the player moves." },
          { t: "Ramp difficulty", d: "'change speed by 1' every few seconds so the game gets harder over time." },
          { t: "Math with variables", d: "Use operators: 'set wait-time to (1 / speed)' so faster speed means shorter waits." }
        ],
        project: {
          title: "Difficulty Dial",
          brief: "A dodging game whose enemy speed is a variable that slowly increases, making it harder the longer you survive.",
          must: ["a speed/difficulty variable", "using it in movement", "increasing it over time"],
          stretch: "Add an on-screen 'Level' that goes up each time the speed increases."
        },
        challenge: "Let the player pick easy/medium/hard at the start (ask & set the speed variable accordingly).",
        vocab: ["difficulty", "ramp", "operator"],
        checklist: ["I use a variable to control speed", "I ramp difficulty over time", "I did math with variables"]
      },
      {
        module: "Variables & Scoring",
        title: "Mini Project — Flappy Score",
        emoji: "🐦",
        theme: "Flappy Bird",
        minutes: 60,
        concept: "Bring scoring, timing, and variables together in a tiny arcade game — Flappy-style tap-to-fly.",
        blocks: ["change y by (gravity)", "space to flap", "score variable", "game over broadcast"],
        objective: "Build a minimal Flappy-style game with a working score.",
        warmup: "Why is Flappy Bird so addictive? One button, instant restart, a score to beat. Simple + fair = fun.",
        exercises: [
          { t: "Gravity", d: "'forever → change y by -4' pulls the bird down constantly." },
          { t: "Flap", d: "'if key space pressed? then change y by 8' — tapping fights gravity." },
          { t: "Score", d: "Add 1 to score each second survived (or each obstacle passed). Reset to 0 on start." }
        ],
        project: {
          title: "Flappy (Mini)",
          brief: "A bird that falls with gravity, flaps up on space, scores over time, and game-overs if it hits the ground.",
          must: ["gravity", "flap on space", "score variable", "game over on ground touch"],
          stretch: "Add one moving pipe/obstacle to dodge (full clone-based pipes come in Level 2)."
        },
        challenge: "Show a 'best score' that survives between attempts.",
        vocab: ["gravity", "one-button game", "restart"],
        checklist: ["I made gravity + flap", "I added a working score", "I handled game over"]
      },

      /* ---------- MODULE G: Level 1 Game Builds (39–50) ---------- */
      {
        module: "Level 1 Game Builds",
        title: "Catch Game — Setup",
        emoji: "🧺",
        theme: "Arcade classic",
        minutes: 60,
        concept: "A full 2-part build: a basket you steer and objects that fall from the top. Today: the moving parts.",
        blocks: ["arrow/mouse movement", "go to x: random y: 180", "change y by (fall)", "touching?"],
        objective: "Build the basket and a falling object that resets to the top.",
        warmup: "Plan the game in one sentence: 'Move the basket to catch falling apples before they hit the floor.'",
        exercises: [
          { t: "Steer the basket", d: "Basket follows the mouse's x (or arrow keys), locked to the bottom of the Stage." },
          { t: "Make it fall", d: "Apple: 'go to x:(pick random -200 to 200) y:180 → forever → change y by -5'." },
          { t: "Respawn", d: "'if y position < -160 then go to x:(random) y:180' so it falls again from a new spot." }
        ],
        project: {
          title: "Catch — Part 1",
          brief: "A basket you control and an apple that falls repeatedly from random positions at the top.",
          must: ["basket control", "falling apple", "respawn at top"],
          stretch: "Add a second falling object at a different speed."
        },
        challenge: "Make the apple fall faster each time it respawns (a speed variable).",
        vocab: ["spawn", "respawn", "random"],
        checklist: ["I built a controllable basket", "I made an object fall and respawn", "I used random positions"]
      },
      {
        module: "Level 1 Game Builds",
        title: "Catch Game — Scoring & Game Over",
        emoji: "🍎",
        theme: "Arcade classic",
        minutes: 60,
        concept: "Add the rules that make it a GAME: score for catches, lose a life for misses, end at zero lives.",
        blocks: ["touching basket?", "change score by 1", "change lives by -1", "broadcast game-over"],
        objective: "Turn the falling-object toy into a complete, winnable/losable game.",
        warmup: "What makes 'catch' a game and not a toy? Consequences: points for catching, penalty for missing.",
        exercises: [
          { t: "Score a catch", d: "Apple: 'if touching basket? then change score by 1 and respawn at top'." },
          { t: "Penalise a miss", d: "'if y < -160 then change lives by -1 and respawn'." },
          { t: "Game over", d: "'if lives = 0 then broadcast game-over → stop all'. Show a Game Over backdrop." }
        ],
        project: {
          title: "Catch — Complete",
          brief: "The full game: catch apples for points, miss and lose a life, game over at 0 lives, with a start reset.",
          must: ["score on catch", "life lost on miss", "game over screen", "reset on green flag"],
          stretch: "Add a golden apple worth 5 points that falls faster."
        },
        challenge: "Add a difficulty ramp: fall speed increases every 10 points.",
        vocab: ["consequence", "game loop", "polish"],
        checklist: ["Catching scores points", "Missing costs a life", "The game ends and resets cleanly"]
      },
      {
        module: "Level 1 Game Builds",
        title: "Maze Game — Movement & Walls",
        emoji: "🧩",
        theme: "Maze / Pac-Man",
        minutes: 60,
        concept: "A maze uses colour collision for walls. Part 1: draw the maze and move without passing through walls.",
        blocks: ["arrow movement", "touching color (wall)?", "set x/y back (push-back)"],
        objective: "Build a maze backdrop and a player that can't walk through walls.",
        warmup: "Trace a paper maze with a finger. Your finger can't cross the lines — that's exactly what colour collision does.",
        exercises: [
          { t: "Draw the maze", d: "Paint a backdrop with thick walls in ONE distinct colour (e.g. blue). Leave clear paths." },
          { t: "Shrink the player", d: "Set the player to ~30–40% size so it fits the corridors." },
          { t: "Block walls", d: "After each move: 'if touching color blue? then move back' (undo the step). Now walls are solid." }
        ],
        project: {
          title: "Maze — Part 1",
          brief: "A maze you can navigate with arrow keys where walls actually stop you.",
          must: ["maze backdrop (one wall colour)", "arrow movement", "wall collision push-back"],
          stretch: "Add a start marker and place the player there on the green flag."
        },
        challenge: "Make the push-back work smoothly in all four directions (store the last safe x and y).",
        vocab: ["maze", "colour collision", "corridor"],
        checklist: ["I drew a maze with one wall colour", "My player fits the corridors", "Walls stop the player"]
      },
      {
        module: "Level 1 Game Builds",
        title: "Maze Game — Goal, Levels & Win",
        emoji: "🏁",
        theme: "Maze / Pac-Man",
        minutes: 60,
        concept: "Add a goal, a timer or coins, and multiple maze levels via backdrops. Now it's a real game.",
        blocks: ["touching goal?", "switch backdrop (next level)", "score/timer variables", "broadcast win"],
        objective: "Complete the maze game with a goal, collectibles, and a second level.",
        warmup: "What turns a maze into a game? A goal, and maybe a clock or coins to make the path meaningful.",
        exercises: [
          { t: "Reach the goal", d: "Place a goal sprite. 'if touching goal? then broadcast next-level'." },
          { t: "Next level", d: "On 'next-level': switch to a harder maze backdrop and move the player back to start." },
          { t: "Collect on the way", d: "Add coins in the corridors (touch to collect + score), like Pac-Man." }
        ],
        project: {
          title: "Maze — Complete",
          brief: "A two-level maze with coins to collect, a goal to reach, and a win screen after the last level.",
          must: ["goal detection", "at least two maze levels", "coins or a timer", "win screen"],
          stretch: "Add a moving enemy that patrols a corridor and sends you to start on touch."
        },
        challenge: "Add a 'best time' using the timer so players race their own record.",
        vocab: ["goal", "level", "progression"],
        checklist: ["Reaching the goal advances the level", "I have more than one maze", "There's a win screen"]
      },
      {
        module: "Level 1 Game Builds",
        title: "Whack-a-Creeper — Setup",
        emoji: "🟩",
        theme: "Minecraft",
        minutes: 60,
        concept: "A Minecraft-themed whack-a-mole: creepers pop up at random spots and you click them fast. Part 1: pop-ups.",
        blocks: ["go to (random position)", "show/hide", "wait (random)", "when this sprite clicked"],
        objective: "Make a creeper that appears at random spots for a short time.",
        warmup: "Whack-a-mole logic: something appears somewhere random, you have a moment to hit it, then it's gone. Simple and addictive.",
        exercises: [
          { t: "Pick random spots", d: "Decide 4–6 'holes' (fixed x/y spots) or use 'go to x:(random) y:(random)'." },
          { t: "Pop up & down", d: "'forever → go to a random hole → show → wait (pick random 0.5 to 1.2) → hide'." },
          { t: "Clickable", d: "'when this sprite clicked → (we'll add score next) → hide immediately'." }
        ],
        project: {
          title: "Whack — Part 1",
          brief: "A creeper that pops up at random holes for random short times and hides when clicked.",
          must: ["random position", "show/hide timing", "clickable creeper"],
          stretch: "Add a second creeper so two can be up at once."
        },
        challenge: "Make some pop-ups an 'innocent' villager you should NOT click.",
        vocab: ["pop-up", "random timing", "target"],
        checklist: ["My creeper appears at random spots", "It shows and hides on a timer", "Clicking it hides it"]
      },
      {
        module: "Level 1 Game Builds",
        title: "Whack-a-Creeper — Score & Timer",
        emoji: "⛏️",
        theme: "Minecraft",
        minutes: 60,
        concept: "Add scoring, a countdown, and penalties to complete the arcade whack game.",
        blocks: ["change score by 1", "countdown variable", "broadcast game-over", "sound on hit"],
        objective: "Finish the whack game with scoring, a timer, and a game-over screen.",
        warmup: "Arcade rule: reward speed. The faster you whack, the higher the score before time runs out.",
        exercises: [
          { t: "Score a whack", d: "'when this sprite clicked → change score by 1 → play a hit sound → hide'." },
          { t: "Countdown", d: "Stage: 'set time to 30 → repeat until time=0 [wait 1, change time by -1] → broadcast game-over'." },
          { t: "Penalty", d: "Clicking the 'wrong' sprite (villager) does 'change score by -2'." }
        ],
        project: {
          title: "Whack — Complete",
          brief: "Whack creepers for points against a 30-second clock; avoid whacking villagers; see a final score.",
          must: ["score on hit", "countdown timer", "penalty for wrong clicks", "final score screen"],
          stretch: "Speed up the pop-ups as time runs down."
        },
        challenge: "Add combos: whacking two creepers within a second gives bonus points.",
        vocab: ["combo", "penalty", "final score"],
        checklist: ["Whacking scores points", "There's a countdown", "Wrong clicks are penalised"]
      },
      {
        module: "Level 1 Game Builds",
        title: "Flappy Clone — Bird & Gravity",
        emoji: "🐤",
        theme: "Flappy Bird",
        minutes: 60,
        concept: "A cleaner Flappy build. Part 1: tune the bird's gravity and flap so it feels good to control.",
        blocks: ["change y by (velocity)", "space to flap", "point in direction (tilt)", "touching ground?"],
        objective: "Build a bird with satisfying gravity-and-flap feel.",
        warmup: "Good 'game feel': the flap should feel snappy but the fall should feel weighty. We'll tune numbers until it's fun.",
        exercises: [
          { t: "Fall", d: "'forever → change y by -4'. Then tune the -4 until the fall feels right." },
          { t: "Flap", d: "'if key space pressed? then set y-boost / change y by 8'. Tune the 8." },
          { t: "Tilt", d: "Point the bird slightly up when flapping and down when falling for personality." }
        ],
        project: {
          title: "Flappy — Part 1",
          brief: "A bird that falls and flaps with a feel you've tuned to be fun, and dies if it hits the ground or ceiling.",
          must: ["gravity", "flap", "ground/ceiling death"],
          stretch: "Add the tilt so the bird nose-dives when falling."
        },
        challenge: "Add a gentle 'idle bob' before the game starts (waiting for the first flap).",
        vocab: ["velocity", "game feel", "tuning"],
        checklist: ["My bird has gravity and flap", "I tuned it to feel fun", "It dies on ground/ceiling"]
      },
      {
        module: "Level 1 Game Builds",
        title: "Flappy Clone — Pipes & Scoring",
        emoji: "🟢",
        theme: "Flappy Bird",
        minutes: 60,
        concept: "Add scrolling pipes and scoring. (We'll do it with a moving sprite now; clones supercharge this in Level 2.)",
        blocks: ["change x by -5 (scroll)", "go to x:240 (respawn)", "touching pipe? (die)", "change score by 1 (pass)"],
        objective: "Add moving obstacles and a score to complete a Flappy game.",
        warmup: "The pipe's job: scroll left, and when it leaves the screen, jump back to the right at a new height. That's an endless obstacle.",
        exercises: [
          { t: "Scroll a pipe", d: "'forever → change x by -5 → if x < -240 then go to x:240 y:(random) and change score by 1'." },
          { t: "Deadly pipe", d: "'if touching pipe? then broadcast game-over'." },
          { t: "Score on pass", d: "Give a point each time a pipe wraps around (passed successfully)." }
        ],
        project: {
          title: "Flappy — Complete",
          brief: "The full loop: flap through scrolling pipes, score for each pipe passed, game over on collision, restart on flag.",
          must: ["scrolling pipe", "collision game-over", "score per pipe", "reset"],
          stretch: "Add a top AND bottom pipe with a gap the bird must fit through."
        },
        challenge: "Increase scroll speed as the score climbs.",
        vocab: ["scrolling", "obstacle", "endless"],
        checklist: ["Pipes scroll and respawn", "Hitting a pipe ends the game", "I score for passing pipes"]
      },
      {
        module: "Level 1 Game Builds",
        title: "Pong / Brick Bounce — Setup",
        emoji: "🏓",
        theme: "Pong",
        minutes: 60,
        concept: "The original video game! A ball that bounces and a paddle you control. Part 1: ball physics + paddle.",
        blocks: ["move + if on edge bounce", "point in direction (angle)", "paddle follows mouse/keys", "touching paddle?"],
        objective: "Build a bouncing ball and a paddle that hits it.",
        warmup: "Real ping-pong: the ball bounces off walls and the paddle at an angle. We'll fake that with 'if on edge, bounce' and paddle hits.",
        exercises: [
          { t: "Bouncing ball", d: "'point in direction 45 → forever → move 8 → if on edge, bounce'." },
          { t: "Paddle", d: "A paddle sprite at the bottom follows the mouse's x (or left/right keys)." },
          { t: "Paddle hit", d: "'if touching paddle? then point in direction (180 - direction)' to bounce it back up." }
        ],
        project: {
          title: "Pong — Part 1",
          brief: "A ball bouncing off the top and side walls and off your paddle.",
          must: ["bouncing ball", "controllable paddle", "paddle bounce"],
          stretch: "Vary the bounce angle based on where the ball hits the paddle."
        },
        challenge: "Add a bit of spin: speed the ball up slightly on each paddle hit.",
        vocab: ["bounce", "angle", "paddle"],
        checklist: ["My ball bounces off walls", "My paddle is controllable", "The ball bounces off the paddle"]
      },
      {
        module: "Level 1 Game Builds",
        title: "Pong / Brick Bounce — Scoring & Lose",
        emoji: "🧱",
        theme: "Pong / Breakout",
        minutes: 60,
        concept: "Add the losing condition (ball hits the floor) and a score for successful hits — or turn it into Breakout.",
        blocks: ["touching color (floor)? → lose", "change score by 1", "clone/stamp bricks (optional)", "broadcast game-over"],
        objective: "Complete Pong with scoring and a lose condition, or extend into brick-breaking.",
        warmup: "Two directions to take this: keep-it-up Pong (score per hit, lose if it drops) or Breakout (smash bricks). Pick one.",
        exercises: [
          { t: "Lose condition", d: "Paint the floor a colour. 'if ball touching color (floor)? then broadcast game-over'." },
          { t: "Score hits", d: "'change score by 1' on each paddle bounce." },
          { t: "Optional bricks", d: "Add a row of brick sprites; the ball hides a brick and scores on touch (Breakout!)." }
        ],
        project: {
          title: "Pong / Breakout — Complete",
          brief: "A complete bounce game: score for hits (or broken bricks), lose when the ball hits the floor, restart on flag.",
          must: ["score", "lose on floor touch", "reset", "(bricks optional)"],
          stretch: "Add a full grid of bricks and win when they're all gone."
        },
        challenge: "Add two paddles for two players (one keys, one mouse).",
        vocab: ["lose condition", "breakout", "grid"],
        checklist: ["I score for hits", "I lose when the ball drops", "The game restarts cleanly"]
      },
      {
        module: "Level 1 Game Builds",
        title: "Capstone — Design Your Own Arcade Game",
        emoji: "🛠️",
        theme: "Your idea",
        minutes: 60,
        concept: "You now know enough to invent your OWN game. Plan it on paper first, then build the core.",
        blocks: ["Everything from Level 1"],
        objective: "Plan and start building an original arcade game using Level 1 skills.",
        warmup: "Steal like a game designer: pick your favourite Level 1 game and change ONE big thing. New theme? New goal? New control? That's your game.",
        exercises: [
          { t: "Design sheet", d: "Write: Name. One-sentence idea. The player's goal. The controls. How you win. How you lose." },
          { t: "Build the core", d: "Build the ONE main mechanic first (the movement or the catching or the bouncing). Test it before adding anything." },
          { t: "Add score & end", d: "Add a score and a clear win or lose. A tiny finished game beats a huge broken one." }
        ],
        project: {
          title: "My Arcade Game — Build",
          brief: "An original game with a controllable player, a scoring system, and a clear win or lose state.",
          must: ["a design sheet", "player control", "score", "win or lose"],
          stretch: "Add a start screen and sound effects."
        },
        challenge: "Play-test with a partner and change one thing based on their feedback.",
        vocab: ["game design", "core mechanic", "play-test"],
        checklist: ["I planned my game on paper", "I built the core mechanic first", "It has a score and an ending"]
      },
      {
        module: "Level 1 Game Builds",
        title: "Level 1 Showcase & Certificate",
        emoji: "🎓",
        theme: "Celebrate",
        minutes: 60,
        concept: "Finish, polish, and present. Explaining your project is where the learning locks in.",
        blocks: ["Polish: start screen, instructions, sound, reset"],
        objective: "Polish and present your capstone game and reflect on what you learned.",
        warmup: "Presentation script (rehearse once): 'My game is ___ and you ___. The hardest part was ___. I fixed it by ___. Next I'd add ___.'",
        exercises: [
          { t: "Polish pass", d: "Add a start screen with instructions, make sure the green flag resets everything, and add at least one sound." },
          { t: "Bug hunt", d: "Play it 3 times. Fix the most annoying bug. 'Change one thing, test, repeat.'" },
          { t: "Present", d: "Demo your game to the class in 2 minutes using the script. Celebrate the debugging, not just the wins." }
        ],
        project: {
          title: "Showcase Build",
          brief: "Your capstone game, polished with a start screen, instructions, sound, and a reliable reset — ready to show.",
          must: ["start screen", "instructions", "reliable reset", "presented to others"],
          stretch: "Share it on the class Scratch studio for others to play."
        },
        challenge: "Write down two ideas you want to build in Level 2.",
        vocab: ["polish", "showcase", "reflection"],
        checklist: ["My game is polished and resets reliably", "I presented it", "I reflected on what I learned"]
      }
    ]
  });
})();
