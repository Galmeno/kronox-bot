#KXBot
#Anders Galmén 2020
import requests
import xml.etree.ElementTree as ET
#import discord_create_msg

def resurs_format(kurskod): #formaterar resurskoden mot kronox-API.
    decorated_resource = 'k.' + kurskod + '%2C'
    return decorated_resource

def url_build():
    pass

def fetch_schdule(url): #request
    result = requests.get(url_build)
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
    tillfalle.append(kommentar)
    tillfalle[2] = "Kl: " + tillfalle[2] + " - " + tillfalle[3]
    tillfalle.pop(3)
    tillfalle[1] = tillfalle[3] +" " + tillfalle[1] + " vecka " + tillfalle[4]
    tillfalle.pop(3)
    tillfalle.pop(3)
    """
    for item in root.findall('./schemaPost/resursTrad/'): #nod 3 lärarkod
        df = item.attrib
        for tag, value in df.items():
            print(tag, ' : ', value)
    """
    return tillfalle

#START URL BREAKDOWN
url_part_1 = 'https://webbschema.mdh.se/setup/jsp/SchemaXML.jsp?'
start_datum = 'idag' #YYYY-MM-DD format, 'idag' fungerar också.
slut_datum ='2020-12-07' #YYYY-MM-DD format, 'idag' fungerar också.
intervall_typ = 'a'
intervall_antal = 1
forklaringar = 'true' #url is string so bool type is not possible
sok_med = 'false' #url is string so bool type is not possible
sprak = 'sv'
kurser = ['DVA131-24025H20-','DVA128-24136H20-']
resurser = resurs_format(kurser[1])

url_build = url_part_1 + "startDatum=" + start_datum + "&slutDatum=" + slut_datum + "&intervallTyp=" + intervall_typ + "&intervallAntal=" + str(intervall_antal) + "&forklaringar=" + forklaringar + "&sokMedAND=false"+"&sprak"+ sprak + "&resurser=" + resurser
#END URL BREAKDOWN

r = fetch_schdule(url_build)
r = r.content
root = ET.fromstring(r)

msg_dva131 = make_msg(root,'DVA131')
msg_dva128 = make_msg(root,'DVA128')

import discord_connect