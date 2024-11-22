X = 0
Y = 1

file = open('part1.txt', 'r')
lines = file.readlines()
file.close()

cols = len(lines[0][:-1])
rows = len(lines)

maze = [[0 for i in range(cols)] for j in range(rows)]

start, end = (), ()

for i in range(rows):
    for j in range(cols):
        maze[i][j] = lines[i][j]
        
        if maze[i][j] == 'S':
            start = (i, j)
        
        if maze[i][j] == 'E':
            end = (i, j)

print(start, end)