from aocd import data
data = [x.strip() for x in data.split('\n\n')]


anyone = 0
everyone = 0
for i in range(len(data)):
    anyone += len(set(data[i].replace('\n', '')))
    alls = data[i].split('\n')
    sets = set(alls[0])
    for i in range(len(alls)):
        sets = sets.intersection(set(alls[i]))
    everyone += len(sets)

print(anyone)
print(everyone)
