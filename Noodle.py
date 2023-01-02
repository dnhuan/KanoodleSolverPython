from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Cord:
    row: int
    col: int


@dataclass
class Noodle(ABC):
    def __init__(self, rotation=0, offset=Cord(0, 0)):
        self.offset = offset
        self.rotation = rotation

    @property
    @abstractmethod
    def all_tiles(self):
        pass

    @property
    @abstractmethod
    def id(self):
        pass

    def get_tiles(self):
        for cord in self.all_tiles[self.rotation]:
            yield Cord(cord.row + self.offset.row, cord.col + self.offset.col)

    def get_space(self):
        return len(self.all_tiles[0])

    def __repr__(self):
        return f"{chr(ord('A') + (self.id - 1))}"
        # R: {self.rotation} | O: {self.offset} |


class NoodleA(Noodle):
    id = 1
    all_tiles = [[Cord(0, 0), Cord(1, 0), Cord(1, 1), Cord(1, 2)],
                 [Cord(0, 1), Cord(1, 1), Cord(2, 1), Cord(0, 2)],
                 [Cord(1, 0), Cord(1, 1), Cord(1, 2), Cord(2, 2)],
                 [Cord(2, 0), Cord(2, 1), Cord(1, 1), Cord(0, 1)],
                 [Cord(1, 0), Cord(1, 1), Cord(1, 2), Cord(0, 2)],
                 [Cord(0, 0), Cord(0, 1), Cord(1, 1), Cord(2, 1)],
                 [Cord(1, 0), Cord(1, 1), Cord(1, 2), Cord(2, 0)],
                 [Cord(0, 1), Cord(1, 1), Cord(2, 1), Cord(2, 2)]]


class NoodleB(Noodle):
    id = 2
    all_tiles = [[Cord(0, 1), Cord(1, 1), Cord(2, 1), Cord(1, 0), Cord(2, 0)],
                 [Cord(0, 0), Cord(0, 1), Cord(1, 0), Cord(1, 1), Cord(1, 2)],
                 [Cord(0, 1), Cord(0, 2), Cord(1, 1), Cord(1, 2), Cord(2, 1)],
                 [Cord(1, 0), Cord(1, 1), Cord(1, 2), Cord(2, 1), Cord(2, 2)],
                 [Cord(0, 1), Cord(1, 1), Cord(1, 2), Cord(2, 1), Cord(2, 2)],
                 [Cord(0, 1), Cord(0, 2), Cord(1, 0), Cord(1, 1), Cord(1, 2)],
                 [Cord(0, 0), Cord(0, 1), Cord(1, 0), Cord(1, 1), Cord(2, 1)],
                 [Cord(1, 0), Cord(1, 1), Cord(1, 2), Cord(2, 0), Cord(2, 1)]]


class NoodleC(Noodle):
    id = 3
    all_tiles = [[Cord(0, 2), Cord(1, 2), Cord(2, 2), Cord(3, 1), Cord(3, 2)],
                 [Cord(1, 0), Cord(2, 0), Cord(2, 1), Cord(2, 2), Cord(2, 3)],
                 [Cord(0, 1), Cord(0, 2), Cord(1, 1), Cord(2, 1), Cord(3, 1)],
                 [Cord(1, 0), Cord(1, 1), Cord(1, 2), Cord(1, 3), Cord(2, 3)],
                 [Cord(0, 1), Cord(1, 1), Cord(2, 1), Cord(3, 1), Cord(3, 2)],
                 [Cord(1, 3), Cord(2, 0), Cord(2, 1), Cord(2, 2), Cord(2, 3)],
                 [Cord(0, 1), Cord(0, 2), Cord(1, 2), Cord(2, 2), Cord(3, 2)],
                 [Cord(1, 0), Cord(1, 1), Cord(1, 2), Cord(1, 3), Cord(2, 0)]]


