from aocd import lines
from copy import copy


offsets = {complex(-1, 0),
           complex(1, 0),
           complex(0, -1),
           complex(0, 1),
           complex(-1, -1),
           complex(-1, 1),
           complex(1, -1),
           complex(1, 1)
           }

board = {complex(r, c): int(col)
         for r, row in enumerate(lines)
         for c, col in enumerate(row)}


def neighbors(board, cell):
    for offset in offsets:
        c = cell + offset
        if c in board:
            yield c


def play_turn(grid):
    grid = {cell: grid[cell] + 1 for cell in grid}
    flashing = {c for c in grid if grid[c] > 9}
    flashed = set()
    while flashing:
        cell = flashing.pop()
        for c in neighbors(board, cell):
            grid[c] = grid[c] + 1
            if grid[c] > 9:
                flashing.add(c)
        flashed.add(cell)
        grid[cell] = 0
    for cell in flashed:
        grid[cell] = 0
    return len(flashed), grid


count = 0
board_copy = copy(board)
for turn in range(100):
    flashes, board_copy = play_turn(board_copy)
    count += flashes
print(count)

board_copy = copy(board)
flashes = 0
turn = 0
while flashes != 100:
    flashes, board_copy = play_turn(board_copy)
    turn += 1

print(turn)
