# Author: Sky Jacobson
# Date: 8/14/20
# Description: Player class holds all methods in relation to keeping score.

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