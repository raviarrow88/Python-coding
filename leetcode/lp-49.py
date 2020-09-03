# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))

            if key not in result:
                result[key] = [strs[i]]
            else:
                result[key].append(strs[i])

        return result.values()
