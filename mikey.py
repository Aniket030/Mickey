import datetime
import os
import random
import sys
import webbrowser
import cv2
import pyttsx3
import speech_recognition as sr
import wikipedia
from requests import get
import pywhatkit as kit
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# covert voices into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        speak("Say that again please....")
        return "none"
    return query


# wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour <= 12:
        speak("Good Morning")
    elif 12 < hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am mikey sir, please tell how can i help you")


# to send email
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('Aniketchaubey030@gmail.com', 'Aniket@3002')
    server.sendmail('Aniketchaubey030@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()

        # logic building for tasks
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open word" in query:
            apath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WORDICON.EXE"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("Webcam", img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
                cap.release()
                cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\Apcha\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))


        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f'your IP address is {ip}')

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
            # print(results)


        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open amazon" in query:
            webbrowser.open("www.amazon.com")

        elif "open amazon prime " in query:
            webbrowser.open("www.primevideo.com")

        elif "open amazon music" in query:
            webbrowser.open("www.music.amazon.in")

        elif "open flipkart" in query:
            webbrowser.open("www.flipkart.com")



        elif "open google" in query:
            speak("Sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "send message" in query:
            kit.sendwhatmsg("+918356859529", "this is testing", 5, 10)

        elif "play songs on youtube" in query:
            speak("Sir, what should i play on youtube")
            cm = takecommand().lower()
            kit.playonyt(cm)

        elif "send email" in query:
            try:
                speak("What should i say?")
                content = takecommand().lower()
                to = "punamchaubey025@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to mummy")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this mail to mummy")

        elif "no thanks" in query:
            speak("Thanks for using me sir, have a good day.")
            sys.exit()

        speak("Sir, do you have any other work")
