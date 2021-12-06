from typing import List

def part1(raw: str, days: int) -> int:
    nums = map(int, raw.split(','))
    next = []
    while days > 0:
        for n in nums:
            if n == 0:
                next.append(6)
                next.append(8)
            else:
                next.append(n - 1)
        days -= 1
        nums = next
        next = []

    return len(nums)
