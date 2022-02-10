import requests
from bs4 import BeautifulSoup
import pandas as pd
import webbrowser

def getCardList(url):
    tables = pd.read_html(url)
    table = tables[2]
    fulllist = table.loc[:, "Name"].tolist()
    abvlist = []
    for entry in fulllist:
        abvlist.append(entry[1:len(entry)-1])
    return abvlist

def tourl(n):
    url = ""
    for c in n:
        if (c == " "):
            url += "%20"
        elif (c == "!"):
            url += "%21"
        else:
            url += c
    return url

def openpages(cardlist):
    for card in cardlist:
        URL = "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&q="
        URL += tourl(card)
        URL += "&setName=speed-duel-arena-of-lost-souls&view=grid"
        webbrowser.open_new(URL)

def main():

    URL = "https://yugipedia.com/wiki/Speed_Duel:_Arena_of_Lost_Souls"
    setName = URL[URL.find("/wiki/")+6:]
    filter = ""
    for c in setName:
        if (c == "_"):
            filter += "-"
        elif (c != ":"):
            filter += c
    filter = filter.lower()
    cardlist = getCardList(URL)
    #print(cardlist)
    #openpages(cardlist[:3])





if __name__ == "__main__":
    main()
