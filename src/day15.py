from typing import Dict, List, Tuple
from queue import PriorityQueue
from heapq import heappush, heappop


def neighbors(coord: Tuple[int, int]) -> List[Tuple[int, int]]:
    """find all neighbors of a coordinate"""
    x, y = coord
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def build_maze(raw: List[str], times: int) -> Dict[Tuple[int, int], int]:
    """build a maze from a raw input and extend it by times"""
    maze = dict()
    size = len(raw)

    for y in range(0, times * len(raw)):
        for x in range(0, times * len(raw[0])):
            val = int(raw[y % size][x % size]) + (x // size) + (y // size)
            maze[(x, y)] = val if val < 10 else val - 9
    return maze


def draw(maze: Dict[Tuple[int, int], int]) -> None:
    """draw the maze"""
    for y in range(0, 50):
        line = ""
        for x in range(0, 50):
            line += str(maze[(x, y)])
        print(line)


def part1(raw: List[str], times: int) -> int:
    """find path with lowest risk level"""
    maze = build_maze(raw, times)
    queue = []
    heappush(queue, (0, (0, 0)))
    target = (times * len(raw[0]) - 1, times * len(raw) - 1)
    visited = set()
    while len(queue) > 0:
        risk, next = heappop(queue)
        if next in visited:
            continue
        visited.add(next)
        if next == target:
            return risk
        for neighbor in neighbors(next):
            if neighbor in maze and neighbor not in visited:
                heappush(queue, (risk + maze[neighbor], neighbor))

    return 0