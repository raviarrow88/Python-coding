#
# 763. Partition Labels
#
# A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
#
#
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        end_index  = [0]*26
        for i in range(len(S)):
            end_index[ord(S[i])-ord('a')]=i

        s,e= 0,0 #start,end
        result_arr = []
        for j in range(len(S)):
            e = max(e,end_index[ord(S[j])-ord('a')])
            if j==e:
                result_arr.append(e-s+1)
                s = e+1
        return result_arr
        
