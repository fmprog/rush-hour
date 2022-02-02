
from .depth_first import DepthFirst
from .breadth_first import BreadthFirst
import copy
import random
from code.classes.game import Game

class HillClimber:
    def __init__(self, game, solution):
        """
        The HillClimber class takes a solution of any algorithm and applies the breadth algorithm to a certain interval of the current path of the solution.
        Each improvement or equivalent solution is kept for the next iteration.
        """
        self.start_board = game
        self.solution = solution
        self.solution_len = len(self.solution)
    

    def mutate_path(self, new_path):
        """
        Changes the solution path from a random start point.
        """

        # Pick a random start position and pick an end position to create an interval with a maximal length of 10
        position = random.randint(5, self.solution_len)
        if self.start_board.size == 6:
            end_point_position = position + 10
            if end_point_position > self.solution_len:
                end_point_position = self.solution_len
        elif self.start_board.size == 9:
            end_point_position = position + 10
            if end_point_position > self.solution_len:
                end_point_position = self.solution_len
        else:
            end_point_position = position + 10
            if end_point_position > self.solution_len:
                end_point_position = self.solution_len
        
        # Define a game object at our random starting position and ending position
        start_point = self.solution[position - 1][0]
        end_point = self.solution[end_point_position - 1][0]
        
        # Define the beginning and ending of the path 
        beginning_path = self.solution[:position]
        end_path = self.solution[end_point_position:]

        # Apply the breadth first algorithm starting from our random starting point to our random ending point
        breadth = BreadthFirst(start_point, hillclimber = [start_point, end_point])
        breadth.run()

        # Add the different parts of the path together to get a new complete path
        new_path = beginning_path + breadth.solution + end_path

        return(new_path)


    def check_solution(self, new_path):
        """
        Checks and accepts better solutions than the current solution.
        """

        # Define the length of the newly created path and original path
        new_path_len = len(new_path)
        old_path_len = self.solution_len

        # Check if the newly created path is shorter than our original path
        if new_path_len < old_path_len:

            # Replace the original solution by our new path
            self.solution = new_path
            self.solution_len = new_path_len


    def run(self, iterations):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations
        
        for iteration in range(iterations):

            # Create a copy of the game object to simulate the change
            old_solution = copy.deepcopy(self.solution)

            # Create a new solution of the game by calling mutate_path()
            new_solution = self.mutate_path(old_solution)

            # Accept the new solution if it is better
            self.check_solution(new_solution)


    def return_solution(self):
        '''
        Returns the path and the corresponding boards.
        '''
        return self.solution


            
        
