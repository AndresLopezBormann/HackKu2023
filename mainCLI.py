from RedditGetter import GetRedditPost
from ChatGPT import ChatGPT_Prompt
from FreeTextToSpeech import TextToMp3 
from TextToSpeech import TextToSpeech
from YoutubeDownloader import YoutubeDownloader
from SentenceSplitter import SentenceSplitter
from VideoBuilder import BuildVideo
from Cleaner import Cleaner
import os
def main():

    #Gets Required information from user
    reddit_url = input("Enter the url of a reddit post you would like to use: ")
    num_comments = int(input("Enter the amount of comments you would like to include: "))
    ChatGPT_prompt = input("Enter the ChatGPT_Prompt you would like to use: ")

    #Gets Reddit post
    reddit_object = GetRedditPost(reddit_url, num_comments)

    #Formatting post for ChatGPT
    comments = ''
    for i in range(num_comments):
        comments += f"\n{reddit_object['comments'][i]['comment_body']}"
    text = f"Title: {reddit_object['title']}\nBody: {reddit_object['body']}\nComments: {comments}"

    # SPELLING_AND_GRAMMAR_FIX = "Fix the spelling and punctuation of this post" 
    # text = ChatGPT_Prompt(SPELLING_AND_GRAMMAR_FIX, text)['choices'][0]['message']['content']

    text = ChatGPT_Prompt(ChatGPT_prompt, text)['choices'][0]['message']['content']
    file = open("resources/text_promt.txt", "w")
    file.write(text)
    file.close()

    input("Check resources/text_promt.txt if you want to make any changes! When you are done press enter to continue...")
    file = open("resources/text_promt.txt", "r")
    text = file.read()
    file.close()
    os.remove("resources/text_promt.txt")
    print(text)
    # Splits the text into sentences
    text_list = SentenceSplitter(text)
    num_sentences = len(text_list)

    #Turns sentences into mp3 files
    voice_name = ["Biden", "Trump", "Freeman", "Rogan", "Musk", "Dumbledore", "Elizabeth", "Ferrell"]
    voice_choice = int(input("Whose voice would you like to use for this creation? (Enter a number 0-7) \n0\tJoe Biden\n1\tDonald Trump\n2\tMorgan Freeman\n3\tJoe Rogan\n4\tElon Musk\n5\tAlbus Dumbledore\n6\tQueen Elizabeth\n7\tWill Ferrell\n\n"))

    print("Voice Chosen: " + voice_name[voice_choice])
    for i in range(num_sentences):
        TextToSpeech(voice_name=voice_name[voice_choice], text=text_list[i], Filename="Sentence"+str(i+1))
    #     # TextToMp3(text_list[i], "Sentence"+str(i+1) )
    # # TextToMp3(text, "FullAudio")
    TextToSpeech(voice_name=voice_name[voice_choice], text=text, Filename="FullAudio")

    #Downloads Background Youtube Video
    youtube_url = input("Enter the YouTube url to play in the background: ")
    YoutubeDownloader(youtube_url)

    #Creates the Video from the mp4 and mp3 files
    BuildVideo(f'resources/Images/{voice_name[voice_choice]}.jpg', 'resources/Mp4/BackgroundVideo.mp4', text_list, 'resources/Mp3/', 'final_video.mp4')
    
    #Deletes Mp3 and background Mp4 video
    # Cleaner()


if __name__ == '__main__':
    main()