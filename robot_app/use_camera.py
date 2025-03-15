import os
import subprocess

def capture_photo(name):
    # Ensure the "images" folder exists
    os.makedirs("images", exist_ok=True)
    
    # Define the command
    command = ["libcamera-still", "-o", f"images/{name}.jpg", "--timeout", "1", "--nopreview"]
    
    # Run the command
    try:
        subprocess.run(command, check=True)
        print("Photo captured successfully: images/test.jpg")
    except subprocess.CalledProcessError as e:
        print(f"Error capturing photo: {e}")


