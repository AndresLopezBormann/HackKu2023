from elevenlabslib import *
from pathlib import Path
from dotenv import load_dotenv
import os
basedir = os.path.dirname(__file__)

def TextToSpeech(userID="ELEVENLABS_USER_ID", voice_name="Dumbledore", text="Test",  Filename="file"):
    load_dotenv()
    userID = os.getenv('ELEVENLABS_USER_ID')

    Path(os.path.join(basedir, "resources", "Mp3")).mkdir(parents=True, exist_ok=True)

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
    voice.Download_audio_bytes(text, filename=os.path.join(basedir, "resources", "Mp3", f"{Filename}.mp3"))
    



# COPY THIS FUNCTION INTO THE elevenlabslib/ElevenLabsVoice.py

# def Download_audio_bytes(self, prompt:str, stability:Optional[float]=None, similarity_boost:Optional[float]=None, filename="Audio.mp3") -> bytes:
#     """
#     Generates speech for the given prompt and returns the audio data as bytes of an mp3 file.

#     Args:
#         prompt: The prompt to generate speech for.
#         stability: A float between 0 and 1 representing the stability of the generated audio. If None, the current stability setting is used.
#         similarity_boost: A float between 0 and 1 representing the similarity boost of the generated audio. If None, the current similarity boost setting is used.
#         filename: The filename lol
#     Returns:
#         The bytes of the audio file, and the json data (such as the number of tokens used).
#     """
#     #The output from the site is an mp3 file.
#     #You can check the README for an example of how to convert it to wav on the fly using pydub and bytesIO.
#     payload = self._generate_payload(prompt, stability, similarity_boost)
#     response = _api_json("/text-to-speech/" + self._voiceID + "/stream", self._linkedUser.headers, jsonData=payload)
#     save_bytes_to_file_object(fp=filename, audioData=response.content, outputFormat="mp3")

#     return response.content

