import pyttsx3
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        print(e)
        print("Say that again please")
        return 'None'
    return query

def speak():
    engine.say(audio)
    engine.runAndWait

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour <18:
        speak('Good Afternoon Sir')
        
    elif hour>18:
        speak('Good Evening Sir')

    speak('Please instruct me')

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourEmailAddress','yourPassword')
    server.sendmail('fromEmailAddress', to, content)
    server.close()

if __name__ == '__main__':
    speak
    wishMe()
            