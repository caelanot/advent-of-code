from aocd import lines

accumulator = 0
ip = 0


def run_instruction(instruction):
    global accumulator
    global ip
    instruction = instruction.split(' ')
    if instruction[0] == "acc":
        accumulator += int(instruction[1])
        ip += 1
    elif instruction[0] == "jmp":
        ip += int(instruction[1])
    else:
        ip += 1


def part1(code):
    instructions_visited = set()
    while ip not in instructions_visited:
        instructions_visited.add(ip)
        run_instruction(code[ip])
    return accumulator


def part2(code):
    global accumulator
    global ip
    for i in range(len(code)):
        # Change instruction if it is nop / jmp
        temp_code = list(code)
        change_instruction = temp_code[i].split(' ')
        if change_instruction[0] == "nop":
            temp_code[i] = "jmp" + change_instruction[1]
        elif change_instruction[0] == "jmp":
            temp_code[i] = "nop" + change_instruction[1]
        else:
            continue

        # Attempt to run, if it gets stuck in infinite loop quit
        accumulator = 0
        ip = 0
        instructions_visited = set()
        while ip not in instructions_visited:
            if ip not in range(len(temp_code)):
                return accumulator
            instructions_visited.add(ip)
            run_instruction(temp_code[ip])


print(part1(lines))
print(part2(lines))
