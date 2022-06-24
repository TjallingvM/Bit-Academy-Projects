Dominique = 0
Zacharia = 0
while True:
    stem = input ("Op wie wil      je stemmen ? ")
    if stem == "Dominique":
        Dominique =+1
    elif stem == "Zacharia":
        Zacharia =+1
    elif stem == "uitslag":
        if Dominique > Zacharia:
            print ("Dominique heeft gewonnen")
        elif Zacharia > Dominique:
            print ("Zacharia heeft gewonnen")
        elif Zacharia == Dominique:
            print ("Dominique en Zacharia hebben een gelijk aantal stemmen")
        break
