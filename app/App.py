from controller.GameController import GameController
from models.GameState import GameState
from models.HumanPlayer import HumanPlayer
from models.PlayerType import PlayerType
from strategies.ColWiseWinningStrategy import ColWiseWinningStrategy
from strategies.DiagonalWiseWinningStrategy import DiagonalWiseWinningStrategy
from strategies.RowWiseWinningStrategy import RowWiseWinningStrategy

if __name__ == "__main__":
    game_controller = GameController()
    dimension = 3
    players = []

    players.append(HumanPlayer('X', "deepa", 1, PlayerType.HUMAN))
    players.append(HumanPlayer('O', "vidit", 2, PlayerType.HUMAN))

    winning_strategies = [
        RowWiseWinningStrategy(),
        ColWiseWinningStrategy(),
        DiagonalWiseWinningStrategy()
    ]
    # ws = DiagonalWiseWinningStrategy()

    game = game_controller.create_game(dimension, players, winning_strategies)

    while game.game_state == GameState.IN_PROGRESS:
        game_controller.print_board(game)

        undo = input("does anyone want undo? (y/n) :")
        if undo == "y":
            game_controller.undo_move(game)
            continue

        game_controller.make_move(game)

    if game.game_state == GameState.CONCLUDED:
        print(f"{game.winner.name} has won the game")
    if game.game_state == GameState.DRAW:
        print("it is a draw")
