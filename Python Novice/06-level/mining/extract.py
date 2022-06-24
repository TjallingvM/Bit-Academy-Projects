'''
Auteur: Tjalling van Mourik
Datum: 04-04-2022

extract.py:
De voorbeelduitwerking van Python Novice -> 6. Python Extended -> 3. Mining The Interweb

Schrijf een Python programma dat een getal vraagt aan de gebruiker.
Dit getal wordt achter de URL geplakt. Het getal 38 levert dus https://jsonplaceholder.typicode.com/todos/38.
Gebruik de requests module om de JSON van deze website op te halen.
Print de informatie die in de JSON achter title zit.
'''

import requests

try:
    number = str(input("Typ een getal: "))
except ValueError:
    print("ongeldige invoer! Try again")

url_path = "https://jsonplaceholder.typicode.com/todos/"
complete_url = url_path + number
req_response = requests.get(complete_url)

if req_response:                  #als er succesvol file is binnengehaal (leeg of niet)
    response  = req_response.json()
    result = response['title']
    print(result)