class NoodleD(Noodle):
    id = 4
    all_tiles = [[Cord(0, 2), Cord(1, 2), Cord(2, 1), Cord(2, 2), Cord(3, 2)],
                 [Cord(1, 1), Cord(2, 0), Cord(2, 1), Cord(2, 2), Cord(2, 3)],
                 [Cord(0, 1), Cord(1, 1), Cord(1, 2), Cord(2, 1), Cord(3, 1)],
                 [Cord(1, 0), Cord(1, 1), Cord(1, 2), Cord(1, 3), Cord(2, 2)],
                 [Cord(0, 1), Cord(1, 1), Cord(2, 1), Cord(2, 2), Cord(3, 1)],
                 [Cord(1, 2), Cord(2, 0), Cord(2, 1), Cord(2, 2), Cord(2, 3)],
                 [Cord(0, 2), Cord(1, 1), Cord(1, 2), Cord(2, 2), Cord(3, 2)],
                 [Cord(1, 0), Cord(1, 1), Cord(1, 2), Cord(1, 3), Cord(2, 1)]]


class NoodleE(Noodle):
    id = 5
    all_tiles = [[Cord(0, 2), Cord(1, 2), Cord(2, 1), Cord(2, 2), Cord(3, 1)],
                 [Cord(1, 0), Cord(1, 1), Cord(2, 1), Cord(2, 2), Cord(2, 3)],
                 [Cord(0, 2), Cord(1, 1), Cord(1, 2), Cord(2, 1), Cord(3, 1)],
                 [Cord(1, 0), Cord(1, 1), Cord(1, 2), Cord(2, 2), Cord(2, 3)],
                 [Cord(0, 1), Cord(1, 1), Cord(2, 1), Cord(2, 2), Cord(3, 2)],
                 [Cord(1, 2), Cord(1, 3), Cord(2, 0), Cord(2, 1), Cord(2, 2)],
                 [Cord(0, 1), Cord(1, 1), Cord(1, 2), Cord(2, 2), Cord(3, 2)],
                 [Cord(1, 1), Cord(1, 2), Cord(1, 3), Cord(2, 0), Cord(2, 1)]]


class NoodleF(Noodle):
    id = 6
    all_tiles = [[Cord(0, 1), Cord(1, 0), Cord(1, 1)],
                 [Cord(0, 0), Cord(0, 1), Cord(1, 1)],
                 [Cord(0, 0), Cord(1, 0), Cord(1, 1)],
                 [Cord(0, 0), Cord(0, 1), Cord(1, 0)]]


class NoodleG(Noodle):
    id = 7
    all_tiles = [[Cord(0, 2), Cord(1, 2), Cord(2, 0), Cord(2, 1), Cord(2, 2)],
                 [Cord(0, 0), Cord(0, 1), Cord(0, 2), Cord(1, 0), Cord(2, 0)],
                 [Cord(0, 0), Cord(1, 0), Cord(2, 0), Cord(2, 1), Cord(2, 2)],
                 [Cord(0, 0), Cord(0, 1), Cord(0, 2), Cord(1, 2), Cord(2, 2)]]


class NoodleH(Noodle):
    id = 8
    all_tiles = [[Cord(0, 2), Cord(1, 1), Cord(1, 2), Cord(2, 0), Cord(2, 1)],
                 [Cord(0, 1), Cord(0, 2), Cord(1, 0), Cord(1, 1), Cord(2, 0)],
                 [Cord(0, 0), Cord(1, 0), Cord(1, 1), Cord(2, 1), Cord(2, 2)],
                 [Cord(0, 0), Cord(0, 1), Cord(1, 1), Cord(1, 2), Cord(2, 2)]]


class NoodleI(Noodle):
    id = 9
    all_tiles = [[Cord(0, 0), Cord(0, 2), Cord(1, 0), Cord(1, 1), Cord(1, 2)],
                 [Cord(0, 1), Cord(0, 2), Cord(1, 1), Cord(2, 1), Cord(2, 2)],
                 [Cord(1, 0), Cord(1, 1), Cord(1, 2), Cord(2, 0), Cord(2, 2)],
                 [Cord(0, 0), Cord(0, 1), Cord(1, 1), Cord(2, 0), Cord(2, 1)]]


class NoodleJ(Noodle):
    id = 10
    all_tiles = [[Cord(0, 1), Cord(1, 1), Cord(2, 1), Cord(3, 1)],
                 [Cord(1, 0), Cord(1, 1), Cord(1, 2), Cord(1, 3)]]


class NoodleK(Noodle):
    id = 11
    all_tiles = [[Cord(0, 0), Cord(1, 0), Cord(0, 1), Cord(1, 1)]]


class NoodleL(Noodle):
    id = 12
    all_tiles = [[Cord(0, 1), Cord(1, 0), Cord(1, 1), Cord(1, 2), Cord(2, 1)]]
