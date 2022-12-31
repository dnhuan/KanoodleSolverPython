from dataclasses import dataclass
from abc import ABC, abstractmethod
from Cord import Cord


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

    def rotateCW(self):
        self.rotation = (self.rotation + 1) % len(self.all_tiles)

    def rotateCCW(self):
        self.rotation = (self.rotation - 1) % len(self.all_tiles)

    def move(self, row, col):
        self.offset.row += row
        self.offset.col += col

    def reset(self):
        self.offset.row = 0
        self.offset.col = 0
        self.rotation = 0

    def __repr__(self):
        return f"R: {self.rotation} | {list(self.get_tiles())}"
