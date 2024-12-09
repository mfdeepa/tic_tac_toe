from typing import Any

from models import BotDifficultyLevel, Board
from models.BotDifficultyLevel import BotDifficulty
from models.Cell import Cell
from models.CellState import CellState
from models.Player import Player
from models.PlayerType import PlayerType
from strategies.BotPlayingStrategy import BotPlayingStrategy


class Bot(Player):
    __difficulty_level: BotDifficultyLevel
    __BotPlayingStrategy: BotPlayingStrategy

    def __init__(self, symbol: str, name: str, id: int, playerType: PlayerType, difficultyLevel: BotDifficultyLevel):
        super().__init__(symbol, name, id, playerType)
        self.__difficulty_level = difficultyLevel
        self.__BotPlayingStrategy = BotPlayingStrategy(self.__difficulty_level)

    @property
    def difficulty_level(self):
        return self.__difficulty_level

    @difficulty_level.setter
    def difficulty_level(self, difficulty_level):
        self.__difficulty_level = difficulty_level

    @property
    def BotPlayingStrategy(self):
        return self.__BotPlayingStrategy

    @BotPlayingStrategy.setter
    def BotPlayingStrategy(self, BotPlayingStrategy):
        self.__BotPlayingStrategy = BotPlayingStrategy
        self.__BotPlayingStrategy = BotPlayingStrategy(self.__difficulty_level)

    def make_move(self, board: Board) -> Cell:
        print("bot is making the move")
        cell: Cell = board.make_move(self)
        cell.cell_state(CellState.FILLED)
        cell.player(self)
        return cell
