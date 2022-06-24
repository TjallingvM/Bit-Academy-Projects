'''
Schrijf een programma dat input voor twee getallen vraagt.
Schrijf een functie om deze twee getallen met elkaar te vermenigvuldigen.
Print het resultaat.
'''
def getMultiplied(a , b) -> int:
    return a * b

while True:
    try:
        input1 = int(input("Getal a:\n"))
        input2 = int(input("Getal b:\n"))
        break
    except ValueError:
        print("Ongeldige invoer..probeer nogmaals.")

print("a x b =",getMultiplied(input1,input2))
