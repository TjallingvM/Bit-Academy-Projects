'''
A famous coding exercise with range() and for-loops and arithmic operators
'''

for i in range(1,101):          # tel van 1 tot 100
    if not i%3 and not i%5 :    # modulo5 en 3  hebben geen restant
        print("FizzBuzz")
    elif not i%3:               # modulo 3 heeft geen restant
        print("Fizz")
    elif not i%5:               # modulo 5 heeft geen restant
        print("Buzz")
    else:
        print(i)
