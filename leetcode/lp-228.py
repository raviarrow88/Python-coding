# 228. Summary Ranges
# You are given a sorted unique integer array nums.
#
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
#
# Each range [a,b] in the list should be output as:
#
# "a->b" if a != b
# "a" if a == b
#
#
# Example 1:
#
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
          return nums

        if len(nums)==1:
          return [str(nums[0])]

        start=end=i =0

        result = []
        while i < len(nums):
          if nums[i]+1 in  nums:
            end+=1
          else:
            if len(nums[start:end+1]) > 1:
              rn_str = str(nums[start])+"->"+str(nums[end])
            else:
              rn_str = str(nums[start])
            result.append(rn_str)
            start=i+1
            end=i+1

          i+=1

        return result
