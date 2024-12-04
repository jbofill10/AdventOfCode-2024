from typing import List


def is_increasing(nums: List[int]) -> int:
    for idx in range(len(nums) - 1):
        if (
            not nums[idx + 1] > nums[idx]
            or not nums[0] < nums[idx + 1]
            or not safe_differ(nums[idx], nums[idx + 1])
        ):
            return 0

    return 1


def is_decreasing(nums: List[int]) -> None:
    for idx in range(len(nums) - 1):
        if (
            not nums[idx + 1] < nums[idx]
            or not nums[0] > nums[idx + 1]
            or not safe_differ(nums[idx], nums[idx + 1])
        ):
            return 0

    return 1


def safe_differ(num1, num2) -> bool:
    return abs(num1 - num2) >= 1 and abs(num1 - num2) <= 3


with open("input.txt", "r") as f:
    total_safe = 0
    for level in f.readlines():
        level_as_int: List[int] = [int(val) for val in level.split()]
        if level_as_int[0] > level_as_int[1]:
            total_safe += is_decreasing(level_as_int)
        elif level_as_int[0] < level_as_int[1]:
            total_safe += is_increasing(level_as_int)
        print(total_safe)
    print(total_safe)
