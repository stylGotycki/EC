file = open("part3.txt", 'r')

tmp = file.readlines()

file.close()

lines = []

for t in tmp:
    lines.append(t[:-1])

FRUIT = '@'
class Node:
    def __init__(self):
        self.depth = 0
        self.con_to = []
        self.parent = ''
    
    def __str__(self):
        return f"{self.parent=} {self.depth=} {self.con_to=}"

    def __repr__(self):
        return f"{self.parent=} {self.depth=} {self.con_to=}"

tree = {}


for line in lines:
    node_index, tmp = line.split(':') # pattern A:B,C
    con_to = tmp.split(",")
    
    if node_index not in tree.keys():
        tree[node_index] = Node()

    for con in con_to:            
        if con != FRUIT and con not in tree.keys():
            tree[con] = Node()
        if con != FRUIT:
            tree[con].parent = node_index
        tree[node_index].con_to.append(con)
        

print(tree)


visited = []
to_visit = ['RR']

counter = 0

while len(to_visit) != 0:
    current = to_visit.pop()
    depth = tree[current].depth
    
    if current in visited:
        continue
    
    if current == FRUIT:
        continue
    
    visited.append(current)
    
    for con in tree[current].con_to:
        if con != FRUIT:
            to_visit.append(con)
            tree[con].depth = depth+1

    counter += 1
    
print(counter)


to_delete = []
for node in tree:
    if node == 'RR':
        continue
    
    if tree[node].depth == 0:
        to_delete.append(node)

for x in to_delete:
    del tree[x]


layers = {}

for node in tree:
    depth = tree[node].depth

    if depth not in layers.keys():
        layers[depth] = []    

    layers[depth].append(node)

    for con in tree[node].con_to:
        if con == FRUIT:
            if depth+1 not in layers.keys():
                layers[depth+1] = []
            layers[depth+1].append(FRUIT)


where = 0

for i in layers.keys():
    if layers[i].count(FRUIT) == 1:
        where = i-1 # points to the last non-fruit node
        break

start = ''
for node in layers[where]:
    if node == FRUIT:
        continue
    if FRUIT in tree[node].con_to:
        start = node
        break
    
print(start)

output = f"@"

current = start
while current != '':
    output += current[0]
    current = tree[current].parent
    
print(output[::-1])