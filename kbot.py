#KXBot
#Anders Galmén 2020
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
#import discord_create_msg

def resurs_format(kurskod): #formaterar resurskoden mot kronox-API.
    decorated_resource = 'k.' + kurskod + '%2C'
    return decorated_resource

def url_build():
    url_part_1 = 'https://webbschema.mdh.se/setup/jsp/SchemaXML.jsp?'
    start_datum = 'idag' #YYYY-MM-DD format, 'idag' fungerar också.
    slut_datum ='2020-12-07' #YYYY-MM-DD format, 'idag' fungerar också.
    intervall_typ = 'a'
    intervall_antal = 1
    forklaringar = 'true' #url is string so bool type is not possible
    sok_med = 'false' #url is string so bool type is not possible
    sprak = 'sv'
    
    url_build = url_part_1 + "startDatum=" + start_datum + "&slutDatum=" + slut_datum + "&intervallTyp=" + intervall_typ + "&intervallAntal=" + str(intervall_antal) + "&forklaringar=" + forklaringar + "&sokMedAND=false"+"&sprak"+ sprak + "&resurser=" + resurser
    
    return url_build

def fetch_schdule(url): #request
    result = requests.get(url)
    if result.status_code == 200:
        print("HTTP code 200, success!")
    else:
        print(f"Bad result, HTTP code: {result.status_code}")
    return result

def add_kurs(kurser):
    kurser.append(input("Lägg till kurskod (Kronox-format): "))
    return kurser

def make_msg(etree,kurskod):

    tillfalle = []
    for schemaPost in root.iter('schemaPost'):        
        for item in root.findall('./schemaPost/bokadeDatum/'):
            tillfalle.append(kurskod + " / " + schemaPost[12].text)
            di = item.attrib
            for tag, value in di.items():
                tillfalle.append(value)
    kommentar = str(schemaPost[13].text).replace('<br', ' ').replace('Krockskyddskod:','Schema:').replace('>', ' ')
    cleanstring = str(tillfalle[0])
    cleanstring = cleanstring.replace("&#246;", "ö").replace("&#228;","ä") #fixar ö och ä
    tillfalle[0] = cleanstring
    tillfalle.append(kommentar)
    tillfalle[2] = " / **" + tillfalle[2] + " - " + tillfalle[3] +"**"
    tillfalle.pop(3)
    tillfalle[1] = "**" + tillfalle[3] +"dag** 20" + tillfalle[1] + " vecka " + tillfalle[4] + tillfalle[2]
    tillfalle.pop(3)
    tillfalle.pop(3)
    tillfalle.pop(2)
    """
    for item in root.findall('./schemaPost/resursTrad/'): #nod 3 lärarkod
        df = item.attrib
        for tag, value in df.items():
            print(tag, ' : ', value)
    """
    return tillfalle

kurser = ['DVA131-24025H20-','DVA128-24136H20-']
resurser = resurs_format(kurser[1])
url = url_build()
r = fetch_schdule(url)
r = r.content
root = ET.fromstring(r)

#current date and time
now = datetime.now()
#date and time format: dd/mm/YYYY H:M:S
format = "%Y%m%d"
#format datetime using strftime()
idag = now.strftime(format)
print(idag)

msg_dva131 = make_msg(root,'DVA131')
msg_dva128 = make_msg(root,'DVA128')

import discord_connect