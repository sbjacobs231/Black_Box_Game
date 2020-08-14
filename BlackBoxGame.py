# Author: Sky Jacobson
# Date: 8/14/20
# Description: Black Box Game with a 10x10 board. Shoot rays from the edge of the board.
# Guess where atoms are located. And retrieve your score.

# import Shoot
# import Board
# import Player

class BlackBoxGame:
    """
    Class for an abstract board game called Black Box.
    This class will interact with the classes Board, Shoot, Player
    """

    def __init__(self, atom_locations):
        """
        Atom_locations will be a list of tuples
        Initialize the board with atoms
        """
        # self._board = Board.Board(atom_locations)
        # self._player = Player.Player(atom_locations)
        self._board = Board(atom_locations)
        self._player = Player(atom_locations)

    def shoot_ray(self, row, column):
        """
        Takes as parameters the row and column where the ray originates
        Return is False if row/column is for corner or non-border tile
        Return is None if there is a hit, False or a tuple (row, column)
        Return is tuple(row, column) for a miss
        """

        if not self._board.is_unused_board_edge(row, column): # if ray shot is a corner edge, used edge, or not an edge return False
            return False

        # shoot = Shoot.Shoot(self._board, row, column)         # initialize a Shot
        shoot = Shoot(self._board, row, column)  # initialize a Shot
        if row == 0 or column == 0 or row == 9 or column == 9:# if tile is an edge
            self._board.update_tile(row, column, 'u')         # mark edge as used

        if shoot.check_if_next_tile_is_hit():                 # if next tile is a hit
            shoot.assign_next_tile()                          # go to next tile
            shoot.mark_hit()                                  # mark tile as a hit
            return None

        if shoot.is_reflection():                             # if shot is a reflection
            return (row, column)                              # return the exit tile

        return shoot.next_tile()                              # use recursion to loop through the board

    def guess_atom(self, row, column):
        """
        Return True if there is an atom at the location
        Return False and subtract 5 from the overall score if there is no atom at the location
        """
        if self._player.find_atom(row, column):               # if atom is found at coords
            self._player.add_correct_guess(row, column)       # add guess to list of correct guesses
            return True                                       # return True
        self._player.subtract_5(row, column)                  # subtract 5 from overall score if it's a new guess
        self._player.add_wrong_guess(row, column)             # otherwise there wasn't an atom at this location
        return False

    def get_score(self):
        """
        Subtracts 1 from every used edge of the board.
        Returns the player's score
        """
        self._player.subtract_used_edges_from_score(self._board.get_board())
        return self._player.get_score()

    def atoms_left(self):
        """
        Returns the number of atoms that haven't been guessed yet
        """
        return self._player.atoms_left()

    def get_board_object(self):
        """Method is for testing purposes"""
        return self._board

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

class Board:
    """
    Class representing the different aspects of the board.
    It has methods of retrieving the board and printing the board.
    This class will be accessed by the BlackBoxGame class.
    """

    def __init__(self, atom_locations):
        """
        The board will be a 10x10 grid where rows 0 and 9, and columns 0 and 9
        are used by the guessing player for shooting rays into the black box.
        The atoms are restricted to being within rows 1-8 and columns 1-8
        """
        # '' = empty
        # 'a' = atom
        # 'c' = corner
        # 'e' = edge
        # 'h' = hit
        # 'u' = used edge
        self._board = [
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c']
        ]
        self.add_atoms_to_board(atom_locations)

    def add_atoms_to_board(self, atoms_locations):
        """
        Upon initialization of the board, add atoms to the board
        """
        for atom in atoms_locations:
            atom_row = atom[0]
            atom_column = atom[1]
            self._board[atom_row][atom_column] = 'a'

    def print_board(self):
        """
        Print the board in a nice format.
        """
        for row in self._board:
            print(row)

    def get_board(self):
        """
        Get the board
        """
        return self._board

    def update_tile(self, row, column, char):
        """
        Update the tile on the board
        """
        self._board[row][column] = char

    def is_unused_board_edge(self, row, column):
        """
        Player's shot is an edge but not a corner
        """
        if self._board[row][column] == 'e':
            return True
        return False

class Player:
    """
    Class representing a player.
    This class will interact with the BlackBoxGame class.
    Each entry/exit of a shot subtracts one point from the total score.
    Each incorrect atom guess subtracts 5 points from the total score.
    """

    def __init__(self, atom_locations):
        """
        Each player starts with 25 points
        List of atom locations come in as a parameter
        Keep track of wrong atom guesses
        Keep track of correct atom guesses
        """
        self._score = 25
        self._atom_locations = atom_locations
        self._wrong_atom_guesses = None
        self._correct_atom_guesses = None

    def add_wrong_guess(self, row, column):
        """
        Add player's atom guess to list of guesses
        """
        if self._wrong_atom_guesses == None:            # if set is not created yet
            self._wrong_atom_guesses = {(row, column)}  # create set with first guess
        else:
            self._wrong_atom_guesses.add((row, column)) # add wrong guess

    def add_correct_guess(self, row, column):
        """
        Add 1 for each correct atom guess, but don't add 1 for repeat guesses
        """
        if self._correct_atom_guesses == None:          # if set is not created yet
            self._correct_atom_guesses = {(row, column)}# create set with first guess
        else:
            self._correct_atom_guesses.add((row, column))    # add correct guess

    def find_atom(self, row, column):
        """
        Does the atom exist in the [row, column] location.
        """
        for atom in self._atom_locations:               # loop through each atom
            if atom[0] == row and atom[1] == column:    # if atom shares the coordinates as the guess
                return True
        return False

    def get_score(self):
        """
        Return player's score
        """
        return self._score

    def subtract_5(self, row, column):
        """
        Minus 5 points for every new incorrect Atom guess
        """
        repeated_guess = False
        if self._wrong_atom_guesses is not None:
            for guess in self._wrong_atom_guesses:           # loop through each wrong guess
                if guess[0] == row and guess[1] == column:   # if player guessed this before
                    repeated_guess = True                    # take note of it
        if repeated_guess == False:                          # if player has not guessed this before
            self._score = self._score - 5                    # subtract 5 points from total score

    def atoms_left(self):
        """
        Subtracts set of atoms from set of correct atom guesses=
        """
        return len(self._atom_locations) - len(self._correct_atom_guesses)

    def subtract_used_edges_from_score(self, board):
        """
        Subtracts 1 from score for every used edge
        """
        for row in board:                           # loop through every row of the board
            for cell in row:                        # loop through every cell of the row
                if cell == 'u':                     # if cell is a used edge
                    self._score = self._score - 1   # subtract 1 from total score