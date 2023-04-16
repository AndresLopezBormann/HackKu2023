from elevenlabslib import *
from pathlib import Path
from dotenv import load_dotenv
import os
def TextToSpeech(userID="ELEVENLABS_USER_ID", voice_name="Dumbledore", text="",  Filename="file"):
    """
    Uses the Eleven Labs text-to-speech API to generate an MP3 file of the input text spoken by a chosen voice and saves it to the "resources/Mp3" directory.

    Args:
        userID (str, optional): The Eleven Labs user ID. Defaults to "ELEVENLABS_USER_ID".
        voice_name (str, optional): The name of the voice to be used for the speech. Must be one of "Biden", "Trump", "Freeman", "Rogan", "Musk", "Dumbledore", "Elizabeth", or "Ferrell". Defaults to "Dumbledore".
        text (str, optional): The text to be spoken. Defaults to "".
        Filename (str, optional): The name of the output MP3 file without the ".mp3" extension. Defaults to "file".

    Returns:
        Creates a new MP3 file
    """
    load_dotenv()
    userID = os.getenv('ELEVENLABS_USER_ID')

    # Creates resources/Mp3 folder for text files to go into
    Path("resources/Mp3").mkdir(parents=True, exist_ok=True)

    voices = {"Biden": "yMfnfIOzluxodSBLGa9R",
              "Trump": "PSv9S5rmNIg1ozYKAzDx",
              "Freeman": "G0M1WHULWsL10PLWylPH",
              "Rogan": "I75MC4wVD1NmxPuHVADh",
              "Musk": "KkmqZkq9NrakIxm41NnN",
              "Dumbledore": "IUdilhpdlWXl4OWD4o8a",
              "Elizabeth": "nWOCUUj2aJdD4IiK6Kwl",
              "Ferrell": "peJHjRFgAZmIxotqRpKo"}

    user = ElevenLabsUser(userID)
    voice = user.get_voice_by_ID(voices[voice_name]) 
    print(f'Creating {Filename}.mp3 file')
    voice.generate_and_download_audio(prompt=text, filename=f"resources/Mp3/{Filename}.mp3")



