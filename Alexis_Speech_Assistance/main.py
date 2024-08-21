import speech_recognition as sr
r = sr.Recognizer()
def recorde_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, i did noit get that")
        except sr.RequestError:
            print("Sorry, my speech service is down")
        return voice_data
    
def respond(voice_data):
    if 'what is my name' in voice_data:
        print("My name is Alexis")
        
print("How can I help you?")
voice_data = recorde_audio()