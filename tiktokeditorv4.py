import os
import sys
import mutagen
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
        applio=os.path

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