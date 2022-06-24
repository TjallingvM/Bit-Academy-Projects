'''
Auteur: Tjalling van Mourik
Datum: 02-04-2022

blok_aanpassen.py:
De voorbeelduitwerking van Python Novice -> 4. Vreemde figuren -> 2. Minecraft

Als eerste willen we een grasblok in een sneeuwblok laten veranderen.
Hiervoor moet je 'snow' op 'True' zetten. Vervolgens willen we de locatie van het blok aanpassen:
we verschuiven het blok + 66 in de y-richting en we maken het z-coördinaat drie keer zo groot.

Lees gras_blok.json in met Python.
Pas de eigenschappen aan zoals hierboven genoemd.
Sla deze aangepaste dictionary op als JSON bestand noem deze sneeuw_blok.json. Deze lever je naast je code ook in.
'''

import json

with open("gras_blok.json") as json_file:
    blok_dict = json.load(json_file)

blok_dict['block']['snow']  = True
blok_dict['block']['coordinates']['y'] += 66
blok_dict['block']['coordinates']['z'] *= 3

with open('sneeuw_blok.json', 'w') as outfile:
    json.dump(blok_dict, outfile)
