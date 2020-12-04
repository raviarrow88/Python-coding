# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        flatten_list = [temp for sublist in matrix for temp in sublist]

        start = 0
        end = len(flatten_list)-1

        while start <= end:
            middle = (start+end)//2

            if target == flatten_list[middle]: return True
            elif target > flatten_list[middle]: start = middle +1
            else: end = middle-1

        return False
