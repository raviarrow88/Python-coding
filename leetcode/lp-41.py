# 41. First Missing Positive
# Given an unsorted integer array nums, find the smallest missing positive integer.
#
# Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?
#
#

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            position = nums[i]-1

            while 1 <= nums[i] <= n and nums[i] != nums[position]:
                nums[i],nums[position] = nums[position],nums[i]
                position = nums[i]-1

        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return n+1
