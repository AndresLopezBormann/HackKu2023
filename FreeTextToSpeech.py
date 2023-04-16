from gtts import gTTS
from pathlib import Path

def TextToMp3(text, filename="test"):
    Path("resources/Mp3").mkdir(parents=True, exist_ok=True)
    print(f'Creating {filename}.mp3 file')
    title = gTTS(text=text, lang='en', slow=False)
    title_file = f"resources/Mp3/{filename}.mp3"            
    title.save(title_file)

