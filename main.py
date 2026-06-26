from subprocess import call
import pyttsx3
import datetime
import speech_recognition as sr

call("cls", shell=True)

"""
Title : Jarvis Assistant
Author : Soham Panse
Date : 26 June, 2026
Purpose : To make an assistant for repetative tasks
"""

# Global variables and Constants
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Functions


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    com = "Jarvis Here. How may i help you"
    if (hour >= 0 and hour < 12):
        speak("Good Morning!" + com)
    elif (hour >= 12 and hour < 18):
        speak("Good Afternoon!" + com)
    else:
        speak("Good Evening!" + com)


def takeFromMic():
    # Takes audio input from microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception:
        print("Say that again...")
        return "None"
    return query


# Main Function
if __name__ == "__main__":
    wishMe()
    while (1):
        takeFromMic()
