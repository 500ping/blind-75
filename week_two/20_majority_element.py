from turtle import clear
from typing import List


def majorityElement(nums: List[int]) -> int:
    unique_nums = set(nums)
    length = len(nums)
    for num in unique_nums:
        if nums.count(num) > (length / 2):
            return num
    return None


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majorityElement(nums))
