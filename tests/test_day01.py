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
        self.assertEqual(day01.increases(input), 7)

    def test_part1(self):
        f = open('data/day01.txt')
        self.assertEqual(day01.increases(list(map(int, f.read().splitlines()))), 1529)

    def test_measurements_window_increases(self):
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
        self.assertEqual(day01.window_increases(input), 5)

    def test_part2(self):
        f = open('data/day01.txt')
        self.assertEqual(day01.window_increases(list(map(int, f.read().splitlines()))), 1567)


if __name__ == '__main__':
    unittest.main()
