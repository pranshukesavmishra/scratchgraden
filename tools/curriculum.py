# -*- coding: utf-8 -*-
"""
curriculum.py — the exercise content, in the reference-platform model.

Sessions -> Exercises. Each exercise is a Mini Project, Home Task, or Recall
Test, with a difficulty, a concept tag, a themed set of REAL Scratch sprites, a
game template (its playable "desired output"), and instructions.
"""

# default step-by-step hints per game template
HINTS = {
 "collect": [
   "Move the player with the arrow keys.",
   "Make each gem vanish and add 1 to the score when the player touches it.",
   "Make the enemy chase the player (point towards it, then move).",
   "If the player touches the enemy, send it back to the start.",
   "When the score reaches 3, the goal sprite celebrates — You Win!",
   "Stretch: add lives, and a second area to explore."],
 "catch": [
   "Make the catcher follow the mouse along the bottom (set x to mouse x).",
   "Make the item fall — change y by a negative number, forever.",
   "If the item touches the catcher, add 1 to the score and send it back to the top.",
   "If the item drops off the bottom, lose a life and reset it.",
   "When lives reach 0, show Game Over.",
   "Stretch: make the item fall faster as your score climbs."],
 "dodge": [
   "Move the player with the arrow keys.",
   "Make each hazard fall from a random spot at the top.",
   "When a hazard passes the bottom, add 1 to the score and reset it.",
   "If a hazard touches the player, it's Game Over.",
   "Stretch: speed the hazards up the longer you survive."],
 "clicker": [
   "Add a score variable and set it to 0 at the start.",
   "When the target is clicked, add 1 to the score.",
   "Make the target pulse (change size, then back) so clicks feel good.",
   "When the score reaches the goal, celebrate — You Win!",
   "Stretch: add an upgrade that earns points automatically."],
 "quiz": [
   "Press the green flag to start the quiz.",
   "Read each question and type your answer, then press Enter.",
   "You earn a point for every correct answer.",
   "Your final score shows at the end.",
   "Stretch: try to score full marks!"],
 "flappy": [
   "Make the player fall — a 'gravity' variable that lowers its y a little every frame.",
   "When Space is pressed, give it an upward boost.",
   "Scroll the obstacle from right to left, forever.",
   "When the obstacle leaves the left edge, send it back to the right at a new height and score +1.",
   "If the player touches the obstacle or falls off the bottom, it's Game Over.",
   "Stretch: add a top and bottom obstacle with a gap to fly through."],
 "whack": [
   "Make the target pop up at a random spot, wait a moment, then hide — forever.",
   "When the target is clicked, add 1 to the score.",
   "Add a countdown timer that starts at 20.",
   "When the timer reaches 0, show the final score and stop the game.",
   "Stretch: make it pop up faster as the timer runs down."],
}

# colour per 'world' (used for the card thumbnail tile)
W = {"fantasy": "#7c3aed", "garden": "#16a34a", "space": "#2563eb",
     "food": "#f59e0b", "sea": "#0891b2", "review": "#e11d48"}


def mini(id, title, level, tag, emoji, color, template, theme, story):
    return {"id": id, "title": title, "type": "Mini Project", "level": level, "tag": tag,
            "emoji": emoji, "color": color, "template": template, "theme": theme,
            "story": story, "hints": HINTS[template]}

def home(id, title, level, tag, emoji, color, template, theme, story):
    d = mini(id, title, level, tag, emoji, color, template, theme, story)
    d["type"] = "Home Task"; return d

def recall(id, tag, color, questions, story):
    return {"id": id, "title": "Recall Test", "type": "Recall Test", "level": "Easy", "tag": tag,
            "emoji": "🧠", "color": W["review"], "template": "quiz",
            "theme": {"host": "Gobo", "backdrop": "Chalkboard", "questions": questions},
            "story": story, "hints": HINTS["quiz"]}


