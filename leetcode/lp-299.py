# 299. Bulls and Cows

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d,cow,bull ={},0,0
        for s in secret:
            d[s] = d.get(s,0)+1

        for i,g in enumerate(guess):
            if g in secret:
                if g == secret[i]:
                    bull+=1
                else:
                    cow+=1

                if d[g]<1:
                    cow-=1
                d[g]-=1

        return '{}A{}B'.format(bull,cow)
