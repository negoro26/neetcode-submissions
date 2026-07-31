class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sTable = {}
        tTable = {}
        
        for char in s:
            if char not in sTable:
                sTable.setdefault(char, 1)
            sTable[char] = sTable.get(char) + 1

        for char in t:
            if char not in tTable:
                tTable.setdefault(char, 1)
            tTable[char] = tTable.get(char) + 1

        if sTable != tTable: return False

        return True

