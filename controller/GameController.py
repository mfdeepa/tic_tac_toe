from models.Game import Game


class GameController:

    def make_move(self, game: Game):
        game.make_move()

    def print_board(self, game):
        """Print the current state of the game board."""
        game.print_board()

    def create_game(self, dimension, players, winning_strategy_list):
        return (Game.get_builder()
                .set_players(players)
                .set_dimension(dimension)
                .set_winning_strategies(winning_strategy_list)
                .build())

    def undo_move(self, game: Game):
        """Undo the last move in the game."""
        game.undo_move()
