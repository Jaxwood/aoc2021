from functools import lru_cache
import string
from typing import Dict, List, Tuple
from collections import Counter


def parse(raw: List[str]) -> Tuple[Dict[str, Tuple[str, str]], List[str]]:
    """parse the input"""
    template = raw[0]
    rules = [rule.split(' ') for rule in raw[2:]]
    rules = {a: (a[0] + c, c + a[1]) for a, _, c in rules}
    pairs = [''.join(p) for p in zip(template, template[1:])]
    return (rules, pairs)


def part1(raw: List[str], steps: int) -> int:
    """substitute the input"""
    template = raw[0]
    rules, pairs = parse(raw)
    ctr = Counter(pairs)
    for _ in range(steps):
        newCtr = {key: 0 for key in rules.keys()}
        for key, value in ctr.items():
            newCtr[rules[key][0]] += value
            newCtr[rules[key][1]] += value
        ctr = newCtr

    letterTotals = {letter: 0 for letter in list(string.ascii_uppercase)}
    for key, value in ctr.items():
        letterTotals[key[0]] += value

    # the last character in the template gets another count
    letterTotals[template[-1]] += 1

    lmax = max(letterTotals.values())
    lmin = min([value for value in letterTotals.values() if value > 0])
    return lmax - lmin