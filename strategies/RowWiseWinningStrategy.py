from abc import ABC

from models.Move import Move
from strategies.WinningStrategy import WinningStrategy


class RowWiseWinningStrategy(WinningStrategy, ABC):
    def __init__(self):
        self.row_maps = {}

    def check_winner(self, board, move:Move):
        row: int = move.cell.row
        symbol: str = move.player.symbol

        if row not in self.row_maps:
            self.row_maps[row] = {}

        row_map = self.row_maps[row]
        if symbol not in row_map:
            row_map[symbol] = 0
        row_map[symbol] += 1
        if row_map[symbol] == board.dimension:
            return True
        return False

    def handle_undo(self, board, move: Move):
        row: int = move.cell.row
        symbol: str = move.player.symbol
        row_map = self.row_maps[row]
        row_map[symbol] -= 1

