from typing import List


def trap(height: List[int]) -> int:
    res = 0
    l = 0
    r = len(height) - 1
    max_left = height[l]
    max_right = height[r]

    while l < r:
        if max_left <= max_right:
            l += 1
            max_left = max(max_left, height[l])
            res += max_left - height[l]
        else:
            r -= 1
            max_right = max(max_right, height[r])
            res += max_right - height[r]

    return res


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))