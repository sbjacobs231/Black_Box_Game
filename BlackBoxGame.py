# Author: Sky Jacobson
# Date: 8/7/20
# Description:

import Shoot
import Board

class BlackBoxGame:
    """
    Class for an abstract board game called Black Box.
    This class will interact with the classes Board and Shoot
    """

    def __init__(self, atom_locations):
        """
        Atom_locations will be a list of tuples
        Initialize the board with atoms
        """
        self._board = Board.Board(atom_locations)
        self._player = Player()

    def shoot_ray(self, row, column):
        """
        Takes as parameters the row and column where the ray originates
        Corner and non-border squares are not valid
        Return may be None, False or a tuple (row, column)
        """
        # if ray shot is a corner edge, used edge, or not an edge return False
        if not self._board.is_unused_board_edge(row, column):
            return False
        shoot = Shoot.Shoot(self._board, row, column)                # initialize a Shot
        if row == 0 or column == 0:                                  # if tile is an edge
            self._board.update_tile(row, column, 'u')                # mark edge as used

        if shoot.check_if_next_tile_is_hit():                        # if next tile is a hit
            shoot.assign_next_tile()                                 # go to next tile
            shoot.mark_hit()                                         # mark tile as a hit

        if shoot.is_reflection():                                    # if shot is a reflection
            return (row, column)                                     # return the exit tile

        shoot.next_tile()
        return self._board.get_board()

    def guess_atom(self, row, column):
        """
        Returns True or False and adjusts the players score based on a hit or miss
        """
        # if there is an atom at the location return True
        for atom in self._atom_locations:
            if (row, column) == atom:
                return True
        # else return False and subtract 5 from the overall score
        self._player.wrong_atom_guess()
        return False

    def get_score(self):
        """
        Returns the player's score
        """
        return self._player.get_score()

    def atoms_left(self):
        """
        Returns the number of atoms that haven't been guessed yet
        """
        pass

    def get_player_object(self):
        """Method is for testing purposes"""
        return self._player

    def get_shoot_object(self):
        """Method is for testing purposes"""
        return self._shoot

    def get_board_object(self):
        """Method is for testing purposes"""
        return self._board

class Player:
    """
    Class representing a player.
    This class will interact with the BlackBoxGame class.
    """

    def __init__(self):
        # Each player starts with 25 points.
        self._score = 25

    def get_score(self):
        """Return player's score"""
        return self._score

    def wrong_atom_guess(self):
        """Minus 5 points for every incorrect Atom guess"""
        self._score = self._score - 5


def main():
    """
    For testing
    """
    game = BlackBoxGame([(3, 2), (1, 7), (4, 6), (8, 8)])
    # move_result = game.shoot_ray(3, 9)
    # game.shoot_ray(0, 2)
    # guess_result = game.guess_atom(5, 5)
    # score = game.get_score()
    # atoms = game.atoms_left()

if __name__ == '__main__':
    main()