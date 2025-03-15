import os
import time


def play_mp3(name):
    os.system(f"cvlc -A alsa --alsa-audio-device hw:2,0 --play-and-exit audio/{name}.mp3")

def set_volume(percent=90):
    os.system(f"amixer -c 2 cset numid=3 {str(percent)}%")

def startup_sound():
    set_volume(90)
    for i in range(3):
        play_mp3("beep")
        time.sleep(0.5)
    play_mp3("fart1")

if __name__ == "__main__":
    startup_sound()