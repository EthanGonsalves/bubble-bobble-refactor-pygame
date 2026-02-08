from enum import Enum
from src.input import InputManager, InputState

class ScreenType(Enum):
    MENU = "menu"
    PLAY = "play"
    GAME_OVER = "game_over"

class App:
    #Main application class that manages screens and game flow.
    
    def __init__(self, game_class=None, player_class=None):
        self.current_screen = None
        self.input_manager = InputManager()
        self._change_screen_to = None  # Used to queue screen changes
        #Store references to Game and Player classes to avoid reimporting
        self.game_class = game_class
        self.player_class = player_class

    def change_screen(self, screen_type: ScreenType, **kwargs):
        #Queue a screen change to happen at the end of the current update.
        #kwargs: Additional arguments to pass to the screen constructor.
        self._change_screen_to = (screen_type, kwargs)

    def _process_screen_change(self):
        #Process any queued screen changes
        if self._change_screen_to:
            screen_type, kwargs = self._change_screen_to
            self._change_screen_to = None
            
            #Import here to avoid circular imports
            if screen_type == ScreenType.MENU:
                from src.screens.menu import MenuScreen
                self.current_screen = MenuScreen(self, **kwargs)
            elif screen_type == ScreenType.PLAY:
                from src.screens.play import PlayScreen
                self.current_screen = PlayScreen(self, **kwargs)
            elif screen_type == ScreenType.GAME_OVER:
                from src.screens.gameover import GameOverScreen
                self.current_screen = GameOverScreen(self, **kwargs)

    def update(self, keyboard):
        #Update the current screen
        input_state = self.input_manager.update(keyboard)
        
        if self.current_screen:
            self.current_screen.update(input_state)
        
        #Process any screen changes that were queued during update
        self._process_screen_change()

    def draw(self):
        #Draw the current screen
        if self.current_screen:
            self.current_screen.draw()
