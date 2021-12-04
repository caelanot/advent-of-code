from aocd import lines as seating
from copy import deepcopy

EMPTY = "L"
TAKEN = "#"
FLOOR = "."

seating = [list(x) for x in seating]
board = []

width = len(seating[0])
height = len(seating)


def check_seat(x, y, dx, dy, part):
    if x < 0 or x >= width or y < 0 or y >= height:
        return None
    if part == 2:
        while board[y][x] == FLOOR:
            x, y = x + dx, y + dy
            if x < 0 or x >= width or y < 0 or y >= height:
                return None
    return board[y][x]


def playTurns(part, count):
    seatingCopy = deepcopy(seating)
    global board
    while seatingCopy != board:
        board, seatingCopy = seatingCopy, [row[:] for row in seatingCopy]
        for y in range(height):
            for x in range(width):
                cnt = sum(TAKEN == check_seat(x + dx, y + dy, dx, dy, part)
                          for dx in [-1, 0, 1] for dy in [-1, 0, 1]
                          if (dx, dy) != (0, 0))
                if board[y][x] == EMPTY and cnt == 0:
                    seatingCopy[y][x] = TAKEN
                if board[y][x] == TAKEN and cnt >= count:
                    seatingCopy[y][x] = EMPTY
    return sum(row.count(TAKEN) for row in seatingCopy)


print(playTurns(1, 4))
print(playTurns(2, 5))
