from typing import List, Tuple
from itertools import compress
import re


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


def check_within_region(cuboid: Cuboid) -> bool:
    """Check if a point is within the cubic region defined by the cuboid"""
    region = Cuboid('on', -50, 50, -50, 50, -50, 50)

    if ((region.x_max >= cuboid.x_min or region.x_min <= cuboid.x_max) and
        (region.y_max >= cuboid.y_min or region.y_min <= cuboid.y_max) and
        (region.z_max >= cuboid.z_min or region.z_min <= cuboid.z_max)):
        return True
    return False


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


def points_in_cubic(cuboid: Cuboid) -> List[Tuple[int, int, int]]:
    """Returns a list of all points in the cubic region defined by the cuboid"""
    result: List[Tuple[int, int, int]] = []
    for x in range(max(cuboid.x_min, -50), min(cuboid.x_max, 50) + 1):
        for y in range(max(cuboid.y_min, -50), min(cuboid.y_max, 50) + 1):
            for z in range(max(cuboid.z_min, -50), min(cuboid.z_max, 50) + 1):
                if check_within_region(cuboid):
                    result.append((x, y, z))
    return result


def part1(lines: List[str]) -> int:
    """Part 1"""
    cuboics = parse(lines)
    grid: Dict[Tuple[int, int, int], bool] = {}

    for cuboic in cuboics:
        for point in points_in_cubic(cuboic):
            if cuboic.toggle == 'on':
                grid[point] = True
            elif cuboic.toggle == 'off':
                grid[point] = False
            else:
                raise ValueError(f'Unknown toggle: {cuboic.toggle}')

    return list(grid.values()).count(True)