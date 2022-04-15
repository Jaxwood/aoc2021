from typing import List, Tuple


def parse(raw: List[str]) -> Tuple[str, List[str]]:
    """parse the input"""
    image: List[List[str]] = []
    for i in range(2, len(raw)):
        image.append(raw[i])
    return raw[0], image


def neighbor_coords(x: int, y: int) -> List[Tuple[int, int]]:
    """returns the coordinates of the neighbors of a given pixel"""
    return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x, y),
            (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]


def binary_neighbors(image: List[List[str]], x: int, y: int,
                     infinity_mark: str) -> int:
    """construct the binary number for a given pixel"""
    binary: str = ""
    for x_, y_ in neighbor_coords(x, y):
        if x_ < 0 or y_ < 0 or x_ >= len(image) or y_ >= len(image[0]):
            binary += '1' if infinity_mark == '#' else '0'
        else:
            binary += '1' if image[y_][x_] == '#' else '0'

    return int(binary, 2)


def infinity_mark(algo: str, iteration: int) -> str:
    """find the infinity mark"""
    start = algo[0]
    end = algo[-1]
    if start == '#' and end == '.':
        return '.' if iteration % 2 == 0 else '#'
    if start == '.' and end == '#':
        return '.'
    if start == '#' and end == '#':
        return '#'
    if start == '.' and end == '.':
        return '.'


def part1(raw: List[str], times: int = 2) -> int:
    """find the number of lit pixels"""
    algo, image = parse(raw)
    for iteration in range(times):
        output: List[str] = []
        mark = infinity_mark(algo, iteration)
        for y in range(-1, len(image[0]) + 1):
            line: str = ""
            for x in range(-1, len(image) + 1):
                line += algo[binary_neighbors(image, x, y, mark)]
            output.append(line)
        image = output

    return sum(1 for line in image for pixel in line if pixel == '#')