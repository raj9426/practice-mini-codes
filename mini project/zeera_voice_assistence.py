import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
from time import ctime
import time
import pywhatkit as kit
import pyautogui
import random as r


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print (voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = (datetime.datetime.now().hour)  
    if hour>=0 and hour<12:
        speak("good morning shakthi")
    elif hour>=12 and hour<17:
        speak("good afternoon shakthi raj")  
    elif hour>=17 and hour<21:
        speak("good evening shakthi")   
    # else:
        # speak("good night shakthi")

    speak("i am subba lakshmi,how may i help you ?")

def TakeCommmand1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
    
    except Exception as e:
        print("voice is not recognized, please try again..")
        return "None"
    return query    

def TakeCommmand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
    
    except Exception as e:
        print("voice is not recognized, please try again..")
        speak("voice is not recognized, please try again..") 
        return "None"
    return query    
def play_music(music):
    os.startfile("spotify")
    time.sleep(5)
    pyautogui.hotkey('ctrl','l')
    time.sleep(2)
    pyautogui.write(music, interval=0.1)
    time.sleep(2)
    pyautogui.click(x=559, y=337)
    time.sleep(3)
    speak("playing "+ music)
    pyautogui.click(x=390, y=486)

if __name__ == "__main__":
    wishMe()
    while True:
            query = TakeCommmand().lower()
            if 'wikipedia' in query or 'who is' in query:
                speak("searching wikipedia..")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=1)
                speak("according to wikipedia")
                print(results)
                speak(results)

            elif 'trending on youtube' in query:
                webbrowser.open("https://www.youtube.com/feed/trending")
            
            elif 'play music' in query or 'music' in query:
                print("ok which one")
                speak("ok....., which one ??")
                music = TakeCommmand()
                play_music(music)
                                        
                # is_on = True
                # while is_on:
                #     q = TakeCommmand1()  
                #     if q == 'pause' or q == 'play':
                #         pyautogui.press('space')
                #     elif q == 'stop':
                #         is_on = False
               

                # os.system("spotify")                         
                # time.sleep(5)
                # pyautogui.press('space')
                # exit()
        
            elif 'play' in query:
                kit.playonyt(query)
                # webbrowser.open(f"https://www.youtube.com/results?search_query={query}\n")
                speak("here is what i found for" + query)

            elif 'search' in query:
                speak("what do you want to search ?")
                search = TakeCommmand()
                url = "https://www.google.com/search?q=" + search
                webbrowser.get().open(url)
                speak("here is what i found for" + search)
            elif 'vs code' in query:
                codepath = "M:\\Microsoft VS Code\\Code.exe"    
                speak("opening vs code")
                os.startfile(codepath)
            
            elif 'html helper' in query:
                webbrowser.open("https://devdocs.io/")
                speak("here is what i found for" + query) 

                
            elif 'time' in query:
                print(ctime())
                speak(ctime())   
            
                
            elif 'exit' in query:
                hour = (datetime.datetime.now().hour)
                if hour>=6 and hour<22:
                    speak("okay sir.....have a good day..")
                    exit()
                else:
                    speak("okay sir...good night..")
                    exit()

            elif query in ["hello", "hi"]:
                reply = r.choice(["hello", "hi", "what's up ?"])
                print(reply)
                speak(reply)