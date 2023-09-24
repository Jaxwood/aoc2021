# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day11


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day11"""
    @parameterized.expand([("data/day11a.txt", 1656),
                           ("data/day11.txt", 1562)])
    def test_part1(self, filename, expected):
        f = open(filename)
        self.assertEqual(day11.part1(f.read().splitlines()), expected)

    @parameterized.expand([("data/day11a.txt", 195),
                           ("data/day11.txt", 268)])
    def test_part1(self, filename, expected):
        f = open(filename)
        self.assertEqual(day11.part2(f.read().splitlines()), expected)


if __name__ == '__main__':
    unittest.main()
