class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount = {}
        tCount = {}

        for c in range(len(s)):
            sCount[s[c]] = 1 + sCount.get(s[c], 0)
            tCount[t[c]] = 1 + tCount.get(t[c], 0)
        
        return sCount == tCount