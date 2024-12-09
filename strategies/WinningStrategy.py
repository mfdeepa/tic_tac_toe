from models.Board import Board
from models.Move import Move
from abc import ABC, abstractmethod


class WinningStrategy(ABC):

    @abstractmethod
    def check_winner(self, board: Board, move: Move) -> bool:
        pass

    @abstractmethod
    def handle_undo(self, board: Board, move: Move):
        pass
