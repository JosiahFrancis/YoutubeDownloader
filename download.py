#to turn into and EXE run auto-py-to-exe

from tkinter import *
from tkinter import filedialog
from moviepy import *
#from moviepy.editor import VideoFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from pytube import YouTube

import shutil
import ctypes
import os

#functions
def select_path():
    #allows user to select a path from explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def alert(title,message):
    ctypes.windll.user32.MessageBoxW(0,message, title, 0)


def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    print(user_path)
    if user_path == "Select Path For Download":
        alert("Error", "Missing File Path!")
    else:
        screen.title('Downloading...')
        #Download video
        mp4_video = YouTube(get_link).streams.get_highest_resolution.download(os.getcwd())
        vid_clip = VideoFileClip(mp4_video)
        vid_clip.close()
        #Move file to selected directory
        shutil.move(mp4_video, user_path)
        screen.title('Download Complete!')

def download_audio():
    #get User Path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")

    if user_path == "Select Path For Download":
        alert("Error", "Missing File Path!")
    else:
        screen.title('Downloading...')
        #Download Audio
        mp4_audio = YouTube(get_link).streams.filter(only_audio=True).first().download()
        shutil.move(mp4_audio, user_path)
        screen.title('Download Complete!')

screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image Logo
logo_imp = PhotoImage(file='img/Yt.png')
#resize
logo_imp = logo_imp.subsample(8,8)
canvas.create_image(250, 80, image=logo_imp)

#link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 15))

#select Path for saving video
path_label = Label(screen, text="Select Path For Download", font=('Arial', 15))
select_btn = Button(screen, text="Select File Path", command=select_path)

#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#add widgets to window
canvas.create_window(250,170, window=link_label)
canvas.create_window(250,220, window=link_field)

#download btns
download_Vid_btn = Button(screen, text="Download Video", command=download_file)
download_audio_btn = Button(screen, text="Download Audio", command=download_audio)
#add to canvas
canvas.create_window(250, 380, window=download_Vid_btn)
canvas.create_window(250, 430, window=download_audio_btn)

screen.mainloop()