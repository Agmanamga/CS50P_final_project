# One Room Text-Based Escape Room Adventure
By Dendy Kurniari Agman
edx id: dendy_kurniary
#### Video Demo: <https://youtu.be/6RnbEqcySi4>

#### Description:
Welcome to the **One Room Text-Based Escape Room Adventure**, an interactive, puzzle-based game where players find themselves in a mysterious room full of secrets. The objective is simple: explore the room, find clues, solve puzzles, and ultimately escape through a locked door. But the process is anything but simple, as players must piece together cryptic hints, locate hidden items, and use resources wisely to progress. This project merges immersive storytelling, logical problem-solving, and interactive text-based exploration to create an engaging escape room experience within a Python console.

### Gameplay Overview:
The game begins with the player waking up in an unfamiliar room with no recollection of how they arrived. The room contains several objects: a **door**, a **board** full of notes, a **desk**, a pile of **books**, and a **safe**. Each of these items holds clues, items, or actions that bring players closer to their goal. Using simple text commands, players can interact with these objects and uncover the secrets hidden within the room.

Players will find themselves examining items, picking up objects, and using them in inventive ways to unlock new paths. For instance, players can `check books` to search through the pile of books, potentially discovering a **cog** that could fit into the safe. As items are found, they’re added to an **inventory** accessible throughout the game. This inventory is key, as players need to track and use collected items strategically to progress.

### Key Features and Game Mechanics:
1. **Command-Based Interaction**:
   - The player interacts with the game environment through simple commands, such as `check [item]`, `use [inventory item] on [item]`, and `check inventory`.
   - This command-based structure allows for easy interaction while challenging players to remember available commands and use them effectively.
   - Some common actions include:
     - `check surrounding` to observe the room's main objects.
     - `check door`, `check board`, `check desk`, etc., to look closely at individual items.
     - `use [inventory item] on [target item]` to attempt to solve a puzzle with an inventory item.

2. **Immersive Descriptions with ANSI Styling**:
   - Descriptions in the game use ANSI escape codes to add bold and italic styling, making important clues and objects stand out.
   - For instance, when discovering new items or reading critical clues, the bold formatting highlights essential parts, helping players identify which details might be significant to their escape.

3. **Puzzle and Inventory System**:
   - The room is full of hints and puzzle pieces, such as a safe that needs both a cog and a combination code to open.
   - Inventory items include the **cog**, **combination code**, and **emblem**, all of which can be used to interact with other objects and unlock new information or items.
   - Players must find these items, remember where they might be useful, and combine them with other objects or actions to progress.
   - This mechanic is similar to real escape rooms, where clues and tools are hidden in plain sight and must be used in creative ways.

4. **Detailed Clues and Hidden Messages**:
   - The game includes a series of notes that give clues about the history and context of the room, creating a more immersive experience.
   - For example, the **board** has notes that hint at global conflicts and conspiracies, gradually unfolding a storyline. Players will read through these notes to uncover the **combination code** needed to open the safe.
   - Every note and description adds depth to the room’s backstory, giving players the sense of uncovering layers of mystery as they progress.

5. **Flexible Endings**:
   - Players can exit the game at any time by typing `exit`, allowing them to end the adventure if they’re unable to solve the puzzles.
   - If they do manage to solve all the puzzles and unlock the door, they escape the room and win the game.
   - These multiple outcomes provide both a satisfying victory condition and a realistic option to "give up" on the escape if the puzzles prove too challenging.

### Development and Design:
This project is built entirely in Python, making use of functions and dictionaries to manage game actions, items, and descriptions. Key components include:
- **Item and Inventory Management**: The game uses a global `inventory` list and `found_items` dictionary to track what the player has discovered and whether certain actions have been completed.
- **Puzzle Logic**: Functions handle each action's logic, such as `check_desk()` and `use_cog_on_safe()`, enabling the game to respond dynamically based on player actions and inventory contents.
- **Text Output Control**: The `slow_print` function prints text character-by-character, creating a typewriter effect for enhanced engagement.

### Installation and Setup:
1. Clone or download the project files.
2. Run the `project.py` file using Python.
3. No additional libraries are required beyond standard Python.

### Example Commands:
- To look around: `check surrounding`
- To inspect specific items: `check [item]`
- To use items: `use [inventory item] on [target]`
- To view inventory: `check inventory`
- To quit the game: `exit`

### Update: Transition to Project V2 (Graphical Version)
Building on the foundation of the text-based escape room adventure, Project V2 introduces a visually immersive upgrade using the tkinter library. This new version maintains all the core mechanics and story of the original game, while improving the experience through a sleek, neon-themed graphical interface.

### What’s New in V2:
Feature	Version 1 (CLI)	Version 2 (GUI)
Interface	Console (Text-Based)	Tkinter-based GUI with styled widgets
Visual Theme	ANSI-styled text (bold/italic in terminal)	Black background with neon-orange text & bold/italic tags
Input Method	Command-line prompt	Text field + EXECUTE button
Title Screen	None	ASCII art intro with "Press Any Key to Begin"
Animation	slow_print() character delay	Typing animation in GUI
Additional Items	-	Letter (new lore content in lock box)
New Commands	-	check letter, check lock box
Restart Option	Manual re-run	Restart button after end game

### Why This Update Matters:
Makes the game more accessible and user-friendly by eliminating the terminal dependency.
Enhances immersion through real-time animations, formatted text, and a consistent visual theme.
Opens possibilities for future updates (e.g., sound, drag-and-drop, visual inventory).


The CLI version is still available via project.py for those who prefer a retro-style terminal adventure.

