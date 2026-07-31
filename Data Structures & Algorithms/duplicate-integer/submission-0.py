class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_counts = {}
        
        for n in nums:
            number_counts[n] = number_counts.get(n, 0) + 1

        for count in number_counts.values():
            if count > 1: return True
        
        return False