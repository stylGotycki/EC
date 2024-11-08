file = open("part1.txt", 'r')

tmp = file.readlines()

file.close()

nails = []

for line in tmp:
    nails.append(int(line[:-1]))

shortest = min(nails)

strikes = 0

for nail in nails:
    if nail <= shortest:
        continue
    strikes += (nail - shortest)
    
print(strikes)