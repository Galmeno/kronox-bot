#KXBot
#Anders Galmén 2020
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, date, timedelta
from setup import questions
#import discord_create_msg

def logger(event_id):
    print(f"Event {event_id} called, {datetime.now()}")

def resurs_format(kurskod): #formaterar resurskoden mot kronox-API.
    kx_kurskod = 'k.' + kurskod + '%2C'
    return kx_kurskod

def url_build(kx_kurs):
    """
    Takes a course id.
    Returns an URL formatted for XML.
    """
    url_part_1 = 'https://webbschema.mdh.se/setup/jsp/SchemaXML.jsp?'
    today = date.today()
    end_date = date.today() + timedelta(2)
    start_datum = today.isoformat() #YYYY-MM-DD format, 'idag' fungerar också.
    slut_datum = end_date.isoformat() #YYYY-MM-DD format, 'idag' fungerar också.
    intervall_typ = 'a'
    intervall_antal = 1
    forklaringar = 'true' #url is string so bool type is not possible
    sok_med = 'false' #url is string so bool type is not possible
    sprak = 'sv'
    
    url_build = url_part_1 + "startDatum=" + start_datum + "&slutDatum=" + slut_datum + "&intervallTyp=" + intervall_typ + "&intervallAntal=" + str(intervall_antal) + "&forklaringar=" + forklaringar + "&sokMedAND=false"+"&sprak"+ sprak + "&resurser=" + kx_kurs
    
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

def add_question(course:str,question:str):
    """
    Add a question to a specific course.
    Args: course DVA248,"What is the time?"
    returns True
    """
    global questions
    #questions.append([course,question,str(datetime.now())])
    questions.append([course,question])
    print(f"Question added for {course}: {question}")
    return True

def show_questions(course:str):
    global questions
    for question in questions:
        if question[0] == course:
            yield question[1]

def del_question(course:str,index):
    global questions
    for question in range(len(questions)):
        if questions[question][0] == course:
            questions[question][1].pop(index-1)
            break
    print(f"Question {question} deleted.")

def make_msg(kurser,kurskod,k_index):
    resurser = resurs_format(kurser[k_index])
    url = url_build(resurser)
    r = fetch_schdule(url)
    r = r.content
    root = ET.fromstring(r)
    etree = root

    tillfalle = []
    for schemaPost in root.iter('schemaPost'):
        try:        
            for item in root.findall('./schemaPost/bokadeDatum/'):
                tillfalle.append(kurskod + " / " + schemaPost[12].text)
                di = item.attrib
                for tag, value in di.items():
                    tillfalle.append(value)
            datum_temp = '20' + tillfalle[1]
            tillfalle[1] = date(int(datum_temp[0:4]),int(datum_temp[4:6]),int(datum_temp[6:8])).isoformat()
            if datum_temp == idag:
                tillfalle[0] = tillfalle[0] + " **IDAG!**"
            kommentar = str(schemaPost[13].text).replace('<br', ' ').replace('Krockskyddskod:','Schema:').replace('>', ' ')
            cleanstring = str(tillfalle[0])
            cleanstring = cleanstring.replace("&#246;", "ö").replace("&#228;","ä") #fixar ö och ä
            tillfalle[0] = cleanstring
            tillfalle.append(kommentar)
            tillfalle[2] = " / **" + tillfalle[2] + " - " + tillfalle[3] +"**"
            tillfalle.pop(3)
            tillfalle[1] = "**" + tillfalle[3] +"dag** " + tillfalle[1] + " vecka " + tillfalle[4] + tillfalle[2]
            tillfalle.pop(3)
            tillfalle.pop(3)
            tillfalle.pop(2)
        except:
            pass
    """
    for item in root.findall('./schemaPost/resursTrad/'): #nod 3 lärarkod
        df = item.attrib
        for tag, value in df.items():
            print(tag, ' : ', value)
    """
    return tillfalle

#current date and time
now = datetime.now()
#date and time format: dd/mm/YYYY H:M:S
format = "%Y%m%d"
#format datetime using strftime()
idag = now.strftime(format)

print(idag)
kurser = ['DVA248-VA248V21-','DVA340-14029V21-']
msg_dva248 = make_msg(kurser,'DVA248',0)
#msg_dva340 = make_msg(kurser,'DVA340',1)

import discord_connect