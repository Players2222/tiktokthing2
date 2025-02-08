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


#creating constants and folders
filename="/tiktokeditorv4.py/"

script_file=__file__+"/script"
video_file=__file__+"/video"
middle_file=__file__+"/middle"
finish_file=__file__+"/finished"
base=__file__+"/"
print(base)

basepath=base.replace("\\","/").replace(filename,"/")
script_file=script_file.replace("\\","/").replace(filename,"/")
video_file=video_file.replace("\\","/").replace(filename,"/")
middle_file=middle_file.replace("\\","/").replace(filename,"/")
finish_file=finish_file.replace("\\","/").replace(filename,"/")

if not os.path.exists(script_file):
            os.mkdir(script_file)

if not os.path.exists(video_file):
            os.mkdir(video_file)

if not os.path.exists(finish_file):
            os.mkdir(finish_file)

if not os.path.exists(middle_file):
            os.mkdir(middle_file)

#tts settings
input_text = script_file+"/script.txt"
text = ""
speaker = "en-US-AndrewNeural"
rate = 0
#infer settings
print(basepath)
pth_path = basepath+"/logs/obama/obamapath.pth"
index_path = basepath+"/logs/obama/obamaindex.index"
input_path = basepath+"/assets/audios/tts_output.wav"
output_path = middle_file+"/tts.wav"

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
        self.start()
    
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
        audio=mutagen.File(middle_file+"/tts.mp3")
        audiolength=int(audio.info.length)
        clip=VideoFileClip(video_file+"/minecraft1.mp4")
        trimmed_video=clip.subclip(0,audiolength+1)
        trimmed_video=trimmed_video.without_audio()
        savepath=middle_file+"/trimmed_video.mp4"
        trimmed_video.write_videofile(savepath) 

        self.videoplusvoice()

    def videoplusvoice(self):
        clip=VideoFileClip(middle_file+"/trimmed_video.mp4")
        audio=AudioFileClip(middle_file+"/tts.mp3")
        trimmed_with_audio = clip.set_audio(audio)
        savepath=middle_file+"/trimmed_video_audio.mp4"
        trimmed_with_audio.write_videofile(savepath)

        self.subtitles()

    def subtitles(self):

        self.videoplussub()
    
    def videoplussub(self):

        self.upload()
    
    def upload(self):
        print("mmm")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Menu()
    window.show()
    sys.exit(app.exec())