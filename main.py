#!/usr/bin/python3
from Grid import preprocess_grid, get_noodle_list, print_grid, solve

if __name__ == '__main__':
    raw_grid = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                ['A', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                ['A', 'A', 'A', 'L', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', 'L', 'L', 'L', '0', '0', '0', '0', 'K', 'K'],
                ['0', '0', '0', 'L', '0', '0', '0', '0', '0', 'K', 'K']]

    grid = preprocess_grid(raw_grid)
    noodle_list = get_noodle_list(grid)
    print(noodle_list)
    print_grid(grid)

    res = solve(noodle_list, grid)
    if res:
        print_grid(res)
    else:
        print('No solution found')
