class Solution:
    def isHappy(self, n: int) -> bool:
        l = []
        while n!=1:
            n = sum(int(i)**2 for i in str(n) )
            if n in l:
                return False
            else:
                l.append(n)
        return True