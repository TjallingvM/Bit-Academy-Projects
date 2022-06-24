'''
Auteur: Tjalling van Mourik
Datum: 02-04-2022

roulette.py:
De voorbeelduitwerking van Python Novice -> 3. Tijdmachine -> 6. Rien Ne Va Plus


Wanneer je het programma begint, begin je met een saldo van 10 chips. De roulettetafel laat je inzetten op
de getallen 1 tot en met 36: elke keer inzetten kost één chip. Je mag meerdere keren een chip inzetten op hetzelfde getal,
of meerdere keren een chip op verschillende getallen. Als je genoeg chips hebt ingezet, dan typ je STOP en begint het spel.

Er wordt rien ne va plus gezegd, en dan wordt er een willekeurig getal tussen de 1 en 36 getrokken.

Er wordt dus een getal als uitkomst genomen. Voor elke chip die de speler op het goede getal heeft ingezet,
krijgt de speler 35 chips cadeau. Als de speler een chip op een verkeerd getal heeft ingezet, dan verliest de speler de chip.

Als de speler uiteraard al zijn chips inzet, dan moet het spel dat zelf detecteren en meteen rien ne va plus zeggen.
De speler mag doorspelen tot zijn chips op zijn. In dat geval zegt het spel GAME OVER en stopt het programma.

Bouw de roulette game met de bovenstaande regels
'''

from random import randint

def getNumber() -> int:
    ''' Krijg een nummer tussen 1 tm 36'''
    return randint(1,36)

def getBets(chips) -> []:
    bets = []
    print(f"Je hebt {chips} chips!")
    print("Op welke nummers wil je inzetten?")
    while chips:
        bet = input()
        if bet.isnumeric():
            bets.append(bet)
            chips -= 1
        elif bet == 'STOP':
            break
    return bets, chips


player_chips = 10
gameOn = True

while gameOn:
    player_bets, player_chips = getBets(player_chips)
    print("rien ne va plus")
    number = getNumber()
    print(f"De uitkomst is {number}")
    for player_bet in player_bets:
        if player_bet == number:
            player_chips += 35

    if player_chips == 0:
        gameOn = False
        print("GAME OVER")
