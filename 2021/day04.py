from aocd import data
import numpy as np


class BingoBoard:
    def __init__(self, boardnums):
        boardnums = [x.split() for x in boardnums.split('\n')]
        self.board = np.vectorize(int)(np.array(boardnums))
        self.hits = np.zeros((5, 5))

    def hit(self, number):
        self.hits += np.where(self.board == number, 1, 0)

    def clear(self):
        self.hits = np.zeros((5, 5))

    @property
    def bingo(self):
        return any(self.hits.sum(axis=0) == 5) or any(self.hits.sum(axis=1) == 5)


def part1(numbers, boards):
    for number in numbers:
        for board in boards:
            board.hit(number)
            if board.bingo:
                return board, number


def part2(numbers, boards):
    for number in numbers:
        for board in boards:
            board.hit(number)
            if all(b.bingo for b in boards):
                return board, number


data = data.split('\n\n')
n = [*map(int, data[0].split(','))]
b = [BingoBoard(board) for board in data[1:]]


first, x = part1(n, b)
print(f"First = {first.board[first.hits != 1].sum() * x}")
for board in b:
    board.clear()
last, y = part2(n, b)
print(f"Last = {last.board[last.hits != 1].sum() * y}")
