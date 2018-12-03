from enum import Enum


class State(Enum):
    OUT_OF_BOUNDS = 1
    FREE_SPACE = 2
    ENTRANCE = 3
    CARGO_ARE = 4

