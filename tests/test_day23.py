# -*- coding: utf-8 -*-
from typing import List, Tuple
import unittest
from parameterized import parameterized
from src import day23


class Day23TestSuite(unittest.TestCase):
    """Test Suite for Day23"""

    @parameterized.expand([
        ('data/day23.txt', 12521),
        ('data/day23a.txt', 16506),
    ])
    def test_part1(self, filename, expected):
        f = open(filename)
        self.assertEquals(day23.part1(f.read().splitlines()), expected)

    @parameterized.expand([
        ('data/day23.txt', (9, 2), [(9, 1)]),
        ('data/day23.txt', (9, 1), [(8, 1), (10, 1), (9, 2)]),
    ])
    def test_get_adjecent(self, filename, coord, expected):
        f = open(filename)
        burrow = day23.parse(f.read().splitlines())
        burrow[(9, 2)] = '.'
        self.assertEquals(day23.get_adjacent(burrow, coord), expected)

    @parameterized.expand([
        ('data/day23.txt', 8),
    ])
    def test_get_amphipods(self, filename, expected):
        f = open(filename)
        burrow = day23.parse(f.read().splitlines())
        self.assertEquals(len(day23.get_amphipods(burrow)), expected)

    @parameterized.expand([
        ('data/day23_room_a.txt', (4, 1), (5, 3), True),
        ('data/day23_room_b.txt', (4, 1), (5, 2), False),
        ('data/day23_room_c.txt', (9, 3), (9, 3), False),
    ])
    def test_room_is_free(self, filename, amphipod: Tuple[int, int],
                          move: Tuple[int, int], expected):
        f = open(filename)
        burrow = day23.parse(f.read().splitlines())
        room: List[Tuple[int,
                         int]] = day23.get_room_for_amphipod(burrow[amphipod])
        self.assertEquals(day23.is_correct_room(burrow, room, amphipod, move),
                          expected)

    @parameterized.expand([
        ('data/day23_done.txt', True),
        ('data/day23.txt', False),
    ])
    def test_done(self, filename, expected):
        f = open(filename)
        burrow = day23.parse(f.read().splitlines())
        self.assertEquals(day23.done(burrow), expected)


if __name__ == '__main__':
    unittest.main()
