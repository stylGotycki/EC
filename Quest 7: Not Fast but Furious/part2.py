#COMPETITORS - correct
competitors = {}

file = open('part2.txt', 'r')

for line in file.readlines():
    name, sequence = line[:-1].split(":")
    
    competitor = {
        'score': 0,
        'speed': 10,
        'sequence': sequence.split(",")
    }
    
    competitors[name] = competitor       
    
file.close()



#TRACK - correct?
file = open('track2.txt', 'r')    
lines = [x[:-1] for x in file.readlines()]
file.close()

track = ''

track += lines[0][1:] 

for i in range(1, len(lines)-1):
    track += lines[i][-1]

track += lines[-1][::-1]

for i in range(len(lines)-2, 0, -1): # [n-2;0)
    track += lines[i][0]

track += 'S'



#ALGO
ROUNDS = 10
BONUSES = {
    '-': -1,
    '=': 0,
    '+': 1
}

moves = len(competitors['A']['sequence']) # assume that A-rider is always present

for _ in range(ROUNDS):
    for i in range(len(track)):
        mark = track[i]
        print(mark, end="")
        for name in competitors:
            if mark == '-' or mark == '+':
                competitors[name]['speed'] += BONUSES[mark]
                competitors[name]['score'] += competitors[name]['speed']
                
            else:         
                bonus = competitors[name]['sequence'][i % moves]
                
                competitors[name]['speed'] += BONUSES[bonus]
                competitors[name]['score'] += competitors[name]['speed']
            
    print()
        
        
for name in competitors: # get rid of useless data, does GC delete it?
    competitors[name] = competitors[name]['score']
    print(name, competitors[name])


output = ''
for w in sorted(competitors, key=competitors.get, reverse=True):
    output += w


print(output)