from abc import ABC, abstractmethod

from models.Board import Board
from models.Cell import Cell


class BotPlayingStrategy(ABC):
    @abstractmethod
    def make_move(self, board:Board) -> Cell:
        pass