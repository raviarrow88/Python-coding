# 57. Insert Interval
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
#
#
# Example 1:
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# Example 3:
#
# Input: intervals = [], newInterval = [5,7]
# Output: [[5,7]]

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i,n = 0,len(intervals)

        while i < n and intervals[i][1]< newInterval[0]:
            result.append(intervals[i])
            i+=1

        m = newInterval

        while i < n and intervals[i][0] <= newInterval[1]:
            m[0] = min(intervals[i][0],m[0])
            m[1] = max(intervals[i][1],m[1])

            i+=1

        result.append(m)

        while i < n :
            result.append(intervals[i])
            i+=1


        return result
