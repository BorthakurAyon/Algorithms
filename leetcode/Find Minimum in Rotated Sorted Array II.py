class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_val = nums[0]
        
        for _item in nums[1:]:
            
            if min_val > _item :
                return _item 
            
        return min_val
