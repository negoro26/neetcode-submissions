class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            sortedString = ''.join(sorted(s))

            if sortedString not in anagram_map:
                anagram_map[sortedString] = []
            
            anagram_map[sortedString].append(s)
        
        return list(anagram_map.values())