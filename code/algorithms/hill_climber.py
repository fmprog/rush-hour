
from .depth_first import DepthFirst
from .breadth_first import BreadthFirst
import copy
import random

class HillClimber:
    def __init__(self, game, solution):
        """
        The HillClimber class .....
        Each improvement or equivalent solution is kept for the next iteration.
        """
        self.start_board = game
        # print(solution)
        # self.first_sol = DepthFirst(game).run()
        # self.first_sol_path = self.first_sol.path
        # self.path = copy.deepcopy(self.first_sol)
        self.solution = solution
        self.solution_len = len(self.solution)
    
    def mutate_path(self, new_path):
        """
        Changes the solution path from a random start point.
        """
        # Pick a random position to pick our starting point
        position = random.randint(5, self.solution_len)
        start_point = self.solution[position][0]
        print(start_point)

        # The path towards the starting point remains the same
        new_path = self.solution[:position]

        # Continue from this board by using the breadth first algorithm
        breadth = BreadthFirst(start_point)
        breadth.run()

        # print(breadth.solution)
        # print(new_path)
        # new = new_path.extend(breadth.solution)
        new_path = new_path + breadth.solution
        # print(new_path)
        # print(len(new_path))

        return(new_path)




    def check_solution(self, new_path):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_path_len = len(new_path)
        print(new_path_len)
        old_path_len = self.solution_len

        # We are looking for maps that cost less!
        if new_path_len <= old_path_len:
            self.solution = new_path
            self.solution_len = new_path_len
        print(self.solution_len)
        for i in self.solution:
            print(i[1])

    def run(self, iterations):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations
        
        for iteration in range(iterations):

            # Create a copy of the graph to simulate the change
            old_solution = copy.deepcopy(self.solution)

            # Create a new solution to the game
            new_solution = self.mutate_path(old_solution)

            # Accept the new solution if it is better
            self.check_solution(new_solution)
        
