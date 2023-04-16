from TextToSpeech import TextToSpeech
from FreeTextToSpeech import TextToMp3 
from dotenv import load_dotenv
import os 
def main():
    load_dotenv()
    
    userID = os.getenv('ELEVENLABS_USER_ID')
    voice_name = ["Biden", "Trump", "Freeman", "Rogan", "Musk", "Dumbledore", "Elizabeth", "Ferrell"]

    text = "This is the body of the paragraph"

    # Use this one for the final product
    # TextToSpeech(userID=userID, voice_name=voice_name[0], text=text, Filename="file")


    # Use this one for testing purposes because ElevenLabs caps text to speech based on usage
    TextToMp3(text=text, filename='file')   


if __name__ == '__main__':
    main()