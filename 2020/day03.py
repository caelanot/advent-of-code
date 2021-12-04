from aocd import lines


def count_trees(trees: list[int], x_change: int, y_change: int) -> int:
    width = len(trees[0])
    treesFound = 0
    xpos = 0
    height = 0
    while height < len(trees):
        if trees[height][xpos % width] == "#":
            treesFound += 1
        xpos += x_change
        height += y_change
    return treesFound


print(count_trees(lines, 3, 1))
print(count_trees(lines, 1, 1)
      * count_trees(lines, 3, 1)
      * count_trees(lines, 5, 1)
      * count_trees(lines, 7, 1)
      * count_trees(lines, 1, 2))
