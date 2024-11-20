X = 0
Y = 1
        #   A  B  C
segments = [1, 2, 3]

file = open('part2.txt', 'r')
lines = file.readlines()
file.close()

# TARGETS
targets = []

for i in range(len(lines)):
    line = lines[i][:-1]
    
    for j in range(len(line)):
        if line[j] == 'T':
            targets.append((j-1, len(lines)-i-1,)) # (x,y) cartesian
        if line[j] == 'H':
            targets.append((j-1, len(lines)-i-1,)) # (x,y) cartesian
            targets.append((j-1, len(lines)-i-1,)) # (x,y) cartesian
            # lol
            
print(targets)


def rank_value(target: tuple[int, int]) -> int:
    vector = (abs(1 - target[Y]), 1 - target[Y])
    
    target_n = (target[X]+vector[X], target[Y]+vector[Y])

    return segments[target_n[X]%3] * (target_n[X]//3)


total = 0    
for target in targets:
    print(rank_value(target))
    total += rank_value(target)
    
print(total)