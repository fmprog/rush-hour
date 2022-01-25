import copy


class DepthFirst:
    """
    A Depth First algorithm 
    """
    def __init__(self, game):
        self.game = game.copy()
        self.states = [self.game]
        self.start_board = game
        self.unique_states = [game.board.tolist()]
        self.path = {}


    def run(self):
        """
        Runs the algorithm until a solution is found
        """

        while len(self.states) > 0:

            new_board = self.get_next_state()

            # check if solution has been found
            if new_board.is_solved():

                # find the first solution
                moves = self.find_path(new_board)
                length_path = len(moves)

                print(f"solved the game in {length_path} moves")
                print(f"Look at the sequence: {moves}")
                break
                
            else:
                self.build_children(new_board)
            

    def get_next_state(self):
            """
            Method that gets the next state from the list of states.
            """
            return self.states.pop()
                        

    def build_children(self, new_board):

        # obtain the possible directions for each vehicle in the game
        #game.show_board_nomove()
        for vehicle in new_board.vehicles:
            #print(vehicle)

            possible_directions = []
            possible_directions = new_board.possible_direction(vehicle)
            #print(possible_directions)

            # for each possible move on the board, make a copy of the game and play the move
            for direction in possible_directions:
                # create a copy of the game
                copy_game = copy.deepcopy(new_board)

                # move the vehicle
                copy_game.move(vehicle, direction)

                #print("unique states")
                #print(self.unique_states)

                list_board = copy_game.board.tolist()
                if list_board not in self.unique_states:
                    self.states.append(copy_game)
                    self.unique_states.append(list_board)

                    # add board and move to the current path
                    self.path[copy_game] = [new_board, [vehicle, direction]]
                    #print(self.path)


    def print(self):
        for i in self.states:
            i.show_board()


    def find_path(self, new_board):
        """
        Creates path
        """
        moves = []

        # new_board represents the winning board
        while new_board != self.start_board:
            # add move to front of list 
            moves.insert(0, self.path[new_board][1])

            # trace back to previous board
            new_board = self.path[new_board][0]

        return moves



        



    

