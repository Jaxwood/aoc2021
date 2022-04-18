from typing import List, Tuple, Callable
from itertools import compress
import re

Point = Tuple[int, int]

class Cuboid:
    """Represents a cuboid of a grid"""

    def __init__(self, toggle: str, x_min: int, x_max: int, 
                 y_min: int, y_max: int, z_min: int, z_max: int):
        self.toggle = toggle
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.z_min = z_min
        self.z_max = z_max

    def __repr__(self):
        """Returns a string representation of the cuboid"""
        return f'{self.toggle} x={self.x_min}..{self.x_max}, y={self.y_min}..{self.y_max}, z={self.z_min}..{self.z_max}'


def parse(lines: List[str]) -> List[Cuboid]:
    """Parse the input inmin a list of Cuboid objects"""
    result: List[Cuboid] = []
    for line in lines:
        [(toggle, x, xx, y, yy, z, zz)] = re.findall(
            '(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)',
            line)
        result.append(
            Cuboid(toggle, int(x), int(xx), int(y),
                   int(yy), int(z), int(zz)))
    return result


def points_in_cubic(cuboid: Cuboid, min_fn: Callable[[int, int], int], max_fn: Callable[[int, int], int]) -> List[Tuple[int, int, int]]:
    """Returns a list of all points in the cubic region defined by the cuboid"""
    result: List[Tuple[int, int, int]] = []
    for x in range(max_fn(cuboid.x_min), min_fn(cuboid.x_max)):
        for y in range(max_fn(cuboid.y_min), min_fn(cuboid.y_max)):
            for z in range(max_fn(cuboid.z_min), min_fn(cuboid.z_max)):
                result.append((x, y, z))
    return result


def part1(lines: List[str]) -> int:
    """Part 1"""
    cuboics = parse(lines)
    grid: Dict[Tuple[int, int, int], bool] = {}

    for cuboic in cuboics:
        for point in points_in_cubic(cuboic, lambda x: min(x, 50) + 1, lambda x: max(x, -50)):
            if cuboic.toggle == 'on':
                grid[point] = True
            elif cuboic.toggle == 'off':
                grid[point] = False
            else:
                raise ValueError(f'Unknown toggle: {cuboic.toggle}')

    return list(grid.values()).count(True)