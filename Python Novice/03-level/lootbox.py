'''
Auteur: Tjalling van Mourik
Datum: 02-04-2022

lootbox.py:
De voorbeelduitwerking van Python Novice -> 3. Tijdmachine -> 4. Shake your Lootbox

Schrijf een bestand dat vijf skins met behulp van een for-loop ophaalt;
Tel hoeveel skins je van elke zeldzaamheid hebt gekregen en print de oplossing in de terminal.

'''
import rewards
lootbox = {"COMMON":0, "RARE":0, "EPIC":0, "LEGENDARY":0}

for i in range(5):
    skin = rewards.get_new_skin()
    lootbox[skin] += 1

for key, value in lootbox.items():
    if value > 0:
        print(str(value)+"x",key.lower())
