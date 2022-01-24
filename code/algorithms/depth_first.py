import copy


class DepthFirst:
    """
    A Depth First algorithm 
    """
    def __init__(self, game):
        self.game = game.copy()
        self.states = [self.game]
        self.moves = {}


    def print(self):
        for i in self.states:
            i.show_board()


    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop()


    def build_children(self, game):
        children = {}

        for car in self.game.vehicles:
            possible_directions = self.game.possible_direction(car)
            for direction in possible_directions:
                # create new copy of the game
                new_game = game.copy()

                # move the car
                new_move = new_game.move(car, direction)
                children[new_move] = [car, direction]

                # sla je hem op
                self.states.append(new_game)

    
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
                
            # else: bekijk de volgende children
            else:
                self.build_children(new_board)

    def solved(self):




    

