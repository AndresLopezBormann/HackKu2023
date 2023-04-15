
from moviepy.editor import *
from SentenceSplitter import SentenceSplitter
from pathlib import Path

# Text in MoviePy depends on ImageMagick and Wand - https://imagemagick.org/script/download.php#windows

# currently depends on folder of audio clips of single sentences

def BuildVideo(video1, video2, text_arr, path_to_audio, final_video):
    Path("resources/Result").mkdir(parents=True, exist_ok=True)
    clip1 = VideoFileClip(video1)
    clip2 = VideoFileClip(video2)
    # make quality worse
    if clip1.h <= 1100:
        clip1 = clip1.resize(width=1920/2, height=1080/2)
        clip2 = clip2.resize(width=1920/2, height=1080/2)
        # Put videos on top of eachother and crop
        final_clip = clips_array([[clip1], [clip2]])
        final_clip = final_clip.resize(height=1920/2)
        final_clip = final_clip.crop(x1=((1920/2)/4),y1=0,x2=((1920/2) - ((1920/2)/4)),y2=(1920/2))
    else:
        clip1 = VideoFileClip(video1).resize(width=1080/2, height=1920/2)
        clip2 = VideoFileClip(video2).resize(width=1080/2, height=1920/2)
        # Put videos on top of eachother and crop
        clip1 = clip1.crop(x1=0,y1=240,x2=1080/2,y2=720)
        clip2 = clip2.crop(x1=0,y1=240,x2=1080/2,y2=720)
        final_clip = clips_array([[clip1], [clip2]])
        final_clip = final_clip.resize(height=960)

    audio = AudioFileClip(path_to_audio + "FullAudio.mp3")
    final_clip = final_clip.set_audio(audio)
    final_clip = final_clip.set_duration(audio.duration)

    # make audio and subtitles
    start_time = 0
    audio_index = 1
    for sentence in text_arr:
        # Create the audio clip
        print("audio path: " + path_to_audio + "Sentence" + str(audio_index) + '.mp3')
        audio_clip = AudioFileClip(path_to_audio + "Sentence" + str(audio_index) + '.mp3', fps = 20)
        
        #add necessary newlines
        modified_text = ''
        char_line_count = 0
        for i in range(len(sentence)):
            char_line_count += 1
            if char_line_count > 25 and sentence[i] == ' ':
                modified_text += '\n'
                char_line_count = 0
            else:
                modified_text += sentence[i]


        # Create the subtitle clip
        subtitle_clip = TextClip(modified_text, fontsize=25, color='white', bg_color='black', font='Arial-Bold')
        subtitle_clip = subtitle_clip.set_start(start_time)
        subtitle_clip = subtitle_clip.set_duration(audio_clip.duration)
        subtitle_clip = subtitle_clip.set_end(start_time + audio_clip.duration)
        subtitle_clip = subtitle_clip.set_position(('center', 'top'))

        # Add the audio and subtitle to the video
        updated_clip = CompositeVideoClip([final_clip, subtitle_clip])
        #updated_clip = CompositeVideoClip([clip1, audio_clip])

        # Increment the start time
        start_time += audio_clip.duration
        final_clip = updated_clip
        audio_index += 1

    # Write the final video to disk
    final_clip.write_videofile("resources/Result/"+final_video, fps=24, threads=16, audio_codec="aac") 
    clip1.close()
    clip2.close()


if __name__ == '__main__':
    # Create the video clip
    clip1 = VideoFileClip('resources/video.mp4')
    clip2 = VideoFileClip('resources/video.mp4')
    sentence_array = SentenceSplitter()
    path_to_audio = 'resources/Mp3/'

    # Write the final video to disk
    BuildVideo(clip1, clip2, sentence_array, path_to_audio, 'final_video.mp4')
