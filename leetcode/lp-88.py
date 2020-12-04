# 88. Merge Sorted Array
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j =0
        for i in range(0,m+n):
            if j == n:
                break
            else:
                if nums1[i]==0:
                    nums1[i] = nums2[j]
                    j+=1


        for j in range(m+n):
            min_ele = j
            for i in range(j+1,m+n):
                if nums1[min_ele] > nums1[i]:
                    min_ele = i
            nums1[min_ele],nums1[j] = nums1[j],nums1[min_ele]
