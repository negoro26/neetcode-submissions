class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        dic1, dic2 = {}, {}

        for c in range(len(s)):
            dic1[s[c]] = 1 + dic1.get(s[c], 0)
            dic2[t[c]] = 1 + dic2.get(t[c], 0)

        return dic1 == dic2
        