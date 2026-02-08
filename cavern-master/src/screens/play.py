from src.input import InputState
from src.app import ScreenType

class PlayScreen:
    #Main gameplay screen - runs the actual game.
    
    def __init__(self, app, game):
        self.app = app
        self.game = game
        self.paused = False

    def update(self, input_state: InputState):
        #Update gameplay logic
        
        #Handle pause toggle
        if input_state.pause_pressed:
            self.paused = not self.paused
        
        #Only update game if not paused
        if not self.paused:
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
                # Pass the current game instance so the GameOver screen can draw the final scene
                self.app.change_screen(ScreenType.GAME_OVER, game=self.game)

    def draw(self):
        #Draw the gameplay screen
        #Game draws itself with game.draw()
        #This is called from the global draw() function
        pass

    def is_paused(self) -> bool:
        #Check if the game is currently paused
        return self.paused
