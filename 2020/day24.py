import re
from collections import defaultdict
from aocd import lines


def flip(tile):
    if tile in flipped_tiles:
        flipped_tiles.remove(tile)
    else:
        flipped_tiles.add(tile)


pattern = "([ns]?[we])"
flipped_tiles = set()
for line in lines:
    x, y = 0, 0
    for dir in re.findall(pattern, line):
        if dir == "w":
            x -= 1
        elif dir == "nw":
            y -= 1
        elif dir == "ne":
            x += 1
            y -= 1
        elif dir == "e":
            x += 1
        elif dir == "se":
            y += 1
        elif dir == "sw":
            x -= 1
            y += 1
    flip((x, y))


def all_neighbors(x, y):
    return [(x-1, y),
            (x, y-1),
            (x+1, y-1),
            (x+1, y),
            (x, y+1),
            (x-1, y+1)]


def conway(turns):
    global flipped_tiles
    for _ in range(turns):
        neighbor_cells = defaultdict(int)

        for cell in flipped_tiles:
            for n in all_neighbors(*cell):
                neighbor_cells[n] += 1
        new_active = set()
        for cell, count in neighbor_cells.items():
            if cell in flipped_tiles:
                if count in (1, 2):
                    new_active.add(cell)
            elif count == 2:
                new_active.add(cell)
        flipped_tiles = new_active


print(len(flipped_tiles))
conway(100)
print(len(flipped_tiles))
