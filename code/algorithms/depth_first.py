import copy


class DepthFirst:
    """
    A Depth First algorithm 
    """
    def __init__(self, game):
        self.game = game.copy()
        self.states = [self.game]
        self.unique_states = set()
        self.children = {}

    def print(self):
        for i in self.states:
            i.show_board()


    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop(0)


    def build_children(self, game):

        for car in self.game.vehicles:
            possible_directions = self.game.possible_direction(car)
            for direction in possible_directions:
                # create new copy of the game
                copy_game = game.copy()

                # move the car
                copy_game.move(car, direction)
 
                # if the state is unique save it to states
                if copy_game not in self.unique_states:
                    self.unique_states.add(copy_game)
                    self.states.insert(0, copy_game)
                    self.children[copy_game] = [game, [car, direction]]


    def run(self):
        """
        Runs the algorithm until a solution is found
        """
        # select the initial game board
        # start_board = self.states[0]

        while len(self.states) > 0: 
            new_board = self.get_next_state()
             
            # if: als oplossing is gevonden, geef de path en stop het programma
            if new_board.is_solved():
                # stop the program
                # break

                # continue looking for a better solution
                self.check_solution(new_board)
                
            # else: bekijk de volgende children
            else:
                self.build_children(new_board)


    def check_solution(self, new_board):
        """
        Checks and accepts better solutions than the current solution.
        """
        # bereken de lengte van het laatst uitgerekende pad 
        length_new_path = len(new_board.create_path(new_board))

        # haal het beste pad op
        length_old_path = len(new_board.best_path)

        if length_new_path < length_old_path:
            self.best_solution = new_board
            self.best_path = new_board.path

            print(f"New best path: {self.best_path} steps")


    def create_path(self, new_board):
        """
        Recreates the path of a solution
        """
        if self.children
        self.solution = self.children + self.solution
        



    

