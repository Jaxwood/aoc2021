from typing import Dict, List, Tuple


def parse(raw: List[str]) -> Dict[Tuple[int, int], str]:
    """parse the raw strings into a dictionary"""
    seafloor: Dict[Tuple[int, int], str] = dict()
    for line in range(len(raw)):
        for point in range(len(raw[line])):
            seafloor[(point, line)] = raw[line][point]
    return seafloor


def part1(lines: List[str]) -> int:
    """find the number of moves before the seacucumber stabilizes"""
    seafloor = parse(lines)
    return 0
