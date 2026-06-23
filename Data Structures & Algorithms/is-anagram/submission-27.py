class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):return False 
        # hash table (array)
        h = [0] * 26
        for i in range(len(s)):
            h[ord(s[i]) - ord('a')] += 1
            h[ord(t[i]) - ord('a')] -= 1

        for val in h:
            if val != 0:
                return False 
        return True  
