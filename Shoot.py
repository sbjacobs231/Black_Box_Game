# Author: Sky Jacobson
# Date: 8/14/20
# Description: Shoot class holds all methods for fulfilling the conditions of the
# different types of shots that can be made in the BlackBoxGame.

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

    def is_reflection(self):
        """
        Is the shot a reflection: True or False
        First comparison made when player shoots.
        """
        self.initial_direction()                        # set initial direction of shot
        board = self._board_object.get_board()          # get the list of lists board
        return self.reflection_helper()


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

    def next_tile(self, iterations = 1):
        """
        Moves the shot forward one tile on the board at a time.
        """
        board = self._board_object.get_board()          # get the list of lists board

        if iterations > 1:                              # if we hit the edge (Base case)
            if board[self._row][self._column] == 'e' or board[self._row][self._column] == 'u':
                self._board_object.update_tile(self._row, self._column, 'u') # update the board
                return (self._row, self._column)        # return the edge coordinates

        if self.check_if_next_tile_is_hit():            # is next tile a hit?
            self.assign_next_tile()                     # move to next tile
            self.mark_hit()                             # update the board
            return None

        self.check_deflection()                         # check for deflection
        self.assign_next_tile()                         # move to next tile
        iterations = iterations + 1                     # allows for base case to occur
        return self.next_tile(iterations)               # rinse and repeat

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

    def mark_hit(self):
        """
        Mark tile as a hit
        """
        self._board_object.update_tile(self._row, self._column, 'h')

    def check_deflection(self):
        """
        Checks next tile's adjacent tiles for atom to see if there is a deflection
        """
        if self.double_deflection() == False:   # if there is no double deflection
            self.single_deflection()            # check for single deflection

    def double_deflection(self):
        """
        Checks for a double deflection.
        Returns True or False
        """
        if self._direction == 'down':           # if double deflection go up
            if self.is_atom(self._row + 1, self._column - 1) and self.is_atom(self._row + 1, self._column + 1):
                self._direction = 'up'
                return True

        elif self._direction == 'up':           # if double deflection go down
            if self.is_atom(self._row - 1, self._column - 1) and self.is_atom(self._row - 1, self._column + 1):
                self._direction = 'down'
                return True

        elif self._direction == 'right':        # if double deflection go left
            if self.is_atom(self._row - 1, self._column + 1) and self.is_atom(self._row + 1, self._column + 1):
                self._direction = 'left'
                return True

        elif self._direction == 'left':         # if double deflection go right
            if self.is_atom(self._row - 1, self._column - 1) and self.is_atom(self._row + 1, self._column - 1):
                self._direction = 'right'
                return True

        return False                            # returns False if there was no double deflection

    def single_deflection(self):
        """
        Checks for a single deflection
        """
        if self._direction == 'down':                          # is next move a deflection going down
            if self.is_atom(self._row + 1, self._column - 1):  # atom down one, left one?
                self._direction = 'right'                      # go right
            if self.is_atom(self._row + 1, self._column + 1):  # atom down one, right one?
                self._direction = 'left'                       # go left


        elif self._direction == 'up':                          # is next move a deflection going up
            if self.is_atom(self._row - 1, self._column - 1):  # atom up one, left one?
                self._direction = 'right'                      # go right
            if self.is_atom(self._row - 1, self._column + 1):  # atom up one, right one?
                self._direction = 'left'                       # go left

        elif self._direction == 'right':                       # is next move a deflection going right
            if self.is_atom(self._row - 1, self._column + 1):  # atom up one, right one?
                self._direction = 'down'                       # go down
            if self.is_atom(self._row + 1, self._column + 1):  # atom down one, right one?
                self._direction = 'up'                         # go up

        elif self._direction == 'left':
            if self.is_atom(self._row - 1, self._column - 1):  # atom up one, left one?
                self._direction = 'down'                       # go down
            if self.is_atom(self._row + 1, self._column - 1):  # atom down one, left one?
                self._direction = 'up'                         # go up