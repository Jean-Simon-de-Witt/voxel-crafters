Installation and Setup:
1. Ensure Python 3.10 or higher is installed.
2. Install the required libraries using the following command: pip install -r requirements.txt
3. Launch the game with: python main.py

Architecture Overview:
1. main.py: The entry point and main Pygame loop.
2. states.py: The game's different states used by the GameState Engine.
3. Player.py: Handles player movement, physics, collision detection, and raycasting.
4. ui.py Manages 2D Pygame to 3D OpenGL rendering for buttons, labels, and the hotbar.

Controls:
1. W, A, S, D: Directional movement (Forward, Left, Backward, Right)
2. Mouse Movement: Look Around
3. Left Mouse Button: Break Block
4. Right Mouse Button: Place Block
5. Keys 1 - 4: Select a block from the hotbar (Grass, Stone, Wood, Leaves)
6. Esc: Pause the Game