import os
import subprocess


applio=__file__.replace(os.path.basename(__file__),"")
applio=applio.replace("\\","/")
applio=applio + "run-applio.bat"
audio=__file__.replace(os.path.basename(__file__),"")
audio=audio.replace("\\","/")
audio=audio+"assets/audios/tts_rvc_output.wav"


ap=subprocess.Popen(applio, shell=True)
id=ap.pid
exit()
print(id)

# r=requests.post("http://127.0.0.1:6969/")
# Check every 1 second

# if r.status_code == 200:
#     print("Reci")
# else:
#     print("hmm")
    


