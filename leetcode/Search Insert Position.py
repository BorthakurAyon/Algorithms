class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        for idx, val in enumerate(nums):
            
            if val >= target: return idx
            
        return idx + 1
