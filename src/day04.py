from typing import List, Set, Tuple
import numpy as np
import re
import functools
import queue

def parse(raw: List[str]) -> Tuple[List[int], List[List[List[int]]]]:
    """parse the raw input into numbers drawn and boards"""
    numbers = []
    boards = []
    board = []
    for num in range(0, len(raw)):
        line = raw[num]
        # first line
        if num == 0:
            numbers = list(map(int, line.split(",")))
            continue
        # second line
        if num == 1:
            continue
        # empty lines
        if line == "":
            boards.append(board)
            board = []
        else:
            chuncks = re.findall(r'\d+', line)
            board.append(list(map(int, chuncks)))
    boards.append(board)
    return (numbers, boards)

def transpose(nums: List[List[int]]) -> List[List[int]]:
    """transpose the lines"""
    return np.array(nums).transpose()

def logical_board(boards: List[List[List[int]]]) -> List[Set[int]]:
    """create a logical board where each row and column are
    represented as a set"""
    logical_board = []
    for board in boards:
        sets = []
        for row in board:
            sets.append(set(row))
        for column in transpose(board):
            sets.append(set(column))
        logical_board.append(sets)
    return logical_board

def play_rounds(numbers: List[int], boards: List[Set[int]]) -> Tuple[int, Set[int]]:
    """continue playing until a row or column is full"""
    for num in numbers:
        for board in boards:
            for row_column in board:
                row_column.discard(num)
                if len(row_column) == 0:
                    return (num, board)

def play_rounds_till_last_board(numbers: List[int], boards: List[Set[int]]) -> Tuple[int, Set[int]]:
    """continue playing until the last board is full"""
    done_boards = set()
    for num in numbers:
        for board_num in range(0, len(boards)):
            if board_num in done_boards:
                continue
            for row_column in boards[board_num]:
                row_column.discard(num)
                if len(row_column) == 0:
                    done_boards.add(board_num)
                    if len(done_boards) == len(boards):
                        return (num, boards[board_num])

def union_except(acc: Set[int], candidate: Set[int], num: int) -> Set[int]:
    """final number should be excluded"""
    candidate.discard(num)
    return acc.union(candidate)

def play(raw: List[str], till_done: bool = False) -> int:
    """play bingo!"""
    (numbers, raw_boards) = parse(raw)
    boards = logical_board(raw_boards)
    if till_done:
        (num, winner) = play_rounds_till_last_board(numbers, boards)
    else:
        (num, winner) = play_rounds(numbers, boards)
    unmarked = functools.reduce(lambda acc, next: union_except(acc, next, num), winner, set())
    return sum(unmarked) * num
