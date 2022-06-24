'''
Vraag de gebruiker om hun leeftijd;
Print of de gebruiker al mag beginnen met rijlessen.
'''
while True:
    try:
        input_age = float(input("Hoe oud ben je?\n"))
        break
    except ValueError:
        print("Ongeldige invoer..probeer nogmaals.")

legal_age = 16.5
if input_age >= legal_age:
    print("Je mag beginnen met rijlessen!")
else:
    print("Helaas, je mag nog niet beginnen met rijlessen.")
