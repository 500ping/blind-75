from bisect import bisect_left
from functools import lru_cache
from typing import List


def jobScheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    N = len(startTime)
    jobs = list(zip(startTime, endTime, profit))
    jobs.sort()
    startTime.sort()

    @lru_cache(None)
    def helper(i):
        if i == N:
            return 0
        j = bisect_left(startTime, jobs[i][1])
        one = jobs[i][2] + helper(j)
        two = helper(i + 1)
        return max(one, two)

    return helper(0)



startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]
print(jobScheduling(startTime, endTime, profit))
