# 290. Word Pattern
# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
#
#
#
# Example 1:
#
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:
#
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d =dict()

        words  = str.split(" ")

        if not len(words) == len(pattern):
            return False

        for i in range(len(words)):
            if pattern[i] not in d:
                if words[i] not in d.values():
                    d[pattern[i]]=words[i]

                else:
                    return False

            else:
                if not d[pattern[i]] == words[i]:
                    return False

        return True
