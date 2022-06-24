'''
Auteur: Tjalling van Mourik
Datum: 02-04-2022

faculteit.py:
De voorbeelduitwerking van Python Novice -> 3. Tijdmachine -> 2. Faculty
Schrijf een applicatie die de faculteit van een getal kan berekenen.
'''

while True: # Controle dat we echt een INT gebruiken, en het anders nogmaals kunnen proberen
    try:
        user_input = int(input("Van welk getal wil je de faculteit weten? "))
        break
    except ValueError:
        print("Ongeldige invoer..probeer nogmaals.")

total = 1
for i in range(1,user_input+1):
    total *= i
print(f"De faculteit van {user_input} is:", total)
