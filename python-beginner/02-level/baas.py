'''
A simple coding exercise with input and boolean comparisson
'''
password = 'baas'
user_input = input("Wat is het wachtwoord? ")
baas_online = bool(user_input == password)

print("Baas ingelogd:", baas_online)
