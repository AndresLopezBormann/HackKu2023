from pytube import YouTube
# I had to use 'python -m pip install git+https://github.com/Zeecka/pytube@fix_1060' for this to work properly


def YoutubeDownloader(url):
# link = input("Enter the link: ")
    link = url
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path='resources', filename='BackgroundVideo.mp4')


    # print("Title: ",yt.title)
    # print("Number of views: ",yt.views)
    # print("Length of video: ",yt.length,"seconds")
    # print("Description: ",yt.description)
