# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#
#
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_g = max_c = nums[0]
        for i in range(1,len(nums)):
            max_c = max(nums[i],max_c+nums[i])
            if max_g < max_c:
                max_g = max_c
        return max_g
        
