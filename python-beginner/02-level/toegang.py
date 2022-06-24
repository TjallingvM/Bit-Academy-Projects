'''
A Simple coding script with IF,ELIF and ELSE
'''
user_input = input("Wat is jouw wachtwoord? ")
if user_input == "baas":
    print("Totale toegang")
elif user_input == 'medewerker':
    print("Gedeeltelijke toegang")
else:
    print("Geen toegang")