SESSIONS = [
 {"id": "S1", "n": 1, "title": "Gem Hunt", "emoji": "💎", "color": W["fantasy"],
  "concept": "Move a sprite with the arrow keys and detect when it touches things.",
  "exercises": [
    mini("S1E1", "Gem Hunt", "Easy", "Movement & collision", "💎", W["fantasy"], "collect",
         {"player": "Wizard", "collectible": "Crystal", "enemy": "Ghost", "goal": "Dragon", "backdrop": "Castle 3",
          "win": "You collected all 3 crystals — YOU WIN!"},
         "A young wizard is trapped in a castle. Collect the three magic crystals, dodge the ghost, and reach the dragon to break the spell."),
    home("S1E2", "Home Task — Haunted Halls", "Easy", "Movement & collision", "👻", W["fantasy"], "collect",
         {"player": "Witch", "collectible": "Star", "enemy": "Ghost", "goal": "Griffin", "backdrop": "Woods",
          "win": "All 3 stars collected — the griffin is free!"},
         "A witch must gather three fallen stars in the haunted woods while a ghost gives chase, then reach the griffin."),
    recall("S1E3", "Movement & collision", W["review"],
           [("Which blocks move a sprite left and right?", "change x"),
            ("What block checks if two sprites touch?", "touching"),
            ("A block that repeats forever is called a ___?", "forever")],
           "Recall what you learned about moving sprites and detecting touches.")]},

 {"id": "S2", "n": 2, "title": "Apple Catch", "emoji": "🍎", "color": W["garden"],
  "concept": "Use coordinates and a score variable to catch falling objects.",
  "exercises": [
    mini("S2E1", "Apple Catch", "Easy", "Coordinates & score", "🍎", W["garden"], "catch",
         {"player": "Bowl", "item": "Apple", "backdrop": "Blue Sky"},
         "Apples are falling from the trees! Move the bowl with your mouse and catch as many as you can before you run out of lives."),
    home("S2E2", "Home Task — Banana Bonanza", "Easy", "Coordinates & score", "🍌", W["garden"], "catch",
         {"player": "Bowl", "item": "Bananas", "backdrop": "Beach Rio"},
         "The monkeys are dropping bananas on the beach. Catch them in your bowl!"),
    recall("S2E3", "Coordinates & score", W["review"],
           [("Which value goes left-right on the stage, x or y?", "x"),
            ("What do we call a labelled box that stores a number?", "variable"),
            ("Which block makes a sprite follow the mouse?", "set x to mouse x")],
           "Recall coordinates and how a score variable works.")]},

 {"id": "S3", "n": 3, "title": "Asteroid Dodge", "emoji": "☄️", "color": W["space"],
  "concept": "Use loops and if-blocks to dodge falling hazards.",
  "exercises": [
    mini("S3E1", "Asteroid Dodge", "Medium", "Loops & conditionals", "☄️", W["space"], "dodge",
         {"player": "Rocketship", "enemy": "Rocks", "backdrop": "Space"},
         "Pilot your rocket through an asteroid field. Dodge the falling rocks and survive as long as you can!"),
    home("S3E2", "Home Task — Meteor Storm", "Medium", "Loops & conditionals", "🤖", W["space"], "dodge",
         {"player": "Robot", "enemy": "Rocks", "backdrop": "Nebula"},
         "A robot explorer is caught in a meteor storm inside a glowing nebula. Keep it safe!"),
    recall("S3E3", "Loops & conditionals", W["review"],
           [("A block that runs code only when something is true is an ___ block?", "if"),
            ("What do we call code that repeats?", "loop"),
            ("Which block picks a random number?", "pick random")],
           "Recall loops and conditionals.")]},

 {"id": "S4", "n": 4, "title": "Donut Clicker", "emoji": "🍩", "color": W["food"],
  "concept": "Use variables and events to build a clicker game.",
  "exercises": [
    mini("S4E1", "Donut Clicker", "Easy", "Variables & events", "🍩", W["food"], "clicker",
         {"target": "Donut", "backdrop": "Party"},
         "Click the donut as fast as you can! Every click adds to your score — reach 25 to win the party."),
    home("S4E2", "Home Task — Star Tapper", "Easy", "Variables & events", "⭐", W["space"], "clicker",
         {"target": "Star", "backdrop": "Galaxy"},
         "Tap the shooting star across the galaxy to light up the sky."),
    recall("S4E3", "Variables & events", W["review"],
           [("Which block runs when you click a sprite? when this sprite ___?", "clicked"),
            ("Which block adds to a variable?", "change score by"),
            ("What starts every script when the flag is pressed? when green flag ___?", "clicked")],
           "Recall variables and events.")]},

 {"id": "S5", "n": 5, "title": "Deep Dive Dodge", "emoji": "🐟", "color": W["sea"],
  "concept": "Sensing and touching in an underwater world.",
  "exercises": [
    mini("S5E1", "Deep Dive Dodge", "Medium", "Sensing & touching", "🐟", W["sea"], "dodge",
         {"player": "Fish", "enemy": "Jellyfish", "backdrop": "Underwater 1"},
         "Swim your little fish through a swarm of drifting jellyfish. Don't get stung!"),
    home("S5E2", "Home Task — Urchin Alley", "Medium", "Sensing & touching", "🦑", W["sea"], "dodge",
         {"player": "Fish", "enemy": "Pufferfish", "backdrop": "Underwater 2"},
         "Pufferfish are drifting down through the reef. Guide your fish safely past them."),
    recall("S5E3", "Sensing & touching", W["review"],
           [("Which category has the touching block? (colour is light blue)", "sensing"),
            ("Which block reports how far one sprite is from another?", "distance to"),
            ("touching [sprite]? reports true or ___?", "false")],
           "Recall sensing and touching.")]},

 {"id": "S6", "n": 6, "title": "Treasure Reef", "emoji": "🐚", "color": W["sea"],
  "concept": "Combine movement, collecting, and a win condition.",
  "exercises": [
    mini("S6E1", "Treasure Reef", "Medium", "Score & win condition", "🐚", W["sea"], "collect",
         {"player": "Diver1", "collectible": "Starfish", "enemy": "Shark 2", "goal": "Octopus", "backdrop": "Underwater 2",
          "win": "All 3 starfish found — the octopus is delighted!"},
         "Dive the reef to gather three glowing starfish, keep clear of the shark, and reach the friendly octopus."),
    home("S6E2", "Home Task — Crab Cove", "Medium", "Score & win condition", "🦀", W["sea"], "collect",
         {"player": "Crab", "collectible": "Crystal", "enemy": "Shark 2", "goal": "Octopus", "backdrop": "Underwater 1",
          "win": "3 crystals collected — you win!"},
         "A brave crab scuttles the cove for crystals while dodging the shark."),
    recall("S6E3", "Score & win condition", W["review"],
           [("What should you set the score to at the very start?", "0"),
            ("Which block ends the game? stop ___?", "all"),
            ("A message you send to all sprites at once is a ___?", "broadcast")],
           "Recall scoring and win conditions.")]},

 {"id": "S7", "n": 7, "title": "Fruit Frenzy", "emoji": "🍉", "color": W["food"],
  "concept": "Lives and game-over screens.",
  "exercises": [
    mini("S7E1", "Fruit Frenzy", "Medium", "Lives & game over", "🍉", W["food"], "catch",
         {"player": "Bowl", "item": "Watermelon", "backdrop": "Farm"},
         "Watermelons are rolling off the farm cart! Catch them — but miss three and it's game over."),
    home("S7E2", "Home Task — Cake Catch", "Medium", "Lives & game over", "🎂", W["food"], "catch",
         {"player": "Bowl", "item": "Cake", "backdrop": "Bedroom 1"},
         "Slices of cake are tumbling down. Catch them before they hit the floor!"),
    recall("S7E3", "Lives & game over", W["review"],
           [("What do we call the tries a player has before the game ends?", "lives"),
            ("Which block subtracts one from lives?", "change lives by -1"),
            ("When lives = 0 we usually show a ___ screen?", "game over")],
           "Recall lives and game over.")]},

 {"id": "S8", "n": 8, "title": "Dragon's Keep (Capstone)", "emoji": "🐉", "color": W["fantasy"],
  "concept": "Put it all together into a bigger adventure.",
  "exercises": [
    mini("S8E1", "Dragon's Keep", "Hard", "Capstone project", "🐉", W["fantasy"], "collect",
         {"player": "Wizard", "collectible": "Crystal", "enemy": "Ghost", "goal": "Dragon", "backdrop": "Castle 1",
          "win": "You freed the dragon — YOU WIN!"},
         "The final challenge. A wizard braves the great keep to collect the crystals, outwit the ghost, and awaken the dragon."),
    home("S8E2", "Home Task — Knight's Quest", "Hard", "Capstone project", "🛡️", W["fantasy"], "collect",
         {"player": "Knight", "collectible": "Crystal", "enemy": "Ghost", "goal": "Dragon", "backdrop": "Castle 2",
          "win": "The knight collected all 3 crystals — victory!"},
         "A knight takes on the same keep. Can you beat it a second way?"),
    recall("S8E3", "Final review", W["review"],
           [("Name the block that repeats code forever.", "forever"),
            ("Name the block that makes a decision.", "if"),
            ("Name the block that stores a number you can change.", "variable")],
           "A final review of everything in this level.")]},

 {"id": "S9", "n": 9, "title": "Flappy Flight", "emoji": "🦜", "color": W["garden"],
  "concept": "Gravity and a flap: fly through gaps with a falling-and-boosting sprite.",
  "exercises": [
    mini("S9E1", "Flappy Parrot", "Medium", "Gravity & flap", "🦜", W["garden"], "flappy",
         {"player": "Parrot", "obstacle": "Tree1", "backdrop": "Jungle"},
         "Tap Space to keep the parrot in the air and flap through the trees. How far can you fly?"),
    home("S9E2", "Home Task — Bat Flight", "Medium", "Gravity & flap", "🦇", W["fantasy"], "flappy",
         {"player": "Bat", "obstacle": "Rocks", "backdrop": "Woods"},
         "A little bat flutters through a rocky cave at dusk. Don't hit the rocks!"),
    recall("S9E3", "Gravity & flap", W["review"],
           [("What pulls a sprite down every frame?", "gravity"),
            ("Which key gives the flap boost in our game?", "space"),
            ("A value that goes up and down like speed is a ___?", "variable")],
           "Recall gravity and the flap boost.")]},

 {"id": "S10", "n": 10, "title": "Whack Attack", "emoji": "🔨", "color": W["food"],
  "concept": "Random positions and a countdown timer.",
  "exercises": [
    mini("S10E1", "Whack-a-Mouse", "Easy", "Random & timing", "🐭", W["food"], "whack",
         {"target": "Mouse1", "backdrop": "Farm"},
         "Mice keep popping out of the barn! Click them as fast as you can before the timer runs out."),
    home("S10E2", "Home Task — Bug Bash", "Easy", "Random & timing", "🐞", W["garden"], "whack",
         {"target": "Beetle", "backdrop": "Garden-rock"},
         "Beetles are popping up all over the garden. Bash as many as you can in 20 seconds!"),
    recall("S10E3", "Random & timing", W["review"],
           [("Which block picks a spot you can't predict? pick ___?", "random"),
            ("Which block pauses the script? wait ___ seconds?", "1"),
            ("What counts down to end the game?", "timer")],
           "Recall random positions and timing.")]},

 {"id": "S11", "n": 11, "title": "Galaxy Gems", "emoji": "🌟", "color": W["space"],
  "concept": "Collecting and scoring, out in space.",
  "exercises": [
    mini("S11E1", "Galaxy Gems", "Medium", "Score & collecting", "🌟", W["space"], "collect",
         {"player": "Robot", "collectible": "Star", "enemy": "Ghost", "goal": "Planet2", "backdrop": "Stars",
          "win": "All 3 stars collected — the planet is yours!"},
         "Pilot a robot through the stars, gather three of them, dodge the space ghost, and reach the planet."),
    home("S11E2", "Home Task — Moon Run", "Medium", "Score & collecting", "🌙", W["space"], "collect",
         {"player": "Retro Robot", "collectible": "Star", "enemy": "Ghost", "goal": "Earth", "backdrop": "Moon",
          "win": "3 stars collected — head home to Earth!"},
         "A retro robot hops across the moon collecting stars on the way back to Earth."),
    recall("S11E3", "Score & collecting", W["review"],
           [("What should the score be set to at the start?", "0"),
            ("Which block adds one to the score?", "change score by 1"),
            ("Which block hides a collected item?", "hide")],
           "Recall scoring and collecting.")]},

 {"id": "S12", "n": 12, "title": "Jungle Dash", "emoji": "🐒", "color": W["garden"],
  "concept": "Dodging falling hazards with loops and if-blocks.",
  "exercises": [
    mini("S12E1", "Jungle Dash", "Medium", "Loops & conditionals", "🐒", W["garden"], "dodge",
         {"player": "Monkey", "enemy": "Rocks", "backdrop": "Jungle"},
         "Coconuts are raining down in the jungle! Move the monkey to dodge them and survive."),
    home("S12E2", "Home Task — Desert Dash", "Medium", "Loops & conditionals", "🐍", W["food"], "dodge",
         {"player": "Snake", "enemy": "Rocks", "backdrop": "Desert"},
         "A snake slithers through a rockslide in the desert. Keep it safe!"),
    recall("S12E3", "Loops & conditionals", W["review"],
           [("Code that repeats is a ___?", "loop"),
            ("A block that checks something is true is an ___ block?", "if"),
            ("Which block makes something happen from a random edge? pick ___?", "random")],
           "Recall loops and conditionals.")]},

 {"id": "S13", "n": 13, "title": "Pet Clicker", "emoji": "🐶", "color": W["food"],
  "concept": "More variables and events, with a friendly pet.",
  "exercises": [
    mini("S13E1", "Puppy Clicker", "Easy", "Variables & events", "🐶", W["food"], "clicker",
         {"target": "Puppy", "backdrop": "Bedroom 1"},
         "Click the happy puppy to give it treats — reach 25 to make it the happiest pup ever!"),
    home("S13E2", "Home Task — Kitty Clicker", "Easy", "Variables & events", "🐱", W["fantasy"], "clicker",
         {"target": "Cat 2", "backdrop": "Room 1"},
         "Pet the kitty by clicking it. Can you reach the goal?"),
    recall("S13E3", "Variables & events", W["review"],
           [("Which block runs on a click? when this sprite ___?", "clicked"),
            ("Which block makes a sprite bigger for feedback? change ___ by?", "size"),
            ("A labelled box that stores your clicks is a ___?", "variable")],
           "Recall variables and events.")]},

 {"id": "S14", "n": 14, "title": "Berry Catch", "emoji": "🍓", "color": W["garden"],
  "concept": "Catching, scoring, and lives — again, with new fruit.",
  "exercises": [
    mini("S14E1", "Berry Catch", "Medium", "Score & lives", "🍓", W["garden"], "catch",
         {"player": "Bowl", "item": "Strawberry", "backdrop": "Hay Field"},
         "Strawberries are dropping from the vines. Catch them in your bowl — miss three and it's over."),
    home("S14E2", "Home Task — Orange Drop", "Medium", "Score & lives", "🍊", W["food"], "catch",
         {"player": "Bowl", "item": "Orange", "backdrop": "Farm"},
         "Oranges are rolling off the farm stand. Don't let them hit the ground!"),
    recall("S14E3", "Score & lives", W["review"],
           [("What do we call the tries before game over?", "lives"),
            ("Which value is left-right on the stage?", "x"),
            ("Which block follows the mouse? set x to mouse ___?", "x")],
           "Recall scoring, coordinates and lives.")]},

 {"id": "S15", "n": 15, "title": "Rocket Rush", "emoji": "🚀", "color": W["space"],
  "concept": "Gravity and flap in space — tune the feel.",
  "exercises": [
    mini("S15E1", "Rocket Rush", "Hard", "Game feel", "🚀", W["space"], "flappy",
         {"player": "Rocketship", "obstacle": "Planet2", "backdrop": "Nebula"},
         "Thread your rocket through the planets. Tap Space to fire the thrusters and don't crash!"),
    home("S15E2", "Home Task — UFO Flight", "Hard", "Game feel", "🛸", W["space"], "flappy",
         {"player": "Retro Robot", "obstacle": "Rocks", "backdrop": "Galaxy"},
         "Fly the little robot's saucer through an asteroid gauntlet across the galaxy."),
    recall("S15E3", "Game feel", W["review"],
           [("Making a game feel good is called game ___?", "feel"),
            ("Numbers you adjust to tune a game are ___?", "variables"),
            ("Which block gives the upward boost? change ___ by?", "y")],
           "Recall tuning and game feel.")]},

 {"id": "S16", "n": 16, "title": "Ocean Whack", "emoji": "🦀", "color": W["sea"],
  "concept": "Random pop-ups and timing, under the sea.",
  "exercises": [
    mini("S16E1", "Crab Whack", "Medium", "Random & timing", "🦀", W["sea"], "whack",
         {"target": "Crab", "backdrop": "Underwater 1"},
         "Crabs keep scuttling out from the sand! Tap them fast before the timer runs out."),
    home("S16E2", "Home Task — Jelly Tap", "Medium", "Random & timing", "🎐", W["sea"], "whack",
         {"target": "Jellyfish", "backdrop": "Underwater 2"},
         "Glowing jellyfish drift up from the deep. Tap as many as you can!"),
    recall("S16E3", "Final review", W["review"],
           [("Name a block that repeats forever.", "forever"),
            ("Name the block that stores a changing number.", "variable"),
            ("Name the block that reacts to a click.", "when this sprite clicked")],
           "A final review across all the games.")]},
]
