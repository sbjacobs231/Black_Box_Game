# Author: Sky Jacobson
# Date: 8/14/20
# Description: Series of tests to make sure BlackBoxGame.py is accurate.

import BlackBoxGame
import unittest

class BlackBoxGameTester(unittest.TestCase):
    """
    This class tests all the classes and methods within BlackBoxGame
    """

    def setUp(self):
        """Initialize an instance of BlackBoxGame"""

        self._BlackBoxGame = BlackBoxGame.BlackBoxGame([(3,2),(1,7),(4,6),(8,8), (8, 2), (3, 1)])
        self._BlackBoxGame1 = BlackBoxGame.BlackBoxGame([(3,1), (3,3), (7,3)])

    def test_initialized_board(self):
        """Tests that the board initializes with the atoms in the correct locations."""

        result = self._BlackBoxGame.get_board_object().get_board()
        expected = [
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c'],
            ['e', '', '', '', '', '', '', 'a', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', 'a', 'a', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', 'a', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', 'a', '', '', '', '', '', 'a', 'e'],
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c']
        ]
        self.assertEqual(result, expected)

    def test_initialized_board_1(self):
        """Tests that the board initializes with the atoms in the correct locations."""

        result = self._BlackBoxGame1.get_board_object().get_board()
        expected = [
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', 'a', '', 'a', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', 'a', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c']
        ]
        self.assertEqual(result, expected)

    def test_corner_shot(self):
        """Tests that a corner shot returns False"""
        result = self._BlackBoxGame.shoot_ray(0, 0)
        self.assertFalse(result)

    def test_middle_of_the_board_shot(self):
        """Tests that a middle of the board shot returns False"""
        result = self._BlackBoxGame.shoot_ray(3, 4)
        self.assertFalse(result)

    def test_reflection_top_row(self):
        """Tests that a reflection happens in the top row"""
        result = self._BlackBoxGame.shoot_ray(0, 8)
        self.assertEqual((0, 8), result)

    def test_2_reflection_top_row(self):
        """Tests that a reflection happens in the top row"""
        result = self._BlackBoxGame.shoot_ray(0, 6)
        self.assertEqual((0, 6), result)

    def test_reflection_bottom_row(self):
        """Tests that a reflection happens in the bottom row"""
        result = self._BlackBoxGame.shoot_ray(9, 7)
        self.assertEqual((9, 7), result)

    def test_2_reflection_bottom_row(self):
        """Tests that a reflection happens in the bottom row"""
        result = self._BlackBoxGame.shoot_ray(9, 1)
        self.assertEqual((9,1), result)

    def test_reflection_right_column(self):
        """Tests that a reflection happens in the right column"""
        result = self._BlackBoxGame.shoot_ray(7, 9)
        self.assertEqual((7,9), result)

    def test_reflection_left_column(self):
        """Tests that a reflection happens in the left column"""
        result = self._BlackBoxGame.shoot_ray(2, 0)
        self.assertEqual((2,0), result)

    def test_hit_down(self):
        """Tests a hit going down"""
        result = self._BlackBoxGame.shoot_ray(0, 7)
        self.assertIsNone(result)

    def test_hit_up(self):
        """Tests a hit going up"""
        result = self._BlackBoxGame.shoot_ray(9, 6)
        self.assertIsNone(result)

    def test_hit_right(self):
        """Tests a hit going right"""
        result = self._BlackBoxGame.shoot_ray(8, 0)
        self.assertIsNone(result)

    def test_hit_left(self):
        """Tests a hit going left"""
        result = self._BlackBoxGame.shoot_ray(4, 9)
        self.assertIsNone(result)

    def test_straight_miss(self):
        """Tests a straight miss"""
        result = self._BlackBoxGame.shoot_ray(6, 0)
        self.assertEqual((6, 9), result)

    def test_single_deflection(self):
        """Tests a simple single deflection"""
        result = self._BlackBoxGame.shoot_ray(9, 5)
        self.assertEqual((5, 0), result)

    def test_double_deflection(self):
        """Tests two deflections in one path, not to confused with a double deflection"""
        result = self._BlackBoxGame1.shoot_ray(0, 2)
        self.assertEqual((0,2), result)

    def test_detour(self):
        """Tests for detour"""
        result = self._BlackBoxGame1.shoot_ray(6, 9)
        self.assertEqual((4, 9), result)

    def test_board_records(self):
        """Tests the board records properly"""
        expected = [
            ['c', 'e', 'u', 'e', 'e', 'e', 'e', 'e', 'e', 'c'],
            ['e', '', '', '', '', '', '', 'a', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'u'],
            ['e', 'a', 'h', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', 'h', '', '', 'e'],
            ['u', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', 'a', '', '', '', '', '', 'h', 'e'],
            ['c', 'e', 'e', 'e', 'e', 'u', 'u', 'e', 'e', 'c']
        ]
        self._BlackBoxGame.shoot_ray(0, 2)
        self._BlackBoxGame.shoot_ray(9, 6)
        self._BlackBoxGame.shoot_ray(9, 5)
        self._BlackBoxGame.shoot_ray(2, 9)
        result = self._BlackBoxGame.get_board_object().get_board()
        self.assertEqual(result, expected)

    def test_board_records_1(self):
        """Second test for board recording properly"""
        expected = [
            ['c', 'e', 'u', 'u', 'e', 'e', 'e', 'e', 'e', 'c'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', 'a', '', 'h', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', 'a', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c']
        ]
        self._BlackBoxGame1.shoot_ray(0, 2)
        self._BlackBoxGame1.shoot_ray(0, 3)
        result = self._BlackBoxGame1.get_board_object().get_board()
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()