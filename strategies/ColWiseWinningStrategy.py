from models.Board import Board
from models.Move import Move


class ColWiseWinningStrategy:
    col_maps = {}

    def __init__(self):
        pass

    def check_winner(self, board, move: Move) -> bool:
        col: int = move.cell.col
        symbol: str = move.player.symbol

        if col not in self.col_maps:
            self.col_maps[col] = {}
        col_map = self.col_maps[col]
        if symbol not in col_map:
            col_map[symbol] = 0
        col_map[symbol] += 1

        if col_map[symbol] == board.dimension:
            return True
        return False

    def handle_undo(self, board: Board, last_move: Move):
        symbol = last_move.player().symbol()
        col = last_move.cell().col()
        col_map = self.col_maps.get(col)
        col_map[symbol] = col_map.get(symbol, 0) - 1
