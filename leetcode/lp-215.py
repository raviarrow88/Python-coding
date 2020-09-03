# 215. Kth Largest Element in an Array
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.qs(nums,0,len(nums)-1,k)



    def partition(self,arr,l,h):
        pivot = arr[h]
        j = l-1
        for i in range(l,h):
            if arr[i]<pivot:
                j+=1
                arr[i],arr[j]=arr[j],arr[i]
        arr[j+1],arr[h] = arr[h],arr[j+1]

        return j+1

    def qs(self,nums,l,h,k):
        if l<h:
            p = self.partition(nums,l,h)
            if p > len(nums)-k:
                self.qs(nums,l,p-1,k)
            elif p < len(nums)-k :
                self.qs(nums,p+1,h,k)
            else:
                return nums[p]

        return nums[len(nums)-k]
