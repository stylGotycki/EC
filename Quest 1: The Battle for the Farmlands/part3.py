file = open('part3.txt', 'r')

line = file.readline()

file.close()

sum = 0

costs = {
    "A": 0,
    "B": 1,
    "C": 3,
    "D": 5,
}

for i in range(0, len(line), 3):
    creatures = [line[i], line[i+1], line[i+2]]
    creatures_counter = 0
    cost = 0
    for creature in creatures:
        if creature != 'x':
            creatures_counter += 1
            sum += costs[creature]
            cost += costs[creature]
            
    if creatures_counter == 2:
        sum += 2
        cost += 2

    if creatures_counter == 3:
        sum += 6
        cost += 6
    
    print(creatures, cost)
print(sum)