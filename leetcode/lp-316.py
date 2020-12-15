# 316. Remove Duplicate Letters
# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
#
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = {char: indx for indx, char in enumerate(s)}

        res = []

        for indx, char in enumerate(s):
            if char not in res:

                while res and indx < d[res[-1]] and char < res[-1]:
                    res.pop()

                res.append(char)

        return "".join(res)        
