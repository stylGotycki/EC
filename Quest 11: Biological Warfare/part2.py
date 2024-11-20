file = open('part2.txt', 'r')

tranformations = {}

for line in file.readlines():
    index, items = line[:-1].split(':')
    
    tranformations[index] = items.split(',')

file.close()


colony = ['Z']
next_day_colony = []

days = 10

for i in range(days):
    for termit in colony:
        for item in tranformations[termit]:
            next_day_colony.append(item)
    
    print(colony)
    print(next_day_colony)        
    colony = next_day_colony
    next_day_colony = []
    

print(len(colony))