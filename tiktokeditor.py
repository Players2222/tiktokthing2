import os 
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui_menu import Ui_Main_menu
from gtts import gTTS
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.config import change_settings 
change_settings({"IMAGEMAGICK_BINARY": "C:\\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})

class Menu(QMainWindow,Ui_Main_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()
    def setup(self):
        #path directory for video and script
        script_file=__file__+"/script"
        video_file=__file__+"/video"
        finish_file=__file__+"/finished"
        global new_script_file,new_video_file,new_finish_file
        new_script_file=script_file.replace("\\","/").replace("/tiktokeditor.py/","/")
        new_video_file=video_file.replace("\\","/").replace("/tiktokeditor.py/","/")
        new_finish_file=finish_file.replace("\\","/").replace("/tiktokeditor.py/","/")

        if not os.path.exists(new_script_file):
            os.mkdir(new_script_file)

        if not os.path.exists(new_video_file):
            os.mkdir(new_video_file)

        if not os.path.exists(new_finish_file):
            os.mkdir(new_finish_file)

        script_dir=QDir(new_script_file)
        script_dir.setFilter(QDir.Files)
        script_dir.setNameFilters(["*.txt"])
        scripts = script_dir.entryList()
        self.ScriptList.addItems(scripts)

        video_dir=QDir(new_video_file)
        video_dir.setFilter(QDir.Files)
        video_dir.setNameFilters(["*.mp4"])
        videos = video_dir.entryList()
        self.VideoList.addItems(videos)

        self.StartB.clicked.connect(self.start)
    
    def start(self):
        script=new_script_file+"/"+self.ScriptList.currentText()
        video=new_video_file+"/"+self.VideoList.currentText()
        print(video)
        self.voiceover(script)
        self.sub_to_vid(video)
        print("hmmm")
    
    def voiceover(self,script_file):
        accent="en"
        with open(script_file,"r") as temp:
            script = temp.read()
        tts = gTTS(script, lang=accent)
        voiceover_name = "voiceovertemp.mp3"
        tts.save(voiceover_name)

        self.subtitles(script)
    
    def subtitles(self,script):
        sentences = script.split(". ")
    
        global subtitles
        subtitles = []
        start_time = 0
        
        for sentence in sentences:
            duration = 5
            subtitles.append({
                'text': sentence + ".",
                'start': start_time,
                'end': start_time + duration
            })
            start_time += duration

    def sub_to_vid(self,video):
        
        vid=VideoFileClip(video)

        subtitle_clips = []

        for subtitle in subtitles:
            txt_clip = TextClip(subtitle['text'], fontsize=24, font="Ariel Bold", color='white', stroke_color='black', stroke_width=0.5)
            txt_clip = txt_clip.set_position(('center', 'bottom')).set_duration(subtitle['end'] - subtitle['start'])
            txt_clip = txt_clip.set_start(subtitle['start'])
            subtitle_clips.append(txt_clip)

        video = CompositeVideoClip([vid] + subtitle_clips)
        video.write_videofile("tempvid.mp4", codec='libx264')


# def main():
#     pass



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=Menu()
    window.show()
    sys.exit(app.exec())
