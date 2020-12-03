# 844. Backspace String Compare
# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def helper(string ,index_of_string):
            num =0
            while index_of_string >= 0:
                if string[index_of_string] == '#':
                    # print "e"
                    num ,index_of_string = num +1 ,index_of_string -1
                elif num >0:
                    num, index_of_string = num - 1, index_of_string - 1
                else:
                    return index_of_string
                # print index_of_string
            return index_of_string

        i, j = len(S) - 1, len(T) - 1
        while i >= 0 or j >= 0:
            # print "(s,i)",s,i
            # print "(t,j)",t,j
            i, j = helper(S, i), helper(T, j)


            if i < 0 and j >= 0 or i >= 0 and j < 0:
                return False
            if S[i] != T[j]:
                return False
            i, j = i - 1, j - 1


        return True
