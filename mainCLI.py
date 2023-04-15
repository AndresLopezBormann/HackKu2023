from RedditGetter import GetRedditPost
from ChatGPT import ChatGPT_Prompt
from FreeTextToSpeech import TextToMp3 
from YoutubeDownloader import YoutubeDownloader
from SentenceSplitter import SentenceSplitter

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
    
    #Commented out to avoid costs
    # text = ChatGPT_Prompt(ChatGPT_prompt, text) 

    # Splits the text into sentences
    text_list = SentenceSplitter(text)
    num_sentences = len(text_list)

    #Turns sentences into mp3 files
    for i in range(num_sentences):
        TextToMp3(text_list[i], "Sentence"+str(i+1) )
    
    #Downloads Background Youtube Video
    youtube_url = input("Enter the YouTube url to play in the background: ")
    YoutubeDownloader(youtube_url)

    #Creates the Video from the mp4 and mp3 files
    #MOVIE_MAKER_FUNC(resourcespath, num_sentences)


if __name__ == '__main__':
    main()