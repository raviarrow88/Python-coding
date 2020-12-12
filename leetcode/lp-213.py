# 213. House Robber II
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
#

class Solution:
    def rob(self, nums: List[int]) -> int:

        def  hb(nums):

            n = len(nums)

            if n == 0 : return 0
            if n == 1 : return nums[0]

            dp = [0]*n
            dp[0],dp[1] = nums[0],max(nums[0],nums[1])

            for i in range(2,n):
                dp[i] = max(dp[i-2]+nums[i],dp[i-1])

            return dp[n-1]

        n = len(nums)
        if n == 0 : return 0
        if n == 1 : return nums[0]

        return max(hb(nums[1:]),hb(nums[:-1]))
