from pytube import YouTube
from pydub import AudioSegment
import os
import sys

def download_audio(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).last()
    output_file = video.download(".")
    return (output_file, yt.title)

def download_video(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_video=True).first()
    output_file = video.download(".")
    return (output_file, yt.title)

def file_to_mp3(data):
    audio = AudioSegment.from_file(data[0])
    audio.export(data[1] + ".mp3", format="mp3")



def yttmp3(url, audioOnly):
    global download_data
    if audioOnly:
        download_data = download_audio(url)
        file_to_mp3(download_data)
        if os.path.exists(download_data[1] + ".webm"):
            os.remove(download_data[1] + ".webm")
        elif os.path.exists(download_data[1] + ".mp4"):
            os.remove(download_data[1] + ".mp4")
    else:
        download_data = download_video(url)



