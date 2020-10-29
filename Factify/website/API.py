import requests
import urllib, json
import pandas as pd

### GOOGLE FACT CHECK API FINAL

def Factcheck(INPUTkey):
  ## Calling the Google Fact Checking Tool API
        API_ENDPOINT = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
        API_KEY = "AIzaSyAcZEv6K8-DWOlZMjALIrpCb5-8exqQ4To"
        text=INPUTkey.replace(' ','%20')
        URL = API_ENDPOINT + '?' + 'languageCode=en-US'+'&'+'query='+text+'%20'+'&'+'key='+API_KEY
        operUrl = urllib.request.urlopen(URL)
        if (operUrl.getcode()==200):
            data = operUrl.read()
            if (json.loads(data) != {}):
                jsonData = json.loads(data)
                ##Creation of empty lists so that the output can be added in this 
                Rating=[]
                Text=[]
                for i in range (len(jsonData['claims'])):
                    ## Getting Rating of the input fact
                    D=jsonData['claims'][i]['claimReview'][0]['textualRating']
                    Rating.append(D)
                    df = pd.DataFrame(Rating,columns=['RATING'])
                    ## Getting the full text from google approved sources
                    E=jsonData['claims'][i]['text']
                    Text.append(E)
                    df1 = pd.DataFrame(Text,columns=['TEXT'])

            ##Combining all the output into a single Data Frame
                    Fin = pd.concat([df[0:5],df1[0:5]], axis=1)
                return(Fin)

            elif (json.loads(data)=={}):
                return("Sorry! This Fact Has Not yet been reviewed by Google")
        else:
            return("Error receiving data")