from typing import List


def maxSubArray(nums: List[int]) -> int:
    # Kadane's Algorithm
    sum = 0
    max_sum = nums[0]

    for num in nums:
        sum += num
        max_sum = max(sum, max_sum)
        if sum < 0: sum = 0
    
    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))