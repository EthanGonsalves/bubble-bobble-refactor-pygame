from src.input import InputState
from src.app import ScreenType

class PlayScreen:
    #Main gameplay screen - runs the actual game.
    
    def __init__(self, app, game):
        self.app = app
        self.game = game

    def update(self, input_state: InputState):
        #Update gameplay logic
        
        #Update game every frame
        self.game.update()
        
        #Apply input to the player
        if self.game.player:
            dx = input_state.get_horizontal_direction()
            self.game.player.apply_input(
                dx=dx,
                jump_pressed=input_state.up,  #UP key for jumping
                fire_pressed=input_state.fire_pressed,
                fire_held=input_state.fire_held
            )
        
        #Check for game over
        if self.game.player and self.game.player.lives < 0:
            self.game.play_sound("over")
            self.app.change_screen(ScreenType.GAME_OVER)

    def draw(self):
        #Draw the gameplay screen
        #Game draws itself with game.draw()
        #This is called from the global draw() function
        pass
