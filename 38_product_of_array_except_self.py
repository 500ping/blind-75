from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n

    prod = 1
    for i in range(1, n):
        prod *= nums[i - 1]
        res[i] *= prod

    prod = 1
    for i in range(n-2, -1, -1):
        prod *= nums[i + 1]
        res[i] *= prod

    return res


nums = [2, 3, 4, 5]
print(productExceptSelf(nums))