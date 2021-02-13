import http.client, urllib.parse
import json
import requests


subscription_key = '49f338f093b4425ebf55c1f0ac08fdb9'

query_string = "VETERANS FOR PEACE"



def interpretJSON(jsonResult, ):



def searchBing(query_string,subscription_key):


    search_url_1 = 'https://api.cognitive.microsoft.com/bing/v7.0/localbusinesses/search'
    search_url_2 = 'https://api.cognitive.microsoft.com/bing/v7.0/entities'

    #Want:

    #Phone #
    #URL
    #Hours

    search_term = query_string

    #TODO: Liam- Add regex to remove inc, any other things?

    #TODO: change abbreviations: STL-> St. Louis
    #                            MO -> Missouri




    #TODO: First run! One call to local business, one call to entities
    

    #TODO: Take both json results, determine if success or failure


    #TODO: Success path: return all known info!

    #TODO: Failure path: add more data(Address, Contact info, etc)
                        

    #cat = 'EatDrink'
    mkt = 'en-US'
    count = '50'
    offset = '0'
    ansCnt = '250'


    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    """
    params = {"q": search_term, "localcategories": cat, "mkt": mkt, "count": count,\
            "offset": offset, "answerCount": ansCnt, "textDecorations": True, "textFormat": "HTML"}
    """
    params = {"q": search_term, "mkt": mkt, "count": count,\
            "offset": offset, "answerCount": ansCnt, "textDecorations": True, "textFormat": "HTML"}


    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    with open('data.json', 'w') as f:
        json.dump(search_results, f)

    #print (json.dumps(json.loads(search_results), indent=4))