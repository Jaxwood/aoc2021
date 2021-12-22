# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day18


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day18"""
    @parameterized.expand([([[[[[9, 8], 1], 2], 3], 4], [[[[0, 9], 2], 3],
                                                         4])])
    def _test_part1(self, candidate, expected):
        self.assertEquals(day18.explode(candidate), expected)

    @parameterized.expand([
        # ("data/day18.txt", 1),
        ("data/day18a.txt", 1),
    ])
    def _test_part1(self, filename, expected):
        f = open(filename)
        self.assertEquals(day18.part1(f.read().splitlines()), expected)

    @parameterized.expand([([[[[[9, 8], 1], 2], 3], 4], True),
                           ([[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1,
                                                                    1]], True),
                           ([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]], False),
                           ([[[[0, 7], 4], [15, [0, 13]]], [1, 1]], False)])
    def test_can_explode(self, candidate, expected):
        self.assertEquals(day18.can_explode(candidate), expected)

    @parameterized.expand([([[[[[9, 8], 1], 2], 3], 4], False),
                           ([[[[0, 7], 4], [[7, 8], [0, [6, 7]]]],
                             [1, 1]], False),
                           ([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]], True),
                           ([[[[0, 7], 4], [15, [0, 13]]], [1, 1]], True)])
    def test_can_split(self, candidate, expected):
        self.assertEquals(day18.can_split(candidate), expected)

    @parameterized.expand([([[[[0, 7], 4], [15, [0, 13]]], [1,
                                                            1]], [[[[0, 7], 4],
                                                                   [[7, 8],
                                                                    [0, 13]]],
                                                                  [1, 1]]),
                           ([[[[0, 7], 4], [[7, 8], [0, 13]]],
                             [1, 1]], [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]],
                                       [1, 1]])])
    def test_split(self, candidate, expected):
        actual = day18.split(candidate)
        self.assertEquals(actual, expected)


if __name__ == '__main__':
    unittest.main()
