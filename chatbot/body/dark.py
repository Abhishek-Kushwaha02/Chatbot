import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import os
import wikipedia
import webbrowser
import pywhatkit
import sys
from googletrans import Translator
import requests



engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')  # getting details of current voice

engine.setProperty('voice', voices[0].id)


def speak(audio):

    engine.say(audio)

    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
        print("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
        print("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")
        print("Good Evening Sir!")

        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('the time is' + time)
        print('the time is' + time)

    speak("I am Dark your Assistance Sir , How may help you.")
    print("I am Dark your Assistance Sir , How may help you.")
    
   

        # listen command......... 
def takecommand ():
    # print("takecommand running")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please....")
        return "none"
    return query    

def TranslationHintoEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"you : {data}.")
    return data

# def MicExecution():
#     query = listen()
#     data = TranslationHintoEng(query)
#     return data



if __name__ == "__main__":
    
     wishMe()
     while True:
    #  if 1:
        query = takecommand().lower()

        if "open notepad" in query:
          npath = "C:\\Windows\\System32\\notepad.exe"
          os.startfile(npath)

        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")  

        elif "open blender" in query:
          npath = "C:\\Program Files\\Blender Foundation\\Blender 3.3\\blender.exe"
          os.startfile(npath)

        elif "close blender" in query:
            speak("okay sir, closing blender")
            os.system("taskkill /f /im blender.exe")    

        elif "open command prompt" in query:
            os.system("start cmd")  
        
        elif "close command prompt" in query:
            speak("okay sir, closing command prompt")
            os.system("taskkill /f /im command prompt.exe") 

        elif "wikipedia" in query:

            speak("searching wikipedia.....")
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube"in query:
            webbrowser.open("youtube.com")

        # elif "close youtube" in query:
        #     speak("okay sir, closing youtube")
        #     webbrowser.close("youtube.com") 
           
        elif "open chrome"in query:
            speak("sir, what should i search on chrome")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        # elif "close chrome" in query:
        #     speak("okay sir, closing chrome")
        #     os.system("taskkill /f /im chrome.com")  

        elif "open linkdin"in query:
            webbrowser.open("linkedin.com")

        # elif "close linkdin" in query:
        #     speak("okay sir, closing linkdin")
        #     os.system("taskkill /f /im linkdin.com")  

        elif "open instagram"in query:
            webbrowser.open("instagram.com")

        # elif "close instagram" in query:
        #     speak("okay sir, closing instagram")
        #     os.system("taskkill /f /im instagram.com")  

        elif "sleep" in query:
            speak("have a good day sir")
            sys.exit()

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")  

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")            

        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather
            api_key = "cb252e94b4126f62449d868ad5210a89"
            base_url = "http://api.openweathermap.org//data//2.5//weather?"
            speak(" City name ")
            print("City name : ")
            city_name =takecommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
             
            if 'code' in x and x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                
            else:
                speak(" City Not Found ")
        
 