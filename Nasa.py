import requests
import os
from PIL import Image
import pyttsx3

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


Api_Key = "oYiCtUaG4AuxcpL21oicr6UcD337xLZa322Khumq" #"6X53oGaknGlXM1YjvW80VAVASKWmHrDui0VUe3Hc"

def NasaNews(Date):
    Speak("Extracting Data From Nasa....")
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)
    Params = {'date': str(Date)}
    r = requests.get(Url,params = Params)
    Data  = r.json()
    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']
    Image_r = requests.get(Image_Url)
    FileName = str(Date) + '.jpg'

    with open(FileName, 'wb') as f:
        f.write(Image_r.content)

    Path_1 = "C:\\Users\\keshav\\Desktop\\NidaAI\\" + str(FileName)
    Path_2 = "C:\\Users\\keshav\\Desktop\\NidaAI\\DataBase\\NasaDataBase\\" + str(FileName)

    os.rename(Path_1,Path_2)
    img = Image.open(Path_2)
    img.show()
    Speak(f"Title is : {Title}")
    Speak(f"According To Nasa : {Info}")




