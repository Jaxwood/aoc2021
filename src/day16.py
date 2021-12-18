from enum import Enum
from functools import reduce
from typing import List, Tuple


class OperationType(Enum):
    """the types of operations"""
    SUM = 0
    PRODUCT = 1
    MIN = 2
    MAX = 3
    LITERAL = 4
    GREATER = 5
    LESS = 6
    EQUAL = 7


type_to_operation = dict([
    (0, OperationType.SUM),
    (1, OperationType.PRODUCT),
    (2, OperationType.MIN),
    (3, OperationType.MAX),
    (4, OperationType.LITERAL),
    (5, OperationType.GREATER),
    (6, OperationType.LESS),
    (7, OperationType.EQUAL),
])

hex_to_binary = dict([
    ("0", "0000"),
    ("1", "0001"),
    ("2", "0010"),
    ("3", "0011"),
    ("4", "0100"),
    ("5", "0101"),
    ("6", "0110"),
    ("7", "0111"),
    ("8", "1000"),
    ("9", "1001"),
    ("A", "1010"),
    ("B", "1011"),
    ("C", "1100"),
    ("D", "1101"),
    ("E", "1110"),
    ("F", "1111"),
])


def to_literal(binary: str) -> int:
    """get the literal value of the packet"""
    total = '0'
    for i in range(6, len(binary), 5):
        segment = binary[i:i + 5]
        if segment[0] == '1':
            total += segment[1:]
        else:
            total += segment[1:]
            return (int(total, 2), binary[i + 5:])

    return int(total, 2)


def evaluate(operations: List[Tuple[int, OperationType]]) -> int:
    """evaluate the operations"""
    print(operations)
    operands = []
    acc = 0
    while len(operations) > 0:
        val, type = operations.pop()
        if type == OperationType.LITERAL:
            operands.append(val)
        elif type == OperationType.SUM:
            result = reduce(lambda acc, x: x + acc, operands, 0)
            acc += result
            operations.append((result, OperationType.LITERAL))
            operands = []
        elif type == OperationType.PRODUCT:
            result = reduce(lambda acc, x: x * acc, operands, 1)
            acc += result
            operations.append((result, OperationType.LITERAL))
            operands = []
        elif type == OperationType.MIN:
            result = min(operands)
            acc += result
            operations.append((result, OperationType.LITERAL))
            operands = []
        elif type == OperationType.MAX:
            result = max(operands)
            acc += result
            operations.append((result, OperationType.LITERAL))
            operands = []
        elif type == OperationType.LESS:
            result = 1 if operands[1] < operands[0] else 0
            acc += result
            operations.append((result, OperationType.LITERAL))
            operands = []
        elif type == OperationType.GREATER:
            result = 1 if operands[1] > operands[0] else 0
            acc += result
            operations.append((result, OperationType.LITERAL))
            operands = []
        elif type == OperationType.EQUAL:
            result = 1 if operands[0] == operands[1] else 0
            acc += result
            operations.append((result, OperationType.LITERAL))
            operands = []
    return acc


def operator(expression: str) -> Tuple[int, List[Tuple[int, OperationType]]]:
    """get the operators of the expression"""
    queue = [expression]
    total = 0
    operations = []
    while len(queue) > 0:
        binary = queue.pop(0)
        if len(binary) <= 7:
            continue
        version = int(binary[0:3], 2)
        typeid = int(binary[3:6], 2)
        total += version

        if typeid == OperationType.LITERAL.value:
            val, rest = to_literal(binary)
            operations.append((val, type_to_operation[typeid]))
            queue.append(rest)
        else:
            length_type = binary[6]
            header_size = 7
            operations.append((0, type_to_operation[typeid]))
            if length_type == '0':
                bit_length = 15
                size = int(binary[header_size:header_size + bit_length], 2)
                queue.append(binary[header_size + bit_length:header_size +
                                    bit_length + size])
                queue.append(binary[header_size + bit_length + size:])
            if length_type == '1':
                bit_length = 11
                size = int(binary[header_size:header_size + bit_length], 2)
                offset = header_size + bit_length
                queue.append(binary[offset:])
    return (total, operations)


def to_binary(packet: str) -> str:
    """convert hex representation to binary"""
    return "".join(list(map(lambda x: hex_to_binary[x], packet)))


def part1(expression: str) -> int:
    """find the sum of the version numbers"""
    val, _ = operator(to_binary(expression))
    return val


def part2(expression: str) -> int:
    """evaulate the expression"""
    _, ops = operator(to_binary(expression))
    return evaluate(ops)