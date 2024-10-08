import pyttsx3
import by_using_gtts

def text_to_voice(rate, volume, voice, text):
    try:
        engine = pyttsx3.init()

        # Set rate and volume properties
        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)

        # Set voice property
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice].id)

        # engine.say(text)
        # engine.runAndWait()
        # engine.stop()

        # Save voice to a file
        engine.save_to_file(text, 'test.mp3')
        engine.runAndWait()
    
    except Exception as e:
        print(print(f"An error occurred: {e}"))

def recognize(voice):
    voice_map = {
        'm': {'rate': 130, 'volume': 0.6},
        'f': {'rate': 160, 'volume': 1.0},
        'r': {'rate': 100, 'volume': 0.8}
    }
    return voice_map.get(voice, {'rate': 80, 'volume': 1.0})

def excepter(voice):
    voice_map = {
        'm': 0,
        'f': 1
    }
    return voice_map.get(voice, None)

voice = input("Enter the voice you required (m for male, f for female, r for robot): ")
rate, volume = recognize(voice)
sound = excepter(voice)
if sound is None:
    ask = input("So you want a robotic voice? Enter m for male robot voice or f for female robot voice: ")
    sound = excepter(ask)

with open("text.txt","r") as f:
    text = f.read()
text_to_voice(rate, volume, sound, text)
by_using_gtts.text_to_voice_using_gtts("Hello ! this is a sample and starting to seeing working of gtts.")

