import requests
import pandas as pd
import webbrowser
import ssl
import time
import selenium
import re
ssl._create_default_https_context = ssl._create_unverified_context

def getCardList(url):
    tables = pd.read_html(url)
    table = tables[2]
    fulllist = table.loc[:, "Name"].tolist()
    abvlist = []
    for entry in fulllist:
        temp = re.findall('"([^"]*)"', entry)
        abvlist.append(temp[len(temp)-1])
    return abvlist

def tourl(n):
    url = ""
    for c in n:
        if (c == " "):
            url += "%20"
        elif (c == "!"):
            url += "%21"
        elif (c == "&"):
            url += "%26"
        elif (c == "β"):
            url += ""
        else:
            url += c
    return url

def openpages(cardlist):
    for card in cardlist:
        URL = "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&q="
        URL += tourl(card)
        URL += "&setName=speed-duel-arena-of-lost-souls&view=grid"
        #webbrowser.open_new(URL)

def getprice(card, set):
    URL = "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&q="
    URL += tourl(card)
    URL += "&setName="
    URL += set
    URL += "&view=grid"
    #webbrowser.open_new(URL)

    from selenium import webdriver
    browser = webdriver.Chrome(executable_path=r'C:/Users/Robert/Downloads/chromedriver_win32/chromedriver')
    browser.get(URL)
    time.sleep(1)
    nav = browser.find_element_by_class_name("inventory__price")
    return(float(str(nav.text)[11:]))


def main():

    wikiURL = "https://yugipedia.com/wiki/Speed_Duel:_Battle_City_Box"

    set = ""
    for c in wikiURL[wikiURL.find("/wiki/")+6:]:
        if (c == "_"):
            set += "-"
        elif (c != ":"):
            set += c.lower()

    cardlist = getCardList(wikiURL)
    print(cardlist)
    
    sum = 0
    for card in cardlist:
        price = -10000000
        while True:
            try:
                price = getprice(card,set)
            except selenium.common.exceptions.NoSuchElementException:
                continue
            else:
                break
        sum += price
        print(sum)
        print(str(cardlist.index(card)+1)+ " / " + str(len(cardlist)))
        print(sum/(1+cardlist.index(card)))







if __name__ == "__main__":
    main()
