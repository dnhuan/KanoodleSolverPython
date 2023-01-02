from copy import deepcopy
from Noodle import *
from Cord import Cord


def noodle_move(noodle, row, col):
    return NoodleA(noodle.rotation, Cord(noodle.offset.row + row, noodle.offset.col + col))


def noodle_rotate(noodle, direction):
    if direction == 'cw':
        return NoodleA((noodle.rotation + 1) % len(noodle.all_tiles), Cord(noodle.offset.row, noodle.offset.col))
    else:
        return NoodleA((noodle.rotation - 1) % len(noodle.all_tiles), Cord(noodle.offset.row, noodle.offset.col))


def noodle_does_fit(noodle, grid):
    for cord in noodle.get_tiles():
        if cord.row < 0 or cord.row >= len(grid) or cord.col < 0 or cord.col >= len(grid[0]):
            return False

        if grid[cord.row][cord.col] != 0:
            return False

    return True


def noodle_place(noodle, grid):
    new_grid = deepcopy(grid)
    for cord in noodle.get_tiles():
        new_grid[cord.row][cord.col] = noodle.id

    return new_grid


def print_grid(grid):
    for row in grid:
        for col in row:
            if col == 0:
                print('_', end=' ')
            else:
                print(chr(ord('A') + col-1), end=' ')
        print()
    print()


def preprocess_grid(raw_grid):
    grid = [[0] * 11 for _ in range(5)]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if raw_grid[row][col] == '0':
                grid[row][col] = 0
            else:
                grid[row][col] = ord(raw_grid[row][col]) - ord('A') + 1
    return grid


def get_noodle_list(grid):
    noodle_dict = {
        1: NoodleA(),
        2: NoodleB(),
        3: NoodleC(),
        4: NoodleD(),
        5: NoodleE(),
        6: NoodleF(),
        7: NoodleG(),
        8: NoodleH(),
        9: NoodleI(),
        10: NoodleJ(),
        11: NoodleK(),
        12: NoodleL(),
    }

    noodle_list = []
    flattened_grid = [item for sublist in grid for item in sublist]
    for k in noodle_dict:
        if k not in flattened_grid:
            noodle_list.append(noodle_dict[k])

    return noodle_list


def dfs(y, x, grid):
    count = 1
    grid[y][x] = -1

    if y > 0 and grid[y-1][x] == 0:
        count += dfs(y-1, x, grid)

    if y < len(grid)-1 and grid[y+1][x] == 0:
        count += dfs(y+1, x, grid)

    if x > 0 and grid[y][x-1] == 0:
        count += dfs(y, x-1, grid)

    if x < len(grid[0])-1 and grid[y][x+1] == 0:
        count += dfs(y, x+1, grid)

    return count


def space_left(original_grid, noodle_list) -> bool:
    print(noodle_list)
    grid = deepcopy(original_grid)
    space_left_list = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                count = dfs(row, col, grid)
                if count <= 2:
                    return False
                space_left_list.append(count)

    print(space_left_list)

    # space_noodle_list = []
    # for noodle in noodle_list:
    #     space_noodle_list.append(noodle.get_space())

    # return sorted(space_noodle_list) == sorted(space_left_list)  # 34s
    return True


def solve(noodle_list, grid, rotation=0, offset=Cord(-1, -1)):
    # print(noodle_list, rotation, offset)
    # print_grid(grid)
    row, col = offset.row, offset.col

    if len(noodle_list) == 0:
        # print('solved')
        return grid

    if col >= len(grid[0]):
        col = -1
        row += 1

    if row >= len(grid):
        row = -1
        rotation += 1

    if rotation >= len(noodle_list[0].all_tiles):
        return []

    NoodleClass = noodle_list[0].__class__
    if noodle_does_fit(NoodleClass(rotation, Cord(row, col)), grid):
        # print('fit')
        new_grid = noodle_place(NoodleClass(rotation, Cord(row, col)), grid)
        new_noodle_list = noodle_list[1:]
        if space_left(new_grid, new_noodle_list):

            # print(noodle_list)
            # print_grid(new_grid)

            res = solve(new_noodle_list, new_grid)
            if res:
                return res

    res = solve(noodle_list, grid, rotation, Cord(row, col+1))
    if res:
        return res
