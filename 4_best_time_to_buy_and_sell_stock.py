def maxProfit(prices):
    max_profit = 0
    min_price = prices[0]
    for price in prices:
        # if is better than min() and max()
        if price < min_price:
            min_price = price
        if price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


prices = [7,1,5,3,6,4]