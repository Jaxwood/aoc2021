# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized
from src import day02


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day02"""

    def test_depth_increases(self):
        input = [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"
            ]
        self.assertEquals(day02.calculate_depth(input), 150)

    def test_part1(self):
        f = open('data/day02.txt')
        self.assertEquals(day02.calculate_depth(f.read().splitlines()), 1855814)


if __name__ == '__main__':
    unittest.main()
