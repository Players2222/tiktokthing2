import os
import subprocess
import requests
import time

def check_change(audio):
    last_changed=os.path.getmtime(audio)
    while True:
        time.sleep(1)

        subprocess.run(applio, shell=True)

# r=requests.post("http://127.0.0.1:6969/")
# Check every 1 second

        current_changed = os.path.getmtime(audio)
        if current_changed != last_changed:
            print("File changed!")
            print("File changed!")
            print("File changed!")
            print("File changed!")
            print("File changed!")
            print("File changed!")
            print("File changed!")
            last_changed = current_changed


# if r.status_code == 200:
#     print("Reci")
# else:
#     print("hmm")
    
    exit()

if __name__ == "__main__":
#   Replace with your file path
    applio=__file__.replace(os.path.basename(__file__),"")
    applio=applio.replace("\\","/")
    applio=applio + "run-applio.bat"
    audio=__file__.replace(os.path.basename(__file__),"")
    audio=audio.replace("\\","/")
    audio=audio+"assets/audios/tts_rvc_output.wav"
    check_change(audio)