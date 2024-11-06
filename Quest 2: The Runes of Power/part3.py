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
        
for line in used_cells:
    print(line)
    
total = 0

# vertical left to right
for x in range(len(text_grid)):
    for word in words:
        print(f"{x}: {word}")
        
        for i in range(len(text_grid[x])):
            start = i
            
            j = 0
            while j < len(word) and line[i+j] == word[j]:
                j += 1
            
            if j == len(word):
                print(20000000)
                for k in range(start, start+j):
                    used_cells[x][k] = True 
    
    

# vertical right to left

# horizontal top do bottom

# horizontal bottom to top



for line in used_cells:
    for cell in line:
        if cell:
            total += 1

for line in used_cells:
    print(line)
    
print(total)
