file = open('part1.txt', 'r')

line = file.readline()

file.close()

sum = 0

for letter in line:
    if letter == 'A':
        continue
    if letter == 'B':
        sum += 1
    if letter == 'C':
        sum += 3
    
print(sum)