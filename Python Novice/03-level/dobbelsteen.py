'''
Auteur: Tjalling van Mourik
Datum: 02-04-2022

dobbelsteen.py:
De voorbeelduitwerking van Python Novice -> 3. Tijdmachine -> 5. Dice and Cubes

Importeer de module random;
Schrijf code waarmee je een getal tussen de één en de zes willekeurig krijgt;
Print je uitkomst in de terminal.

'''
from random import randint

number = randint(1,6)
print("Je rolde een",number)
