file = open('part1.txt','r')

competitors = {}

for line in file.readlines():
    name, sequence = line[:-1].split(":")
    
    competitor = {
        'score': 0,
        'speed': 10,
        'sequence': sequence.split(",")
    }
    
    competitors[name] = competitor       
    
file.close()

ROUNDS = 10
BONUSES = {
    '-': -1,
    '=': 0,
    '+': 1
}

for i in range(ROUNDS):
    for name in competitors:
        competitor = competitors[name]

        index = i % (len(competitor['sequence']))
        bonus = competitor['sequence'][index]
        competitor['speed'] += BONUSES[bonus]        
        competitor['score'] += competitor['speed']

        
for name in competitors: # get rid of useless data, do GC deletes them?
    competitors[name] = competitors[name]['score']

output = ''
for w in sorted(competitors, key=competitors.get, reverse=True):
    output += w
    
print(output)