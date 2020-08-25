# Author: Sky Jacobson
# Date: 8/13/20
# Description: Black Box Game with a 10x10 board. Shoot rays from the edge of the board.
# Guess where atoms are located. And retrieve your score.

import Shoot
import Board
import Player

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
        self._board = Board.Board(atom_locations)
        self._player = Player.Player(atom_locations)

    def shoot_ray(self, row, column):
        """
        Takes as parameters the row and column where the ray originates
        Return is False if row/column is for corner or non-border tile
        Return is None if there is a hit, False or a tuple (row, column)
        Return is tuple(row, column) for a miss
        """

        if not self._board.is_unused_board_edge(row, column): # if ray shot is a corner edge, used edge, or not an edge return False
            return False

        shoot = Shoot.Shoot(self._board, row, column)         # initialize a Shot
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