'''
Vraag user input voor de score van speler 1 en speler 2.
Schrijf een programma dat print wie er heeft gewonnen of dat er gelijk is gespeeld.

'''
while True:
    try:
        input1 = int(input("Wat is de score van speler 1?\n"))
        input2 = int(input("Wat is de score van speler 2?\n"))
        break
    except ValueError:
        print("Ongeldige invoer..probeer nogmaals.")

if input1 > input2:
    print("Speler 1 heeft gewonnen!")
elif input1 < input2:
    print("Speler 2 heeft gewonnen!")
else:
    print("Gelijkspel!")
