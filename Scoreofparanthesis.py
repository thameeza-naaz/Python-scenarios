class Solution:
    def ScoreOfParnthss(self, S: str) -> int:
        stack = []
        output,mul = 0,0
        for i,p in enumerate(S):
            if p == "(":
                mul += 1
            elif p == ")":
                mul -= 1 
                if i>0 and S[i-1] == "(":
                    output += 2**mul
        return output               