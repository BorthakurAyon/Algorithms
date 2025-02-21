class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
    
        n = len(nums)
        ans = nums[n-1]
        
        if n == 1: return nums[0]
        
        for i in range(0, n-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        
        return ans
