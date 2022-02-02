from .depth_first import DepthFirst


class BreadthFirst(DepthFirst):
    """"
    A Breadth First algorithm that solves the rush hour puzzle by building a queue of children boards and finding the first solution horizontally.  
    The DepthFirst class is used as the parent class as all methods apart the the get_next_state method overlap. 
    """


    def get_next_state(self):
        """
        Method that gets the next state from the queue of states.
        """
        return self.states.pop(0)