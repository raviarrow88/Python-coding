# 188. Best Time to Buy and Sell Stock IV
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
#
#
#
# Example 1:
#
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k >= len(prices)//2:
            return sum(i-j for i, j in zip(prices[1:], prices[:-1]) if i-j > 0)
        hold, release = [float('-inf')]*(k+1), [0]*(k+1)
        for p in prices:
            for i in range(1, k+1):
                release[i] = max(release[i], hold[i]+p)
                hold[i] = max(hold[i], release[i-1]-p)
        return release[k]
