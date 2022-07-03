from collections import deque
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = [[]] + [[num] for num in nums]
    visited = set()

    q = deque()
    for num in nums:
        q.append([num])

    while q:
        curr = q.popleft()
        for num in nums:
            if num not in curr:
                subset = curr + [num]
                if tuple(sorted(subset)) not in visited:
                    res.append(subset)
                    q.append(subset)
                    visited.add(tuple(subset))

    return res


nums = [4,1,0]
print(subsets(nums))