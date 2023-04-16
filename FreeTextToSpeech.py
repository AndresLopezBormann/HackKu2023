from gtts import gTTS
from pathlib import Path

def TextToMp3(text, filename="filename"):
    """
        Converts the input text to an MP3 file using Google Text-to-Speech (gTTS) and saves it to the "resources/Mp3" directory.

        Args:
            text (str): The text to be converted to speech.
            filename (str, optional): The name of the output MP3 file without the ".mp3" extension. Defaults to "filename".
        Returns:
        Creates a new MP3 file
    """
    Path("resources/Mp3").mkdir(parents=True, exist_ok=True)
    print(f'Creating {filename}.mp3 file')
    title = gTTS(text=text, lang='en', slow=False)
    title_file = f"resources/Mp3/{filename}.mp3"            
    title.save(title_file)

