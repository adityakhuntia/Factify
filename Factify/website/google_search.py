import requests
from bs4 import BeautifulSoup

def googleSearch(INPUTfact):
    google_input = requests.get("https://www.google.com/search?q=" + INPUTfact)
    soup = BeautifulSoup(google_input.text, 'html.parser')
    a = soup.find_all("div", class_ = "kCrYT")
    b = list()
    for items in a:
        b.append(str(items))
    c = list()
    for things in b:
        if "/url?q=" in things:
            c.append(things)       
    d = list()
    for shit in c:
        d.append(shit[shit.index("/url?q="):])
    e = list()
    for FINALlinks in d:
        e.append(FINALlinks[(int(FINALlinks.index("="))+1):(int(FINALlinks.index("&amp")))])
    LIS = list()
    for links in e[:5]:
        LIS.append(links)
    return(LIS)