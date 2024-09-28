from gtts import gTTS
import os

def text_to_voice(text, lang='en', filename='test.mp3'):
    try:
        # Convert text to speech
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        print(f"Audio saved as {filename}")
        
    except Exception as e:
        print(f"An error occurred: {e}")


with open("text.txt","r") as f:
    text = f.read()
text_to_voice(text)
