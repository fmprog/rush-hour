import copy


class DepthFirst:
    """
    A Depth First algorithm 
    """
    def __init__(self, game):
        self.game = game.copy()
        self.states = [self.game]
        self.start_boad = game
        self.unique_states = []
        self.path = {}


    def run(self):
        """
        Runs the algorithm until a solution is found
        """
       
        print("start!")
        #while len(self.states) > 0:
        for i in range(4):
            new_board = self.get_next_state()
            print("This is the new board:")
            new_board.show_board_nomove()

            # check if solution has been found
            if new_board.is_solved():
                # stop the program
                # break

                # continue to look for a better solution
                moves = self.find_path(new_board)
                length_path = len(moves)
                print(f"solved the game in {length_path} moves")
                print(f"Look at the sequence: {moves}")
                
            else:
                self.build_children(new_board)
            


    def get_next_state(self):
            """
            Method that gets the next state from the list of states.
            """
            return self.states.pop(0)
                        

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
 
                # if this state has not been reached before add it to the queue
                if copy_game.board not in self.unique_states:
                    self.states.insert(0, copy_game)
                    self.unique_states.append(copy_game.board)
                    
                    # add board and move to the current path
                    self.path[copy_game] = [new_board, [vehicle, direction]]

                    #self.children[copy_game] = [game, [car, direction]]


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



        



    

