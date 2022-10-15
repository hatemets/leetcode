# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

from typing import List
from timeit import default_timer as timer

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max: int = 0
        low = prices[0]

        for i, price in enumerate(prices):
            if low > price:
                profit = prices[i - 1] - low
                if i > 0 and profit > max:
                    max = profit
                low = price
            else:
                profit = price - low
                if profit > max:
                    max = profit
        return max

sol = Solution()
print(sol.maxProfit([2,7,3,0,5,9]))
