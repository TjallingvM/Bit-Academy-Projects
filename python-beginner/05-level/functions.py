'''
Maak een functie die het volume van een kubus berekent.
volume kubus = lengte * breedte * hoogte.
Alle zijden van een kubus zijn even lang.
Maak een functie die het oppervlakte van een kubus berekent.
oppervlakte kubus = 6 * zijde * zijde.
Maak een functie die beide functies combineert om zowel het volume als de oppervlakte in één keer te berekenen.
Bereken vervolgens de volumes en oppervlakte van kubussen van met zijden van lengte 5, 10 en 20.
'''

def get_volume(kub_side):
    return kub_side**3

def get_opp(kub_side):
    return 6*kub_side**2

def get_volume_and_opp(kub_side):
    vol = get_volume(kub_side)
    opp = get_opp(kub_side)
    return vol,opp

sides = [5,10,20]
for side in sides:
    kub_vol,kub_opp = get_volume_and_opp(side)
    print(f"oppervlakte = {kub_opp} en volume = {kub_vol}")
