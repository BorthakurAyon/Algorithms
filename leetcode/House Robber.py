class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob = 0
        no_rob = 0
        
        for item in nums:
            
            tmp = rob
            
            rob = item + no_rob
            
            no_rob = max(tmp, no_rob)
            
        return max(rob, no_rob)
