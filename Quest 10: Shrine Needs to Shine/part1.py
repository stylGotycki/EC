file = open('part1.txt', 'r')

lines = []

for line in file.readlines():
    lines.append(line[:-1])
    
file.close()

width = len(lines[0]) - 4
height = len(lines) - 4

start_x, end_x = 2, width + 1 
start_y, end_y = 2, height + 1

