'''
Auteur: Tjalling van Mourik
Datum: 03-04-2022

hoeveel_dagen.py:
De voorbeelduitwerking van Python Novice -> 4. Vreemde figuren -> 3. What Day Is It

Vraag de gebruiker om het jaar.
Vraag de gebruiker om de maand.
Vraag de gebruiker om de dag.
Print hoeveel dagen verschil er zit tussen deze datum en vandaag.
'''

from datetime import datetime

year = int(input("Wat is het jaar?\n"))
month = int(input("Wat is het maandnummer?\n"))
day = int(input("Wat is de dag?\n"))

user_date = datetime(year,month,day)
current_date = datetime.now()

print(user_date - current_date)
