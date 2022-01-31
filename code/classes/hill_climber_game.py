
from .game import Game

class HillClimberGame(Game):

    def is_solved(self, current_board, end_board):
        """
        Checks if...
        """

        if current_board == end_board:
            return True

        else:
            return False