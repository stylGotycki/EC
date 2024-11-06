import re

file = open('part1.txt', 'r')

tmp = file.readline()
words = tmp[6:].split(',')
tmp = words[len(words)-1][:-1]
words[len(words)-1] = tmp
file.readline()
text = file.readline()

file.close()

total = 0

print(text)

for word in words:
    total += text.count(word)

print(total)