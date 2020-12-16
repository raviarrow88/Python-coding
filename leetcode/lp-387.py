# 387. First Unique Character in a String
from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c= Counter(s)
        for i in range(len(s)):
            e =s[i]
            if c[e] == 1:
                return i
        return -1
