# not the proudest code
file = open("part3.txt")

tmp = file.readlines()

file.close()

LEFT = 0
RIGHT = 1


tmpp = []

for i in range(len(tmp)):
    nums = tmp[i][:-1].split(" ")
    tmpp.append([])
    for num in nums:
        tmpp[i].append(int(num))
    
    
knights = [[tmpp[j][i] for j in range(len(tmpp))] for i in range(len(tmpp[0]))]

print(knights)


occurences = {}

final_shout = 0
i = 0
dancing = True

file = open("part2t.txt", 'w')

while dancing:
    c_index = i % len(knights)
    n_index = (i+1) % len(knights)
    n_column_len = len(knights[n_index])
    
    #print(knights)
    
    knight = knights[c_index][0]
    del knights[c_index][0]
    
    side = ((knight-1) // n_column_len) % 2 # left = 0, right = 1
    
    #print(knights)
    
    new_pos = (knight-1) % n_column_len
    
    if side == LEFT:
        #print("L: ", end="")
        
        knights[n_index].insert(new_pos, knight)
    
    else:
        #print("R: ", end="")
        
        new_pos = (n_column_len) - new_pos
        knights[n_index].insert(new_pos, knight)
    
    
    shout = ''
    for line in knights:
        shout += str(line[0])

    if shout not in occurences.keys():
        occurences[shout] = 0
    occurences[shout] += 1
    
    test = occurences[shout]

    occ = occurences[shout]
        
    if occ == 5:
        final_shout = shout
        dancing = False
    
    file.write(f"{i+1}: {shout} {test}" + '\n')
    # print(f"{i+1}: {shout} {test}")
        
    i += 1
    
file.close()

nums = []

for key in occurences.keys():
    nums.append(int(key))
    
print(max(nums))