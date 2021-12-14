from aocd import data
import imager
import numpy as np
import re

palette = {
    0: (0, 0, 0),
    1: (255, 255, 255),
}

dots, folds = data.split('\n\n')
dots = dots.splitlines()
folds = folds.splitlines()

paper = set()
for dot in dots:
    x, y = dot.split(',')
    x, y = int(x), int(y)
    paper.add((x, y))

for fold in folds:
    axis, line = re.findall(r'fold along ([xy])=(\d+)', fold)[0]
    line = int(line)
    match axis:
        case "x":
            paper = {dot if dot[0] < line
                     else (2*line - dot[0], dot[1])
                     for dot in paper}
        case "y":
            paper = {dot if dot[1] < line
                     else (dot[0], 2*line - dot[1])
                     for dot in paper}

max_x = max(paper, key=lambda x: x[0])[0]
max_y = max(paper, key=lambda y: y[1])[1]

grid = np.zeros((max_y+1, max_x+1))
for dot in paper:
    grid[dot[1], dot[0]] = 1

imager.make_image(grid, palette, name="code", resize=20)
