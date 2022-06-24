'''
A simple coding exercise for finding highest number without built-in function max()
'''
highest = 0
my_list = [3, 7, 10, 40, 2, 4, 8]
for item in my_list:
    if item > highest:
        highest = item
print(highest)
