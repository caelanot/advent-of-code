from aocd import data

crabs = [*map(int, data.split(','))]
crabs.sort()

med = crabs[len(crabs)//2]
print(sum(abs(crab - med) for crab in crabs))

mean = sum(crabs)//len(crabs)
around = range(mean-3, mean+4)
print(min(sum((n := abs(mean - crab)) * (n+1)//2
              for crab in crabs)
          for mean in around))
