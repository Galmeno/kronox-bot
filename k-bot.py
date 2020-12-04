#k-bot.py
"""
XML version av schemat borde vara det som är lättast att parsea.
    https://webbschema.mdh.se/setup/jsp/SchemaXML.jsp?startDatum=idag&intervallTyp=a&intervallAntal=1&forklaringar=true&sokMedAND=false&sprak=SV&resurser=k.DVA131-24025H20-%2C
"""
import requests
import json
import xml.etree.ElementTree as ET #https://docs.python.org/3/library/xml.etree.elementtree.html

def resurs_format(kurskod): #formaterar resurskoden mot kronox-API.
    decorated_resource = 'k.' + kurskod + '%2C'
    return decorated_resource

def url_build():
    pass

def fetch_schdule(url): #request
    result = requests.get(url_build)
    #Error handling, 200 msg osv...
    return result

def print_kurser(kurser):
    i = len(kurser)

    if i == 1:
        print(f'\nListar {i} kurs.\n')
    else:
        print(f'\nListar {i} kurser.\n')
    
    i -= 1
    while i >= 0:
        print(kurser[i])
        i -= 1

def add_kurs(kurser):
    kurser.append(input("Lägg till kurskod (Kronox-format): "))
    return kurser

def print_post(etree,kurskod):
    print(f'Kurskod: {kurskod}')
    for schemaPost in root.iter('schemaPost'):
        """
        #print(schemaPost[0].text) #bokningsId
        #print(schemaPost[1].text) #bokningstid
        #print(schemaPost[2].text) #timestamp_bokning
        print(schemaPost[3].text) #bokningssignatur
        #print(schemaPost[4].text) #version
        #print(schemaPost[5].text) #senast ändrad
        #print(schemaPost[6].text) #senast ändrad ICAL
        #print(schemaPost[7].text) #senast ändrad av
        print(schemaPost[8][0].text) #Bokningen finns här
        print(schemaPost[9].text) #Resursträd
        #print(schemaPost[10].text)
        #print(schemaPost[11].text)
        #print(schemaPost[12].text)
        print(schemaPost[13].text)#Beskrivning
        print(schemaPost[14].text) #kommentar, krockskydd
        print(schemaPost[15].text)
        #bokningsId
        """
        #print(len(root.findall('./schemaPost/bokadeDatum/')))
        
        for item in root.findall('./schemaPost/bokadeDatum/'):
            print(f"\nTillfälle: {schemaPost[12].text}")#Beskrivning - fel nivå
            di = item.attrib
            for tag, value in di.items():
                print(tag, ' : ', value)
    kommentar = str(schemaPost[13].text).replace('<br>', ' ').replace('Krockskyddskod:','Schema:')
    print(f'Kommentar: {kommentar}')
    print("\n")
    """
    for item in root.findall('./schemaPost/resursTrad/'): #nod 3 lärarkod
        df = item.attrib
        for tag, value in df.items():
            print(tag, ' : ', value)
    """

#START URL BREAKDOWN
url_part_1 = 'https://webbschema.mdh.se/setup/jsp/SchemaXML.jsp?'
start_datum = '2020-12-07' #YYYY-MM-DD format, 'idag' fungerar också.
slut_datum ='2020-12-07' #YYYY-MM-DD format, 'idag' fungerar också.
intervall_typ = 'a'
intervall_antal = 1
forklaringar = 'true' #url is string so bool type is not possible
sok_med = 'false' #url is string so bool type is not possible
sprak = 'sv'
kurser = ['DVA131-24025H20-','DVA128-24136H20-']
resurser = resurs_format(kurser[1])

url_build = url_part_1 + "startDatum=" + start_datum + "&slutDatum=" + slut_datum + "&intervallTyp=" + intervall_typ + "&intervallAntal=" + str(intervall_antal) + "&forklaringar=" + forklaringar + "&sokMedAND=false"+"&sprak"+ sprak + "&resurser=" + resurser

print("\n\n")
print(url_build)
print("\n")
#END URL BREAKDOWN

r = fetch_schdule(url_build)
r = r.content
root = ET.fromstring(r)

#main
print_post(root,kurser[0])
kurser = add_kurs(kurser)
print_kurser(kurser)