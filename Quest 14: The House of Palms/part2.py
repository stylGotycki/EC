X = 0
Y = 1
Z = 2

file = open("part2.txt", 'r')

paths = []

for line in file.readlines():
    paths.append(line[:-1].split(','))
    
file.close()

positions = []

for path in paths:
         # X  Y  Z
    pos = [0, 0, 0]
    
            # X  Y  Z
    vector = [0, 0, 0]
    for instruction in path:
        match instruction[0]:
            case 'U':
                vector = [0, 1, 0]
            case 'R':
                vector = [1, 0, 0]
            case 'D':
                vector = [0, -1, 0]
            case 'L':
                vector = [-1, 0, 0]            
            case 'F':
                vector = [0, 0, 1]
            case 'B':
                vector = [0, 0, -1]
        
        a = int(instruction[1:])
        #print(a)
        for _ in range(a):
            pos[X] += vector[X]
            pos[Y] += vector[Y]
            pos[Z] += vector[Z]
            
            positions.append([pos[X], pos[Y], pos[Z]])
                                        
                                        
            
unique = []
for pos in positions:
    if pos in unique:
        continue
    unique.append(pos)


print(len(unique))