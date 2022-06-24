'''
A coding exercise with arithmic operators and input validation
'''
# Get user input for operation
operate = input("Welke operatie wil je uitvoeren? (+, -, *, / of %\n")
if operate not in "+-*/%":
    print(operate, "is geen geldige operatie. Kies een van +, -, *, / of %")
    exit()

# get validated first number
try:
    x = input("Eerste getal?\n")
    x  = float(x)
except ValueError:
    print("Kan",x,"niet omzetten naar een getal. Zorg dat je '.' gebruikt in plaats van ','.")
    exit()

#get validated second number
try:
    y = input("Tweede getal?\n")
    y  = float(y)
except ValueError:
    print("Kan",y,"niet omzetten naar een getal. Zorg dat je '.' gebruikt in plaats van ','.")
    exit()

# do corresponding operation and output to terminal
if operate == '+':
    print("Resultaat:",x+y)
elif operate == '-':
    print("Resultaat:",x-y)
elif operate == '*':
    print("Resultaat:",x*y)
elif operate == "/":
    if y == 0:
        print("Kan niet delen door 0")
        exit()
    else:
        print("Resultaat:",x/y)
elif operate == '%':
    if y == 0:
        print("Kan niet delen door 0")
        exit()
    else:
        print("Resultaat:",x%y)
