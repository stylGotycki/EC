file = open("part2.txt", "r")

tmp = file.readlines()

file.close()

grid = []
for t in tmp:
    grid.append(list(t[:-1]))
    
for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = 1 if grid[i][j] == '#' else 0


possible = True
while possible:
    possible = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 0:
                depth = grid[i][j]
                
                if grid[i-1][j] < depth:
                    continue
                if grid[i+1][j] < depth:
                    continue
                if grid[i][j-1] < depth:
                    continue
                if grid[i][j+1] < depth:
                    continue
                
                grid[i][j] += 1
                possible = True
    
                
    for i in range(len(grid)):
        print(grid[i])
        
total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        total += grid[i][j]
        
print(total)