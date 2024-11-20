file = open('part2.txt', 'r')

notes = []

for line in file.readlines():
    notes.append(int(line[:-1]))
    
file.close()

dots = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]

divisible_by = {
    2: [],
    3: [],
    5: []
}


for key in divisible_by:
    for dot in dots:
        if dot % key == 0:
            divisible_by[key].append(dot)

# print(divisible_by)

bettles_count = 0

for note in notes:
    value = note
    i = len(dots)-1
    
    while value != 0:
        if value - dots[i] < 0:
            i -= 1
            continue

        value -= dots[i]
        print(dots[i], end=' ')
        bettles_count += 1
        
    print()

print(bettles_count)