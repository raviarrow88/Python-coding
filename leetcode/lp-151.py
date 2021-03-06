# 151. Reverse Words in a String
#
# Given an input string, reverse the string word by word.
#
#
#
# Example 1:
#
# Input: "the sky is blue"
# Output: "blue is sky the"
# Example 2:
#
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:
#
# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
#


class Solution:
    def reverseWords(self, s):
        l =len(s)

        if l<1:
            return s

        rev_str=''

        re = len(s)-1   #right end

        while re >=0:

            while re >= 0 and ' ' == s[re]:
                re-=1
            right = re

            while re >=0 and ' ' != s[re]:
                re-=1
            left = re+1

            word = s[left:right+1] if right >=0 else ""

            rev_str = rev_str + word + ' '

        return rev_str.rstrip()
