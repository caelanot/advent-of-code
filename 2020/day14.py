from aocd import lines


def part1(array):
    # mem = defaultdict(int)
    mem = {}
    for _, line in enumerate(array):
        line = line.split(' = ')
        # Change mask
        if line[0] == "mask":
            mask = int(line[1].replace('0', '1').replace('X', '0'), 2)
            newvalue = int(line[1].replace('X', '0'), 2)
        # Change value
        else:
            value = int(line[1])
            index = int(line[0][4:-1])
            value = (value & ~mask) | (newvalue & mask)

            # Set to memory
            mem[index] = value
    return mem


def addresses(address):
    if 'X' not in address:
        yield address
    else:
        yield from addresses(address.replace('X', '0', 1))
        yield from addresses(address.replace('X', '1', 1))


def part2(array):
    mem = {}
    for _, line in enumerate(array):
        line = line.split(" = ")
        if line[0] == "mask":
            mask = line[1]
        else:
            a = f"{int(line[0][4:-1]):036b}"
            x = ''.join([x if x != "0" else a[i] for i, x in enumerate(mask)])
            for k in addresses(x):
                mem[int(k, 2)] = int(line[1])
    return mem


memory1 = part1(lines)
print(sum([memory1[key] for key in memory1]))
memory2 = part2(lines)
print(sum([memory2[key] for key in memory2]))
