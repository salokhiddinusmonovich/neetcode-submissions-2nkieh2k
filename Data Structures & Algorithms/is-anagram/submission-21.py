class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        coutnT, countS = {},{}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            coutnT[t[i]] = 1 + coutnT.get(t[i],0)
        return coutnT == countS
            