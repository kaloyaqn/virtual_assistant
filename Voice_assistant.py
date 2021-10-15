import datetime
import json
import os
import subprocess
import time
import webbrowser
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
from win10toast import ToastNotifier
#from ecapture import ecapture as ec
import wolframalpha


#nachalo
def speak(text):
    engine.say(text)
    engine.runAndWait()

print('Zarejdam...')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

#pozdravqva shefcheto spored chasa
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Dobro Utro")
        print("Ko staa putko")
    elif hour>=12 and hour<18:
        speak("Добър Следобяд")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

#razpoznavane

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='bg-bg')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Mojesh li da povtorite")
            return "None"
        return statement

speak("Zarejdam")
wishMe()

#main

if __name__=='__main__':


    while True:
        speak("")
        statement = takeCommand().lower()
        if statement==0:
            continue

            #kazva chao na shefcheto

        if "чао" in statement or "млъкни" in statement or "спри се" in statement:
            speak('your personal assistant Maika ti is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            break

        
        if "много съм умен" in statement or "айкюто върти" in statement:
            speak("da,  taka,   e,    mnogo,    ste,    umen, sir,  ")
            print("da taka e mnogo ste umen,  sir")
            break



            #wikipediata
        if 'уикипедия' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

            #youtube
        elif 'отвори ютуб' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("ютуб е отворен")
            time.sleep(5)

        elif 'пусни ми новините' in statement:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=RXPGslO_fxo")
            speak("puskam,  vi,  novnite,  sir")
            time.sleep(5)

        #google
        elif 'Отвори google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        #gmail
        elif 'отвори gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        #vreme (meteo)
        elif "кажи ми времето" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("Kakwo  e  imeto  na grada  vi, sir")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")


        #vreme

        elif 'Време' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        #koi si ti
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('Az sum bashtati')

        #koi ta naprai ma
        elif "Кой те е направил" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Kaloyan")
            print("I was built by Kaloyan")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        #camera (nqmame skripta)
       # elif "camera" in statement or "take a photo" in statement:
       #     ec.capture(0,"robo camera","img.jpg")


        #tursene v neta
        elif 'потърси' in statement or "търси" in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(20)

        #pitame
        elif 'питай' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        #log off
        elif "заминавай" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
