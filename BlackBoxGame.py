# Author: Sky Jacobson
# Date: 8/7/20
# Description:

import Shoot

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
        self._board = Board(atom_locations)
        self._player = Player()
        self._shoot = Shoot.Shoot()

    def shoot_ray(self, row, column):
        """
        Takes as parameters the row and column where the ray originates
        Corner and non-border squares are not valid
        Return may be None, False or a tuple (row, column)
        """
        # if ray shot is a corner edge, used edge, or not an edge return False
        if not self._board.is_unused_board_edge(row, column):
            return False
        # Test
        self._shoot.next_tile(self._board, row, column)
        return self._board.get_board()
        # else
            # if there was a hit then return None and adjust player score
            # else return (row, column) of the exit border square

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
        """Upon initialization of the board, add atoms to the board"""
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