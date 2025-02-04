import os
import sys
# import mutagen
import random
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from textwrap import wrap
from ui_menu import Ui_Main_menu
from gtts import gTTS
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
from moviepy.config import change_settings 
change_settings({"IMAGEMAGICK_BINARY": "C:\\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})


class Menu(QMainWindow,Ui_Main_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()
    def setup(self):
        filename="/tiktokeditorv3.py/"

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
        script=script_file+"/"+self.ScriptList.currentText()
        video=video_file+"/"+self.VideoList.currentText()
        self.voiceover(script,video)

    def voiceover(self,script_file,video):
        accent="en"
        with open(script_file,"r") as temp:
            script = temp.read()
        tts = gTTS(script, lang=accent)
        voiceover_name = "voiceovertemp.mp3"
        tts.save(voiceover_name)
        self.cutvideo(voiceover_name,script,video)

    def cutvideo(self,voiceover_name,script,video):
        audiol=mutagen.File(voiceover_name)
        audiolength=int(audiol.info.length)

        # videol=mutagen.File(video)
        # videolength=int(videol.info.length)
        clip=VideoFileClip(video)

        new_video=clip.subclip(0,audiolength+1)

        new_video=new_video.without_audio()

        # audioclip= AudioFileClip("voiceovertemp.mp3")
        # new_audio=CompositeVideoClip([audioclip])
        # new_video.audio=new_audiosc   q
        new_video.write_videofile("trimmed_video.mp4") 

        video_dir="trimmed_video.mp4"
        #I still have to make a text that shows the directory of the trimmed video

        # remove audio



        self.subtitles(script,video_dir,audiolength)

    def subtitles(self,script,video,audiolength):
        sentences = wrap(script,30)

        global subtitles
        subtitles = []
        start_time = 0
        
        for sentence in sentences:
            duration = 2
            subtitles.append({
                'text': sentence ,
                'start': start_time,
                'end': start_time + duration
            })
            start_time += duration
        self.subtitle_to_vid(video)
    def subtitle_to_vid(self,video):
        
        vid=VideoFileClip(video)

        subtitle_clips = []

        for subtitle in subtitles:  
            txt_clip = TextClip(subtitle['text'], fontsize=24, font="Ariel Bold", color='white', stroke_color='black', stroke_width=0.5)
            txt_clip = txt_clip.set_position(('center', 'center')).set_duration(subtitle['end'] - subtitle['start'])
            txt_clip = txt_clip.set_start(subtitle['start'])
            subtitle_clips.append(txt_clip)

        video = CompositeVideoClip([vid] + subtitle_clips)
        video.write_videofile("tempvid.mp4", codec='libx264')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Menu()
    window.show()
    sys.exit(app.exec())