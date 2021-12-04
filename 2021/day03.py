from aocd import lines
from collections import Counter
import copy


def bits(numbers: list, position: int):
    count = Counter()
    for number in numbers:
        count[number[position]] += 1
    return count


lines.sort(key=str.lower)


gamma = ''.join(max(n := bits(lines, pos), key=n.get) for pos in range(12))
beta = ''.join(min(n := bits(lines, pos), key=n.get) for pos in range(12))

ox = co2 = copy.copy(lines)
for pos in range(12):
    a, b = bits(ox, pos), bits(co2, pos)
    ox = [*filter(lambda x: x[pos] == max(a, key=lambda y:(a[y], y)), ox)]
    co2 = [*filter(lambda x: x[pos] == min(b, key=lambda y:(b[y], y)), co2)]

print(f"Power = {int(gamma, 2) * int(beta, 2)}")
print(f"Life Support = {int(ox[0], 2) * int(co2[0], 2)}")
