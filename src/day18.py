from typing import List
from itertools import chain


def parse(raw: List[str]) -> List:
    """parse the input"""
    for line in raw:
        yield eval(line)


def can_split(candidate: List) -> bool:
    """check if the candidate can split"""
    flat_list = list()

    def flatten_list(list_of_lists):
        for item in list_of_lists:
            if type(item) == list:
                flatten_list(item)
            else:
                flat_list.append(item)

        return flat_list

    return any(map(lambda x: x >= 10, flatten_list(candidate)))


def split(candidate: List) -> List:
    """split the candidate"""
    return candidate


def can_explode(candidate: List, acc: int = 0) -> bool:
    """check if the candidate can explode"""
    queue = [(candidate, 0)]
    while len(queue) > 0:
        c, depth = queue.pop(0)
        if isinstance(c, list):
            for d in c:
                queue.append((d, depth + 1))
    return depth > 4


def explode(candidate: List) -> List:
    """explode the candidate"""
    return candidate


def magnitude(candidate: List) -> int:
    """find the magnitude of the candidate"""
    return 0


def part1(raw: List[str]) -> int:
    """find the magnitude of the final sum of snailfish"""
    numbers = list(parse(raw))
    total = []
    for num in numbers:
        total = total + [num]
        while can_explode(total):
            total = explode(total)
        while can_split(total):
            total = split(total)

    return 0