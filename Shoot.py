# Author: Sky Jacobson
# Date: 8/14/20
# Description:

class Shoot:
    """
    Class with methods that represent every type of shot on the board.
    """
    def __init__(self, board_object, row, column):
        """
        Keep track of the direction the shot is going (up/down/left/right).
        And set direction back to None when the shot ends.
        Keep track of the board too.
        Row and column is the shot origin
        """
        self._direction = None
        self._board_object = board_object
        self._row = row
        self._column = column
        self._first_compare = True                          # for assessing reflection

    def is_reflection(self):
        """
        Is the shot a reflection: True or False
        First comparison made when player shoots.
        """
        if self._first_compare:
            self.initial_direction()                        # set initial direction of shot
            board = self._board_object.get_board()          # get the list of lists board
            return self.reflection_helper()
        self._first_compare = False                         # This function ran once.
        return False                                        # We only want this to run once per shot.


    def reflection_helper(self):
        """
        Look at appropriate tiles to determine if shot is a reflection
        Returns True or False
        """
        if self._direction == 'down':                       # is next move a reflection going down
            if self._column == 8:                           # atom down one, left one?
                return self.is_atom(self._row + 1, self._column - 1)
            if self._column == 1:                           # atom down one, right one?
                return self.is_atom(self._row + 1, self._column + 1)
            # atom down one, left one or right one?
            return self.is_atom(self._row + 1, self._column - 1) or self.is_atom(self._row + 1, self._column + 1)
        if self._direction == 'up':                         # is next move a reflection going up
            if self._column == 8:                           # atom up one, left one?
                return self.is_atom(self._row - 1, self._column - 1)
            if self._column == 1:                           # atom up one, right one?
                return self.is_atom(self._row - 1, self._column + 1)
            # atom up one, left one or right one?
            return self.is_atom(self._row - 1, self._column - 1) or self.is_atom(self._row - 1, self._column + 1)
        if self._direction == 'right':                      # is next move a reflection going right
            if self._row == 8:                              # atom up one, right one?
                return self.is_atom(self._row - 1, self._column + 1)
            if self._row == 1:                              # atom down one, right one?
                return self.is_atom(self._row + 1, self._column + 1)
            # atom right one, up one or down one?
            return self.is_atom(self._row - 1, self._column + 1) or self.is_atom(self._row + 1, self._column + 1)
        if self._direction == 'left':                       # is next move a reflection going left
            if self._row == 8:                              # atom up one, left one?
                return self.is_atom(self._row - 1, self._column - 1)
            if self._row == 1:                              # atom down one, left one?
                return self.is_atom(self._row + 1, self._column - 1)
            # atom left one, up one or down one?
            return self.is_atom(self._row - 1, self._column - 1) or self.is_atom(self._row + 1, self._column - 1)

    def is_atom(self, row, column):
        """
        Is there an atom at this coordinate?
        Returns True or False
        """
        board = self._board_object.get_board()              # get the list of lists board
        if board[row][column] == 'a' or board[row][column] == 'h':
            return True
        return False

    def initial_direction(self):
        """
        Assesses initial direction shot is going
        """
        if self._row == 0:          # starting point is top row
            self._direction = 'down'
        elif self._row == 9:        # starting point is bottom row
            self._direction = 'up'
        elif self._column == 0:     # starting point is left column
            self._direction = 'right'
        else:                       # starting point is right column
            self._direction = 'left'

    def dive_into_board(self):
        """
        If the shot is not a reflection or immediate hit then dive further into the board.

        """

    def assign_next_tile(self):
        """
        Assigns next row and column of tile.
        """
        if self._direction == 'down':
            self._row = self._row + 1
        if self._direction == 'up':
            self._row = self._row - 1
        if self._direction == 'right':
            self._column = self._column + 1
        if self._direction == 'left':
            self._column = self._column - 1

    def next_tile(self):
        """
        Moves the shot forward one tile on the board at a time.
        """
        board = self._board_object.get_board()          # get the list of lists board
        # if we hit the edge (Base case)
        if board[self._row][self._column] == 'e' or board[self._row][self._column] == 'u':
            return (self._row, self._column)            # return the edge coordinates
        self.assign_next_tile()                         # assigns row and column of next tile
        self.mark_hit()                                 # is next tile a hit?
        self.next_tile()                                # proceed to next tile

    def mark_hit(self):
        """
        Mark tile as a hit
        """
        self._board_object.update_tile(self._row, self._column, 'h')

    def check_if_next_tile_is_hit(self):
        """
        Checks if the next tile is a hit.
        """
        board = self._board_object.get_board()
        if self._direction == 'down':
            if board[self._row + 1][self._column] == 'a' or board[self._row + 1][self._column] == 'h':
                return True
        if self._direction == 'up':
            if board[self._row - 1][self._column] == 'a' or board[self._row - 1][self._column] == 'h':
                return True
        if self._direction == 'right':
            if board[self._row][self._column + 1] == 'a' or board[self._row][self._column + 1] == 'h':
                return True
        if self._direction == 'left':
            if board[self._row][self._column - 1] == 'a' or board[self._row][self._column - 1] == 'h':
                return True
        return False

    def deflection(self, row, column):
        """
        Is the shot a deflection: True or False
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
