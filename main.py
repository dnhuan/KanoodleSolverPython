#!python3

from Grid import solve, print_grid
from NoodleA import NoodleA
from NoodleK import NoodleK

if __name__ == '__main__':
    raw_grid = [['E', 'E', 'G', 'G', 'G', 'J', 'A', 'A', 'A', 'A', 'A'],
                ['A', 'E', 'E', 'E', 'G', 'A', 'A', 'A', 'A', 'A', 'A'],
                ['A', 'A', 'A', 'A', 'G', 'A', 'A', 'A', 'A', 'A', 'A'],
                ['B', 'B', 'A', 'A', 'A', 'A', 'F', 'A', 'A', 'A', 'A'],
                ['B', 'B', 'B', 'A', 'A', 'A', 'F', 'F', 'A', 'A', 'A']]

    grid = [[0] * 11 for _ in range(5)]
    for row in range(len(raw_grid)):
        for col in range(len(raw_grid[0])):
            grid[row][col] = ord(raw_grid[row][col]) - ord('A') + 1
    print_grid(grid)
    noodle_list = [NoodleA(), NoodleK()]
    res = solve(noodle_list, grid)
    if res:
        print_grid(res)
