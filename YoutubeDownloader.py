from pytube import YouTube
# I had to use 'python -m pip install git+https://github.com/Zeecka/pytube@fix_1060' for this to work properly
from pathlib import Path


def YoutubeDownloader(url):
    """
    Downloads the highest resolution video from a YouTube URL and saves it as 'BackgroundVideo.mp4'
    in the 'resources/Mp4' folder.

    Args:
        url (str): The URL of the YouTube video to be downloaded.

    Returns:
        Downloads the highest resolution video from a YouTube video
    """
    Path("resources/Mp4").mkdir(parents=True, exist_ok=True)
    link = url
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()

    ys.download(output_path='resources/Mp4/', filename='BackgroundVideo.mp4')

