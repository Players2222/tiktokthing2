import os
import sys
import csv
import praw
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


reddit = praw.Reddit(
    client_id="l8nzxC1a_GSPVDmVR4UI2g",
    client_secret="9RJM4I6RUNPkC_i3RXpQuMQx-LCK1A",
    user_agent="MerMer by /u/Comfortable-Sky6282",
    username="Comfortable-Sky6282",
    password="Aalywbwdy830312@"
)

# subreddits=["AITAH","Creepypasta","TwoHotTakes"]

subreddits=["AITAH"]

filename="/testing2.py/"

script_file=__file__+"/script"

script_file=script_file.replace("\\","/").replace(filename,"/")


limit=1
for sub in subreddits:
    csv_filename = script_file+"/"+sub+'_output.csv'

    print(script_file)
    print(csv_filename)


    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)

        writer.writerow(['Title', 'Post Content'])

        subreddit = reddit.subreddit(sub)

        for submission in subreddit.new(limit=limit):
            title = submission.title
            post=submission.selftext

            writer.writerow([title, post])
            print({title})
            print("-" * 40)
            time.sleep(2)


    # with open(csv_filename, mode='r', newline='', encoding='utf-8') as temp:
        # reader=csv.DictReader(temp)
        script=post
        print(type(script))
        sentences = wrap(script,20)

        global subtitles
        subtitles = []
        start_time = 0

        for sentence in sentences:
            duration = 1.2
            subtitles.append({
                'text': sentence ,
                'start': start_time,
                'end': start_time + duration
            })
            start_time += duration
            # print(f"Title: {title}")
            # print(f"POST: {post}")

            print(subtitles)