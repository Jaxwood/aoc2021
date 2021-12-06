from typing import List

def part1(raw: str, days: int) -> int:
    nums = list(map(int, raw.split(',')))
    while days > 0:
        until = len(nums)
        for idx in range(0, until):
            n = nums[idx]
            if n == 0:
                nums[idx] = 6
                nums.append(8)
            else:
                nums[idx] = n - 1
        days -= 1

    return len(nums)
