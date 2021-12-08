from typing import List

num_to_segment_size = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}

num_to_segments = {
    0: ('a', 'b', 'c', 'e', 'f', 'g'),
    1: ('c', 'f'),
    2: ('a', 'c', 'd', 'e', 'g'),
    3: ('a', 'c', 'd', 'f', 'g'),
    4: ('b', 'c', 'd', 'f'),
    5: ('a', 'b', 'd', 'f', 'g'),
    6: ('a', 'b', 'd', 'e', 'f', 'g'),
    7: ('a', 'c', 'f'),
    8: ('a', 'b', 'c', 'd', 'e', 'f', 'g'),
    9: ('a', 'b', 'c', 'd', 'f', 'g'),
}

def part1(lines: List[str]) -> int:
    """find the amount of times digit 1, 4, 7 and 8 appear in the output"""
    counter = 0
    for line in lines:
        [digits_line, output_line] = line.split('|')
        digits = digits_line.strip().split(' ')
        outputs = output_line.strip().split(' ')
        for digit in outputs:
            size = len(digit)
            # only check for digits 1, 4, 7 and 8
            if size == 2 or size == 4 or size == 3 or size == 7:
                counter += 1
    return counter

def part2(lines: List[str]) -> int:
    """find the sum of all digits in the output"""
    total = 0
    digit_map = {}
    for line in lines:
        [digits_line, output_line] = line.split('|')
        digits = digits_line.strip().split(' ')
        outputs = output_line.strip().split(' ')
        for digit in digits:
            if len(digit) == 2:
                digit_map[1] = list(map(str, digit))
            if len(digit) == 4:
                digit_map[4] = list(map(str, digit))
            if len(digit) == 3:
                digit_map[7] = list(map(str, digit))
            if len(digit) == 7:
                digit_map[8] = list(map(str, digit))
        print(digit_map)
    return total