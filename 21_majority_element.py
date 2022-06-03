from typing import List


def majorityElement(nums: List[int]) -> int:
    unique_nums = set(nums)
    length = len(nums)
    for num in unique_nums: 
        if nums.count(num) > (length / 2):
            return num
    return None


nums = [3,2,3]
print(majorityElement(nums))