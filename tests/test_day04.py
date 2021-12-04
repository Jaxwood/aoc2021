# -*- coding: utf-8 -*-
import unittest
from src import day04


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day04"""

    def test_power_consumption(self):
        f = open('data/day04a.txt')
        self.assertEquals(day04.play(f.read().splitlines()), 4512)

    def test_part1(self):
        f = open('data/day04.txt')
        self.assertEquals(day04.play(f.read().splitlines()), 0)

if __name__ == '__main__':
    unittest.main()
