from heapq import heapify
from typing import List


def maxProfit(prices: List[int]) -> int:
    res = 0
    min_price = prices[0]

    for i in range(1, len(prices)):
        res = max(res, prices[i] - min_price)
        min_price = min(min_price, prices[i])

    return res


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))
