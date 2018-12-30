from enum import Enum


class State(Enum):
    OUT_OF_BOUNDS = 1
    WALL = 2
    FREE_SPACE = 3
    ENTRANCE = 4
    CARGO = 5

