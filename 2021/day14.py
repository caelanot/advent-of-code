from aocd import data
from collections import Counter
import re

template, insertions = data.split('\n\n')
insertions = insertions.splitlines()
rules = {}
for insertion in insertions:
    pair, element = re.findall(r'(\w+) -> (\w)', insertion)[0]
    rules[pair] = element


def polymer(turns):
    pairs = Counter(a+b for a, b in zip(template, template[1:]))
    for _ in range(turns):
        new_pairs = Counter()
        for pair, count in pairs.items():
            a, b = list(pair)
            new = rules[a+b]
            new_pairs[a+new] += count
            new_pairs[new+b] += count
        pairs = new_pairs

    elements = Counter()
    for k, v in pairs.items():
        elements[k[0]] += v
    elements[template[-1]] += 1

    return elements.most_common()[0][1] - elements.most_common()[-1][1]


print(polymer(10))
print(polymer(40))
