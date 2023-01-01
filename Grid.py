from copy import deepcopy
from NoodleA import NoodleA
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
            elif col == -1:
                print('*', end=' ')
            else:
                print(chr(ord('A') + col-1), end=' ')
        print()
    print()


def solve(noodle_list, grid, rotation=0, offset=Cord(0, 0)):
    # print(noodle_list, rotation, offset)
    # print_grid(grid)
    row, col = offset.row, offset.col

    if len(noodle_list) == 0:
        return grid

    if col >= len(grid[0]):
        col = 0
        row += 1

    if row >= len(grid):
        row = 0
        rotation += 1

    if rotation >= len(noodle_list[0].all_tiles):
        return []

    NoodleClass = noodle_list[0].__class__
    if noodle_does_fit(NoodleClass(rotation, Cord(row, col)), grid):
        # print('fit')
        new_grid = noodle_place(NoodleClass(rotation, Cord(row, col)), grid)
        # print_grid(new_grid)
        res = solve(noodle_list[1:], new_grid, 0, Cord(0, 0))
        if res:
            return res

    res = solve(noodle_list, grid, rotation, Cord(row, col+1))
    if res:
        return res
