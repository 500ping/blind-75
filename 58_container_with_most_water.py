from typing import List


def maxArea(height: List[int]) -> int:
    result = 0
    start = 0
    end = len(height) - 1

    while start < end:
        if height[start] > height[end]:
            min_height = height[end]
            end -= 1
        else:
            min_height = height[start] 
            start += 1
        water_volume = min_height * (end - start + 1)
        result = water_volume if water_volume > result else result

    return result



height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))