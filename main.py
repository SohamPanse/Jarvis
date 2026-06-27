from subprocess import call
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

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
chrome_path = "Chrome Location In File System"
vs_path = r"VS code Location In File System"
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
        query = takeFromMic().lower()

        if ("open youtube" in query):
            webbrowser.get(chrome_path).open("youtube.com")
        elif ("open google" in query):
            webbrowser.get(chrome_path).open("google.com")
        elif ("quit" in query):
            pyttsx3.speak("Jarvis signing off")
            print("Jarvis logged out")
            exit(0)
        elif "restart" in query:
            pyttsx3.speak("Jarvis restarting")
            call('python main.py', shell=True)
            exit(0)
        elif "clear" in query:
            call('cls', shell=True)
        elif "wikipedia" in query:
            pyttsx3.speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
            except Exception:
                print("Wiki API fail. Try Again")
                results = "None"
            pyttsx3.speak("According to Wikipedia")
            print(results)
            pyttsx3.speak(results)
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            pyttsx3.speak(f"It's {strTime} now")
        elif "open code" in query:
            os.startfile(vs_path)
        elif "open chrome" in query:
            os.startfile(chrome_path[0:-3])
        else:
            pass
