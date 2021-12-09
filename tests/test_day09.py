# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day09


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day09"""
    @parameterized.expand([("data/day09a.txt", 15), ("data/day09.txt", 508)])
    def test_part1(self, filename, expected):
        f = open(filename)
        self.assertEquals(day09.part1(f.read().splitlines()), expected)

    @parameterized.expand([("data/day09a.txt", 1134), ("data/day09.txt", 508)])
    def test_part2(self, filename, expected):
        f = open(filename)
        self.assertEquals(day09.part2(f.read().splitlines()), expected)


if __name__ == '__main__':
    unittest.main()
