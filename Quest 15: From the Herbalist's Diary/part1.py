X = 0
Y = 1

PERMITTED = '#'
ALLOWED = '.'
HERB = 'H'

file = open('part1.txt', 'r')

grid = []
distances = []

lines = file.readlines()

for i in range(len(lines)):
    grid.append([])
    distances.append([])

    for c in lines[i][:-1]:
        grid[i].append(c)
        distances[i].append(0)

file.close()

start = []
for i in range(len(grid[0])):
    if grid[0][i] == ALLOWED:
        start = [0, i]


WIDTH = len(grid[0])
HEIGHT = len(grid)

to_visit = [start]
visited = []

herb_distance = 0

while len(to_visit) != 0:
    current = to_visit.pop(0)
    
    if current in visited:
        continue
    
    visited.append(current)
    # print(current, end="")
    
    x = current[X]
    y = current[Y]
    distance = distances[x][y]
    
    if grid[x][y] == HERB:
        print(f"found at ({x},{y})")
        herb_distance = distances[x][y]
        break
    
    if x-1 > 0 and grid[x-1][y] != PERMITTED:
        to_visit.append([x-1, y])
        if distances[x-1][y] == 0: 
            distances[x-1][y] = distance + 1
    
    if y-1 > 0 and grid[x][y-1] != PERMITTED:
        to_visit.append([x, y-1])
        if distances[x][y-1] == 0: 
            distances[x][y-1] = distance + 1
        
    if x+1 < WIDTH and grid[x+1][y] != PERMITTED:
        to_visit.append([x+1, y])
        if distances[x+1][y] == 0: 
            distances[x+1][y] = distance + 1
        
    if y+1 < HEIGHT and grid[x][y+1] != PERMITTED:
        to_visit.append([x, y+1])
        if distances[x][y+1] == 0: 
            distances[x][y+1] = distance + 1

    
print(herb_distance*2)




# for line in distances:
#     print(line)
    
# for line in grid:
#     print(line)