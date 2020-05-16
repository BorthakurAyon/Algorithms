class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        n = len(nums)
        for idx, val in enumerate(nums):
            if not idx and nums[idx] !=0:
                return 0
            elif idx + 1 < n:
                if nums[idx + 1] - nums[idx] != 1:
                    return nums[idx] + 1
                
                
        return nums[idx] + 1
