from dataclasses import dataclass
from typing import List, Optional

from exceptions.DuplicateSymbolForPlayer import DuplicateSymbolForPlayer
from exceptions.MoreThanOneBotException import MoreThanOneBotException
from exceptions.PlayersAndBoardCountMismatch import PlayersAndBoardCountMismatch
from models.Board import Board
from models.Cell import Cell
from models.CellState import CellState
from models.GameState import GameState
from models.Move import Move
from models.Player import Player
from models.PlayerType import PlayerType
from strategies import WinningStrategy


@dataclass
class Game:
    __player: List[Player]
    __winner: Optional[Player]
    __board: Board
    __winning_strategy: List[WinningStrategy]
    __game_state: GameState
    __next_player_index: int
    __moves: List[Move]

    def __init__(self, players: List[Player], dimension: int, winning_strategies: List[WinningStrategy]):
        # self.__next_player = None
        self.__players = players
        self.__winning_strategies = winning_strategies
        self.__board = Board(dimension)
        self.__moves = []
        self.__next_player_index = 0
        self.__winner: Optional[
            'Player'] = None  # if winner is not define then it would be None else it would be Player
        self.__game_state = GameState.IN_PROGRESS  #if we want to access the name of enum then we will write name else write .value .

    @property
    def players(self) -> List[Player]:
        return self.__players

    @players.setter
    def players(self, players: List[Player]):
        self.__players = players

    @property
    def board(self) -> Board:
        return self.__board

    @board.setter
    def board(self, board: Board):
        self.__board = board

    @property
    def winning_strategies(self) -> List[WinningStrategy]:
        return self.__winning_strategies

    @winning_strategies.setter
    def winning_strategies(self, strategies: List[WinningStrategy]):
        self.__winning_strategies = strategies

    @property
    def game_state(self) -> GameState:
        return self.__game_state

    @game_state.setter
    def game_state(self, game_state: GameState):
        self.__game_state = game_state

    @property
    def moves(self) -> List[Move]:
        return self.__moves

    @moves.setter
    def moves(self, moves: List[Move]):
        self.__moves = moves

    @property
    def next_player_index(self) -> int:
        return self.__next_player_index

    @next_player_index.setter
    def next_player_index(self, next_player_index: int):
        self.__next_player_index = next_player_index

    @property
    def winner(self) -> Optional[Player]:
        return self.__winner

    @winner.setter
    def winner(self, winner: Player):
        self.__winner = winner

    @property
    def game_state(self) -> GameState:
        return self.__game_state

    @game_state.setter
    def game_state(self, gameStatus: GameState):
        self.__game_state = gameStatus

    @staticmethod
    def get_builder():
        return Builder()

    def print_board(self):
        self.__board.print_board()

    def check_winner(self, move: Move, board: Board) -> bool:
        for winning_strategy in self.__winning_strategies:
            if winning_strategy.check_winner(board, move):
                return True
        return False

    def make_move(self):
        player: Player = self.__players[self.next_player_index]
        cell: Cell = player.make_move(board=self.__board)

        move: Move = Move(cell, player)
        self.__moves.append(move)

        if self.check_winner(move, self.__board):
            self.__game_state = GameState.CONCLUDED
            self.__winner = player
            return None

        if len(self.__moves) == self.__board.dimension * self.__board.dimension:
            game_state: GameState = GameState.DRAW
            return


        next_player_index = self.next_player_index + 1
        self.__next_player_index = next_player_index % len(self.__players)

    def undo_move(self):
        if len(self.__moves) == 0:
            print("no move to undo")
            return None
        # last_move = self.__moves[-1]
        last_move = self.__moves.pop()

        cell = last_move.cell
        cell.player = None
        # cell.CellState(CellState.EMPTY)
        cell.cell = CellState.EMPTY


class Builder:
    __players: List[Player]
    __dimension: int
    __winning_strategies: [WinningStrategy]

    def __init__(self):
        self.__players = []
        self.__dimension = 0
        self.__winning_strategies = []

    # @property
    def get_players(self) -> List[Player]:
        return self.__players

    # @players.setter
    def set_players(self, players: List[Player]):
        self.__players = players
        return self

    # @property
    def get_dimension(self) -> int:
        return self.__dimension

    # @dimension.setter
    def set_dimension(self, dimension: int):
        self.__dimension = dimension
        return self

    # @property
    def get_winning_strategies(self) -> List[WinningStrategy]:
        return self.__winning_strategies

    # @winning_strategies.setter
    def set_winning_strategies(self, strategies: List[WinningStrategy]):
        self.__winning_strategies = strategies
        return self

    def validateBotCount(self):
        bot_count: int = 0
        for player in self.__players:
            if player.player_type == PlayerType.BOT:
                bot_count += 1
            if bot_count > 1:
                raise MoreThanOneBotException()

    def validateDimensionAndPlayerCount(self):
        if len(self.__players) != self.__dimension - 1:
            raise PlayersAndBoardCountMismatch()

    def validateUniqueSymbolForEachPlayer(self):
        symbols = set()
        for player in self.__players:
            if player.symbol in symbols:
                raise DuplicateSymbolForPlayer()  # Raise exception if a duplicate is found
            symbols.add(player.symbol)

    def build(self) -> Game:
        self.validateBotCount()
        self.validateDimensionAndPlayerCount()
        self.validateUniqueSymbolForEachPlayer()
        return Game(self.__players, self.__dimension, self.__winning_strategies)
