import pyttsx3
import datetime
engine= pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate=140
engine.setProperty('rate',newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("hi i am jarvis")