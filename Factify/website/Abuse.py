import requests
from bs4 import BeautifulSoup
import urllib, json
import pandas as pd


def abuse(inputURL):
    if inputURL.split("/")[0] == "https:":
        website = inputURL.split("/")[2]
    else:
        URLlist = inputURL.split(".")
        website = URLlist[-2] + "." + URLlist[-1].split("/")[0]
    result = requests.get("https://domainbigdata.com/" + website)
    soup = BeautifulSoup(result.text, 'html.parser')
    table_1 = soup.find_all("table", class_ = "websiteglobalstats em-td2 trhov")

    for items in table_1:
        e = items.find_all("tr", id = "tr2")
        for IDitems2 in e:
            f = IDitems2.find_all("td")
            IPresult = requests.get("https://ip-46.com/" + f[1].text.split()[0])
            IPsoup = BeautifulSoup(IPresult.text, 'html.parser')
            status = IPsoup.title.text.split("-")
            if status[-1].strip() == "No abuse detected":
                return("No abuse detected")
            else:
                return("Abuse Detected")
