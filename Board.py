# Author: Sky Jacobson
# Date: 8/14/20
# Description: Board class has all methods relating to reading and writing to the board.

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