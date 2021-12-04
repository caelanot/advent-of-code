from aocd import numbers
from collections import defaultdict

numbers.append(0)
numbers.append(max(numbers)+3)
numbers.sort()


def part1(voltages):
    diff_list = []
    for x, y in zip(voltages[0:], voltages[1:]):
        diff_list.append(y-x)
    return diff_list.count(1)*diff_list.count(3)


adapterDict = defaultdict(int)
adapterDict[0] = 1
for i in numbers[1:]:
    adapterDict[i] = adapterDict[i-1] + adapterDict[i-2] + adapterDict[i-3]


print(f'Part 1: {part1(numbers)}')
print(f'Part 2: {adapterDict[max(numbers)]}')
