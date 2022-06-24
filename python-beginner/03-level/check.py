#variabelen
operatie = input('operatie? ') #gewenste berekening
getal_1 = float(input('Eerste getal? ')) #eerste getal
getal_2 = float(input('Tweede getal? ')) #tweede getal
#berekeningen
if operatie == '+':
    print("Resultaat: ", getal_1 + getal_2) #optellen
elif operatie == '-':
    print("Resultaat: ", getal_1 - getal_2) #aftrekken
elif operatie == '*':
    print("Resultaat: ", getal_1 * getal_2) #vermenigvuldigen
elif operatie == '%':
    if getal_2 == 0:
        print('kan niet delen door 0') #errormelding delen en door 0
    else:
        print("Resultaat: ", getal_1 % getal_2) #modulo
elif operatie == '/' and getal_2 == 0:
    print('Kan niet delen door 0') #errormelding delen en door 0
else:
    print('Resultaat: ', getal_1 / getal_2)
