file = open("part3.txt", "r")

tmp = file.readlines()

file.close()

print(tmp[len(tmp)-1])
print(tmp)
grid = []
for t in tmp:
    grid.append(list(t[:-1]))
    
for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = 1 if grid[i][j] == '#' else 0


print(grid)

file = open("part3t.txt", 'w')
possible = True
while possible:
    possible = False
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            if grid[i][j] > 0:
                depth = grid[i][j]

                # horizontal
                if grid[i-1][j] < depth:
                    continue
                if grid[i+1][j] < depth:
                    continue
                
                #vertical
                if grid[i][j-1] < depth:
                    continue
                if grid[i][j+1] < depth:
                    continue
                
                #diagonal
                if grid[i-1][j-1] < depth:
                    continue
                if grid[i+1][j-1] < depth:
                    continue
                if grid[i-1][j+1] < depth:
                    continue
                if grid[i+1][j+1] < depth:
                    continue
                
                grid[i][j] += 1
                possible = True
    
    for row in grid:
        for el in row:
            file.write(str(el))
        file.write("\n")
    
    file.write("=========================================================\n")

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        total += grid[i][j]


for row in grid:
    for el in row:
        file.write(str(el))
    file.write("\n")
    
    
file.close()

print(total)