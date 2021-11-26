import pyttsx3
import speech_recognition as sr
from Features import GoogleSearch
import webbrowser
import pywhatkit
from gtts import gTTS
from playsound import playsound 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 170)

def Speak(audio):
    print("   ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print("   ")

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


def TakeCommand_Hindi():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        print(": Recognizing....")

        query = r.recognize_google(audio, language='hi')
        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def TaskExe():

    def Music():
        Speak("Tell me the name of song..!")
        musicName = TakeCommand()
        pywhatkit.playonyt(musicName)
        Speak("Your song has been started, Enjoy sir..!")

    while True:
        query = TakeCommand()
        if 'hello' in query:
            Speak("Hello Sir, I Am Nida")
            Speak("Your Personal A I Assistant!")
            Speak("How may i help you?")
        
        elif 'how are you' in query:
            Speak("I Am fine sir, My all function is working very good and I am ready to take your command")

        elif 'break' in query:
            Speak("Ok sir! You can call me any time")
            break

        elif 'chetan' in query:
            Speak("chetan is your best friend boss but I think he is an idiot!")

        elif 'yash' in query:
            Speak("yash is you best friend boss but I think he is very irritating guy!")

        elif 'very good' in query:
            Speak("thank boss! I am always ready to assist you!")

        elif 'thanks' in query:
            Speak("thank boss! I am always ready to assist you!")

        elif 'who are you' in query:
            Speak("Now me to introduce my self, I am Nida an advanced artificial inteligence created in pythone programming language but i am made by the name of the ex-girlfriend of my boss")

        elif 'who made you' in query:
            Speak("My Boss! Keshav Gosar")
        
        elif 'your boss' in query:
            Speak("his name is Keshav Gosar, He is a computer science student")

        elif 'bye' in query:
            Speak('Ok sir! Bye...!')
            break

        #elif 'youtube search' in query:
           # Speak("Ok sir!")
           # query = query.replace("nida","")
           # query = query.replace("youtube search","")
           # web = 'https://www.youtube.com/results?search_query=' + query
           # webbrowser.open(web)
           # Speak("Done sir!")

        elif 'google search' in query:
            Speak("this is what i found for you")
            GoogleSearch(query)
            Speak("Done sir!")
        
        elif 'youtube search' in query:
            Query = query.replace("nida","")
            Query = query.replace("youtube search","")
            from Features import YouTubeSearch
            YouTubeSearch(query)
        
        elif 'set alarm' in query:
            from Features import Alarm
            Alarm(query)

        elif 'download' in query:
            from Features import YouTubeVideoDownload
            YouTubeVideoDownload()

        elif 'speed test' in query:
            from Features import SpeedTest
            SpeedTest()
            from Features import Temp
            Temp(query)

        elif 'calculate' in query:
            from Features import Calculator
            Calculator(query)

        elif 'message' in query:
            name = query.replace("send whatsapp ", "")
            name = name.replace("send ", "")
            name = name.replace("to ", "")
            name = name.replace("message ", "")
            name = name.replace("whatsapp ", "")
            Name = str(name)
            Speak(f"whats the message for {Name}..")
            MSG = TakeCommand()
            from Automations import WhatsappMsg
            WhatsappMsg(Name, MSG)
            Speak(f"message sended to {Name}..")

        elif 'call' in query:
            from Automations import WhatsappCall
            name = query.replace("call ", "")
            name = name.replace("nida ", "")
            name = name.replace("to ", "")
            Name = str(name)
            Speak(f"calling...{Name}..")
            WhatsappCall(Name)

        elif 'show chat' in query:
            Speak("with whome...?")
            name = TakeCommand()
            from Automations import WhatsaapChat
            WhatsaapChat(name)
            Speak(f"chats opened of {name}...")

        elif 'chrome' in query:
            from Automations import ChromAuto
            ChromAuto(query)

        elif 'youtube' in query:
            from Automations import YoutubeAuto
            YoutubeAuto(query)

        elif 'music' in query:
            Music()

        elif 'space news' in query:
            Speak("which date of news you want sir....?")
            Date = TakeCommand()
            from Features import DateConverter
            Value = DateConverter(Date)
            from Nasa import NasaNews
            NasaNews(Value)

      #  else:
      #      from Features import WolfRam
      #      WolfRam(query)
      #      Speak(WolfRam(query))

TaskExe()





