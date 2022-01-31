
from .depth_first import DepthFirst
from .breadth_first import BreadthFirst
import copy
import random
from code.classes.game import Game

class HillClimber:
    def __init__(self, game, solution):
        """
        The HillClimber class .....
        Each improvement or equivalent solution is kept for the next iteration.
        """
        self.start_board = game
        self.solution = solution
        self.solution_len = len(self.solution)
        print(f'this is the current sol len: {self.solution_len}')
    
    def mutate_path(self, new_path):
        """
        Changes the solution path from a random start point.
        """
        # Pick a random position to pick our starting point
        position = random.randint(5, self.solution_len)
        print(f'this is the position: {position}')
        start_point = self.solution[position - 1][0]

        end_point_position = random.randint(position, self.solution_len)

        print(f'this is the end_point_position: {end_point_position}')
        print(f'len van solution: {len(self.solution)}')

        end_point = self.solution[end_point_position - 1][0]
        

        # The path towards the starting point remains the same
        beginning_path = self.solution[:position]
        end_path = self.solution[end_point_position:]


        # Continue from this board by using the breadth first algorithm untill we find the end point
        breadth = BreadthFirst(start_point, hillclimber = [start_point, end_point])
        breadth.run()
        print("start")
        print(f"length begin = {len(beginning_path)}")
        for i in beginning_path:
            print(i[1])
        print("middle")
        print(f"length middle= {len(breadth.solution)}")
        for i in breadth.solution:
            print(i[1])
        print("end")
        print(f"length end = {len(end_path)}")
        for i in end_path:
            print(i[1])
        new_path = beginning_path + breadth.solution + end_path

        return(new_path)

    def check_solution(self, new_path):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_path_len = len(new_path)
        print(f"new path length: {new_path_len}")
        old_path_len = self.solution_len

        # We are looking for maps that cost less!
        if new_path_len < old_path_len:
            self.solution = new_path
            self.solution_len = new_path_len
        print(f"solution length = {self.solution_len}")
        print("SOLUTION:")
        j = 1
        for i in self.solution:
            print(j)
            print(i[1])
            j += 1

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

            
        
