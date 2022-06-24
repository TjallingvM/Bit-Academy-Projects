'''
Coding exercise for the famous Gauss calculation
'''

# De simpele, maar langdurige versie
def simple_calc(start,eind, stap) -> int:
    total = 0
    for i in range(start,eind+1,stap):
        total += i
    return total

# De basis versie van Gauss:
def gauss_calc(eind) -> int:
    ''' Deze werkt alleen als er vanaf 1 geteld wordt..'''
    total = int(eind * (eind+1) / 2)

    return total

# Een aangepaste versie van Gauss:
def gauss_calc_ext(start,eind,stap):
    ''' Deze variate zou moeten kunnen starten vanaf elk getal, en met elke gewenste stap'''
    pairs = 1 + ((eind-start) / stap)
    pair_sum = start + eind

    total_sum = pairs * pair_sum / 2

    return total_sum

print("Kies startgetal,eindgetal en stap:")
start_int =  int(input("Startgetal? :\n"))
end_int = int(input("Eindgetal? :\n"))
step_int = int(input("Geef stap\n"))

print(f"\nTotale som van de getallen: {gauss_calc_ext(start_int, end_int, step_int)}")
