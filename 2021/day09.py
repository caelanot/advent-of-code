from aocd import lines


offsets = {complex(-1, 0),
           complex(1, 0),
           complex(0, -1),
           complex(0, 1),
           }

grid = {complex(r, c): int(col)
        for r, row in enumerate(lines)
        for c, col in enumerate(row)}


def neighbors(cell):
    for offset in offsets:
        c = cell + offset
        if c in grid:
            yield c


def is_low(cell):
    for c in neighbors(cell):
        if grid[cell] >= grid[c]:
            return False
    return True


sizes = []
for cell in (c for c in grid if is_low(c)):
    visited = set()
    candidates = {cell}

    while candidates:
        n = candidates.pop()
        candidates.update({x for x in neighbors(n)
                           if x not in visited
                           and grid[x] < 9})
        visited.add(n)
    sizes.append(len(visited))

print(sum(1 + grid[cell] for cell in grid if is_low(cell)))
sizes.sort(reverse=True)
print(sizes[0] * sizes[1] * sizes[2])
