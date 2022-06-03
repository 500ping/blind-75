from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    unique_nums = set(nums)
    return len(unique_nums) < len(nums)