import os
import sys
import mutagen
import random
import asyncio
import time
import edge_tts
from rvc.infer.infer import VoiceConverter
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from textwrap import wrap
from ui_menu import Ui_Main_menu
from gtts import gTTS
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
from moviepy.config import change_settings 
change_settings({"IMAGEMAGICK_BINARY": "C:\\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})

#tts settings
input_text = "C:/Users/DongYu/Desktop/things/code/python_projects/Capcut/script/script.txt"
text = ""
speaker = "en-US-AndrewNeural"
rate = 0
#infer settings
pth_path = "C:/Users/DongYu/Desktop/things/code/python_projects/Capcut/logs/obama/obamapath.pth"
index_path = "C:/Users/DongYu/Desktop/things/code/python_projects/Capcut/logs/obama/obamaindex.index"
input_path = "C:/Users/DongYu/Desktop/things/code/python_projects/Capcut/assets/audios/tts_output.wav"
output_path = "C:/Users/DongYu/Desktop/things/code/python_projects/Capcut/assets/audios/infer_out.wav"

pitch = 0
filter_radius = 3
index_rate = 0.75
volume_envelope = 1
protect = 0.5
hop_length = 128
f0_method = "rmvpe"
split_audio = False
f0_autotune = False
clean_audio = True
clean_strength = 0.5
export_format = "MP3"
upscale_audio = True
f0_file = None
embedder_model = "contentvec"
embedder_model_custom = None

async def main(text):
    rates = f"+{rate}%" if rate >= 0 else f"{rate}%"
    start_time1 = time.time()
    await edge_tts.Communicate(
        text,
        speaker,
        rate=rates,
    ).save(input_path)
    elapsed_time = time.time() - start_time1
    print(f"TTS gen time in {elapsed_time:.2f} seconds.")

class Menu(QMainWindow,Ui_Main_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()
    def setup(self):
        filename="/tiktokeditorv4.py/"

        global script_file, video_file, finish_file

        script_file=__file__+"/script"
        video_file=__file__+"/video"
        finish_file=__file__+"/finished"

        script_file=script_file.replace("\\","/").replace(filename,"/")
        video_file=video_file.replace("\\","/").replace(filename,"/")
        finish_file=finish_file.replace("\\","/").replace(filename,"/")

        if not os.path.exists(script_file):
            os.mkdir(script_file)

        if not os.path.exists(video_file):
            os.mkdir(video_file)

        if not os.path.exists(finish_file):
            os.mkdir(finish_file)

        script_dir=QDir(script_file)
        script_dir.setFilter(QDir.Files)
        script_dir.setNameFilters(["*.txt"])
        scripts = script_dir.entryList()
        self.ScriptList.addItems(scripts)

        video_dir=QDir(video_file)
        video_dir.setFilter(QDir.Files)
        video_dir.setNameFilters(["*.mp4"])
        videos = video_dir.entryList()
        self.VideoList.addItems(videos)

        self.StartB.clicked.connect(self.start)
    
    def start(self):
        print("Starting!")
        self.webscrape()
    
    def webscrape(self):

        self.voiceover()

    def voiceover(self):
        with open(input_text, 'r') as file:
            text = file.read()
        
        asyncio.run(main(text))

        start_time1 = time.time()
        infer_pipeline = VoiceConverter()
        infer_pipeline.convert_audio(
            pitch=pitch,
            filter_radius=filter_radius,
            index_rate=index_rate,
            volume_envelope=volume_envelope,
            protect=protect,
            hop_length=hop_length,
            f0_method=f0_method,
            audio_input_path=input_path,
            audio_output_path=output_path,
            model_path=pth_path,
            index_path=index_path,
            split_audio=split_audio,
            f0_autotune=f0_autotune,
            clean_audio=clean_audio,
            clean_strength=clean_strength,
            export_format=export_format,
            upscale_audio=upscale_audio,
            f0_file=f0_file,
            embedder_model=embedder_model,
            embedder_model_custom=embedder_model_custom,
        )
        elapsed_time = time.time() - start_time1
        print(f"Inference time in {elapsed_time:.2f} seconds.")

        self.cutvideo()

    def cutvideo(self):

        self.videoplusvoice()

    def videoplusvoice(self):

        self.subtitles()

    def subtitles(self):

        self.videoplussub()
    
    def videoplussub(self):

        self.upload()
    
    def upload(self):
        pass

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Menu()
    window.show()
    sys.exit(app.exec())