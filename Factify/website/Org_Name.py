import requests
from bs4 import BeautifulSoup


def orgname(inputURL):
    if inputURL.split("/")[0] == "https:":
        website = inputURL.split("/")[2]
    elif inputURL.split("/")[0] == "http:":
        website = inputURL.split("/")[2]
    else:
        URLlist = inputURL.split(".")
        website = URLlist[-2] + "." + URLlist[-1].split("/")[0]
    result = requests.get("https://domainbigdata.com/" + website)
    soup = BeautifulSoup(result.text, 'html.parser')
    table_1 = soup.find_all("table", class_ = "websiteglobalstats em-td2 trhov")

    for items in table_1:
        c = items.find_all("tr", id = "MainMaster_trRegistrantOrganization")
    if c == []: 
        return("NA")

    for items2 in c:
        d = items2.find_all("td")
        for words in d[1]:
            for letters in words:
                if c != []:
                    return(letters)

    