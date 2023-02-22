alpha_list = [chr(i) for i in range(65, 91)]
print(alpha_list)

# alpha_list_exclude=[chr(i) for i in range(65,91) if i%5 !=0]
# print(alpha_list_exclude)

# alpha_list_exclude=[chr(i) for i in range(65,91) if i not in range(70,86,5)]
# print(alpha_list_exclude)

alpha_list_exclude = [
    chr(i) for i in range(65, 91) if i not in [70, 75, 80, 85]
]
print(alpha_list_exclude)

alpha_list_exclude_second = [
    chr(i) for i in range(65, 91)
    if i not in range((ord('F') + 1), ord('O'), 2)
]
print(alpha_list_exclude_second)

#nested list comprehension

[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)]
l = []
for i in range(3):
    for j in range(2):
        l.append((i, j))
print(l)

li_nested = [(i, j) for i in range(3) for j in range(2)]
print(li_nested)

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']
soled_out = [('Black', 'm'), ('White', 's')]

colors_sizes = [(color, size) for color in colors for size in sizes]

colors_sizes_av = [(color, size) for color in colors for size in sizes
                   if (color, size) not in soled_out]
print(colors_sizes_av)

##Sys exercise
# import sys 
import sys

def greeting(x):

    if len(x) == 2 and x[1] == '-it':
        print('interactive terminal started')
    if len(x) == 3 and x[2] == '--rm':
        print('Will be removed at exit')
    else:
        print('Usage: python script.py [-it]{--rm}')

greeting(sys.argv)
