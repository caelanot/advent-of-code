from aocd import lines
import networkx as nx
import numpy as np


def neighbors(x, y, m, n):
    neighbor = {
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1)
    }
    for cell in neighbor:
        if 0 <= cell[0] < m and 0 <= cell[1] < n:
            yield cell


def create_graph(grid: np.ndarray):
    m, n = grid.shape
    G = nx.grid_2d_graph(m, n, create_using=nx.DiGraph)
    for x in range(m):
        for y in range(n):
            for neighbor in neighbors(x, y, m, n):
                G.add_edge((x, y), neighbor, weight=grid[neighbor])
    return G


def part1():
    G = create_graph(grid)
    return nx.dijkstra_path_length(G, (0, 0), (99, 99))


def part2():
    big_grid = np.block(
        [[(grid + i + j - 1) % 9 + 1
          for j in range(5)]
         for i in range(5)]
    )
    G = create_graph(big_grid)
    return nx.dijkstra_path_length(G, (0, 0), (499, 499))


grid = np.array([[int(x) for x in row] for row in lines])

print(part1())
print(part2())
