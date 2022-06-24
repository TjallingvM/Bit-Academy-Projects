'''
Auteur: Tjalling van Mourik
Datum: 02-04-2022

faculteit.py:
De voorbeelduitwerking van Python Novice -> 3. Tijdmachine -> 2. Vote or Die
Bouw een applicatie die dit stemproces uitvoert
'''

uitslag = False
votes_dom = 0
votes_zac = 0

while not uitslag:
    vote = input("Op wie wil je stemmen? ")
    if vote.upper() == 'DOMINIQUE':
        votes_dom += 1
    elif vote.upper() == "ZACHARIA":
        votes_zac += 1
    elif vote.upper() == "UITSLAG":
        uitslag = True

if votes_dom > votes_zac:
    print("Dominique heeft gewonnen")
elif votes_dom < votes_zac:
    print("Zacharia heeft gewonnen")
else:
    print("Het is gelijkspel")
