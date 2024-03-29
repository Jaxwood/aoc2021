# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day22


class Day22TestSuite(unittest.TestCase):
    """Test Suite for Day22"""
    @parameterized.expand([
        ('data/day22a.txt', 39),
        ('data/day22b.txt', 590784),
        ('data/day22.txt', 567496),
    ])
    def test_part1(self, filename, expected):
        f = open(filename)
        self.assertEqual(day22.part1(f.read().splitlines()), expected)

    @parameterized.expand([
        ('data/day22c.txt', 2758514936282235),
    ])
    def _test_part2(self, filename, expected):
        f = open(filename)
        self.assertEqual(day22.part2(f.read().splitlines()), expected)

if __name__ == '__main__':
    unittest.main()
