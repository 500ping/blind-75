from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []
    for i, lap in enumerate(intervals):
        # case not overlapping
        if newInterval[1] < lap[0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > lap[1]:
            res.append(lap)
        
        # if overlap, merge the lap
        else:
            newInterval = [min(newInterval[0], lap[0]), max(newInterval[1], lap[1])]
    res.append(newInterval)
    return res

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval))
        