import copy


class DepthFirst:
    """
    A Depth First algorithm that solves the rush hour puzzle by building a stack of children boards and finding the first solution vertically.  
    """
    def __init__(self, game, hillclimber = False):
        self.states = [game]
        self.start_board = game
        self.unique_states = [game.board.tolist()]
        self.path = {}
        self.solution = []
        self.board = hillclimber


    def run(self):
        """
        Method that creates children until a solution to the puzzle is found or there are no more children boards in the stack.
        """
        while len(self.states) > 0:
            new_board = self.get_next_state()

            # If a solution is found, quit running the program
            if new_board.is_solved(board = new_board, hillclimber = self.board):
                
                # Create the sequence of moves that lead to the solution
                self.moves = self.find_path(new_board)
                break
                
            # If no solution is found, keep building children
            else:
                self.build_children(new_board)
            

    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop()
                        

    def build_children(self, new_board):
        """
        Build children boards and add them to the front of the stack.
        """
        
        # Get the possible directions for each vehicle in the game
        for vehicle in new_board.vehicles:
            possible_directions = new_board.possible_direction(vehicle)

            # For each possible move on the board make a copy of the game and play the move
            for direction in possible_directions:
                copy_game = copy.deepcopy(new_board)
                copy_game.move(vehicle, direction)

                # If state has not been reached before, add it to the stack
                list_board = copy_game.board.tolist()
                
                if list_board not in self.unique_states:
                    self.states.append(copy_game)
                    self.unique_states.append(list_board)

                    # Add board and move to the path
                    self.path[copy_game] = [new_board, [vehicle, direction]]


    def find_path(self, new_board):
        """
        Traces back the path to reach the solution.
        """
        moves = []
        solution = []

        while new_board != self.start_board:
            moves.insert(0, self.path[new_board][1])
            solution.insert(0, [new_board, self.path[new_board][1]])

            # Trace back to previous board
            new_board = self.path[new_board][0]
            
        self.solution = solution

        return moves
    
    
    def return_solution(self):
        '''
        Returns all moves and corresponding boards that lead to the solution.
        '''
        return self.solution



        



    

