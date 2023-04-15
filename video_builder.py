
from moviepy.editor import *


def build_video(video1, video2, final_video):
    # make quality worse
    clip1 = video1.resize(width=1920/2, height=1080/2)
    clip2 = video2.resize(width=1920/2, height=1080/2)

    # Put cideos on top of eachother and crop
    final_clip = clips_array([[clip1], [clip2]])
    final_clip = final_clip.resize(height=1920)
    final_clip = final_clip.crop(x1=(1920/4),y1=0,x2=(1920 - (1920/4)),y2=1920)

    # Write the final video to disk
    final_clip.write_videofile(final_video,fps=20,threads=16,codec="mpeg4",preset="slow",ffmpeg_params=['-b:v','10000k'])


if __name__ == '__main__':
    # Create the video clip
    clip1 = VideoFileClip('resources/video.mp4')
    clip2 = VideoFileClip('resources/video.mp4')

    # Write the final video to disk
    build_video(clip1, clip2, 'final_video.mp4')
