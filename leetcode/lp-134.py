# 134. Gas Station
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
#
# Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
#
# Note:
#
# If there exists a solution, it is guaranteed to be unique.
# Both input arrays are non-empty and have the same length.
# Each element in the input arrays is a non-negative integer.
# Example 1:
#
# Input:
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_neg, max_neg, idx = 0, 0, -1
        for i in range(len(gas)):
            curr_neg += gas[i] - cost[i]
            if max_neg > curr_neg:
                max_neg = curr_neg
                idx = i

        return -1 if curr_neg < 0 else idx + 1
