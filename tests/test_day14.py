# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day14


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day14"""
    @parameterized.expand([
        ("data/day14a.txt", 10, 1588),
        ("data/day14.txt", 10, 2321),
        ("data/day14a.txt", 40, 2188189693529),
        ("data/day14.txt", 40, 2399822193707),
    ])
    def test_part1(self, filename, until, expected):
        f = open(filename)
        self.assertEqual(day14.part1(f.read().splitlines(), until), expected)


if __name__ == '__main__':
    unittest.main()
