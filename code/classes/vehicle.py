class Vehicle:
    def __init__(self, uid, orientation, column, row, length, position):
        '''Creates a vehicle'''
        self.uid = uid
        self.orientation = orientation
        self.column = column
        self.row = row
        self.length = length
        self.position = position