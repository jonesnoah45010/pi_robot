import os
import time


# installed voices = (kal_diphone)


def wait_for_file(filename, timeout=5, check_interval=0.1):
    """Waits for the file to exist, checking every check_interval seconds."""
    start_time = time.time()
    while not os.path.exists(filename):
        if time.time() - start_time > timeout:
            print(f"Timeout: {filename} not found")
            return False
        time.sleep(check_interval)
    return True


def text_to_speech_to_wav(text, filename="tts.wav", voice="kal_diphone"):
    os.system(f"rm -f {filename}")
    #c = f'echo "{text}" | text2wave -o {filename}'
    c = f'echo "{text}" | text2wave -eval "(voice_{voice})" -o {filename}'
    os.system(c)
    return filename


def play_audio(filename):
    os.system(f"cvlc -A alsa --alsa-audio-device hw:2,0 --play-and-exit {filename}")


def set_volume(percent=90):
    os.system(f"amixer -c 2 cset numid=3 {str(percent)}%")


def say(text):
    f = text_to_speech_to_wav(text)
    
    # Wait for the file to be created before playing it
    if wait_for_file(f):
        play_audio(f)






if __name__ == "__main__":
    set_volume()
    say("I am a robot that can talk")






















