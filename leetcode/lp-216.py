# 216. Combination Sum III
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Note:
#
# The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:
#
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []


        def get_combinations(start,n,temp):
            if len(temp)==k:
                if n == 0: result.append(temp[:])
                return

            for i in range(start,10):
                temp.append(i)

                get_combinations(i+1,n-i,temp)
                temp.pop()

        get_combinations(1,n,[])

        return result 
