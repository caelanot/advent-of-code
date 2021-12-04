from aocd import numbers
from itertools import combinations
from math import prod


def summer(arr, nums):
    for x in combinations(arr, nums):
        if sum(x) == 2020:
            return prod(x)


print(summer(numbers, 2))
print(summer(numbers, 3))
