import enum
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    cache = {}

    for i, num in enumerate(nums):
        remain = target - num
        if remain in cache:
            return [cache[remain], i]
        cache[num] = i

    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))
