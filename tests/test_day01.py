# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized
from src import day01


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day01"""

    def test_measurements_increases(self):
        input = [
                199,
                200,
                208,
                210,
                200,
                207,
                240,
                269,
                260,
                263]
        self.assertEquals(day01.increases(input), 7)

    def test_part1(self):
        f = open('data/day01.txt')
        self.assertEquals(day01.increases(list(map(int, f.read().splitlines()))), 1529)


if __name__ == '__main__':
    unittest.main()
