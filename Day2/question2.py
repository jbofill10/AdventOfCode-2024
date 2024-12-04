from typing import List


def is_increasing(nums: List[int]) -> int:
    for idx in range(len(nums) - 1):
        if nums[idx + 1] <= nums[idx] or not safe_differ(nums[idx], nums[idx + 1]):
            return 0
    return 1


def is_decreasing(nums: List[int]) -> int:
    for idx in range(len(nums) - 1):
        if nums[idx + 1] >= nums[idx] or not safe_differ(nums[idx], nums[idx + 1]):
            return 0
    return 1


def safe_differ(num1, num2) -> bool:
    return abs(num1 - num2) >= 1 and abs(num1 - num2) <= 3


def is_safe_by_removing_one(nums: List[int]) -> int:
    for i in range(len(nums)):
        new_list = nums[:i] + nums[i + 1 :]
        if is_increasing(new_list) or is_decreasing(new_list):
            return 1
    return 0


with open("input.txt", "r") as f:
    total_safe = 0
    for level in f.readlines():
        level_as_int: List[int] = [int(val) for val in level.split()]

        if is_increasing(level_as_int) or is_decreasing(level_as_int):
            total_safe += 1
        else:
            if is_safe_by_removing_one(level_as_int):
                total_safe += 1

    print(total_safe)
