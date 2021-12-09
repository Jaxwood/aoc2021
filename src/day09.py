from typing import Dict, List, Tuple
from functools import reduce

def low_points(cave: Dict[Tuple[int, int], int], points: List[List[int]]) -> List[Tuple[int, int]]:
    """find all low points"""
    lows = []
    for x in range(0, len(points[0])):
        for y in range(0, len(points)):
            # check for adjacent points
            point = cave[(x, y)]
            valid = True

            if x > 0 and cave[(x-1, y)] <= point:
                valid = False
            
            if x < len(points[0]) - 1 and cave[(x+1,y)] <= point:
                valid = False
                
            if y > 0 and cave[(x, y-1)] <= point:
                valid = False
                
            if y < len(points) - 1 and cave[(x,y+1)] <= point:
                valid = False

            if valid == True:
                lows.append((x, y))
    return lows

def part1(lines: List[str]) -> int:
    """find the sum of the lowest points"""
    integers = list(map(lambda xs: list(map(int, xs)), lines))
    cave = dict()
    # map into dictionary
    for x in range(0, len(integers[0])):
        for y in range(0, len(integers)):
            cave[(x,y)] = integers[y][x]

    return reduce(lambda acc, x: acc + cave[x] + 1, low_points(cave, integers), 0)

def part2(lines: List[str]) -> int:
    """find the basin of the lowest points"""
    integers = list(map(lambda xs: list(map(int, xs)), lines))
    cave = dict()
    # map into dictionary
    for x in range(0, len(integers[0])):
        for y in range(0, len(integers)):
            cave[(x,y)] = integers[y][x]

    points = low_points(cave, integers)