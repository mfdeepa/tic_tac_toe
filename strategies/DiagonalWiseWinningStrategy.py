from models.Board import Board
from models.Move import Move
from strategies.WinningStrategy import WinningStrategy


class DiagonalWiseWinningStrategy(WinningStrategy):
    def __init__(self):
        self.left_dia = {}
        self.right_dia = {}

    def check_winner(self, board: Board, move: Move):
        row: int = move.cell.row
        col: int = move.cell.col

        symbol: str = move.player.symbol

        if row == col:
            if symbol not in self.left_dia:
                self.left_dia[symbol] = 0
            self.left_dia[symbol] += 1
            if self.left_dia[symbol] == board.dimension:
                return True

        if row + col == board.dimension - 1:
            if symbol not in self.right_dia:
                self.right_dia[symbol] = 0
            self.right_dia[symbol] += 1
            if self.right_dia[symbol] == board.dimension:
                return True

            return False

    def handle_undo(self, board: Board, move: Move):
        symbol: str = move.player().symbol()
        row: int = move.cell().row()
        col: int = move.cell().col()
        if row == col:
            self.left_dia[symbol] = self.left_dia[symbol] - 1

        if row + col == board.dimension() - 1:
            self.right_dia[symbol] = self.right_dia.get(symbol, 0) - 1
