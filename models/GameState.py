from enum import Enum


class GameState(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    DRAW = "DRAW"
    SUCCESS = "SUCCESS"
    PAUSE = "PAUSE"
    CONCLUDED = "CONCLUDED"
