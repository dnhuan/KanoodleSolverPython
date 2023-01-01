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

    def __repr__(self):
        return f"{chr(ord('A') + (self.id - 1))}"
        # R: {self.rotation} | O: {self.offset} |
