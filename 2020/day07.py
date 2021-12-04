from aocd import lines
from collections import defaultdict
import re


contains = defaultdict(list)
contained_in = defaultdict(set)
for bag_info in lines:
    color = re.match(r'(.+) bags contain', bag_info)[1]
    for count, contain_color in re.findall(r'(\d+) (.+?) bags?[,.]', bag_info):
        count = int(count)
        contained_in[contain_color].add(color)
        contains[color].append((count, contain_color))


shinygold = set()


def check(color):
    for c in contained_in[color]:
        shinygold.add(c)
        check(c)


def total_bags(color):
    total = 0
    for count, contain_color in contains[color]:
        total += count
        total += count * total_bags(contain_color)
    return total


check('shiny gold')
print(len(shinygold))
print(total_bags('shiny gold'))
