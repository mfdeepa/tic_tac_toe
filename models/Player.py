from tokenize import String
from models import PlayerType, Board
from abc import ABC, abstractmethod

from models.Cell import Cell


class Player(ABC):
    __symbol: String
    __name: String
    __id: int
    __player_type: PlayerType

    @abstractmethod
    def make_move(self, board:Board):
        pass

    def __init__(self, symbol: String, name: String, id: int, player_type: PlayerType):
        self.__symbol = symbol
        self.__name = name
        self.__id = id
        self.__player_type = player_type

    @property
    def symbol(self) -> str:
        return self.__symbol

    # Setter for symbol
    @symbol.setter
    def symbol(self, value: str):
        self.__symbol = value

    # Getter for name
    @property
    def name(self) -> str:
        return self.__name

    # Setter for name
    @name.setter
    def name(self, value: str):
        self.__name = value

    # Getter for id
    @property
    def id(self) -> int:
        return self.__id

    # Setter for id
    @id.setter
    def id(self, value: int):
        self.__id = value

    # Getter for player_type
    @property
    def player_type(self) -> 'PlayerType':
        return self.__player_type

    # Setter for player_type
    @player_type.setter
    def player_type(self, value: 'PlayerType'):
        self.__player_type = value
