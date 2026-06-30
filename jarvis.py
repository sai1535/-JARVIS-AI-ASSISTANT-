-import pyttsx3
import speech_recognition as sr
import webbrowser
import pyjokes
from datetime import datetime
import os

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        return ""

# Welcome
speak("Hello! I am Jarvis. How can I help you?")

while True:
    command = listen()

    if command == "":
        continue

    elif "hello" in command:
        speak("Hello Sanjeev!")

    elif "time" in command:
        current = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current}")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")

    elif "search" in command:
        query = command.replace("search", "")
        speak(f"Searching {query}")
        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

    elif "joke" in command:
        speak(pyjokes.get_joke())

    elif "notepad" in command:
        os.system("notepad")

    elif "calculator" in command:
        os.system("calc")

    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        break

    else:
        speak("Sorry, I didn't understand.")
