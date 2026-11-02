import numpy as np

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = np.asarray(nums)
        return np.unique(arr).size != arr.size