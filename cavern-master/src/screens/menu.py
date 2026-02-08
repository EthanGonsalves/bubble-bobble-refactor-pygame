from src.input import InputState
from src.app import ScreenType

class MenuScreen:
    #Menu/title screen for the game.
    
    def __init__(self, app, game=None):
        self.app = app
        #Store game reference for drawing
        self.game = game
        self.timer = 0

    def update(self, input_state: InputState):
        #Update menu screen logic
        self.timer += 1
        
        #Update the game timer for animation
        if self.game:
            self.game.timer += 1
        
        #Start game when space is pressed
        if input_state.jump_pressed:
            #Use app's stored Game and Player classes
            self.app.change_screen(
                ScreenType.PLAY,
                game=self.app.game_class(self.app.player_class())
            )

    def draw(self):
        #Draw the menu screen
        #This will be drawn by the global draw() which also handles the background
        pass
