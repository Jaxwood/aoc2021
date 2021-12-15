from typing import List, Tuple
from collections import deque


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
    current = deque(template)
    # do the substitution until we reach the target
    for _ in range(0, until):
        idx = 0
        until = len(current) - 1
        for _ in range(0, until):
            if current[idx] in rules:
                current[idx] = rules[current[idx]]
            segment = current[idx] + current[idx + 1]
            if len(segment) == 2 and segment in rules:
                current.insert(idx + 1, rules[segment])
                idx += 2

    # find most common and least common letter
    letters = {}
    for x in current:
        if x in letters:
            letters[x] += 1
        else:
            letters[x] = 1
    return max(letters.values()) - min(letters.values())
