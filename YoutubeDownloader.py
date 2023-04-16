from pytube import YouTube
# I had to use 'python -m pip install git+https://github.com/Zeecka/pytube@fix_1060' for this to work properly
from pathlib import Path
import os
basedir = os.path.dirname(__file__)
def YoutubeDownloader(url):
    Path(os.path.join(basedir, "resources", "Mp4")).mkdir(parents=True, exist_ok=True)
    link = url
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()

    ys.download(output_path=os.path.join(basedir, "resources", "Mp4"), filename='BackgroundVideo.mp4')
    # print("Title: ",yt.title)
    # print("Number of views: ",yt.views)
    # print("Length of video: ",yt.length,"seconds")
    # print("Description: ",yt.description)
