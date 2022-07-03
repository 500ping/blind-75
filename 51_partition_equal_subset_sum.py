from typing import List


def canPartition(nums: List[int]) -> bool:
    all_sum = sum(nums)
    if all_sum % 2 != 0:
        return False

    dp = set()
    dp.add(0)
    target = all_sum // 2

    for i in range(len(nums)-1, -1, -1):
        next_dp = set()
        for t in dp:
            next_dp.add(t + nums[i])
            next_dp.add(t)
        dp = next_dp

    return target in dp


nums = [1,5,11,5]
print(canPartition(nums))