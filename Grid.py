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
    for cord in noodle.get_tiles():
        grid[cord.row][cord.col] = noodle.id

    return grid


def solve(noodle, grid, rotation=0, offset=Cord(0, 0)):
    print(noodle, rotation, offset)
    row, col = offset.row, offset.col
    # if rotation >= len(noodle.all_tiles) or offset.row >= len(grid) or offset.col >= len(grid[0]):
    #     return True

    if col >= len(grid[0]):
        col = 0
        row += 1

    if row >= len(grid):
        row = 0
        rotation += 1

    if noodle_does_fit(NoodleA(rotation, Cord(row, col)), grid):
        print('fit')
        grid = noodle_place(NoodleA(rotation, Cord(row, col)), grid)
        print_grid(grid)
        return True

    solve(noodle, grid, rotation, Cord(row, col+1))


def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end=' ')
        print()
