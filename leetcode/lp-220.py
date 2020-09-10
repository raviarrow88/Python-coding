# 220. Contains Duplicate III
# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        len_nums = len(nums)

        if t==0 and len(nums)==len(set(nums)):
            return False

        for index,val in enumerate(nums):
            for j in range(index+1,min(index+1+k,len_nums)):
                if abs(val-nums[j])<=t:
                    return True
        return False
