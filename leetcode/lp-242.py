# 242. Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)

        if l1!=l2:
            return False

        s1 = sorted(s)
        t1 = sorted(t)

        for i in range(0,l1):
            if s1[i] != t1[i]:
                return False
        return True
