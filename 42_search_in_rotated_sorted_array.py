from typing import List


def search(nums: List[int], target: int) -> int:
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[left]: # left rotated
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else: # right rotated
            if nums[mid] < target  <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))