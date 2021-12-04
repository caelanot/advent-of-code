from collections import defaultdict


def solver(timer):
    spoken_numbers = defaultdict(lambda: turn)

    for turn, number in enumerate(arr):
        spoken_numbers[number] = turn
        last_number = number

    for turn in range(turn, timer - 1):
        next_number = turn - spoken_numbers[last_number]
        spoken_numbers[last_number] = turn
        last_number = next_number
    return last_number


arr = [15, 5, 1, 4, 7, 0]
print(solver(2020))
print(solver(30000000))
