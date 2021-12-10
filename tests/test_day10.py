# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day10


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day10"""
    @parameterized.expand([("data/day10a.txt", 26397),
                           ("data/day10.txt", 339537)])
    def test_part1(self, filename, expected):
        f = open(filename)
        self.assertEquals(day10.part1(f.read().splitlines()), expected)

    @parameterized.expand([("data/day10a.txt", 288957),
                           ("data/day10.txt", 2412013412)])
    def test_part2(self, filename, expected):
        f = open(filename)
        self.assertEquals(day10.part2(f.read().splitlines()), expected)


if __name__ == '__main__':
    unittest.main()
