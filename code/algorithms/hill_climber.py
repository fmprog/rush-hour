from .breadth_first import BreadthFirst
import copy
import random


class HillClimber:
    def __init__(self, game, solution):
        """
        The HillClimber class takes a solution of the depth first or random algorithm and applies the breadth first algorithm a chosen number of iterations on a chosen path length.
        """
        self.start_board = game
        self.solution = solution
        self.solution_len = len(self.solution)
    

    def run(self, iterations):
        """
        Runs the hillclimber algorithm for a chosen number of iterations.
        """
        self.iterations = iterations
        
        for iteration in range(iterations):
            old_solution = copy.deepcopy(self.solution)

            # Create a new solution of the game
            new_solution = self.mutate_path(old_solution)

            # Accept the new solution if it is better than the old one
            self.check_solution(new_solution)


    def mutate_path(self, new_path):
        """
        Changes the solution from a randomly chosen start board to a randomly chosen end point.
        """
        # Pick a random start and end position to create an interval with a maximal length of 10
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
        
        # Select the game object at the random start position and end position
        start_point = self.solution[position - 1][0]
        end_point = self.solution[end_point_position - 1][0]
        
        # Select the path surrounding the selected path 
        beginning_path = self.solution[:position]
        end_path = self.solution[end_point_position:]

        # Apply the breadth first algorithm on the selected part of the path
        breadth = BreadthFirst(start_point, hillclimber = [start_point, end_point])
        breadth.run()

        # Add the different parts of the path together to get a new complete path
        new_path = beginning_path + breadth.solution + end_path

        return(new_path)


    def check_solution(self, new_path):
        """
        Checks and accepts better solutions than the current solution.
        """
        # Define the length of the newly created path
        new_path_len = len(new_path)

        # Replace the solution if the new solution is shorter than the current one
        if new_path_len < self.solution_len:
            self.solution = new_path
            self.solution_len = new_path_len


    def return_solution(self):
        """
        Returns all moves and corresponding boards that lead to the solution.
        """
        return self.solution