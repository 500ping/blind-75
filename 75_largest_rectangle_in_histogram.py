from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    res = 0
    stack = []

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, heigh = stack.pop()
            res = max(res, heigh * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        res = max(res, h * (len(heights) - i))
    
    return res

    # heights.append(0)
    # stack = [-1]
    # ans = 0
    # for i in range(len(heights)):
    #     while heights[i] < heights[stack[-1]]:
    #         h = heights[stack.pop()]
    #         w = i - stack[-1] - 1
    #         ans = max(ans, h * w)
    #     stack.append(i)
    # return ans



heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))