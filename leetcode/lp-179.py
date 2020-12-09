# 179. Largest Number
# Given a list of non-negative integers nums, arrange them such that they form the largest number.
#
# Note: The result may be very large, so you need to return a string instead of an integers


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)

        if all(i==0 for i in nums):
            return str(0)



        for i in range(0,n):
            for j in range(i+1,n):
                ij = str(nums[i])+str(nums[j])
                ji = str(nums[j])+str(nums[i])



                if int(ji) > int(ij):
                        nums[i],nums[j] = nums[j],nums[i]

        return "".join([str(i) for i in nums])
