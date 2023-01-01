from Noodle import Noodle
from Cord import Cord


class NoodleA(Noodle):
    id = 1
    all_tiles = [[Cord(0, 0), Cord(1, 0), Cord(1, 1), Cord(1, 2)], [Cord(0, 0), Cord(0, 1), Cord(1, 0), Cord(2, 0)],
                 [Cord(0, 0), Cord(0, 1), Cord(0, 2), Cord(1, 2)], [
        Cord(0, 1), Cord(1, 1), Cord(2, 1), Cord(2, 0)],
        [Cord(0, 2), Cord(1, 0), Cord(1, 1), Cord(1, 2)], [
        Cord(0, 0), Cord(0, 1), Cord(1, 1), Cord(2, 1)],
        [Cord(0, 0), Cord(0, 1), Cord(1, 1), Cord(2, 1)], [Cord(0, 0), Cord(1, 0), Cord(2, 0), Cord(2, 1)]]
