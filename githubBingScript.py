import http.client, urllib.parse
import json
import requests



subscription_key = '49f338f093b4425ebf55c1f0ac08fdb9'

#search_url = 'https://api.cognitive.microsoft.com/bing/v7.0/localbusinesses/search'
search_url = 'https://api.cognitive.microsoft.com/bing/v7.0/entities'


#Want:

#Phone #
#URL
#Hours


search_term = "Kalamazoo Community Foundation"
#cat = 'EatDrink'
mkt = 'en-US'
count = '50'
offset = '0'
ansCnt = '250'
clientID = '2006AB3908B26A1023A8A6E9094F6BDB'
locationList = '["lat":38.5767; "long":-92.1735; "re":250000]'

headers = {"Ocp-Apim-Subscription-Key": subscription_key,"X-MSEdge-ClientID": clientID, "X-Search-Location" : locationList}

params = {"q": search_term, "mkt": mkt, "count": count,\
          "offset": offset, "answerCount": ansCnt, "textDecorations": True, "textFormat": "HTML", "responseFilter": "Places"}




response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()


search_results = response.json()

if(search_results["_type"]!="SearchResponse"):
    print("search failed!")

else:
    print("search succeeded!")
    

with open('data.json', 'w') as f:
    json.dump(search_results, f)


#print (json.dumps(json.loads(search_results), indent=4))