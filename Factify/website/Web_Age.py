import requests
from bs4 import BeautifulSoup

def webage(inputURL):
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
            g = items.find_all("tr", id = "trWebAge")
            for items4 in g:
                h = items4.find_all("td")
                i = (h[-1].text.split())
                z = int(i[i.index("months")-1]) if "months" in i else 0
                w = (int(i[i.index("years")-1])*12) + z
                if w != None:
                    return(str(w) + " months") 
                else: return("NA")
