class Solution:
    def reverseWords(self, s: str) -> str:
        L=0
        rev_str = ''
        for i in range(len(s)):
            if s[i]==' ':
                rev_str += self.rv(s[L:i])+' '
                L = i+1
            elif i+1 == len(s):
                rev_str += self.rv(s[L:len(s)])
        return rev_str


    def rv(self,word):
        l=0
        r= len(word)-1
        word = list(word)
        while l<r:
            temp = word[l]
            word[l] = word[r]
            word[r] = temp
            l+=1
            r-=1
        return "".join(word)
