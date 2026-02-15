import random

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lower_c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

upper_c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

compine= digits+lower_c+upper_c

max_l=8
passw=''
for x in range(max_l):
    passw= passw +random.choice(compine)

print(passw)