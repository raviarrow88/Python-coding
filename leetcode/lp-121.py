121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit ,curr_profit=0,0
        n = len(prices)-1
        for i in range(n):
            curr_profit =max(prices[i+1:])- prices[i]

            if curr_profit > max_profit:
                max_profit = curr_profit

        return max_profit
