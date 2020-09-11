# 152. Maximum Product Subarray
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example 1:
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0 or nums=='': return 0
        if len(nums)==1 : return nums[0]

        currentProd,maxProd = 1,0
        
        for i in range(0,len(nums)-1):
            currentProd = currentProd * nums[i]
            maxProd = max(maxProd,currentProd)
            if (currentProd==0) : currentProd=1

        currentProd=1
        for i in range(len(nums)-1,-1,-1):
            currentProd = currentProd * nums[i]
            maxProd = max(maxProd,currentProd)
            if (currentProd==0): currentProd =1


        return maxProd
