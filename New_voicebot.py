import pyttsx3
import webbrowser
import speech_recognition as sr 
import wikipedia
import os
import smtplib
import datetime
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 7000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google('audio', language='en-in')

        print(f"User said: {query} \n")

    except Exception as e:
        print(e)
        print("Say that again Please")
        return "None"
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am your helping hand sir, please give me some instructions")

if __name__ == "__main__":
   speak("Hello sir, I am your artificially intelligent voicebot, give me some instructions")
   wishMe()

   while True:
       #if 1:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)

        if 'open youtube' in query:
            webbrowser.open("youtube.com")