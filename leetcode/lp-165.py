# 165. Compare Version Numbers
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1= version1.split('.')
        v2 = version2.split('.')

        v1_len = len(v1)
        v2_len = len(v2)

        for  i in range(max(v1_len,v2_len)):
            i1 = int(v1[i]) if i < v1_len else 0
            i2 = int (v2[i]) if i < v2_len else 0

            if i1 != i2:
                return 1 if i1>i2 else -1

        return 0
