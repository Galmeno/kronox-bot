#k-bot.py
"""
XML version av schemat borde vara det som är lättast att parsea.
https://webbschema.mdh.se/setup/jsp/SchemaXML.jsp?startDatum=idag&intervallTyp=a&intervallAntal=1&forklaringar=true&sokMedAND=false&sprak=SV&resurser=k.DVA131-24025H20-%2C
"""
import requests
import json
import xml.etree.ElementTree as ET #https://docs.python.org/3/library/xml.etree.elementtree.html

#START URL BREAKDOWN
url_part_1 = 'https://webbschema.mdh.se/setup/jsp/SchemaXML.jsp?'
start_datum = 'idag'
slut_datum ='2020-12-31'
intervall_typ = 'a'
intervall_antal = 1
forklaringar = 'true' #url is string so bool type is not possible
sok_med = 'false' #url is string so bool type is not possible
sprak = 'sv'
resurser = 'k.DVA131-24025H20-%2C' #kurskod med decorator

url_build = url_part_1 + "startDatum=" + start_datum + "&slutDatum=" + slut_datum + "&intervallTyp=" + intervall_typ + "&intervallAntal=" + str(intervall_antal) + "&forklaringar=" + forklaringar + "&sokMedAND=false"+"&sprak"+ sprak + "&resurser=" + resurser
print("\n\n")
print(url_build)
print("\n")
#END URL BREAKDOWN

#Request
r = requests.get(url_build)
r = r.content

#XML-parse
root = ET.fromstring(r) #variant 2
print(type(root))

for child in root:
    print(child.tag, child.attrib)