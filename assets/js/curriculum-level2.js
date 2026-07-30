/* =====================================================================
   GRADE NEXT — SCRATCH CODING ACADEMY
   Curriculum data — LEVEL 2 "Game Architect" (50 sessions, ages 8–12+)
   ---------------------------------------------------------------------
   Level 2 goes deeper: clones, lists, custom blocks (functions), and
   full builds of the game genres kids ask for by name — platformers
   (Mario / Roblox obby), top-down adventures (Zelda / Minecraft),
   endless runners (Subway Surfers / Geometry Dash), and tycoon/clicker
   games (Roblox tycoon / Cookie Clicker) — ending in a big capstone.

   Same data shape as Level 1 (see README).
   ===================================================================== */
(function () {
  window.GN_LEVELS = window.GN_LEVELS || [];

  window.GN_LEVELS.push({
    level: 2,
    codename: "Game Architect",
    tagline: "Big games, real mechanics, your own worlds.",
    emoji: "🏗️",
    ageNote: "For students who finished Level 1 (or already know the Scratch basics).",
    color: "#9966FF",
    modules: [
      "Level Up: Advanced Motion",
      "Clones — Many at Once",
      "Lists & Data",
      "Custom Blocks & Clean Code",
      "Game Genres Deep Dive",
      "Polish & Pro Skills",
      "Capstone"
    ],
    sessions: [
      /* ---------- MODULE A: Level Up — Advanced Motion (1–6) ---------- */
      {
        module: "Level Up: Advanced Motion",
        title: "Welcome to Level 2 + Velocity",
        emoji: "🎯",
        theme: "Smooth movement",
        minutes: 60,
        concept: "Real games move things with a 'velocity' variable (a speed that can build up and slow down), not fixed steps. This is the secret to smooth movement.",
        blocks: [
          "velocity variables (xv / yv) — Variables",
          "change x by (xv) — Motion",
          "set xv to (xv * 0.9) — friction (Operators)"
        ],
        objective: "Move a sprite using a velocity variable with acceleration and friction.",
        warmup: "Push a toy car: it speeds up while you push (acceleration) and coasts to a stop (friction). Velocity captures both.",
        exercises: [
          { t: "Add velocity", d: "Make 'xv'. In a forever loop: 'change x by xv'. Right arrow does 'change xv by 1' (accelerate)." },
          { t: "Add friction", d: "Each frame: 'set xv to (xv * 0.9)'. The sprite glides to a stop instead of stopping dead." },
          { t: "Feel the difference", d: "Compare velocity movement to Level 1's fixed 'change x by 10'. Velocity feels alive." }
        ],
        project: {
          title: "Ice Skater",
          brief: "A character that accelerates and glides on 'ice' using x/y velocity and friction.",
          must: ["velocity variables", "acceleration on key press", "friction each frame"],
          stretch: "Tune the friction lower for slippery ice, higher for grippy ground."
        },
        challenge: "Add a max speed so the skater can't accelerate forever.",
        vocab: ["velocity", "acceleration", "friction"],
        checklist: ["I move a sprite with a velocity variable", "I can accelerate on key press", "I added friction for smooth stops"]
      },
      {
        module: "Level Up: Advanced Motion",
        title: "Gliding & Easing",
        emoji: "🪁",
        theme: "Smooth movement",
        minutes: 60,
        concept: "Easing makes movement feel natural by moving a FRACTION of the remaining distance each frame — fast then slowing as it arrives.",
        blocks: [
          "change x by ((target x - x position) / 5) — easing (Operators)",
          "glide () secs to () — Motion",
          "forever — Control"
        ],
        objective: "Make a sprite ease smoothly toward a target instead of snapping.",
        warmup: "A closing automatic door slows as it arrives — it doesn't slam. That gentle arrival is 'easing'.",
        exercises: [
          { t: "Ease to mouse", d: "'forever → change x by ((mouse x - x position)/5)'. The sprite chases the mouse smoothly, slowing as it nears." },
          { t: "Ease in both axes", d: "Add the same for y. Now it floats to the mouse like a cursor with weight." },
          { t: "Tune the feel", d: "Change the /5 to /2 (snappy) or /10 (floaty). Numbers are game-design decisions." }
        ],
        project: {
          title: "Floaty Follower",
          brief: "A sprite that eases toward the mouse with a satisfying, weighty feel.",
          must: ["easing formula", "both x and y", "a tuned divisor"],
          stretch: "Make a trail of 3 followers, each easing toward the one in front."
        },
        challenge: "Make a camera-style effect: the background eases in the opposite direction to the player.",
        vocab: ["easing", "interpolation", "feel"],
        checklist: ["I can ease a sprite toward a target", "I understand fraction-of-distance movement", "I tuned the divisor for feel"]
      },
      {
        module: "Level Up: Advanced Motion",
        title: "Gravity & Jumping",
        emoji: "🦘",
        theme: "Platformer physics",
        minutes: 60,
        concept: "Platformer jumping = a vertical velocity that gravity constantly pulls down, plus a ground check that lets you jump again.",
        blocks: [
          "yv (vertical velocity) — Variables",
          "change yv by -1 (gravity) — Operators",
          "if touching ground? then set yv to 0 — Sensing/Control"
        ],
        objective: "Build a jump with gravity that stops on the ground.",
        warmup: "Jump on the spot. You shoot up, slow, stop at the top, then fall faster and faster. That deceleration-then-acceleration IS gravity.",
        exercises: [
          { t: "Gravity", d: "'forever → change yv by -1 → change y by yv'. The sprite falls faster and faster." },
          { t: "Ground stop", d: "'if touching ground? then set yv to 0 and sit on top'. Now it lands." },
          { t: "Jump", d: "'if key up pressed? and on ground then set yv to 14'. A satisfying hop." }
        ],
        project: {
          title: "Jump Test",
          brief: "A character on a ground platform that falls with gravity and jumps with the up key — the core of every platformer.",
          must: ["gravity via yv", "land on ground", "jump only when grounded"],
          stretch: "Tune jump height and gravity until the jump feels like Mario's."
        },
        challenge: "Add a double-jump (allow one extra jump in the air).",
        vocab: ["gravity", "vertical velocity", "grounded"],
        checklist: ["My sprite falls with gravity", "It lands on the ground", "It jumps only when grounded"]
      },
      {
        module: "Level Up: Advanced Motion",
        title: "Smooth Character Control",
        emoji: "🎮",
        theme: "Platformer physics",
        minutes: 60,
        concept: "Combine horizontal velocity + gravity into a controller that runs and jumps with real game feel.",
        blocks: [
          "xv & yv together — Variables",
          "friction + gravity — Operators",
          "if key left/right/up — Sensing/Control"
        ],
        objective: "Build a run-and-jump controller with acceleration, friction, and gravity.",
        warmup: "List what makes Mario feel good: a little slide when you stop, a jump you can steer mid-air. We're coding those exact feelings.",
        exercises: [
          { t: "Run with velocity", d: "Left/right change xv; apply friction; 'change x by xv'." },
          { t: "Jump with gravity", d: "Add the gravity + ground + jump from last session using yv." },
          { t: "Air control", d: "Allow left/right to work in the air too, so you can steer your jumps." }
        ],
        project: {
          title: "Platformer Controller",
          brief: "A reusable run-and-jump character with acceleration, friction, gravity, and air control — the base for your platformer.",
          must: ["horizontal velocity + friction", "gravity + jump", "air steering"],
          stretch: "Add coyote time (a few frames where you can still jump just after leaving a ledge)."
        },
        challenge: "Add variable jump height: tap = small hop, hold = full jump.",
        vocab: ["controller", "air control", "coyote time"],
        checklist: ["My character runs with velocity", "It jumps with gravity", "I can steer in the air"]
      },
      {
        module: "Level Up: Advanced Motion",
        title: "Scrolling Worlds",
        emoji: "🗺️",
        theme: "Bigger levels",
        minutes: 60,
        concept: "A scrolling camera lets levels be bigger than the screen: the player stays put and the WORLD moves.",
        blocks: [
          "scrollX variable — Variables",
          "set x to (my level x - scrollX) — Operators",
          "change scrollX by (player speed)"
        ],
        objective: "Build a simple side-scrolling camera so the level extends beyond one screen.",
        warmup: "Side-scroller trick: in Mario, Mario stays near the middle and the pipes slide past him. The camera is a lie we tell with math.",
        exercises: [
          { t: "Camera variable", d: "Make 'scrollX'. When the player walks right, 'change scrollX by (speed)'." },
          { t: "Move the world", d: "Each scenery sprite: 'set x to (its world position - scrollX)'. Now scenery slides as scrollX changes." },
          { t: "Keep player centred", d: "Leave the player near the middle; only scrollX changes as they 'walk'." }
        ],
        project: {
          title: "Scrolling Ground",
          brief: "A ground and a few landmarks that scroll past as the player walks right, making the level feel long.",
          must: ["scrollX variable", "scenery positioned by scrollX", "player stays centred"],
          stretch: "Add a parallax background layer that scrolls slower for depth."
        },
        challenge: "Add vertical scrolling too (scrollY) for a tall level.",
        vocab: ["camera", "scroll", "parallax"],
        checklist: ["I have a scrollX camera", "Scenery scrolls with the camera", "The player stays centred"]
      },
      {
        module: "Level Up: Advanced Motion",
        title: "Mini Project — Feel Lab",
        emoji: "🧪",
        theme: "Game feel",
        minutes: 60,
        concept: "Great games live or die on 'feel'. Combine velocity, gravity, and easing and tune them until movement is a joy.",
        blocks: ["velocity", "gravity", "easing", "friction"],
        objective: "Build a movement playground and tune it to feel excellent.",
        warmup: "Two clips of the same jump, different gravity numbers. Which feels better? You can't calculate feel — you tune it.",
        exercises: [
          { t: "Assemble", d: "Put your run-jump controller on a scrolling ground with an easing camera." },
          { t: "Tune", d: "Make sliders (variables shown on Stage) for gravity, jump, and friction. Change them live and feel the difference." },
          { t: "Pick your favourite", d: "Lock in the numbers that feel best and write them down — this is YOUR game's feel." }
        ],
        project: {
          title: "Feel Lab",
          brief: "A tunable movement demo where you can adjust gravity, jump, and friction live and find the feel you love.",
          must: ["combined velocity + gravity + easing", "live-tunable variables", "your chosen final numbers"],
          stretch: "Add a 'reset to defaults' button."
        },
        challenge: "Share two feel presets ('floaty moon' and 'heavy tank') the player can switch between.",
        vocab: ["game feel", "tuning", "preset"],
        checklist: ["I combined the advanced motion tools", "I tuned movement live", "I chose numbers that feel great"]
      },

      /* ---------- MODULE B: Clones — Many at Once (7–13) ---------- */
      {
        module: "Clones — Many at Once",
        title: "Clones — What & Why",
        emoji: "👥",
        theme: "Core power",
        minutes: 60,
        concept: "A clone is a live copy of a sprite that runs its own code. Clones let you have hundreds of bullets, enemies, or coins from ONE sprite.",
        blocks: [
          "create clone of [myself] — Control",
          "when I start as a clone — Control",
          "delete this clone — Control"
        ],
        objective: "Create clones and give them their own behaviour.",
        warmup: "A photocopier: one page in, many identical copies out — and each copy can then be marked up differently. That's a clone.",
        exercises: [
          { t: "Make clones", d: "'when green flag → repeat 10 [ create clone of myself → wait 0.2 ]'. Ten copies appear." },
          { t: "Clone behaviour", d: "'when I start as a clone → go to a random spot → forever move'. Each clone acts on its own." },
          { t: "Clean up", d: "'when I start as a clone → ... → delete this clone' when it's done, so clones don't pile up." }
        ],
        project: {
          title: "Rain",
          brief: "One raindrop sprite that spawns clones falling from random x at the top, each deleting itself at the bottom.",
          must: ["create clone", "when I start as a clone", "delete this clone"],
          stretch: "Add splashes: a clone switches to a splash costume for a moment before deleting."
        },
        challenge: "Make a starfield: clones as stars drifting at different speeds.",
        vocab: ["clone", "instance", "spawn"],
        checklist: ["I can create clones", "Each clone runs its own code", "I delete clones to clean up"]
      },
      {
        module: "Clones — Many at Once",
        title: "Clones for Projectiles",
        emoji: "🔫",
        theme: "Shooters",
        minutes: 60,
        concept: "Every bullet in a shooter is a clone: spawned at the player, flying straight, deleted when it leaves or hits.",
        blocks: [
          "create clone of myself (on shoot) — Control",
          "when I start as a clone → point + move — Control/Motion",
          "if touching edge/enemy → delete this clone"
        ],
        objective: "Fire bullets as clones that travel and disappear correctly.",
        warmup: "Why clones for bullets? You might fire 50 shots. One sprite can't be in 50 places — but 50 clones can.",
        exercises: [
          { t: "Fire on space", d: "Player/bullet sprite: 'when space pressed → create clone of myself'." },
          { t: "Fly", d: "'when I start as a clone → go to player → point up → repeat until edge [ move 15 ]'." },
          { t: "Despawn", d: "'... → delete this clone' at the edge so bullets don't linger." }
        ],
        project: {
          title: "Blaster",
          brief: "A player that fires a stream of bullet-clones upward that vanish at the top of the screen.",
          must: ["clone on shoot", "clone travels", "clone deletes at edge"],
          stretch: "Add a fire-rate limit (a short cooldown) so you can't spam infinitely."
        },
        challenge: "Fire in the direction the player is aiming (towards the mouse).",
        vocab: ["projectile", "cooldown", "despawn"],
        checklist: ["I fire bullets as clones", "Bullets travel from the player", "Bullets delete when done"]
      },
      {
        module: "Clones — Many at Once",
        title: "Clones for Enemies",
        emoji: "👾",
        theme: "Shooters",
        minutes: 60,
        concept: "Waves of enemies are clones that spawn over time and move on their own — the challenge of any action game.",
        blocks: [
          "repeat / forever → create clone (spawner) — Control",
          "when I start as a clone → move / target player — Motion",
          "if touching bullet? → delete this clone (+score)"
        ],
        objective: "Spawn enemy clones that move and can be destroyed.",
        warmup: "Space Invaders: rows of aliens, all the same, all marching. Perfect job for clones.",
        exercises: [
          { t: "Spawn a wave", d: "'forever → wait 1 → create clone of myself' drops a steady stream of enemies." },
          { t: "Enemy movement", d: "'when I start as a clone → go to top at random x → repeat until edge [ change y by -3 ]'." },
          { t: "Destroy on hit", d: "'if touching bullet? then change score by 1 → delete this clone'." }
        ],
        project: {
          title: "Invasion",
          brief: "Enemy clones descend from the top; your bullets destroy them and score points.",
          must: ["enemy spawner", "enemy clone movement", "destroy on bullet hit + score"],
          stretch: "Make enemies also hurt the player on touch (lose a life)."
        },
        challenge: "Increase spawn rate as the score climbs (harder over time).",
        vocab: ["wave", "spawner", "enemy"],
        checklist: ["I spawn enemy clones", "Enemies move on their own", "Bullets destroy enemies and score"]
      },
      {
        module: "Clones — Many at Once",
        title: "Clones for Particles & Effects",
        emoji: "✨",
        theme: "Game feel",
        minutes: 60,
        concept: "Explosions, sparkles, and dust are bursts of short-lived clones. Particles make a game feel juicy.",
        blocks: [
          "repeat (burst count) → create clone — Control",
          "when I start as a clone → point in random direction → move + fade — Motion/Looks",
          "delete this clone (when faded)"
        ],
        objective: "Create a particle burst effect from clones.",
        warmup: "Fireworks: one launch, a burst of sparks flying outward and fading. That's a particle system.",
        exercises: [
          { t: "Burst", d: "On a trigger: 'repeat 12 → create clone of myself'." },
          { t: "Scatter & fade", d: "'when I start as a clone → point in direction (pick random 0 to 360) → repeat 10 [ move 6 → change ghost by 10 ] → delete this clone'." },
          { t: "Trigger it", d: "Fire the burst when an enemy is destroyed or a coin is collected." }
        ],
        project: {
          title: "Juice It",
          brief: "Add a particle burst whenever something is collected or destroyed in one of your earlier games.",
          must: ["clone burst", "scatter + fade + delete", "triggered by a game event"],
          stretch: "Colour the particles to match what was destroyed."
        },
        challenge: "Add a continuous trail of particles behind a moving sprite (rocket exhaust).",
        vocab: ["particle", "burst", "juice"],
        checklist: ["I can make a particle burst", "Particles scatter and fade", "I triggered particles on a game event"]
      },
      {
        module: "Clones — Many at Once",
        title: "Managing Many Clones",
        emoji: "🧹",
        theme: "Performance",
        minutes: 60,
        concept: "Scratch limits clones (~300). Delete them when done, and use a counter so you never spawn too many at once.",
        blocks: [
          "delete this clone — Control",
          "a 'clone count' variable — Variables",
          "if (clone count < max) then create clone"
        ],
        objective: "Keep clone counts under control so games stay fast and don't hit the limit.",
        warmup: "A room fills with balloons that never pop — soon you can't move. Clones you never delete do the same to your game.",
        exercises: [
          { t: "Count them", d: "Increase 'clone count' when creating, decrease when deleting. Watch it on the Stage." },
          { t: "Cap the count", d: "'if clone count < 50 then create clone' — never overflow." },
          { t: "Always delete", d: "Make sure EVERY clone path ends in 'delete this clone'." }
        ],
        project: {
          title: "Clone Budget",
          brief: "Take a clone-heavy game and add a live clone counter and a cap so it never lags or hits the limit.",
          must: ["clone count variable", "cap check before creating", "reliable deletion"],
          stretch: "Show a warning when you're near the cap."
        },
        challenge: "Pool clones: instead of deleting, hide-and-reuse them (advanced!).",
        vocab: ["clone limit", "counter", "cleanup"],
        checklist: ["I count my clones", "I cap how many can exist", "Every clone deletes itself when done"]
      },
      {
        module: "Clones — Many at Once",
        title: "Clone Variables & Communication",
        emoji: "🔗",
        theme: "Advanced clones",
        minutes: 60,
        concept: "'For this sprite only' variables give each clone its own private data (its speed, its type). Broadcasts let them all react together.",
        blocks: [
          "variables 'for this sprite only' — Variables",
          "when I start as a clone (set private vars) — Control",
          "broadcast / when I receive — Events"
        ],
        objective: "Give clones individual properties and coordinate them with broadcasts.",
        warmup: "A class of students: same 'sprite', but each has their own name and speed (private variables), and all react to the bell (broadcast).",
        exercises: [
          { t: "Private speed", d: "Make a 'for this sprite only' variable 'myspeed'. Each clone: 'set myspeed to (pick random 2 to 6)'. Clones now move at their own speeds." },
          { t: "Types", d: "Give each clone a 'type' (1=fast/2=slow) and switch costume/behaviour to match." },
          { t: "All react", d: "'broadcast freeze' → 'when I receive freeze → stop moving' affects every clone at once." }
        ],
        project: {
          title: "Mixed Swarm",
          brief: "A swarm of clones each with its own random speed and type, that all freeze when you broadcast 'freeze'.",
          must: ["'for this sprite only' variable", "per-clone behaviour", "broadcast that affects all clones"],
          stretch: "Add a 'time freeze' power that pauses only enemy clones."
        },
        challenge: "Make a boss that broadcasts 'attack' and all its minion clones fire at once.",
        vocab: ["local variable", "per-clone data", "coordination"],
        checklist: ["Each clone has private data", "Clones behave individually", "I can command all clones with a broadcast"]
      },
      {
        module: "Clones — Many at Once",
        title: "Mini Project — Space Shooter",
        emoji: "🚀",
        theme: "Galaga / Space Invaders",
        minutes: 60,
        concept: "Combine bullet clones, enemy clones, and particle clones into a complete arcade shooter.",
        blocks: ["clones (bullets, enemies, particles)", "score & lives", "collision", "waves"],
        objective: "Build a full space shooter with waves, scoring, and lives.",
        warmup: "Break a shooter into parts: ship (you), bullets (clones), enemies (clones), explosions (clones), score & lives. You have all of them now.",
        exercises: [
          { t: "Assemble", d: "Player ship (velocity movement) + bullet clones (fire on space) + enemy clones (waves)." },
          { t: "Rules", d: "Bullet hits enemy → explosion particles + score. Enemy hits player → lose a life." },
          { t: "End states", d: "Game over at 0 lives; consider a boss or a win at a score target." }
        ],
        project: {
          title: "Star Blaster",
          brief: "A complete shooter: move, shoot enemy waves, score, take damage, explode enemies, and game-over at 0 lives.",
          must: ["ship movement", "bullet + enemy clones", "score + lives", "explosions", "game over"],
          stretch: "Add a boss enemy with lots of health after wave 5."
        },
        challenge: "Add power-ups (a clone you catch that upgrades your fire rate).",
        vocab: ["shooter", "wave", "boss"],
        checklist: ["I combined bullet, enemy, and particle clones", "It has score and lives", "It has clear win/lose states"]
      },

      /* ---------- MODULE C: Lists & Data (14–20) ---------- */
      {
        module: "Lists & Data",
        title: "Lists — Many Values in One Place",
        emoji: "📋",
        theme: "Core concept",
        minutes: 60,
        concept: "A list is a variable that holds MANY values in order — like a numbered shopping list the program can read and change.",
        blocks: [
          "Make a List — Variables",
          "add () to () — Variables",
          "item () of () / length of () — Variables"
        ],
        objective: "Create a list, add items, and read items by position.",
        warmup: "A real numbered list on the board: item 1, item 2, item 3. A Scratch list is exactly this — each slot has a number.",
        exercises: [
          { t: "Make a list", d: "Variables → 'Make a List' → name it 'inventory'. Tick it to show on the Stage." },
          { t: "Add items", d: "'add sword to inventory', 'add shield to inventory'. See them appear numbered." },
          { t: "Read an item", d: "'say (item 1 of inventory)'. Try 'length of inventory' to count items." }
        ],
        project: {
          title: "My Top 5",
          brief: "Ask the player for their 5 favourite games and store them in a list, then read them back.",
          must: ["a list", "add (from answer)", "read items back with a loop or item-of"],
          stretch: "Say them as a ranked countdown from 5 to 1."
        },
        challenge: "Show a random item: 'item (pick random 1 to length) of list'.",
        vocab: ["list", "item", "index"],
        checklist: ["I can make a list", "I can add items", "I can read an item by its number"]
      },
      {
        module: "Lists & Data",
        title: "Inventory System",
        emoji: "🎒",
        theme: "Minecraft",
        minutes: 60,
        concept: "Games use lists for inventories: pick something up and it's added; use it and it's removed.",
        blocks: [
          "add (item) to inventory — Variables",
          "delete (n) of inventory — Variables",
          "item (n) of inventory / length — Variables"
        ],
        objective: "Build a working pick-up-and-use inventory with a list.",
        warmup: "Empty your (pretend) backpack: each item comes out one at a time. Adding and removing from a list works the same way.",
        exercises: [
          { t: "Pick up", d: "Touch an item sprite → 'add its name to inventory' → hide the item." },
          { t: "Show it", d: "Display the inventory list on the Stage so the player sees what they carry." },
          { t: "Use/drop", d: "A button that 'delete 1 of inventory' (use the first item) — watch the list shrink." }
        ],
        project: {
          title: "Backpack",
          brief: "Walk around collecting item sprites into a visible inventory list you can add to and remove from.",
          must: ["inventory list", "add on pickup", "delete on use", "list shown on Stage"],
          stretch: "Prevent duplicates, or cap the inventory at a max size."
        },
        challenge: "Add a 'crafting' rule: if the inventory contains wood AND string, add a 'bow'.",
        vocab: ["inventory", "add/remove", "crafting"],
        checklist: ["I add items to an inventory list", "I remove items when used", "The inventory shows on screen"]
      },
      {
        module: "Lists & Data",
        title: "High-Score Table",
        emoji: "🥇",
        theme: "Every game",
        minutes: 60,
        concept: "A leaderboard is a list of scores you add to, then sort or scan to find the best.",
        blocks: [
          "add (score) to scores — Variables",
          "loop through the list to find the max — Control/Variables",
          "ask & join (for player names) — Sensing/Operators"
        ],
        objective: "Store scores in a list and find/display the top score.",
        warmup: "Arcade high-score screen: three initials and a number, ranked. It's just a sorted list.",
        exercises: [
          { t: "Record scores", d: "At game over: 'add score to scores'." },
          { t: "Find the best", d: "Loop through the list keeping the biggest value in a 'best' variable." },
          { t: "Name it", d: "Ask for the player's name and store 'name: score' with a join." }
        ],
        project: {
          title: "Leaderboard",
          brief: "After each game, record the score with the player's name and display the top 3.",
          must: ["scores list", "add name+score", "find/show the top score(s)"],
          stretch: "Keep only the top 5 (delete the lowest when the list gets too long)."
        },
        challenge: "Sort the whole list from highest to lowest (a real sorting algorithm — a great challenge!).",
        vocab: ["leaderboard", "max", "sort"],
        checklist: ["I store scores in a list", "I can find the highest score", "I display a leaderboard"]
      },
      {
        module: "Lists & Data",
        title: "Quiz & Question Banks",
        emoji: "🧠",
        theme: "Quiz games",
        minutes: 60,
        concept: "Store questions in one list and answers in a matching list; use the same index to pair them.",
        blocks: [
          "two matching lists (questions, answers)",
          "item (i) of questions / item (i) of answers",
          "ask & answer, = comparison — Sensing/Operators"
        ],
        objective: "Build a data-driven quiz where questions come from a list.",
        warmup: "Flashcards: question on the front, answer on the back, matched by being the SAME card. Two lists, same index.",
        exercises: [
          { t: "Two lists", d: "'questions' and 'answers'. Add matching pairs so item 1 of each go together." },
          { t: "Ask by index", d: "Loop i from 1 to length: 'ask (item i of questions)', check against 'item i of answers'." },
          { t: "Score it", d: "Add 1 to score for each correct answer; show the total at the end." }
        ],
        project: {
          title: "Quiz Master",
          brief: "A quiz that pulls questions and answers from lists, scores the player, and shows a final result.",
          must: ["matching question/answer lists", "loop through by index", "scoring + result"],
          stretch: "Shuffle the order so the quiz differs each time."
        },
        challenge: "Add a lives system: three wrong answers ends the quiz early.",
        vocab: ["parallel lists", "index matching", "data-driven"],
        checklist: ["I store questions and answers in lists", "I match them by index", "The quiz scores and ends properly"]
      },
      {
        module: "Lists & Data",
        title: "Searching & Editing Lists",
        emoji: "🔎",
        theme: "Core concept",
        minutes: 60,
        concept: "Find, insert, replace, and remove specific items — the operations behind saving, editing, and searching data.",
        blocks: [
          "insert () at () — Variables",
          "replace item () of () with () — Variables",
          "item # of () in () (find) — Variables",
          "() contains ()? — Variables"
        ],
        objective: "Use the full set of list operations to search and edit data.",
        warmup: "Editing a class list: cross one name out (delete), squeeze one in (insert), fix a spelling (replace), 'is Sam on the list?' (contains).",
        exercises: [
          { t: "Contains & find", d: "'if inventory contains apple? then say (item # of apple in inventory)'." },
          { t: "Insert & replace", d: "'insert gold at 1' (top of the list); 'replace item 2 with silver'." },
          { t: "Delete a match", d: "Find an item's position, then 'delete (that number) of the list'." }
        ],
        project: {
          title: "To-Do Manager",
          brief: "A little app: add tasks, mark one done (delete it), insert an urgent task at the top, and check if a task exists.",
          must: ["add", "insert at", "delete a found item", "contains?"],
          stretch: "Replace a task's text to 'edit' it."
        },
        challenge: "Prevent duplicate entries using 'contains?' before adding.",
        vocab: ["insert", "replace", "search"],
        checklist: ["I can search a list", "I can insert and replace items", "I can delete a specific matched item"]
      },
      {
        module: "Lists & Data",
        title: "Lists + Loops = Power",
        emoji: "🔁",
        theme: "Core concept",
        minutes: 60,
        concept: "Looping through a list (index 1 to length) lets you process every item — the pattern behind almost all data work.",
        blocks: [
          "set i to 1 → repeat (length) [ ... item i ... → change i by 1 ] — Control/Variables",
          "sum / count / max while looping — Operators"
        ],
        objective: "Iterate over a list to compute totals and transform every item.",
        warmup: "Register call: go down the class list name by name, ticking each. That's iterating — visit every item in order.",
        exercises: [
          { t: "Iterate", d: "'set i to 1 → repeat (length of scores) [ say (item i of scores) → change i by 1 ]'." },
          { t: "Total", d: "Add each item to a 'total' variable as you loop — get the sum of a list." },
          { t: "Transform", d: "Loop and 'replace item i with (item i × 2)' to double every value." }
        ],
        project: {
          title: "Stats Machine",
          brief: "Given a list of numbers, compute and show the total, the average, and the biggest by looping through it.",
          must: ["index loop", "running total", "max while looping"],
          stretch: "Also count how many items are above the average."
        },
        challenge: "Draw a bar chart of the list using the pen (one bar per item).",
        vocab: ["iterate", "accumulate", "transform"],
        checklist: ["I can loop through a whole list", "I computed a total/average", "I transformed every item"]
      },
      {
        module: "Lists & Data",
        title: "Mini Project — Save System",
        emoji: "💾",
        theme: "RPG / Minecraft",
        minutes: 60,
        concept: "Combine variables + lists into a save/load system so a game remembers the player's progress.",
        blocks: ["lists for saved data", "join to encode", "ask/answer or cloud (concept) to persist"],
        objective: "Build a simple save-and-load feature for a game.",
        warmup: "Why saving matters: no one wants to restart a big Minecraft world every time. Games remember with data.",
        exercises: [
          { t: "Gather state", d: "Collect what to save (score, level, inventory) into a 'save' list." },
          { t: "Show a save code", d: "Join the save list into one text string the player can copy — their 'save code'." },
          { t: "Load", d: "Ask for a save code, split it back out, and restore the variables/list." }
        ],
        project: {
          title: "Save & Load",
          brief: "A game that can output a save code and later restore progress from it.",
          must: ["collect state into a list", "produce a save code (join)", "restore from a code"],
          stretch: "Add a checksum digit so bad codes are rejected."
        },
        challenge: "Auto-save the high-score list so it survives (discuss cloud variables and their limits).",
        vocab: ["save/load", "serialize", "persistence"],
        checklist: ["I gathered game state into data", "I created a save code", "I can restore from it"]
      },

      /* ---------- MODULE D: Custom Blocks & Clean Code (21–27) ---------- */
      {
        module: "Custom Blocks & Clean Code",
        title: "Custom Blocks (My Blocks)",
        emoji: "🧩",
        theme: "Core concept",
        minutes: 60,
        concept: "A custom block is your OWN block: name a group of steps once, then use it anywhere. It's how pros keep code tidy.",
        blocks: [
          "Make a Block — My Blocks",
          "define (your block) — My Blocks",
          "calling your block by name"
        ],
        objective: "Create a custom block that packages several steps under one name.",
        warmup: "'Get ready for school' means: brush teeth, dress, pack bag. One name, many steps. That's a custom block.",
        exercises: [
          { t: "Make one", d: "My Blocks → 'Make a Block' → name it 'reset game'. It appears with a 'define' hat." },
          { t: "Define it", d: "Under 'define reset game', put: set score to 0, set lives to 3, go to start." },
          { t: "Use it", d: "Now 'reset game' is one block you drop wherever you need a reset. Cleaner instantly." }
        ],
        project: {
          title: "Tidy-Up",
          brief: "Take a messy earlier game and replace a repeated group of blocks with a well-named custom block.",
          must: ["a custom block", "a clear define", "the block used in 2+ places"],
          stretch: "Make a second custom block (e.g. 'game over')."
        },
        challenge: "Turn your whole game-start into custom blocks: setup, spawn, ready.",
        vocab: ["custom block", "define", "abstraction"],
        checklist: ["I made a custom block", "I defined its steps", "I used it in more than one place"]
      },
      {
        module: "Custom Blocks & Clean Code",
        title: "Custom Blocks with Inputs",
        emoji: "🎛️",
        theme: "Core concept",
        minutes: 60,
        concept: "Inputs (parameters) make a custom block flexible: 'jump (height)' or 'spawn enemy at (x)'. One block, many uses.",
        blocks: [
          "Make a Block → add an input — My Blocks",
          "using the input inside the define",
          "calling the block with different values"
        ],
        objective: "Create a custom block that takes inputs and behaves differently based on them.",
        warmup: "'Draw a square of size ___'. The size is the input. One instruction, any size you like.",
        exercises: [
          { t: "Add an input", d: "Make a block 'square (size)' with a number input. In the define: 'repeat 4 [ move (size) → turn 90 ]'." },
          { t: "Call it", d: "Use 'square 50' then 'square 120'. Same block, different squares." },
          { t: "Two inputs", d: "Make 'say (text) (times)' that repeats a message — mix a text and a number input." }
        ],
        project: {
          title: "Shape Kit",
          brief: "A 'polygon (sides) (size)' custom block that can draw any regular shape, used to draw several shapes.",
          must: ["a block with 2 inputs", "inputs used in the define", "called with different values"],
          stretch: "Add a 'colour' input and change the pen colour per shape."
        },
        challenge: "Make a 'spawn enemy at (x) (speed)' block for your shooter.",
        vocab: ["input", "parameter", "reusable"],
        checklist: ["I added inputs to a custom block", "I used inputs inside the definition", "I called it with different values"]
      },
      {
        module: "Custom Blocks & Clean Code",
        title: "Thinking in Functions",
        emoji: "⚙️",
        theme: "Real programming",
        minutes: 60,
        concept: "Custom blocks are 'functions' — the building blocks of ALL real programming languages. Breaking a big job into small named functions is the core skill.",
        blocks: [
          "several small custom blocks working together",
          "a 'main' script that calls them in order"
        ],
        objective: "Decompose a program into several small functions and orchestrate them.",
        warmup: "A recipe has sub-recipes: 'make the sauce', 'cook the pasta', 'combine'. Each is a function; the recipe calls them in order.",
        exercises: [
          { t: "Break it down", d: "Take a game and list its jobs: setup, spawn, handle input, check collisions, draw HUD." },
          { t: "One block each", d: "Make a custom block for each job." },
          { t: "Main loop", d: "A short main script: 'setup → forever [ handle input, spawn, check collisions ]'. Readable at a glance." }
        ],
        project: {
          title: "Function Refactor",
          brief: "Rebuild one of your games so the main script is just a handful of well-named custom-block calls.",
          must: ["3+ custom blocks", "a short readable main script", "same behaviour as before"],
          stretch: "Have one function call another (functions using functions)."
        },
        challenge: "Explain your main script to a partner using only the block names — if it reads like English, you nailed it.",
        vocab: ["function", "decomposition", "main loop"],
        checklist: ["I broke a program into functions", "My main script is short and readable", "The functions work together"]
      },
      {
        module: "Custom Blocks & Clean Code",
        title: "Recursion (Just for Fun)",
        emoji: "🌀",
        theme: "Mind-bending",
        minutes: 60,
        concept: "A custom block that calls ITSELF is 'recursion'. It makes gorgeous patterns like fractal trees and spirals.",
        blocks: [
          "a custom block that calls itself — My Blocks",
          "a 'stop' condition (so it doesn't run forever)",
          "pen blocks — Pen"
        ],
        objective: "Use recursion to draw a simple fractal.",
        warmup: "Two mirrors facing each other: reflections inside reflections inside reflections. That endless nesting is recursion.",
        exercises: [
          { t: "Countdown", d: "Make 'countdown (n)': if n > 0 → say n → countdown (n-1). It calls itself with a smaller number." },
          { t: "Stop condition", d: "Notice the 'if n > 0' — without it, recursion never stops. The stop condition is essential." },
          { t: "Fractal branch", d: "'branch (length)': if length > 5 → draw a line, turn, branch(length×0.7), turn back, branch(length×0.7). A tree!" }
        ],
        project: {
          title: "Fractal Tree",
          brief: "A recursive custom block that draws a branching tree with the pen.",
          must: ["a self-calling custom block", "a stop condition", "pen drawing"],
          stretch: "Add slight randomness to branch angles for a natural tree."
        },
        challenge: "Draw a Koch snowflake or a recursive spiral.",
        vocab: ["recursion", "base case", "fractal"],
        checklist: ["I made a block that calls itself", "I included a stop condition", "I drew a recursive pattern"]
      },
      {
        module: "Custom Blocks & Clean Code",
        title: "Organising a Big Project",
        emoji: "🗂️",
        theme: "Pro skills",
        minutes: 60,
        concept: "Big projects need order: name things clearly, group scripts, comment your code, and split work across sprites sensibly.",
        blocks: [
          "comments (right-click → Add Comment)",
          "clear variable/sprite/message names",
          "one job per sprite where possible"
        ],
        objective: "Apply organisation habits that keep a large project understandable.",
        warmup: "A messy vs tidy bedroom: finding your football boots. Tidy code is finding the bug in seconds, not an hour.",
        exercises: [
          { t: "Rename", d: "Rename vague names ('sprite4', 'var1') to meaningful ones ('player', 'score')." },
          { t: "Comment", d: "Add short comments explaining any tricky script: WHY it exists, not just what." },
          { t: "Group", d: "Lay scripts out in tidy columns by job (input, movement, collisions). Right-click → Clean Up Blocks." }
        ],
        project: {
          title: "Project Cleanup",
          brief: "Take your biggest project and make it readable: clear names, comments, tidy layout, sensible sprite roles.",
          must: ["clear names", "helpful comments", "tidy layout"],
          stretch: "Write a one-paragraph 'how it works' note as a Stage comment."
        },
        challenge: "Give your project to a partner cold — can they understand it without you explaining?",
        vocab: ["naming", "comments", "organisation"],
        checklist: ["I renamed things clearly", "I commented tricky code", "My scripts are tidy and grouped"]
      },
      {
        module: "Custom Blocks & Clean Code",
        title: "Debugging Big Projects",
        emoji: "🐞",
        theme: "Pro skills",
        minutes: 60,
        concept: "Debugging a big game is detective work: reproduce the bug, narrow down where it is, change one thing, test.",
        blocks: [
          "say / show a variable to trace values",
          "isolate a script (test it alone)",
          "change one thing → test → repeat"
        ],
        objective: "Use a systematic debugging process on a real bug.",
        warmup: "A detective doesn't guess randomly — they gather clues and narrow suspects. Debugging is the same.",
        exercises: [
          { t: "Reproduce", d: "Make the bug happen ON PURPOSE, reliably. A bug you can't reproduce you can't fix." },
          { t: "Trace", d: "Add temporary 'say (variable)' blocks to watch values, or show variables on the Stage." },
          { t: "Bisect", d: "Disable half the code (drag it aside). Bug gone? It's in that half. Repeat to zero in." }
        ],
        project: {
          title: "Bug Hunt",
          brief: "Fix a deliberately-buggy game (teacher-provided or a partner's) using reproduce → trace → bisect → fix.",
          must: ["reproduce the bug", "trace with variables/say", "narrow it down", "a verified fix"],
          stretch: "Write down the bug, the cause, and the fix — a real bug report."
        },
        challenge: "Plant a subtle bug in your own game for a partner to find.",
        vocab: ["reproduce", "trace", "bisect"],
        checklist: ["I can reproduce a bug on purpose", "I trace values to find it", "I fix one thing at a time"]
      },
      {
        module: "Custom Blocks & Clean Code",
        title: "Mini Project — Rebuild It Right",
        emoji: "♻️",
        theme: "Craft",
        minutes: 60,
        concept: "Take a scrappy Level 1 game and rebuild it with everything you now know: functions, clean names, comments, good structure.",
        blocks: ["custom blocks", "clean structure", "comments", "your best motion/collision"],
        objective: "Produce a professional-quality version of an earlier project.",
        warmup: "Version 2 of anything is better because you know what you're building. Pick a Level 1 game to remaster.",
        exercises: [
          { t: "Plan the structure", d: "Before coding, list the custom blocks and sprites you'll use." },
          { t: "Build clean", d: "Rebuild with functions, clear names, and comments from the start (don't just tidy the old mess)." },
          { t: "Compare", d: "Put v1 and v2 side by side. Note what's clearer and what plays better." }
        ],
        project: {
          title: "Remaster",
          brief: "A clean, function-based rebuild of an earlier game that plays better and reads clearly.",
          must: ["custom blocks", "clean names + comments", "improved gameplay"],
          stretch: "Add one new feature the original couldn't easily support."
        },
        challenge: "Write release notes: 'What's new in v2'.",
        vocab: ["refactor", "remaster", "craft"],
        checklist: ["I planned the structure first", "I built it clean with functions", "v2 is clearly better than v1"]
      },

      /* ---------- MODULE E: Game Genres Deep Dive (28–39) ---------- */
      {
        module: "Game Genres Deep Dive",
        title: "Platformer 1 — Physics",
        emoji: "🍄",
        theme: "Super Mario / Roblox obby",
        minutes: 60,
        concept: "Start the big platformer build. Session 1: rock-solid run-and-jump physics on a single platform.",
        blocks: ["xv/yv velocity", "gravity", "jump when grounded", "friction"],
        objective: "Lay down tight platformer physics as the foundation of the build.",
        warmup: "Name the best-feeling jump you know (Mario? a Roblox obby?). We're chasing that exact feel over the next four sessions.",
        exercises: [
          { t: "Player physics", d: "Bring in your Module A run-jump controller (velocity + gravity + grounded jump)." },
          { t: "One platform", d: "Add a ground platform sprite; land on top, don't fall through." },
          { t: "Tune", d: "Dial in gravity, jump strength, and run speed until it feels great." }
        ],
        project: {
          title: "Platformer — Physics",
          brief: "A character with tuned run-and-jump physics standing on a ground platform.",
          must: ["velocity movement", "gravity + grounded jump", "landing on a platform"],
          stretch: "Add variable jump height (hold to jump higher)."
        },
        challenge: "Add wall-slide: slow the fall when pressing into a wall.",
        vocab: ["platformer", "physics", "grounded"],
        checklist: ["My platformer physics feel tight", "I land on a platform", "I tuned the jump"]
      },
      {
        module: "Game Genres Deep Dive",
        title: "Platformer 2 — Platforms & Collision",
        emoji: "🧱",
        theme: "Super Mario / Roblox obby",
        minutes: 60,
        concept: "Multiple platforms need reliable collision: land on tops, bonk on bottoms, stop at sides.",
        blocks: ["touching platform color?", "resolve collision (push out)", "separate x and y checks"],
        objective: "Build multi-platform collision that behaves correctly from every direction.",
        warmup: "Think about a real ledge: you land on TOP but bonk your head on the BOTTOM. Good collision knows the difference.",
        exercises: [
          { t: "One wall colour", d: "Draw platforms in ONE colour so 'touching color?' catches them all." },
          { t: "Vertical resolve", d: "After moving in y: if touching platform, step back out and set yv to 0 (land or bonk)." },
          { t: "Horizontal resolve", d: "After moving in x: if touching platform, step back out (stop at the side)." }
        ],
        project: {
          title: "Platformer — Platforms",
          brief: "A level with several platforms you can jump between, with correct landing and side collisions.",
          must: ["multiple platforms (one colour)", "vertical collision resolve", "horizontal collision resolve"],
          stretch: "Add a moving platform you can ride."
        },
        challenge: "Add one-way platforms you can jump up through but land on.",
        vocab: ["collision resolution", "one-way platform", "push-out"],
        checklist: ["I have multiple platforms", "I land and bonk correctly", "I stop at platform sides"]
      },
      {
        module: "Game Genres Deep Dive",
        title: "Platformer 3 — Enemies, Coins & Hazards",
        emoji: "👹",
        theme: "Super Mario / Roblox obby",
        minutes: 60,
        concept: "Add the content that makes a platformer fun: coins to grab, enemies to dodge or stomp, hazards to avoid.",
        blocks: ["coin collect + score", "enemy patrol (clone or sprite)", "stomp vs get-hit logic", "hazard = lose a life"],
        objective: "Populate the level with coins, enemies, and hazards.",
        warmup: "Mario's rules: coins = good, Goombas = bad unless you stomp them, pits/lava = instant loss. Clear rules make fun games.",
        exercises: [
          { t: "Coins", d: "Coin sprites/clones: touch to collect + score + a particle sparkle." },
          { t: "Enemies", d: "An enemy that patrols back and forth; touching its side hurts you." },
          { t: "Stomp", d: "If you touch it while falling (yv < 0) from above, you defeat it and bounce; otherwise you take damage." }
        ],
        project: {
          title: "Platformer — Content",
          brief: "Your level with collectible coins, a patrolling enemy you can stomp, and a hazard that costs a life.",
          must: ["coins + score", "patrolling enemy", "stomp vs damage logic", "a hazard"],
          stretch: "Add a power-up that makes you temporarily invincible."
        },
        challenge: "Add an enemy that shoots (reuse your bullet clones).",
        vocab: ["patrol", "stomp", "hazard"],
        checklist: ["I added coins with scoring", "I have an enemy you can stomp", "Hazards cost a life"]
      },
      {
        module: "Game Genres Deep Dive",
        title: "Platformer 4 — Levels & Win",
        emoji: "🚩",
        theme: "Super Mario / Roblox obby",
        minutes: 60,
        concept: "Finish the platformer: multiple levels, a goal flag, a win screen, and a full game loop.",
        blocks: ["goal flag → next level", "switch backdrop per level", "lives + game over", "win screen"],
        objective: "Complete a multi-level platformer with win and lose states.",
        warmup: "A game is levels + a reason to keep going. Design your level order from easy to hard.",
        exercises: [
          { t: "Goal", d: "A flag at the level end: 'if touching flag? then broadcast next-level'." },
          { t: "Level layouts", d: "Use a backdrop (or platform layout) per level; reposition platforms/player on level change." },
          { t: "Win/lose", d: "Beat the last level → win screen. Lives at 0 → game over. Green flag resets everything." }
        ],
        project: {
          title: "Platformer — Complete",
          brief: "A 3-level platformer with coins, enemies, hazards, a goal flag, lives, and win/lose screens.",
          must: ["3 levels", "goal flag progression", "lives + game over", "win screen", "clean reset"],
          stretch: "Add a level-select or a checkpoint system."
        },
        challenge: "Add a timer and a 'coins collected' total on the win screen.",
        vocab: ["level progression", "goal", "game loop"],
        checklist: ["My platformer has multiple levels", "There's a goal and a win screen", "Lives and reset work correctly"]
      },
      {
        module: "Game Genres Deep Dive",
        title: "Top-Down Adventure 1 — World & Movement",
        emoji: "🧭",
        theme: "Zelda / Minecraft",
        minutes: 60,
        concept: "Top-down games (Zelda, Minecraft, Pokémon) view the world from above. Start with 8-direction movement and a world.",
        blocks: ["4/8-direction movement", "facing (up/down/left/right costumes)", "wall collision"],
        objective: "Build a top-down character moving around a walled world.",
        warmup: "Look down at a table-top map. Top-down games are that view. Movement is free in all directions, not just left-right.",
        exercises: [
          { t: "8-way move", d: "Combine x and y key movement so diagonals work; normalise so diagonal isn't faster." },
          { t: "Facing", d: "Switch costume to face the last direction moved (up/down/left/right)." },
          { t: "Walls", d: "Draw walls in one colour; block movement into them (push-out like the maze)." }
        ],
        project: {
          title: "Adventure — World",
          brief: "A top-down hero that walks a walled world in 8 directions and faces the way they move.",
          must: ["8-direction movement", "facing costumes", "wall collision"],
          stretch: "Add an idle vs walking animation."
        },
        challenge: "Normalise diagonal speed precisely so all directions move at the same pace.",
        vocab: ["top-down", "8-direction", "facing"],
        checklist: ["My hero moves in 8 directions", "It faces the way it moves", "Walls block movement"]
      },
      {
        module: "Game Genres Deep Dive",
        title: "Top-Down Adventure 2 — Rooms & Scrolling",
        emoji: "🚪",
        theme: "Zelda / Minecraft",
        minutes: 60,
        concept: "Bigger worlds use rooms (screen-by-screen, like classic Zelda) or scrolling (like Minecraft). Build one.",
        blocks: ["room = backdrop; door → switch backdrop + reposition", "OR scrollX/scrollY camera"],
        objective: "Expand the world into multiple connected rooms or a scrolling map.",
        warmup: "Two ways to make a world bigger than the screen: swap rooms at the doors (Zelda) or scroll the camera (Minecraft). Pick one.",
        exercises: [
          { t: "Doors (room method)", d: "Walk to a door edge → switch to that room's backdrop → place the hero at the matching entrance." },
          { t: "Or scroll (camera method)", d: "Use scrollX/scrollY so the map moves around a centred hero." },
          { t: "Keep it consistent", d: "Make sure walls line up with the new backdrop/room so the hero can't walk into scenery." }
        ],
        project: {
          title: "Adventure — Bigger World",
          brief: "A world of at least three connected rooms (or one scrolling map) the hero can explore.",
          must: ["3 rooms with doors OR a scrolling camera", "correct hero placement", "matching walls"],
          stretch: "Add a mini-map showing which room you're in."
        },
        challenge: "Make a locked door that only opens once you have a key item.",
        vocab: ["room", "scrolling", "world"],
        checklist: ["My world is bigger than one screen", "I can travel between areas", "Walls match each area"]
      },
      {
        module: "Game Genres Deep Dive",
        title: "Top-Down Adventure 3 — Items & Combat",
        emoji: "⚔️",
        theme: "Zelda / Minecraft",
        minutes: 60,
        concept: "Bring the world to life: collect items into an inventory, attack enemies, and gate progress behind items.",
        blocks: ["inventory list", "attack (hitbox / bullet clone)", "enemy health", "item-gated doors"],
        objective: "Add items, a simple combat system, and item-based progression.",
        warmup: "Zelda's loop: explore → fight → find an item → the item unlocks new areas → repeat. Design one such loop.",
        exercises: [
          { t: "Combat", d: "Space swings a sword (a brief hitbox) or fires a bolt (clone). Enemies lose health and are defeated at 0." },
          { t: "Items", d: "Pick up items into your inventory list (from Module C)." },
          { t: "Gate", d: "A door/enemy that only lets you past if the inventory contains the right item." }
        ],
        project: {
          title: "Adventure — Complete",
          brief: "A mini top-down adventure: explore rooms, fight enemies, collect an item, and use it to reach the goal.",
          must: ["combat with enemy health", "inventory pickups", "item-gated progression", "a goal"],
          stretch: "Add hearts (health) and a game-over."
        },
        challenge: "Add a boss room that needs the special item to win.",
        vocab: ["combat", "item gate", "progression loop"],
        checklist: ["I added combat", "I collect items to an inventory", "An item gates progress"]
      },
      {
        module: "Game Genres Deep Dive",
        title: "Endless Runner 1 — Core Loop",
        emoji: "🏃‍♂️",
        theme: "Subway Surfers / Geometry Dash",
        minutes: 60,
        concept: "Endless runners auto-run forever; the player only dodges. Build the auto-run + jump/lane core.",
        blocks: ["auto-scrolling ground/obstacles (clones)", "jump or lane-switch", "distance score"],
        objective: "Build the endless-runner core loop: always moving, dodge to survive.",
        warmup: "Geometry Dash: you don't move forward — the world rushes at you and you just jump at the right moment. Simple and gripping.",
        exercises: [
          { t: "Auto-run", d: "Obstacles are clones spawning at the right and scrolling left at a set speed (the 'running')." },
          { t: "Dodge", d: "Player jumps (platformer physics) or switches lanes (up/down) to avoid obstacles." },
          { t: "Distance score", d: "Score increases over time/distance survived." }
        ],
        project: {
          title: "Runner — Core",
          brief: "An endless runner where obstacles rush at you and you jump/dodge, with a distance score.",
          must: ["auto-scrolling obstacle clones", "jump or lane dodge", "distance score"],
          stretch: "Add coins to collect while dodging."
        },
        challenge: "Add a double-jump or a slide move.",
        vocab: ["endless runner", "auto-scroll", "dodge"],
        checklist: ["Obstacles auto-scroll at me", "I can dodge them", "I score by distance"]
      },
      {
        module: "Game Genres Deep Dive",
        title: "Endless Runner 2 — Difficulty & Polish",
        emoji: "📈",
        theme: "Subway Surfers / Geometry Dash",
        minutes: 60,
        concept: "Endless games need rising difficulty and a strong game-over/restart loop to be addictive.",
        blocks: ["speed variable ramps up", "collision → game over", "restart instantly", "best score"],
        objective: "Add escalating difficulty, a clean game-over, and instant restart.",
        warmup: "Why 'one more go'? Instant restart + a best score to beat. We're building that hook.",
        exercises: [
          { t: "Ramp speed", d: "Slowly increase the scroll speed (and spawn rate) as distance grows." },
          { t: "Game over", d: "Hitting an obstacle → game over screen showing your score." },
          { t: "Instant restart", d: "One key/click restarts immediately (reset everything, go)." }
        ],
        project: {
          title: "Runner — Complete",
          brief: "A polished endless runner with rising difficulty, a best score, and instant restart.",
          must: ["difficulty ramp", "game over + score", "instant restart", "best score kept"],
          stretch: "Add power-ups (shield, magnet for coins)."
        },
        challenge: "Add three lanes with obstacles that force quick lane decisions.",
        vocab: ["difficulty curve", "restart loop", "hook"],
        checklist: ["Difficulty rises over time", "Game over shows my score", "Restart is instant"]
      },
      {
        module: "Game Genres Deep Dive",
        title: "Clicker / Tycoon 1 — The Economy",
        emoji: "🍪",
        theme: "Cookie Clicker / Roblox tycoon",
        minutes: 60,
        concept: "Clicker/tycoon games are about numbers growing: click to earn, and passive income that earns while you wait.",
        blocks: ["currency variable", "click to earn", "passive income (forever + wait)", "big-number display"],
        objective: "Build the earning core of a clicker: manual clicks + passive income.",
        warmup: "Why is Cookie Clicker weirdly fun? Watching a number go up, faster and faster. It's the purest game economy.",
        exercises: [
          { t: "Click to earn", d: "'when sprite clicked → change coins by 1'. The satisfying core." },
          { t: "Passive income", d: "'forever → wait 1 → change coins by (income)'. Coins arrive while you wait." },
          { t: "Feedback", d: "Add a click pop/particle and a satisfying sound each click." }
        ],
        project: {
          title: "Clicker — Core",
          brief: "A clicker where clicking earns currency and a passive income also ticks up over time.",
          must: ["currency variable", "click to earn", "passive income loop", "juicy click feedback"],
          stretch: "Show numbers nicely (e.g. 1.2k) as they grow large."
        },
        challenge: "Add a 'per click' variable so upgrades can increase click value next session.",
        vocab: ["currency", "passive income", "economy"],
        checklist: ["Clicking earns currency", "I have passive income", "Clicks feel satisfying"]
      },
      {
        module: "Game Genres Deep Dive",
        title: "Clicker / Tycoon 2 — Upgrades",
        emoji: "🏭",
        theme: "Cookie Clicker / Roblox tycoon",
        minutes: 60,
        concept: "Upgrades are the heart of tycoons: spend currency to earn faster, with rising prices to keep it balanced.",
        blocks: ["upgrade buttons", "if coins >= price then buy", "price increases after buying", "income increases"],
        objective: "Add buyable upgrades with rising costs that increase earning.",
        warmup: "The upgrade loop: earn → buy an upgrade → earn faster → buy a bigger upgrade. Balancing the prices is game design.",
        exercises: [
          { t: "An upgrade", d: "A button: 'if coins >= price then change coins by -price → change income by +amount → raise price'." },
          { t: "Rising cost", d: "After each buy, multiply the price (e.g. price × 1.5) so it stays challenging." },
          { t: "Multiple upgrades", d: "Add 2–3 upgrades that boost clicks or passive income differently." }
        ],
        project: {
          title: "Tycoon — Complete",
          brief: "A tycoon with several upgrades that cost rising currency and increase your income, plus a goal to reach.",
          must: ["2+ upgrades", "afford-check + purchase", "rising prices", "increasing income", "a goal/prestige"],
          stretch: "Add a 'prestige' reset that grants a permanent multiplier."
        },
        challenge: "Add an achievement list (reuse lists) for milestones.",
        vocab: ["upgrade", "cost scaling", "balance"],
        checklist: ["I have upgrades that cost currency", "Prices rise as you buy", "Income grows with upgrades"]
      },
      {
        module: "Game Genres Deep Dive",
        title: "Survival / Defense Intro",
        emoji: "🛡️",
        theme: "Minecraft survival / Tower Defense",
        minutes: 60,
        concept: "Survival & tower-defense mix earlier skills: waves of enemy clones, a base/health to protect, and resources to spend.",
        blocks: ["enemy waves (clones)", "base health", "place defenders / build", "resource economy"],
        objective: "Prototype a wave-survival or tower-defense core.",
        warmup: "Minecraft night or a TD wave: enemies come in waves, you defend, you get a breather, then a harder wave. Design your waves.",
        exercises: [
          { t: "Waves", d: "Spawn increasing waves of enemy clones that head for your base." },
          { t: "Defend", d: "Either fight them (shooter skills) or place defender sprites that auto-attack (clones firing)." },
          { t: "Base health", d: "Enemies reaching the base reduce base health; 0 = game over." }
        ],
        project: {
          title: "Last Stand",
          brief: "A wave-survival prototype: defend your base across increasingly hard waves of enemies.",
          must: ["enemy waves", "a way to defend", "base health + game over"],
          stretch: "Add resources you earn per kill and spend on defenders/upgrades."
        },
        challenge: "Add a between-waves shop to buy upgrades.",
        vocab: ["wave survival", "tower defense", "base"],
        checklist: ["I spawn enemy waves", "I can defend the base", "Base health leads to game over"]
      },

      /* ---------- MODULE F: Polish & Pro Skills (40–45) ---------- */
      {
        module: "Polish & Pro Skills",
        title: "Menus & Start Screens",
        emoji: "🖥️",
        theme: "Presentation",
        minutes: 60,
        concept: "A start menu makes a game feel finished: title, instructions, a play button, and states (menu / playing / game over).",
        blocks: ["a 'game state' variable", "broadcast start / game-over", "show/hide sprites per state"],
        objective: "Add a start menu and manage game states cleanly.",
        warmup: "Every real game boots to a menu, not straight into play. What's on a good start screen? (Title, Play, how-to.)",
        exercises: [
          { t: "Game state", d: "A variable 'state' = 'menu' / 'playing' / 'over'. Everything checks the state before acting." },
          { t: "Menu screen", d: "Title + Play button visible only in 'menu'; clicking Play sets state to 'playing' and broadcasts start." },
          { t: "Show/hide", d: "Gameplay sprites hide in menu/over and show in playing." }
        ],
        project: {
          title: "Front End",
          brief: "Add a proper start menu and game-over screen to one of your games, managed by a game-state variable.",
          must: ["state variable", "menu with Play", "game-over screen", "correct show/hide per state"],
          stretch: "Add a settings toggle (e.g. sound on/off)."
        },
        challenge: "Add a pause screen (freeze gameplay, show 'Paused').",
        vocab: ["game state", "menu", "front end"],
        checklist: ["I have a start menu", "A state variable controls the flow", "Menu/game-over screens work"]
      },
      {
        module: "Polish & Pro Skills",
        title: "Sound Design & Music",
        emoji: "🔊",
        theme: "Presentation",
        minutes: 60,
        concept: "Sound transforms a game: background music loops, and short SFX punctuate every action (jump, coin, hit).",
        blocks: [
          "play sound () until done / start sound () — Sound",
          "forever play music (loop) — Sound",
          "set volume — Sound"
        ],
        objective: "Add looping music and responsive sound effects.",
        warmup: "Play a game clip muted, then with sound. Same visuals, totally different feel. Sound is half the experience.",
        exercises: [
          { t: "Music loop", d: "On the Stage: 'forever → play music until done' for continuous background music." },
          { t: "SFX", d: "Add 'start sound' on jump, coin, hit, win. Use 'start' (not 'until done') so they don't block the game." },
          { t: "Balance", d: "Lower the music volume so SFX are clearly heard over it." }
        ],
        project: {
          title: "Soundtrack",
          brief: "Add looping music and at least four sound effects to one of your games, balanced so nothing drowns out.",
          must: ["looping music", "4+ SFX on actions", "balanced volume", "start vs until-done used correctly"],
          stretch: "Duck the music briefly on big events."
        },
        challenge: "Make your own sound effect in the Sound editor.",
        vocab: ["SFX", "loop", "mix/balance"],
        checklist: ["I added looping music", "Actions trigger sound effects", "The mix is balanced"]
      },
      {
        module: "Polish & Pro Skills",
        title: "Game Feel — Juice It!",
        emoji: "🧃",
        theme: "Pro polish",
        minutes: 60,
        concept: "'Juice' is the little effects that make actions feel great: screen shake, hit flashes, squash-and-stretch, particles.",
        blocks: ["quick size pulse (squash/stretch)", "screen shake (jitter positions)", "hit flash (colour/ghost)", "particles (clones)"],
        objective: "Add juice effects that make interactions feel powerful.",
        warmup: "Two identical games, one 'juiced'. The juiced one feels 10× better with the SAME mechanics. Small effects, big impact.",
        exercises: [
          { t: "Squash & stretch", d: "On landing/jumping: a quick size change (e.g. wider on land) then back to normal." },
          { t: "Hit flash", d: "On damage: flash the sprite white/red for a few frames." },
          { t: "Screen shake", d: "On a big hit: briefly jitter sprite positions (or a fake shake) then settle." }
        ],
        project: {
          title: "Juice Pass",
          brief: "Take one game and add three juice effects (e.g. squash-stretch, hit flash, screen shake, particles).",
          must: ["3 juice effects", "tied to real game events", "they settle back cleanly"],
          stretch: "Add hit-stop (freeze for 2–3 frames on a big impact)."
        },
        challenge: "Add a satisfying combo effect that escalates as combos rise.",
        vocab: ["juice", "screen shake", "squash & stretch"],
        checklist: ["I added squash/stretch or a pulse", "I added a hit flash or shake", "Effects tie to real events"]
      },
      {
        module: "Polish & Pro Skills",
        title: "Persistent High Scores",
        emoji: "☁️",
        theme: "Community",
        minutes: 60,
        concept: "Cloud variables (numbers only, shared online) let a game remember a high score across players — with real limits to understand.",
        blocks: [
          "☁ cloud variable (numbers only) — Variables",
          "if score > ☁ highscore then set ☁ highscore to score",
          "encode text as numbers (for names)"
        ],
        objective: "Save a high score that persists, and understand cloud-variable limits.",
        warmup: "How does an online leaderboard remember scores forever? Data stored on a server. Scratch's version is the cloud variable.",
        exercises: [
          { t: "Make a cloud var", d: "Create a ☁ cloud variable 'highscore' (needs a shared, logged-in project)." },
          { t: "Update it", d: "'if score > ☁ highscore then set ☁ highscore to score'." },
          { t: "Know the limits", d: "Cloud vars store NUMBERS only, update slowly, and are shared — discuss what that means for cheating/privacy." }
        ],
        project: {
          title: "Global Best",
          brief: "Add a persistent high score to a game and display it, respecting cloud-variable rules.",
          must: ["a cloud variable", "high-score update logic", "display it", "understand the limits"],
          stretch: "Encode 3-letter initials as numbers to store a named high score."
        },
        challenge: "Design a simple anti-cheat check for impossible scores.",
        vocab: ["cloud variable", "persistence", "leaderboard"],
        checklist: ["I made a cloud high score", "It updates correctly", "I can explain cloud-var limits"]
      },
      {
        module: "Polish & Pro Skills",
        title: "Two-Player Games",
        emoji: "🤝",
        theme: "Multiplayer",
        minutes: 60,
        concept: "Local 2-player is easy and hugely fun: give each player their own keys, sprite, and score on one keyboard.",
        blocks: ["separate key sets (WASD vs arrows)", "two players, two scores", "shared win logic"],
        objective: "Build a local two-player game sharing one keyboard.",
        warmup: "Best couch multiplayer memories? Two players, one screen, instant fun. Let's make one.",
        exercises: [
          { t: "Two control schemes", d: "Player 1 uses WASD; Player 2 uses the arrow keys. Independent movement." },
          { t: "Two scores", d: "Separate score variables and a clear winner check." },
          { t: "Shared rules", d: "One win condition that compares both players (first to X, or last standing)." }
        ],
        project: {
          title: "Versus",
          brief: "A two-player game (race, tag, or arena) with separate controls and scores and a clear winner.",
          must: ["two control schemes", "two players/scores", "a winner declared"],
          stretch: "Add a best-of-3 match with rounds."
        },
        challenge: "Add a co-op mode instead of versus (both players share a goal).",
        vocab: ["local multiplayer", "control scheme", "versus"],
        checklist: ["Two players have separate controls", "Each has a score", "A winner is declared"]
      },
      {
        module: "Polish & Pro Skills",
        title: "Sharing & Remixing",
        emoji: "🌍",
        theme: "Community",
        minutes: 60,
        concept: "Scratch is a community: share projects, write good instructions/credits, and remix others' work respectfully.",
        blocks: [
          "Project page: instructions, notes & credits",
          "Share button (with teacher's guidance)",
          "See inside / Remix (learning from others)"
        ],
        objective: "Prepare a project for sharing and learn to remix responsibly.",
        warmup: "Why share? Others play it, give feedback, and remix it into something new. That's how coders learn from each other.",
        exercises: [
          { t: "Write it up", d: "Fill the Instructions ('How to play') and Notes & Credits (who made what, any assets used)." },
          { t: "Share safely", d: "With teacher guidance, share the project; discuss online safety (no personal info in projects)." },
          { t: "Remix to learn", d: "'See inside' a shared project and remix ONE thing to understand how it works — always credit the original." }
        ],
        project: {
          title: "Ship It",
          brief: "Publish a finished game with clear instructions and credits to the class Scratch studio.",
          must: ["instructions", "notes & credits", "shared to the class studio (with guidance)"],
          stretch: "Play and give kind, useful feedback on two classmates' projects."
        },
        challenge: "Remix a classmate's game to add one respectful improvement (credited).",
        vocab: ["share", "credits", "remix"],
        checklist: ["I wrote instructions and credits", "I shared responsibly", "I understand remixing and crediting"]
      },

      /* ---------- MODULE G: Capstone (46–50) ---------- */
      {
        module: "Capstone",
        title: "Capstone 1 — Design Document",
        emoji: "📝",
        theme: "Your dream game",
        minutes: 60,
        concept: "Real games start with a plan. Write a design doc for the game you'll build over the next five sessions.",
        blocks: ["planning: genre, core loop, controls, win/lose, art & sound plan, scope"],
        objective: "Produce a clear, realistic design document for a capstone game.",
        warmup: "Pick your genre from Level 2: platformer, adventure, shooter, runner, tycoon, or survival. Steal the parts you loved.",
        exercises: [
          { t: "Pitch", d: "One sentence: 'It's a ___ game where you ___ to ___.'" },
          { t: "Core loop & controls", d: "What does the player DO over and over? What are the exact controls?" },
          { t: "Scope check", d: "List features as MUST / NICE / DREAM. Circle a realistic MUST list for 4 build sessions." }
        ],
        project: {
          title: "Design Doc",
          brief: "A one-page design document: pitch, genre, core loop, controls, win/lose, art/sound plan, and a scoped feature list.",
          must: ["pitch", "core loop + controls", "win/lose", "scoped MUST list"],
          stretch: "Sketch the main screen and the HUD."
        },
        challenge: "Show your doc to a partner; cut one feature that's too big.",
        vocab: ["design doc", "scope", "core loop"],
        checklist: ["I chose a genre", "I defined the core loop and controls", "I scoped a realistic feature list"]
      },
      {
        module: "Capstone",
        title: "Capstone 2 — Build the Core",
        emoji: "🔩",
        theme: "Your dream game",
        minutes: 60,
        concept: "Build the ONE core mechanic first and make it fun before adding anything else. A fun core is the whole game.",
        blocks: ["your genre's core (movement/physics/economy)", "custom blocks for structure"],
        objective: "Implement and playtest the core mechanic of your capstone.",
        warmup: "The 'toy test': if the core mechanic isn't fun with NOTHING else, more features won't save it. Get the toy fun first.",
        exercises: [
          { t: "Set up structure", d: "Create your sprites and a 'setup' custom block from the start (build clean)." },
          { t: "Build the core", d: "Implement just the core loop (e.g. run-jump, or click-earn, or shoot-dodge)." },
          { t: "Toy test", d: "Play only the core for two minutes. Is it fun? Tune it until it is." }
        ],
        project: {
          title: "Core Build",
          brief: "The playable core mechanic of your capstone, built cleanly and tuned to be fun on its own.",
          must: ["core mechanic working", "clean structure (custom blocks)", "tuned to be fun"],
          stretch: "Add placeholder art you'll improve later."
        },
        challenge: "Get one classmate to play your core and note their first reaction.",
        vocab: ["core mechanic", "toy test", "iteration"],
        checklist: ["My core mechanic works", "I built it cleanly", "The core is already fun"]
      },
      {
        module: "Capstone",
        title: "Capstone 3 — Build the Content",
        emoji: "🧱",
        theme: "Your dream game",
        minutes: 60,
        concept: "Now add the content around the core: levels/enemies/items/upgrades, plus scoring and win/lose.",
        blocks: ["clones for content", "lists for data", "variables for score/progress", "custom blocks"],
        objective: "Flesh out your game with content and a full game loop.",
        warmup: "Content is everything the core interacts with: enemies, levels, items, upgrades. Add from your MUST list only.",
        exercises: [
          { t: "Add content", d: "Build your MUST features: enemies (clones), levels (backdrops/data), items (lists), upgrades (variables)." },
          { t: "Full loop", d: "Wire up score/progress and a clear win and lose so it's a complete game, start to finish." },
          { t: "Test as you go", d: "Add one feature, test it, then the next. Never add three untested things at once." }
        ],
        project: {
          title: "Content Build",
          brief: "Your capstone with its MUST content in place and a complete start-to-finish game loop.",
          must: ["MUST-list content added", "score/progress", "win and lose states"],
          stretch: "Add one NICE-to-have feature if time allows."
        },
        challenge: "Add difficulty progression so it gets harder as you play.",
        vocab: ["content", "game loop", "incremental testing"],
        checklist: ["I added my core content", "The game has a full loop", "I tested as I built"]
      },
      {
        module: "Capstone",
        title: "Capstone 4 — Polish & Playtest",
        emoji: "💎",
        theme: "Your dream game",
        minutes: 60,
        concept: "Polish and playtesting turn a project into a game people love: menus, sound, juice, and fixes from real feedback.",
        blocks: ["start menu + game state", "music + SFX", "juice effects", "bug fixes"],
        objective: "Polish the capstone and improve it using real playtest feedback.",
        warmup: "Playtesting rule: watch someone play WITHOUT helping them. Where they get stuck is your to-do list.",
        exercises: [
          { t: "Polish pass", d: "Add a start menu, music + SFX, and 2–3 juice effects from the Polish module." },
          { t: "Playtest", d: "Have a classmate play silently. Note every confusion and bug — don't explain, just watch." },
          { t: "Fix the top issues", d: "Fix the two biggest problems the playtest revealed." }
        ],
        project: {
          title: "Polish Build",
          brief: "A polished capstone (menu, sound, juice) improved with fixes from a real playtest.",
          must: ["start menu", "sound", "juice", "fixes from playtest feedback"],
          stretch: "Add instructions and a credits screen."
        },
        challenge: "Do a second playtest to confirm your fixes worked.",
        vocab: ["polish", "playtest", "feedback"],
        checklist: ["I polished with menu/sound/juice", "I ran a real playtest", "I fixed the top issues"]
      },
      {
        module: "Capstone",
        title: "Capstone 5 — Showcase & Graduation",
        emoji: "🏆",
        theme: "Celebrate",
        minutes: 60,
        concept: "Ship, present, and celebrate. You can now design and build real games — you're a Game Architect.",
        blocks: ["final build + share", "presentation", "reflection"],
        objective: "Present the finished capstone and reflect on the whole journey.",
        warmup: "Presentation script (rehearse once): 'My game is ___. The core idea is ___. The hardest thing I solved was ___. I'm proudest of ___. Next I'd build ___.'",
        exercises: [
          { t: "Final check", d: "Reset works, no crashes, instructions clear. Share to the class studio." },
          { t: "Present", d: "Demo your capstone in 3 minutes using the script. Celebrate the hard problems you solved." },
          { t: "Reflect", d: "Write down: your biggest win, your hardest bug, and the next game you want to make." }
        ],
        project: {
          title: "Graduation Showcase",
          brief: "Your finished, shared capstone game, presented to the group with a reflection on your journey.",
          must: ["finished + shared game", "a 3-minute presentation", "a written reflection"],
          stretch: "Set a goal for what you'll learn/build next (real Scratch community, a game jam, or a new language)."
        },
        challenge: "Award class certificates: Best Mechanic, Best Polish, Best Story, Best Debugger, Most Ambitious.",
        vocab: ["showcase", "reflection", "graduation"],
        checklist: ["My capstone is finished and shared", "I presented it", "I reflected and set a next goal"]
      }
    ]
  });
})();
