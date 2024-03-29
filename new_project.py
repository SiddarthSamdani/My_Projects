import pyttsx3
import speech_recognition as sr 
import wikipedia
import webbrowser
import os 
import datetime
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

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
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("What can i do for you")

def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email id','password')
    server.sendmail('from email',to , content)
    server.close()

if __name__ == "__main__":
    speak("Hello sir, this is a voicebot, Please provide the instructions")
    wishMe()

while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=4)
        speak("According to wikipedia")
        print(wikipedia.suggest(query))
        print(wikipedia.search(query))
     
       

    elif 'open youtube' in query:
        speak("I am opening youtube right now, enjoy the videos Sir")
        webbrowser.open("youtube.com")

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'quit' in query:
        exit()
