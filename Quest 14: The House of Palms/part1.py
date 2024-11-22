X = 0
Y = 1
Z = 2

file = open("part1.txt", "r")

instructions = file.readlines()[0][:-1].split(',')

file.close()

     # X  Y  Z
pos = [0, 0, 0]
max_y = 0

        # X  Y  Z
vector = [0, 0, 0]
for instruction in instructions:
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
    
    pos[X] += vector[X]*a
    pos[Y] += vector[Y]*a
    pos[Z] += vector[Z]*a
        
    if pos[Y] > max_y:
        max_y = pos[Y]
    
    print(pos)
    
print(max_y)