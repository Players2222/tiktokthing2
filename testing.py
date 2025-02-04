import os
import subprocess
import requests

applio=__file__.replace(os.path.basename(__file__),"")
applio=applio.replace("\\","/")
applio=applio + "/run-applio.bat"

# data={
# }

r=requests.post("http://127.0.0.1:6969/")

process=subprocess.Popen(applio)

