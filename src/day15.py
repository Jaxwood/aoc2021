from typing import Dict, List, Tuple
from queue import PriorityQueue


def neighbors(coord: Tuple[int, int]) -> List[Tuple[int, int]]:
    """find all neighbors of a coordinate"""
    x, y = coord
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def build_maze(raw: List[str], times: int) -> Dict[Tuple[int, int], int]:
    """build a maze from a raw input and extend it by times"""
    maze = dict()
    for time in range(0, times):
        for y in range(0, len(raw)):
            for x in range(0, len(raw[0])):
                maze[(x, y)] = int(raw[y][x])
    return maze


def part1(raw: List[str], times: int) -> int:
    """find path with lowest risk level"""
    maze = build_maze(raw, times)
    queue = PriorityQueue()
    queue.put((0, (0, 0)))
    target = (len(raw[0]) - 1, len(raw) - 1)
    visited = set()
    while not queue.empty():
        risk, next = queue.get()
        visited.add(next)
        if next == target:
            return risk
        for neighbor in neighbors(next):
            if neighbor in maze and neighbor not in visited:
                queue.put((risk + maze[neighbor], neighbor))

    return 0