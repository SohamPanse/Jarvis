from subprocess import call
import pyttsx3

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

# Main Function
if __name__ == "__main__":
    speak("Mike")
