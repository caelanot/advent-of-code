from aocd import data
from collections import defaultdict
import numpy as np


def generate_tiles(tile_input):
    tiles = {}
    for tile in tile_input.split("\n\n"):
        tile = tile.strip().splitlines()
        tile_id = int(tile[0][5:-1])
        grid = np.array([list(line) for line in tile[1:]])
        tiles[tile_id] = grid
    return tiles


def generate_borders(grid):
    top = grid[0]
    right = ''.join(line[-1] for line in grid)
    bottom = grid[-1]
    left = ''.join(line[0] for line in grid)
    return (top, right, bottom, left)


def grid_rotation(grid):
    rotations = []
    rotations.append(grid)
    rotations.append(np.rot90(grid))
    rotations.append(np.rot90(grid, 2))
    rotations.append(np.rot90(grid, 3))
    return rotations


def all_orientations(grid):
    orientations = []
    orientations.extend(grid_rotation(grid))
    grid = np.fliplr(grid)
    orientations.extend(grid_rotation(grid))
    return orientations


def generate_tiling(tiles_to_orient):
    dim = 12

    def impl(tiling, x, y, seen):
        if y == dim:
            return tiling
        next_x = x+1
        next_y = y
        if next_x == dim:
            next_x = 0
            next_y += 1

        for num, options in tiles_to_orient.items():
            if num in seen:
                continue
            seen.add(num)
            for idx, borders in options.items():
                top, _, _, left = borders
                # Tile goes to the right
                if x > 0:
                    n_num, n_orient = tiling[x-1][y]
                    _, n_right, _, _ = tiles_to_orient[n_num][n_orient]
                    if n_right != left:
                        continue
                # Tile goes below
                if y > 0:
                    n_num, n_orient = tiling[x][y-1]
                    _, _, n_bottom, _ = tiles_to_orient[n_num][n_orient]
                    if np.any(n_bottom != top):
                        continue
                tiling[x][y] = (num, idx)
                answer = impl(tiling, next_x, next_y, seen)
                if answer is not None:
                    return answer
            seen.remove(num)
        tiling[x][y] = None
        return None
    tiling = [[None] * dim for _ in range(dim)]
    return impl(tiling, 0, 0, set())


def part1(s):
    tiles = generate_tiles(s)
    tile_options = {num: all_orientations(grid)
                    for num, grid in tiles.items()}
    tiles_to_orient = defaultdict(dict)
    for num, options in tile_options.items():
        for idx, grid in enumerate(options):
            borders = generate_borders(grid)
            tiles_to_orient[num][idx] = borders
    tiling = generate_tiling(tiles_to_orient)
    answer = (
        tiling[0][0][0] *
        tiling[0][-1][0] *
        tiling[-1][0][0] *
        tiling[-1][-1][0]
        )
    return answer


def make_superimage(tile_options, tiling):
    output = []
    for row in tiling:
        grids = []
        for num, orient in row:
            grid = tile_options[num][orient]
            # Chop off borders
            grid = [line[1:-1] for line in grid[1:-1]]
            grids.append(grid)
        for y in range(len(grids[0][0])):
            out_r = []
            for idx in range(len(grids)):
                out_r.extend(grids[idx][x][y] for x in range(len(grids[idx])))
            output.append(''.join(out_r))
    return output


MONSTER_PATTERN = '''
                  #
#    ##    ##    ###
 #  #  #  #  #  #
'''


def test_for_monsters(image):
    monster_coords = []
    max_x = 0
    max_y = 0
    for dy, line in enumerate(MONSTER_PATTERN.splitlines()):
        for dx, c in enumerate(line):
            if c == '#':
                monster_coords.append((dx, dy))
                max_x = max(dx, max_x)
                max_y = max(dy, max_y)
    monster_tiles = set()
    for y in range(len(image)):
        if y+max_y >= len(image):
            break
        for x in range(len(image[y])):
            if x+max_x >= len(image[y]):
                break
            has_monster = True
            for dx, dy in monster_coords:
                if image[y+dy][x+dx] != '#':
                    has_monster = False
                    break
            if has_monster:
                for dx, dy in monster_coords:
                    monster_tiles.add((x+dx, y+dy))
    if len(monster_tiles) == 0:
        return None
    all_pounds = set()
    for y, row in enumerate(image):
        for x, c in enumerate(row):
            if c == '#':
                all_pounds.add((x, y))
    return len(all_pounds - monster_tiles)


def part2(s):
    tiles = generate_tiles(s)
    tile_options = {num: all_orientations(grid)
                    for num, grid in tiles.items()}
    tiles_to_orient = defaultdict(dict)
    for num, options in tile_options.items():
        for idx, grid in enumerate(options):
            borders = generate_borders(grid)
            tiles_to_orient[num][idx] = borders
    tiling = generate_tiling(tiles_to_orient)

    image = make_superimage(tile_options, tiling)

    image_opts = all_orientations([list(line) for line in image])

    for opt in image_opts:
        answer = test_for_monsters(opt)
        if answer is not None:
            break

    return answer


print(part1(data))
print(part2(data))
