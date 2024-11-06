file = open('part2.txt', 'r')

line = file.readline()

file.close()

sum = 0

costs = {
    "A": 0,
    "B": 1,
    "C": 3,
    "D": 5,
}

for i in range(0, len(line), 2):
    letterA, letterB = line[i], line[i+1]
    x_flag = False

    cost = 0
    
    if letterA != 'x':
        sum += costs[letterA]
        cost += costs[letterA]
    else:
        x_flag = True
    
    if letterB != 'x':
        sum += costs[letterB]
        cost += costs[letterB]
    else:
        x_flag = True
        
        
    sum  += 0 if x_flag else 2
    cost += 0 if x_flag else 2
    print(f'{letterA} {letterB} = {cost}')
    x_flag = False

    
print(sum)