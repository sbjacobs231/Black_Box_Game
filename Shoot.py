# Author: Sky Jacobson
# Date: 8/14/20
# Description:

class Shoot:
    """
    Class with methods that represent every type of shot on the board.
    """
    def __init__(self):
        """
        Keep track of the direction the shot is going (up/down/left/right).
        And set direction back to None when the shot ends.
        Keep track of the board too.
        """
        self._direction = None

    def next_tile(self, board_object, row, column):
        """
        Moves the shot forward one tile on the board at a time.
        """
        # Base case
        if self._direction != None:
            board = board_object.get_board()                # get the list of lists board
            if board[row][column] == 'e' or board[row][column] == 'u':  # if we hit the edge
                return (row, column)                        # return the edge coordinates
        # assess initial direction
        if self._direction == None:
            self.initial_direction(row, column)             # set initial direction of shot
        # find new tile to look at
        if self._direction == 'down':
            row = row + 1
        if self._direction == 'up':
            row = row - 1
        if self._direction == 'right':
            column = column + 1
        if self._direction == 'left':
            column = column - 1
        self.assess_hit(board_object, row, column)          # is next tile a hit
        self.next_tile(board_object, row, column)           # proceed to next tile

    def assess_hit(self, board_object, row, column):
        """
        Assess next tile to see if it's a hit
        """
        tile = board_object.get_board()[row][column]
        if tile == 'a' or tile == 'h':            # if it's a hit then change the tile to h
            board_object.update_tile(row, column, 'h')

    def initial_direction(self, row, column):
        """
        Assesses initial direction shot is going
        """
        if row == 0:  # starting point is top row
            self._direction = 'down'
        elif row == 9:  # starting point is bottom row
            self._direction = 'up'
        elif column == 0:  # starting point is left column
            self._direction = 'right'
        else:  # starting point is right column
            self._direction = 'left'

    def deflection(self, row, column):
        """
        Is the shot a deflection: True or False
        """
        pass

    def reflection(self, row, column):
        """
        Is the shot a reflection: True or False
        """
        pass

    def double_deflection(self, row, column):
        """
        Is the shot a double deflection: True or False
        """
        pass

    def miss(self, row, column):
        """
        Is the shot a miss: True or False
        """
        pass

    def go_up(self, row, column):
        """"""
        pass

    def go_down(self, row, column):
        """"""
        pass

    def go_right(self, row, column):
        """"""
        pass

    def go_left(self, row, column):
        """"""
        pass
