from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


obj = MedianFinder()
obj.addNum(6)
obj.addNum(10)
obj.addNum(2)
obj.addNum(6)
obj.addNum(5)
obj.addNum(0)
obj.addNum(6)
obj.addNum(3)
obj.addNum(1)
obj.addNum(0)
obj.addNum(0)
print(obj.findMedian())