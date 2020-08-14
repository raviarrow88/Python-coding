# 122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_sf,max_profit = 0,0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i]-prices[i-1]
        return max_profit

        
