from math import *


file = open("part3.txt", 'r')

tmp = file.readlines()

file.close()

nails = []

for line in tmp:
    nails.append(int(line[:-1]))

strikes = 0

tries = []

for t in nails: # not so proud of this...
    strikes = 0
    for nail in nails:
        strikes += abs(nail - t)
    tries.append(strikes)
    
print(min(tries))
    
print(strikes)