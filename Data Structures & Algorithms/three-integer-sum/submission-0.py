class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, fixed in enumerate(nums):
            if fixed > 0:
                break
            
            if i > 0 and fixed == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                target = fixed + nums[l] + nums[r]
                
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    res.append([fixed, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums [l - 1] and l < r:
                        l += 1
        
        return res