
import time
import sys
from use_camera import capture_photo
from use_servos import stop, forward, backward, left, right, forward_step, backward_step, left_step, right_step
from use_dist_sensor import start_dist_sensor, stop_dist_sensor, get_dist
from use_speaker import play_mp3
from use_keyboard import get_current_key
from use_drive_controller import drive_controller

def key_test():
    while True:
        key = get_current_key()
        if key:
            print(f"Last key pressed: {key}")
        time.sleep(0.1)  # Reduce CPU usage

if __name__ == "__main__":
    stop()
    start_dist_sensor()
    
    driver = drive_controller()
    print("MANUAL DRIVE MODE")
    while True:
        key = get_current_key()
        if key == "KEY_UP":
            driver.forward()
        elif key == "KEY_RIGHT":
            driver.right()
        elif key == "KEY_LEFT":
            driver.left()
        elif key == "KEY_DOWN":
            driver.backward()
        elif key == "KEY_SPACE":
            driver.stop()
        elif key == "KEY_ESC":
            print("END MANUAL DRIVE MODE")
            driver.stop()
            break
        else:
            driver.stop()
        time.sleep(0.1)
        
    



