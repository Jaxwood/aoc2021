from typing import List, Tuple
from itertools import groupby


def parse(raw: List[str]) -> List[Tuple[str, str]]:
    """parse the input"""
    for idx in range(0, len(raw)):
        if idx < 2:
            continue
        yield tuple(raw[idx].split(" -> "))


def part1(raw: List[str], until: int) -> int:
    """substitute the input"""
    template = raw[0]
    rules = dict(parse(raw))
    current = template

    # do the substitution until we reach the target
    for _ in range(0, until):
        next = current[0]
        for idx in range(0, len(current)):
            segment = current[idx:idx + 2]
            if len(segment) == 2:
                if segment in rules:
                    next += rules[segment] + segment[1]
                else:
                    next += segment
        current = next

    # find most common and least common letter
    letters = {}
    for x in current:
        if x in letters:
            letters[x] += 1
        else:
            letters[x] = 1
    return max(letters.values()) - min(letters.values())