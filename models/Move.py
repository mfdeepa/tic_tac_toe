from models.Cell import Cell
from models.Player import Player


class Move:
    __cell: Cell
    __player: Player

    def __init__(self, cell: Cell, player: Player):
        self.__cell = cell
        self.__player = player

    @property
    def cell(self):
        return self.__cell

    @cell.setter
    def cell(self, cell: Cell):
        self.__cell = cell

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player: Player):
        self.__player = player
