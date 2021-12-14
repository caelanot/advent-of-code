from aocd import lines
from collections import defaultdict

connections = defaultdict(list)

for line in lines:
    first, second = line.split('-')
    connections[first].append(second)
    connections[second].append(first)


def get_paths(current: str, end: str, nodes: list[str], part: int) -> int:
    if current.islower():
        nodes.append(current)

    if current == end:
        nodes.pop()
        return 1

    count = 0
    for neighbor in connections[current]:
        if neighbor == "start":
            continue
        if neighbor in nodes:
            if len(set(nodes)) == len(nodes) and part == 2:
                count += get_paths(neighbor, end, nodes, part)
            continue
        count += get_paths(neighbor, end, nodes, part)

    if current.islower():
        nodes.pop()
    return count


print(get_paths("start", "end", [], part=1))
print(get_paths("start", "end", [], part=2))
