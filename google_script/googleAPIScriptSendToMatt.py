import http.client, urllib.parse
import json
import requests
import pandas as pd
import numpy as np


data = {}


import re


INC_RE_STR = r'inc(?:.|orporated)?'
PHONE_RE_STR = r'(\([0-9]{3}\)|[0-9]{3})[ -._]?([0-9]{3})[ -._]?([0-9]{4})'
PHONE_RE = re.compile(PHONE_RE_STR)

#begin Liam's utility code

def format_phone_number(raw_phone_string):
    # type: (str) -> str
    phone_match = PHONE_RE.search(raw_phone_string)
    if phone_match is None:
        return None
    phone_number = '314'
    if phone_match.group(1)[0] == '(':
        phone_number = str(phone_match.group(1))[1:4]
    else:
        phone_number = phone_match.group(1)
    phone_number = '{}{}{}'.format(phone_number,
                                   phone_match.group(2),
                                   phone_match.group(3))
    return phone_number

def get_search_term_for_company(company_name, city, state):
    # strip inc from company_name
    search_term = re.sub(INC_RE_STR, '', company_name, flags=re.IGNORECASE)
    search_term = search_term.strip()
    if city:
        search_term = '{} {}'.format(search_term, city)
    if state:
        search_term = '{} {}'.format(search_term, state)
    return search_term

#End Liam's utility code


##Returns an array of website, phonenumber, and hours
def pass_to_google_places(organization_name):
    organization_name=organization_name.replace(" ", "%20")
    #Pulls the placeID from search parameters
    searchID_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input='+organization_name+'&inputtype=textquery&fields=place_id&locationbias=circle:2000@47.6918452,-122.2226413&key=___API___KEY______'
    response = requests.get(searchID_url)
    response.raise_for_status()
    search_results = response.json()
    place_id=search_results["candidates"][0]["place_id"]
    
    #pulls the name, website, phonenumber, and hours
    searchDetails_Url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid='+place_id+'&fields=name,website,opening_hours,formatted_phone_number&key=___API___KEY______'
    response = requests.get(searchDetails_Url)
    response.raise_for_status()
    search_details = response.json()

    if 'result' not in search_details:
        phone_number = None
        website = None
        json_data = None
        return website,phone_number,json_data

    if 'formatted_phone_number' in search_details['result']:
        raw_phone_number = search_details['result']['formatted_phone_number']
        phone_number = format_phone_number(raw_phone_number)
    else:
        phone_number = None
    
    if 'website' in search_details['result']:
        website = search_details['result']['website']
    else:
        website = None
    open_all_the_time = False
    if 'opening_hours' in search_details['result']:
        day_names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        to_remove = [0,1,2,3,4,5,6]
        stringToDump = "data = {\n\t'hours': {\n"
        for i in search_details['result']['opening_hours']['periods']:
            day_of_week = i['open']['day']
            if(day_of_week ==0):
                open_all_the_time = True
                break
            thisDay = day_names[day_of_week-1]
            to_remove[day_of_week-1]=-1
            currentString = "\t\t'"
            currentString=currentString+thisDay+"': {\n\t\t\t'opens_at': '"
            openTime = i['open']['time']
            openTime = openTime[0:2]+":"+openTime[2:4]
            currentString = currentString + openTime + "',\n\t\t\t'closes_at': '"
            if 'close' not in i or (i['close']['time']=="00:00" and i['open']['time']=="00:00"):
                closingTime = '24:00'
            else:
                closingTime = i['close']['time']
                closingTime = closingTime[0:2]+":"+closingTime[2:4]
            currentString = currentString + closingTime + "'\n\t\t},\n "
            stringToDump = stringToDump + currentString

        for j in to_remove :
            if j > -1:
                thisDay = day_names[j]
                currentString = "\t\t'"
                currentString=currentString+thisDay+"': {\n\t\t\t'opens_at': '"
                openTime = '00:00'
                currentString = currentString + openTime + "',\n\t\t\t'closes_at': '"
                if open_all_the_time:
                    closingTime = '24:00'
                else:
                    closingTime = '00:00'
                currentString = currentString + closingTime + "'\n\t\t},\n "
                stringToDump = stringToDump + currentString


        stringToDump = stringToDump + "\t},\n}"

        exec(stringToDump, None, globals())
        
        json_data = json.dumps(data)
    
    else:
        json_data = None

    #with open('output_data.json', 'w') as f:
    #   json.dump(data, f)


    #with open('data2.json', 'w') as f:
    #    json.dump(search_details, f)

    return website,phone_number,json_data

organization_name = "mcdonalds 24 hour"
print(pass_to_google_places(organization_name))