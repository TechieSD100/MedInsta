import speech_recognition as sr

r = sr.Recognizer()

# Set the microphone as the audio source
with sr.Microphone() as source:
    print("Listening...")
    # Listen to the microphone and store the audio data
    audio_data = r.listen(source)

# Convert the audio data to text
text = r.recognize_google(audio_data)

print(text)
