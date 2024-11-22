X = 0
Y = 1
Z = 2

file = open("part3.txt", 'r')

paths = []

for line in file.readlines():
    paths.append(line[:-1].split(','))
    
file.close()

positions = []
max_y = 0

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
        
        if pos[Y] > max_y:
            max_y = pos[Y]
            
    positions.append(pos)


# it's nice, but does not solve the problem
# todo: somehow get to know where leaves start appearing
# then solve for murkiness (retarted distance...)                                        
y_coords = [pos[Y] for pos in positions]

y_coords.sort()
n = len(y_coords)

if n % 2 == 1:
    median_y = y_coords[n//2]
else:
    median_y = (y_coords[n//2 - 1] + y_coords[n//2]) // 2

optimal = [0, median_y, 0]

distance = 0
for x, y, z in positions:
    distance += abs(x) + abs(z) + abs(y - median_y)

print(median_y, max_y)
print(max_y - median_y)
print(distance)     