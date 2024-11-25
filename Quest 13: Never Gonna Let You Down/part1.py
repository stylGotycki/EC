from graph import MazeGraph, Vertex

file = open('part1.txt', 'r')
tmp = file.readlines()
file.close()

lines = [t[:-1] for t in tmp]
print(lines)

cols = len(lines[0])
rows = len(lines)

maze_info = {}

for i in range(rows):
    for j in range(cols):
        if lines[i][j] != '#':
            adjacent = []
            
            if i-1 > 0 and lines[i-1][j] != '#':
                adjacent.append((i-1,j))
                
            if j-1 > 0 and lines[i][j-1] != '#':
                adjacent.append((i,j-1))
                
            if i+1 < rows and lines[i+1][j] != '#':
                adjacent.append((i+1,j))
                
            if j+1 < cols and lines[i][j+1] != '#':
                adjacent.append((i,j+1))
            
            maze_info[(i,j,lines[i][j])] = adjacent


maze_graph = MazeGraph(maze_info)

maze_graph.find_shortest_path()
