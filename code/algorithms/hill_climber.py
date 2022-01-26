
from .depth_first import DepthFirst
import copy

class HillClimber:
    def __init__(self, game):
        """
        The HillClimber class...
        """
        self.first_sol = DepthFirst(game)
        self.first_sol_path = self.first_sol.path
        self.path = copy.deepcopy(self.first_sol)
        self.path_len = len(DepthFirst.find_path(DepthFirst.get_next_state()))
    
    def mutate_single_move(self, new_path):
        """
        Changes a single move in the path.
        """


    def check_solution(self, new_path):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_path_len = len(new_path)
        old_path_len = self.path_len

        # We are looking for maps that cost less!
        if new_path_len <= old_path_len:
            self.path = new_path
            self.path_len = new_path_len

    def run(self, iterations):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """

        self.iterations = iterations
        
        for iteration in range(iterations):
