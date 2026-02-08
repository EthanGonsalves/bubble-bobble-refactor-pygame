# Bubble Bobble/Cavern Master (refactor)

Repository: https://github.com/EthanGonsalves/bubble-bobble-refactor-pygame.git

## Prerequisites
- Python 3.8+ installed
- pip

## Run the game
From the repository root run:

python cavern.py

## Tests
There are no automated tests included in this repository. To run tests if added, use:

pytest

## Short summary of architectural changes
- Added `src.app.App` to manage screen lifecycle and move screen creation out of the global script.
- Split UI into screen classes under `src/screens/` (`menu`, `play`, `gameover`) so each screen owns update/draw logic.
- Added `src/input.py` with `InputManager`/`InputState` to handle input press detection and state for each frame.
- Kept game logic in `cavern.py` but refactored initialization to use `App` and separate `Game`/`Player` classes where appropriate.
- Result: clearer separation (input, screens, game logic) and easier testing
