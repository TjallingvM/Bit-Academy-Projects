operator = input("Operator?")
alist = ["+", "-", "*", "/", "%"]
if operator not in alist:
    exit()

if operator in alist:
    try:
        number1 = input("geef me een getal ")
        input_in = float(number1)
    except ValueError:
        print("Dit is geen number, zorg, dat je een number gebruikt!")
    try:
        number2 = input("Geef me nog een getal")
        input_in2 = float(number2)
    except ValueError:
        print("Dit is geen number, zorg, dat je hier ook een number gebruikt!")

    if input_in2 == 0 and operator == "/" or input_in2 == 0 and operator == "%":
        print("Kan niet delen door 0")
    elif operator == "+":
        print(input_in + input_in2)
    elif operator == "*":
        print(input_in * input_in2)
    elif operator == "/":
        print(input_in / input_in2)
    elif operator == "-":
        print(input_in - input_in2)
    elif operator == "%":
        print(input_in % input_in2)
