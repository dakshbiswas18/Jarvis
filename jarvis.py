import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning daksh")
    elif hour>=12 and hour<18:
        speak("Good afternoon daksh")
    else:
        speak("Good evening daksh")
    speak("I am jaarvis how can i help you")

def takeCommand():
#will take speech from user and return a string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print("You said: ",query)
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'music' in query:
            music_dir = 'C:\\Users\\daksh\\Desktop\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            break
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
        elif 'code editor' in query:
            os.startfile("C:\\Users\\daksh\\AppData\\Local\\atom\\atom.exe")
        elif 'fifa' in query:
            os.startfile("D:\\Games\\FIFA 19\\FIFA19.exe")
        elif 'message' in query:
            speak("who is the recipient")
            recipient = takeCommand().lower()
            if 'daksh' in recipient:
                speak("what should i send")
                content = takeCommand()
                # init gmail setup
                mail = smtplib.SMTP("smtp.gmail.com", 587)
                # identify the server
                mail.ehlo()
                # encrypt session
                mail.starttls()
                # login
                mail.login('biswasdaksh007@gmail.com', '9329699000')
                # send msg
                mail.sendmail('daksh', 'biswasdaksh007@gmail.com', content)
                # close connection
                mail.close()
                speak("mail sent")
        elif 'thank you' in query:
            break
