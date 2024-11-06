file = open('part2.txt', 'r')

lines = file.readlines()

file.close()

words = lines[0][6:].split(',')
tmp = words[len(words)-1][:-1]
words[len(words)-1] = tmp

text = []
for line in lines[2:]:
    text.append(line.replace('\n', ''))

total = 0

for line in text:
    line_cost = 0
    used = [False] * len(line)
    normal_words = 0
    reversed_words = 0
       
    for word in words:
        for i in range(len(line) - len(word) + 1):
            start = i
            
            j = 0
            while j < len(word) and line[i+j] == word[j]:
                j += 1
            
            if j == len(word):
                for k in range(start, start+j):
                    used[k] = True
    
    
    for word in words:
        for i in range(len(line) - 1, len(word) - 2, -1):
            start = i
            
            j = 0
            while j < len(word) and line[i-j] == word[j]:
                j += 1
            
            if j == len(word):
                for k in range(start, start - j, -1):
                    used[k] = True
    
    
    for use in used:
        if use:
            total += 1
            line_cost += 1
    print(line_cost)

print(total)