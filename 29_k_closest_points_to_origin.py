from math import sqrt
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    def sort_with_distance(point):
        return sqrt(point[0]**2 + point[1]**2)

    return sorted(points, key=sort_with_distance)[:k]


points = [[3,3],[5,-1],[-2,4]]
k = 2
print(kClosest(points, k))