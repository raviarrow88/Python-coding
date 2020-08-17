# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start  = 0
        end = len(nums)-1


        while start<=end:
            mid = (start+end)//2
            if (nums[start]==target and nums[end]==target):
                return [start,end]
            if  nums[mid] > target:
                end = mid-1
            elif nums[mid]<target:
                start = mid+1
            else:
                if nums[start]!=target:
                    start+=1
                if nums[end]!=target:
                    end-=1

        return [-1,-1]
