from aocd import lines
from collections import defaultdict
from itertools import product


def conway(dimension):
    active_cubes = {(x, y) + (0,) * (dimension - 2)
                    for y, line in enumerate(lines)
                    for x, cell in enumerate(line)
                    if cell == "#"}

    for _ in range(6):
        neighbor_cubes = defaultdict(int)
        for cube in active_cubes:
            for offset in product([-1, 0, 1], repeat=dimension):
                if not any(offset):
                    continue
                neighbor = zip(cube, offset)
                neighbor_cubes[tuple(pos + d for pos, d in neighbor)] += 1
        new_active = set()
        for cube, count in neighbor_cubes.items():
            if cube in active_cubes:
                if count in (2, 3):
                    new_active.add(cube)
            elif count == 3:
                new_active.add(cube)
        active_cubes = new_active
    return len(active_cubes)


print(conway(3))
print(conway(4))
