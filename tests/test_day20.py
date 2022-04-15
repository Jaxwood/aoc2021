# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day20


class Day20TestSuite(unittest.TestCase):
    """Test Suite for Day20"""
    @parameterized.expand([
        ("data/day20a.txt", 35),
        ("data/day20.txt", 5647),
    ])
    def test_part1(self, filename, expected):
        f = open(filename)
        self.assertEquals(day20.part1(f.read().splitlines()), expected)

    @parameterized.expand([
        ("data/day20a.txt", 3351),
        ("data/day20.txt", 15653),
    ])
    def test_part1(self, filename, expected):
        f = open(filename)
        self.assertEquals(day20.part1(f.read().splitlines(), 50), expected)


if __name__ == '__main__':
    unittest.main()
