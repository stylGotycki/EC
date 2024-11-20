file = open('part3.txt', 'r')

tranformations = {}

for line in file.readlines():
    index, items = line[:-1].split(':')
    
    tranformations[index] = items.split(',')

file.close()

colonies_rank = {}
next_day_colony = []

days = 20

for key in tranformations:
    colony = [key]
    print(key)
    for i in range(days):
        for termit in colony:
            for item in tranformations[termit]:
                next_day_colony.append(item)
        
        colony = next_day_colony
        next_day_colony = []
        if (len(colony) == 1000):
            print('AAALLL')
    
    colonies_rank[key] = len(colony)    

print(colonies_rank)
print(max(colonies_rank) - min(colonies_rank)) 