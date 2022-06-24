'''
A simple coding exercise with functions
'''
def has_a(string):
    if "a" in string:
        print(f"a zit in {string}")
    else:
        print(f"a zit niet in {string}")

word_list = ["functies","zijn","handig"]

for word in word_list:
    has_a(word)
