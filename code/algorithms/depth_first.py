import copy


class DepthFirst:
    """
    A Depth First algorithm  
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
        Method that runs the algorithm untill a solution to the puzzle is found
        """
        while len(self.states) > 0:
            new_board = self.get_next_state()

            # Check if puzzle is solved
            if new_board.is_solved(board = new_board, hillclimber = self.board):
                # Create the sequence of moves that lead to the winning position and count the number of moves
                self.moves = self.find_path(new_board)

                # Quit after puzzle is solved once
                break
                
            # If the puzzle is not solved, keep building children
            else:
                self.build_children(new_board)
            

    def get_next_state(self):
            """
            Method that gets the next state from the list of states.
            """
            return self.states.pop()
                        

    def build_children(self, new_board):
        """
        Build children and add to the stack
        """
        # Obtain the possible directions for each vehicle in the game
        for vehicle in new_board.vehicles:

            possible_directions = []
            possible_directions = new_board.possible_direction(vehicle)

            # for each possible move on the board, make a copy of the game and play the move
            for direction in possible_directions:
                # create a copy of the game
                copy_game = copy.deepcopy(new_board)

                # move the vehicle
                copy_game.move(vehicle, direction)

                list_board = copy_game.board.tolist()
                if list_board not in self.unique_states:
                    self.states.append(copy_game)
                    self.unique_states.append(list_board)

                    # add board and move to the current path
                    self.path[copy_game] = [new_board, [vehicle, direction]]


    def find_path(self, new_board):
        """
        Creates path
        """
        moves = []
        solution = []

        # new_board represents the winning board
        while new_board != self.start_board:
            # add move to front of list 
            moves.insert(0, self.path[new_board][1])
            solution.insert(0, [new_board, self.path[new_board][1]])

            # trace back to previous board
            new_board = self.path[new_board][0]
            
        self.solution = solution

        return moves
    
    def return_solution(self):
        '''
        Returns the path and the corresponding boards.
        '''
        return self.solution



        



    

