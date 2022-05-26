def twoSum(nums, target):
    h = {}
    for i in range(len(nums)):
        remaining = target - nums[i]
        if remaining in h:
            return [i, h[remaining]]
        h[nums[i]] = i
    return []


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

