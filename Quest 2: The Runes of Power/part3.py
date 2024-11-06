file = open('part3.txt', 'r')

lines = file.readlines()

file.close()

words = lines[0][6:].split(',')
tmp = words[len(words)-1][:-1]
words[len(words)-1] = tmp

text_grid = []
for line in lines[2:]:
    text_grid.append(line.replace('\n', ''))
    
used_cells = []
for i in range(len(text_grid)):
    used_cells.append([])
    for character in line:
        used_cells[i].append(False)
        
#for line in used_cells:
 #   print(line)
    
total = 0

# vertical left to right - correct
for x in range(len(text_grid)):
    for word in words:
        for i in range(len(text_grid[x])):
            start = i
            
            j = 0                             # is that the right thing to do?
            while j < len(word) and text_grid[x][(i + j) % len(text_grid[x])] == word[j]:
                j += 1
            
            if j == len(word):
                for k in range(start, start+j):
                    used_cells[x][k % len(text_grid[x])] = True 
    
# vertical right to left
for x in range(len(text_grid)):
    for word in words:
        for i in range(len(text_grid[x]), 0, -1):
            start = i
            
            j = 0                             # is that the right thing to do?
            while j < len(word) and text_grid[x][(i - j) % len(text_grid[x])] == word[j]:
                j += 1
            
            if j == len(word):
                for k in range(start, start-j, -1):
                    used_cells[x][k % len(text_grid[x])] = True 

# horizontal top do bottom
for x in range(len(text_grid[0])):
    for word in words:
        for i in range(len(text_grid) - len(word) + 1):
            start = i
            
            j = 0
            while j < len(word) and text_grid[i+j][x] == word[j]:
                j += 1
            
            if j == len(word):
                for k in range(start, start+j):
                    used_cells[k][x] = True

# horizontal bottom to top
for x in range(len(text_grid[0])):
    for word in words:
        for i in range(len(text_grid) - 1, len(word) - 2, -1):
            start = i
            
            j = 0
            while j < len(word) and text_grid[i-j][x] == word[j]:
                j += 1
            
            if j == len(word):
                for k in range(start, start-j, -1):
                    used_cells[k][x] = True


for line in used_cells:
    for cell in line:
        if cell:
            total += 1

for line in used_cells:
    print(line)
    
print(total)

# print(1 % 7, 0 % 7, -1 % 7, -2 % 7)