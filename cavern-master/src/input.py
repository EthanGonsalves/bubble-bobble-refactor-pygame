from dataclasses import dataclass

@dataclass
class InputState:
    #Snapshot of input state for the current frame.
    #Distinguishes between edge-detected (pressed/released) and level-detected (held) inputs.

    left: bool = False
    right: bool = False
    up: bool = False
    jump_pressed: bool = False  #Edge-detected: pressed this frame
    fire_pressed: bool = False  #Edge-detected: pressed this frame
    fire_held: bool = False     #Level-detected: currently held down
    pause_pressed: bool = False #Edge-detected: pressed this frame

    def get_horizontal_direction(self) -> int:
        #Returns -1 for left, 1 for right, 0 for no movement.
        #If both left and right are pressed, returns 0.

        if self.left and self.right:
            return 0
        elif self.left:
            return -1
        elif self.right:
            return 1
        return 0


class InputManager:
    #Manages input state and edge detection across frames.

    def __init__(self):
        self._prev_space_down = False
        self._prev_p_down = False

    def update(self, keyboard) -> InputState:
        #Capture current keyboard state and compute edge-detected values.
        #Must be called once per frame before any input is consumed.
        
        #Get current frame's basic key states
        left = keyboard.left
        right = keyboard.right
        up = keyboard.up
        space = keyboard.space
        p_key = keyboard.p

        #Edge detection for space (jump/fire)
        space_pressed = space and not self._prev_space_down

        #Edge detection for P (pause)
        pause_pressed = p_key and not self._prev_p_down

        #Update previous states for next frame
        self._prev_space_down = space
        self._prev_p_down = p_key

        return InputState(
            left=left,
            right=right,
            up=up,
            jump_pressed=space_pressed,
            fire_pressed=space_pressed,
            fire_held=space,
            pause_pressed=pause_pressed,
        )
