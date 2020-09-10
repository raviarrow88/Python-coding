# Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.
#
# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.
#
# Return the latest 24-hour time in "HH:MM" format.  If no valid time can be made, return an empty string.
#
#  Example 1:
#
# Input: A = [1,2,3,4]
# Output: "23:41"
# Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.

from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        combs = sorted(list(permutations(A)),reverse=True)

        for c in combs:
            i,j,k,l = c

            hour = (i*10+j)

            mins = (k*10+l)

            if hour < 24 and mins < 59:
                return f"{i}{j}:{k}{l}"

        return ""
