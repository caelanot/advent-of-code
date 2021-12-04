input = "963275481"


def play(original, number, rounds):
    input_size = len(original)
    cups = dict()
    cur = first = original[0]

    for val in original[1:]:
        cups[cur] = cur = val

    for idx in range(input_size+1, number+1):
        cups[cur] = cur = idx
    cups[cur] = cur = first

    for _ in range(rounds):
        removed = (a := cups[cur], b := cups[a], c := cups[b])

        dest = cur
        while dest in removed or dest == cur:
            dest = dest - 1 if dest > 1 else number

        cups[cur], cups[c], cups[dest] = cups[c], cups[dest], a

        cur = cups[cur]

    return cups


final = play([*map(int, input)], 9, 100)
string = ""
cup = final[1]
while cup != 1:
    string += str(cup)
    cup = final[cup]
print(f'Part 1: {string}')

final = play([*map(int, input)], 1000000, 10000000)
print(f'Part 2: {final[1] * final[final[1]]}')
