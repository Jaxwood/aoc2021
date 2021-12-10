from typing import Dict, List, Tuple

openings = set(['(', '<', '[', '{'])

def is_openings(char: str) -> bool:
    """check if tag is an open tag"""
    return char in openings

def matches_closing(char: str, last: str) -> bool:
    """check if closing tag matches previous found opening tag"""
    if last == '(' and char == ')':
        return True

    if last == '<' and char == '>':
        return True

    if last == '{' and char == '}':
        return True

    if last == '[' and char == ']':
        return True

    return False

def score(char: str) -> int:
    """score the syntax errors"""
    if char == ')':
        return 3
    if char == '}':
        return 1197
    if char == '>':
        return 25137
    if char == ']':
        return 57
    return 0

def part1(lines: List[str]) -> int:
    """find all syntax errors"""
    syntax_errors = []
    total = 0
    for line in lines:
        history = [line[0]]
        for idx in range(1, len(line)):
            char = line[idx]
            if is_openings(char):
                history.append(char)
            else:
                last = history.pop()
                if not matches_closing(char, last):
                    total += score(char)

    return total