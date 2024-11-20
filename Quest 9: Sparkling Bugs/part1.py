file = open('part1.txt', 'r')

notes = []

for line in file.readlines():
    notes.append(int(line[:-1]))
    
file.close()

dots = [1, 3, 5, 10]

bettles_count = 0

for note in notes:
    value = note
    i = len(dots)-1
    
    while value != 0:
        if value - dots[i] < 0:
            i -= 1
            continue
        
        value -= dots[i]
        
        bettles_count += 1
        

print(bettles_count)