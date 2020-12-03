# 58. Length of Last Word
# Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
#
# A word is a maximal substring consisting of non-space characters only.
#
#
#
# Example 1:
#
# Input: s = "Hello World"
# Output: 5
# Example 2:
#
# Input: s = " "
# Output: 0

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n,count = len(s),0

        while n > 0:
            n-=1
            if s[n]!=' ': count+=1
            elif count >0 : return count

        return count
