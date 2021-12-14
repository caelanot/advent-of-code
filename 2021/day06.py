from aocd import data
from collections import deque

fishes = [*map(int, data.split(','))]
fishes = [fishes.count(x) for x in range(9)]


def fishy(fish, turns):
    fish = deque(fish)
    for _ in range(turns):
        n = fish.popleft()
        fish[6] += n
        fish.append(n)
    return sum(fish)


print(fishy(fishes, 80))
print(fishy(fishes, 256))
