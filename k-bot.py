#k-bot.py
"""
XML version av schemat borde vara det som är lättast att parsea.
https://webbschema.mdh.se/setup/jsp/SchemaXML.jsp?startDatum=idag&intervallTyp=a&intervallAntal=1&forklaringar=true&sokMedAND=false&sprak=SV&resurser=k.DVA131-24025H20-%2C

"""
import requests
import json

#url breakdown
url = "https://webbschema.mdh.se/setup/jsp/Schema.jsp?startDatum=idag&intervallTyp=a&intervallAntal=1&forklaringar=true&sokMedAND=false&sprak=SV&resurser=k.DVA131-24025H20-%2C"
r = requests.get(url)
rd = r.json()

url_part_1 = 'https://webbschema.mdh.se/setup/jsp/SchemaXML.jsp?'
start_datum = 'idag'
intervall_typ = 'a'
intervall_antal = 1
forklaringar = 'true' #url is string so bool type is not possible
sok_med = 'false' #url is string so bool type is not possible
sprak = 'sv'
resurser = 'k.DVA131-24025H20-%2C'

url_build = url_part_1 + "startDatum=" + startdatum + "&intervallTyp=" + intervall_typ + "&intervallAntal" + intervall_antal + "&forklaringar=" + forklaringar + "&sokMedAND=false"+"&sprak"+ sprak + "&resurser=" + resurser



