class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        k = 0
        for n in seen:
            length = 1
            while (n + length) in seen:
                length += 1
            k = max(length, k)
        return k
