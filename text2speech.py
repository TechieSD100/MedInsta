# import pyaudio
# import pocketsphinx

# Set the text to be spoken
# text = "Hello how are you today"

# Set up the pocketsphinx text-to-speech engine
# engine = pocketsphinx.AudioFile(text)

# Speak the text
# engine.play()


from gtts import gTTS
import os

# The text that you want to convert to audio
mytext = 'Hi everyone, how are you. Welcome to MedInsta! Please tell me about your unusualness.'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("speech.mp3")

# Playing the converted file
os.system("speech.mp3")
