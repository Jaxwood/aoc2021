# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day08


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day08"""

    @parameterized.expand([
        ("data/day08a.txt", 26),
        ("data/day08.txt", 344)
    ])
    def test_part1(self, filename, expected):
        f = open(filename)
        self.assertEqual(day08.part1(f.read().splitlines()), expected)

    @parameterized.expand([
        ("data/day08a.txt", 61229),
        ("data/day08.txt", 1048410),
    ])
    def test_part2(self, filename, expected):
        f = open(filename)
        self.assertEqual(day08.part2(f.read().splitlines()), expected)

if __name__ == '__main__':
    unittest.main()
