import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
       print('Recognizing') 
       query = r.recognize_google(audio, language='en-in')
       print(f"User said: {query} \n")

    except Exception as e:
        print(e)
        print("Say that again please")
        return 'None'
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Give me instructions please , Sir")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','your password')
    server.sendmail('from email id', to , content)
    server.close()

if __name__ == "__main__":
    speak("How are you sir, what can i do for you")
    wishMe()

    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'how are you' in query:
            speak("I am fine Sir, what can i do for you.")

        elif 'open youtube' in query:
            speak("Sure, sir i will do it right now, enjoy videos on youtube.")
            webbrowser.open("youtube.com")
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'quit' in query:
            exit()
            
           
