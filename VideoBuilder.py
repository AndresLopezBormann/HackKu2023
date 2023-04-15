
from moviepy.editor import *
from SentenceSplitter import SentenceSplitter

# Text in MoviePy depends on ImageMagick and Wand - https://imagemagick.org/script/download.php#windows

# currently depends on folder of audio clips of single sentences

def BuildVideo(video1, video2, text_arr, path_to_audio, final_video):
    # make quality worse
    clip1 = VideoFileClip(video1).resize(width=1920/2, height=1080/2)
    clip2 = VideoFileClip(video2).resize(width=1920/2, height=1080/2)

    #audio = CompositeAudioClip([concatenate_audioclips(audio_clips)]).subclip(0, clip1.duration)
    audio = AudioFileClip(path_to_audio + "FullAudio.mp3")
    # Put videos on top of eachother and crop
    final_clip = clips_array([[clip1], [clip2]])
    final_clip = final_clip.set_audio(audio)
    final_clip = final_clip.resize(height=1920)
    final_clip = final_clip.set_duration(audio.duration)
    final_clip = final_clip.crop(x1=(1920/4),y1=0,x2=(1920 - (1920/4)),y2=1920)

    # make audio and subtitles
    start_time = 0
    audio_index = 1
    for sentence in text_arr:
        # Create the audio clip
        print("audio path: " + path_to_audio + "Sentence" + str(audio_index) + '.mp3')
        audio_clip = AudioFileClip(path_to_audio + "Sentence" + str(audio_index) + '.mp3', fps = 20)

        # Create the subtitle clip
        subtitle_clip = TextClip(sentence, fontsize=30, color='white')
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
    final_clip.write_videofile(final_video, fps=24, threads=16, audio_codec="aac") 


if __name__ == '__main__':
    # Create the video clip
    clip1 = VideoFileClip('resources/video.mp4')
    clip2 = VideoFileClip('resources/video.mp4')
    sentence_array = SentenceSplitter()
    path_to_audio = 'resources/Mp3/'

    # Write the final video to disk
    BuildVideo(clip1, clip2, sentence_array, path_to_audio, 'final_video.mp4')
