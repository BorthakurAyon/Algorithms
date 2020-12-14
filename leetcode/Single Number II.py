class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        nums = sorted(nums)
        
        rep_item = nums[0]
        ans.append(rep_item)
        
        for _item in nums[1:]:
            
            if _item != rep_item:
                
                ans.append(_item)
                rep_item = _item
                
            elif len(ans) and _item == ans[-1]:
                ans.pop(-1)
            
        return ans
