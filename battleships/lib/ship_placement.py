class ShipPlacement:
    def __init__(self, length, orientation, row, col):
        self.length = length
        self.orientation = orientation
        self.row = row
        self.col = col

    def covers(self, row, col):
        if self.orientation == "vertical":
            if self.col != col:
                return False
            return self.row <= row < self.row + self.length
        else:
            if self.row != row:
                return False
            return self.col <= col < self.col + self.length

    # used to provide a concise, human-readable representation of an object that can be used to recreate the object.
    # By default, if __repr__ is not defined for a class, Python will return a string that contains the class name and memory address of the object, which is not very informative.
    def __repr__(self):
        return f"ShipPlacement(length={self.length}, orientation={self.orientation}, row={self.row}, col={self.col})"

    # ship = ShipPlacement(3, "horizontal", 2, 5)
    # print(ship)
    # => ShipPlacement(length=3, orientation=horizontal, row=2, col=5)