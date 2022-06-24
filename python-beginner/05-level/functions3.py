'''
A simple coding exercise with functions
'''

def tel_kleine_letters(woord):
    aantal_kleine_letters = 0
    for karakter in woord:
        if 'a' <= karakter <= 'z': # letter is kleine letter
            aantal_kleine_letters += 1
    return aantal_kleine_letters

def alle_kleine_letters(string_list):
    '''Telt alle kleine letters per woord en totaal'''
    totaal = 0
    for string in string_list:
        aantal = tel_kleine_letters(string) #We roepen de functie aan, en geven een woord mee.
        print(f"Er zitten {aantal} kleine letters in {string}") #we printen het aantal kleine letters in het meegegeven woord
        totaal += aantal # we tellen het totaal aantal kleine letters op bij het totaal aantal kleine letters
    print(f"Totaal getelde aantal kleine letters: {totaal}") # we printen het totaal aantal kleine letters van alle woorden;
                                                            # zie dat we dit print-statement buiten de for-loop zetten...

strings = ('Bit' 'Academy' 'Bit-Academy' 'bit' '-''AcAdEmY')
# print(strings)
alle_kleine_letters(strings)
