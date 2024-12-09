from models.Board import Board
from models.Cell import Cell
from models.CellState import CellState
from strategies.BotPlayingStrategy import BotPlayingStrategy


class EasyBotPlayingStrategy(BotPlayingStrategy):
    # noinspection PyTypeChecker
    def make_move(self, board: Board):
        for row in board:
            for col in row:
                if CellState.EMPTY == col.CellState.value:
                    return Cell(col.x, col.y)
        return None
