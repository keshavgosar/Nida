import os
from GoogleImageScrapper.GoogleImageScrapper import GoogleImageScraper

def GoogleImage():
    oo = open('C:\\Users\\keshav\\Desktop\\NidaAI\\Data.txt','rt')
    query = str(oo.read())
    oo.close()
    pppp = open('C:\\Users\\keshav\\Desktop\\NidaAI\\Data.txt','r+')
    pppp.truncate(0)
    pppp.close()

    webdriver = "C:\\Users\\keshav\\Desktop\\NidaAI\\DataBase\\webdriver\\chromedriver.exe"
    photos = "C:\\Users\\keshav\\Desktop\\NidaAI\\DataBase\\GooglePhotos\\"

    search_key = [f"{query}"]
    number = 10
    head = False
    max = (1000, 1000)
    min = (0,0)

    for search_key in search_key:
        image_search = GoogleImageScraper(webdriver,photos,search_key,number,head,min,max)
        image_url = image_search.find_image_urls()
        image_search.save_images(image_url)

    os.startfile(photos)

GoogleImage()