from src.input import InputState
from src.app import ScreenType

class GameOverScreen:
    #Game Over screen - shown when the player runs out of lives.
    
    def __init__(self, app, game=None):
        self.app = app
        self.game = game

    def update(self, input_state: InputState):
        #Update game over screen logic
        
        #Return to menu when space is pressed
        if input_state.jump_pressed:
            #Switch to menu screen with a fresh game (no player)
            menu_game = self.app.game_class() if self.game else None
            self.app.change_screen(
                ScreenType.MENU,
                game=menu_game
            )

    def draw(self):
        #Draw the game over screen
        #This will be drawn by the global draw() which also handles the background
        pass
