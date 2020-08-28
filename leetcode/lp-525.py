# 525. Contiguous Array
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dict = {}
        sub_array,count = 0,0

        for i in range(len(nums)):
            if nums[i]==0:
                count -=1
            else:
                count +=1

            if count == 0:
                sub_array = i + 1

            if count in dict:
                sub_array = max(sub_array,i-dict[count])

            else:
                dict[count] = i

        return sub_array
        
