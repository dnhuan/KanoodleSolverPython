from Grid import solve
from NoodleA import NoodleA

if __name__ == '__main__':
    grid = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 0, 0, 1]]
    current_noodle = NoodleA()
    solve(current_noodle, grid)
