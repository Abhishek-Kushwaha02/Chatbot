from brain.logicai import ReplyBrain
from body.dark import speak
from body.dark import takecommand
from body.dark import  wishMe

import os
import wikipedia
import webbrowser
import sys

# import tkinter as tk
# import tkinter

    # speak("I m darek your assistant sir")
if __name__=="__main__":    
    # print("inside name")

    # wn = tkinter.Tk()
    
    Data = wishMe()
    while True:
        # print("inside while command")
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
        
        elif "open ms word/word" in query:
          npath = "C:\\Program Files\\Microsoft Office\\root\\Office16"
          os.startfile(npath)

        elif "ms word/word" in query:
            speak("okay sir, closing ms word")
            os.system("taskkill /f /im ms word.exe") 
        
        elif "open powerpoint" in query:
          npath = "C:\\Program Files\\Microsoft Office\\root\\Office16"
          os.startfile(npath)

        elif "powerpoint" in query:
            speak("okay sir, closing powerpoint")
            os.system("taskkill /f /im powerpoint.exe") 
        





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

        # tkinter=callVoiceAssistant()
        Data  = takecommand()
        query = takecommand(). lower()
        # print("outside data")
        Data  = str(Data)
        Reply = ReplyBrain(Data)
        speak(Reply)
        # UI = activate_voice_input()


        