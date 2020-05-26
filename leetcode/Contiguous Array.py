class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        counter = {}
        counter[0] = -1
        
        n = len(nums)
        
        count = 0
        max_count = 0
        
        for i in range(n):
            
            if nums[i]:
                count += 1
            else:
                count -= 1
                
            if count in counter:
                max_count = max(max_count, i - counter[count])
            else:
                counter[count] = i
        
        
        return max_count
        
        
