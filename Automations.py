from os import name, startfile
from re import search
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import pyttsx3
import speech_recognition as sr
import webbrowser as web

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 170)

def Speak(audio):
    print("   ")
    print(f": {audio}")
    print("   ")
    engine.say(audio)
    engine.runAndWait()

#Speak("Hello sir")
#def Speak(audio):
#    kk = gTTS(audio)
 #   kk.save('Assis.mp3')
#    playsound('Assis.mp3')

#Speak("और चुतिये कैसा हे")

def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        print(": Recognizing....")

        query = r.recognize_google(audio, language='eng-in')
        print(f": Your Command : {query}\n")

    except:
        return ""

    #kk = open('Data.txt', 'rb')
    #kk.write(f": {query}")
    #kk.close()


    return query.lower()

def WhatsappMsg(name , message):

    startfile("C:\\Users\\keshav\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    
    sleep(30)
    click(x=359, y=144)
    sleep(1)
    write(name)
    sleep(1)
    click(x=288,y=314)
    sleep(1)
    click(x=1073, y=991)
    sleep(1)
    write(message)
    press('enter')

def WhatsappCall(name):
    startfile("C:\\Users\\keshav\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    
    sleep(30)
    click(x=359, y=144)
    sleep(2)
    write(name)
    sleep(2)
    click(x=288,y=314)
    sleep(2)
    click(x=1073, y=991)
    sleep(1)
    click(x=1725, y=68)

def WhatsaapChat(name):

    startfile("C:\\Users\\keshav\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    
    sleep(30)
    click(x=359, y=144)
    sleep(2)
    write(name)
    sleep(2)
    click(x=288,y=314)
    sleep(2)
    click(x=1073, y=991)
    sleep(1)

def ChromAuto(command):
    
    query = str(command)

    if 'new tab' in query:
        press_and_release('ctrl + t')
    
    elif 'close tab' in query:
        press_and_release('ctrl + w')

    elif 'new window' in query:
        press_and_release('ctrl + n')

    elif 'history' in query:
        press_and_release('ctrl + h')

    elif 'downloads' in query:
        press_and_release('ctrl + j')

    elif 'bookmark' in query:
        press_and_release('ctrl + d')
        press('enter')

    elif 'incognito' in query:
        press_and_release('ctrl + shift + n')

    elif 'switch tab' in query:
        #Speak("to which tab sir...?")
        #tab = TakeCommand()
        #Tab = int(tab)
        #press_and_release()
        tab = query.replace("switch tab ","")
        Tab = tab.replace("to ", "")
        num = Tab
        bb = f'ctrl + {num}'
        press_and_release(bb)

    elif 'open' in query:
        name = query.replace("open ","")
        name = query.replace("nida ","")
        NameA = str(name)

        if 'youtube' in NameA:
            web.open("https://www.youtube.com/")

        elif 'instagram' in NameA:
            web.open("https://www.instagram.com/")

        else:
            string  = 'https://www.' + NameA + ".com"
            string_2 = string.replace(" ", "")
            web.open(string_2)

def YoutubeAuto(command):
    query = str(command)
    if 'pause' in query:
        press('space bar')
    elif 'resume' in query:
        press('space bar')
    elif 'full screen' in query:
        press('f')
    elif 'theater mode' in query:
        press('t')
    elif 'miniplayer' in query:
        press('m')
    elif 'mute' in query:
        press('m')
    elif 'unmute' in query:
        press('p')
    elif 'fast forward' in query:
        press('l')
    elif 'rewind' in query:
        press('j')
    elif 'increase' in query:
        press_and_release('SHIFT + .')
    elif 'decrease' in query:
        press_and_release('SHIFT + ,')
    elif 'previous' in query:
        press_and_release('SHIFT + p')
    elif 'next' in query:
        press_and_release('SHIFT + n')
    elif 'on caption' in query:
        press('c')
    elif 'off caption' in query:
        press('c')
    elif 'search' in query:
        click(x=676, y=126)
        Speak("what you want to search...!")
        search = TakeCommand()
        write(search)
        sleep(1)
        press('enter')
    else:
        Speak("No command found....!")
