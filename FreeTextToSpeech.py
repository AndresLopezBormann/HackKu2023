from gtts import gTTS
from pathlib import Path

def TextToMp3(text, filename='text'):
    Path("Mp3").mkdir(parents=True, exist_ok=True)
    text = gTTS(text=text, lang='en', slow=False)
    text_file = filename + '.mp3'
    text.save(text_file)
