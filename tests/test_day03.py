# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day03


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day03"""

    def test_power_consumption(self):
        input = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010"
            ]
        self.assertEquals(day03.calculate_power_consumption(input), 198)

    def test_part1(self):
        f = open('data/day03.txt')
        self.assertEquals(day03.calculate_power_consumption(f.read().splitlines()), 2261546)


if __name__ == '__main__':
    unittest.main()
