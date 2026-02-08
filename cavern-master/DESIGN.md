DESIGN: Bubble Bobble/Cavern Master (refactor)

Screens architecture
- The app uses `src.app.App` to manage the active screen. Screens are classes responsible for updating and drawing their own view:
  - `MenuScreen` — non-interactive menu, starts a `Game` instance when played.
  - `PlayScreen` — contains `Game` instance and routes player input into the `Game`/`Player` classes. Maintains a `paused` flag to suspend updates.
  - `GameOverScreen` — displays game-over state; can draw the final `Game` snapshot passed in on transition.

Input design
- `src/input.py` provides `InputState` (per-frame snapshot) and `InputManager` which performs edge-detection (pressed this frame) for keys like jump/fire (space) and pause (P). Each frame `App.update()` requests the current `InputState` from the `InputManager` and forwards it to the active screen.

How Pause works
- Pause is implemented in `PlayScreen` as a boolean `paused` toggled when `InputState.pause_pressed` is true. When paused, `PlayScreen.update()` skips `game.update()` and the player input application, effectively freezing game state while allowing the screen to continue receiving input to unpause.

Design rationale (brief)
- Separating screens and handling input in one place simplifies state transitions and keeps `Game`/`Player` logic independent of keyboard handling, making unit testing and future controllers easier to add.
