from typing import List

from models.Cell import Cell


class Board:
    from models.Cell import Cell
    __dimension: int
    __board: List[List[Cell]]

    def __init__(self, dimension: int):
        self.__dimension = dimension
        self.__board = [[Cell(i,j) for j in range(dimension)] for i in range(dimension)]

    def print_board(self):
        for row in self.__board:
            for cell in row:
                cell.print_cell()
            print()

    @property
    def dimension(self):
        return self.__dimension

    @dimension.setter
    def dimension(self, dimension):
        self.__dimension = dimension

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, board):
        self.__board = board

    def __getitem__(self, index):
        # Allow access to board using board[row]
        return self.__board[index]