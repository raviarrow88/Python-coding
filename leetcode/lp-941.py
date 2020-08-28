# 941. Valid Mountain Array
# Given an array A of integers, return true if and only if it is a valid mountain array.
#
# Recall that A is a mountain array if and only if:
#
# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        flag1 = flag2 = False
        for i in range(len(A)-1):
            if A[i]==A[i+1]:
                return False
            elif A[i]<A[i+1]:
                if flag2==True:
                    return False
                flag1=True
            elif A[i]>A[i+1]:
                flag2=True

        return flag1 and flag2
