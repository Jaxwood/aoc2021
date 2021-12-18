from functools import reduce
from typing import Literal

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


def operator(seq: str) -> int:
    """get the operator of the packet"""
    queue = [seq]
    total = 0
    while len(queue) > 0:
        binary = queue.pop(0)
        if len(binary) <= 7:
            continue
        version = int(binary[0:3], 2)
        typeid = int(binary[3:6], 2)
        total += version

        if typeid == 4:
            val, rest = to_literal(binary)
            queue.append(rest)
        else:
            length_type = binary[6]
            header_size = 7
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
    return total


def to_binary(packet: str) -> str:
    """convert hex representation to binary"""
    return "".join(list(map(lambda x: hex_to_binary[x], packet)))


def part1(packet: str) -> int:
    """find the sum of the version numbers"""
    return operator(to_binary(packet))