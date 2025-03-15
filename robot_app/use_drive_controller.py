


from use_servos import stop, forward, backward, left, right, forward_step, backward_step, left_step, right_step
from use_keyboard import get_current_key
import time


class drive_controller:
    def __init__(self):
        self.current_movement = None
    
    
    def stop(self):
        self.current_movement = None
        stop()
        
    def forward(self):
        self.current_movement = "forward"
        forward()
    
    def backward(self):
        self.current_movement = "backward"
        backward()
    
    
    def left(self):
        self.current_movement = "left"
        left()
    
    def right(self):
        self.current_movement = "right"
        right()


        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
