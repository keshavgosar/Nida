import pyperclip
from pytube import query
import pywhatkit
import pyttsx3
from pywhatkit.main import search
import wikipedia
from pywikihow import WikiHow , search_wikihow
import os
import wolframalpha
import webbrowser as web

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def Speak(audio):
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()

def  GoogleSearch(term):

    query = term.replace("nida","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("who is","")
    query = query.replace("what do you mean by","")
    writeab = str(query)

    oooooo = open('C:\\Users\\keshav\\Desktop\\NidaAI\\Data.txt','a')
    oooooo.write(writeab)
    oooooo.close()


    Query = str(term)
    pywhatkit.search(Query)
    os.startfile('C:\\Users\\keshav\\Desktop\\NidaAI\\DataBase\\ExtraPro\\start.py')

    if 'how to' in Query:
        max_result = 1
        how_to_func = search_wikihow(query=Query,max_result=max_result)
        assert len(how_to_func) == 1
        how_to_func[1].print()
        Speak(how_to_func[1].summary)
    
    else:
        search = wikipedia.summary(Query,1)
        Speak(f": According To Your Search : {search}")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term

    web.open(result)

    Speak("This is what i found for you sir..!")

    pywhatkit.playonyt(term)

    Speak("This may also helps you sir...!")

def Alarm(query):
    TimeHere = open('C:\\Users\\keshav\\Desktop\\NidaAI\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("C:\\Users\\keshav\\Desktop\\NidaAI\\DataBase\\ExtraPro\\Alarm.py")

def YouTubeVideoDownload():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip 
    from time import sleep

    sleep(2)

    click(x=589,y=66)

    hotkey('ctrl','c')

    value = pyperclip.paste()

    Link = str(value)

    def Download(link):

        url = YouTube(link)

        video = url.streams.first()

        video.download('C:\\Users\\keshav\\Desktop\\NidaAI\\DataBase\\YouTube Download\\')

    Download(Link)
    Speak("video downloaded sir...!")
    Speak("now i am opening it...")
    os.startfile("C:\\Users\\keshav\\Desktop\\NidaAI\\DataBase\\YouTube Download\\")

def SpeedTest():
    os.startfile("C:\\Users\\keshav\\Desktop\\NidaAI\\DataBase\\Gui Programs\\SpeedTestGui.py")

def WolfRam(query):
    api_key = "Y5VWGL-HK63HH7EYA"
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        Answer = next(requested.results).text
        return Answer

    except:
        Speak("SORRY...! The String Value Is Not Answerable..")

def Calculator(query):
    Term = str(query)
    Term = Term.replace("nida","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("substract","-")
    Term = Term.replace("divide","/")
    Term = Term.replace("into","*")
    Term = Term.replace("remainder","%")
    Term = Term.replace("percentage","%")

    Final = str(Term)

    try:
        result = WolfRam(Final)
        Speak(f": the answer is : {result}")
    
    except:
        Speak("SORRY..! the string is not answerable...")

    
def Temp(query):
    Term = str(query)
    Term = Term.replace("nida","")
    Term = Term.replace("in ","")
    Term = Term.replace("what is the ","")
    Term = Term.replace("temperature ","")
    Term = Term.replace("what is ","")

    temp_query = str(Term)

    if 'outside' in temp_query:
        var1 = "Temperature in Indore"
        answer = WolfRam(var1)
        Speak(f"{var1} is {answer}..")

    else:
        var2 = "Temperature in " + temp_query
        answ = WolfRam(var2)
        Speak(f"{var2} is {answ}")

def DateConverter(Query):
    Date = Query.replace("and","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)







    



