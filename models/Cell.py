from dataclasses import dataclass
from models.CellState import CellState


@dataclass
class Cell:
    row: int
    col: int
    _cell_state: CellState

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self._player = None
        self._cell_state = CellState.EMPTY

    def get_player(self):
        return self._player

    def set_player(self, player):
        self._player = player

    @property
    def cell_state(self):
        return self._cell_state

    @cell_state.setter
    def cell_state(self, cell_state):
        self._cell_state = cell_state

    def print_cell(self):
        if self._cell_state == CellState.FILLED:
            print(f"| {self._player.symbol} |", end="")
        else:
            print("|  - |", end="")

    def player(self, player):
        self.set_player(player)
