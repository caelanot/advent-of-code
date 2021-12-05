from aocd import lines
from collections import Counter
from itertools import product
import re

straight = Counter()
diagonal = Counter()
pattern = r'(\d+),(\d+) -> (\d+),(\d+)'
for line in lines:
    x1, y1, x2, y2 = map(int, re.findall(pattern, line)[0])
    if x1 == x2 or y1 == y2:
        for x, y in product(range(min(x1, x2), max(x1, x2)+1),
                            range(min(y1, y2), max(y1, y2)+1)):
            straight[x, y] += 1
    else:
        a = range(x1, x2+1) if x1 < x2 else range(x1, x2-1, -1)
        b = range(y1, y2+1) if y1 < y2 else range(y1, y2-1, -1)
        for x, y in zip(a, b):
            diagonal[x, y] += 1

print(sum(x > 1 for x in straight.values()))
print(sum(x > 1 for x in (straight + diagonal).values()))
