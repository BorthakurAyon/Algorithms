    if not len(nums): return 0
        
        max_sum =  sub_sum = nums[0]
        
        
        for val in nums[1:]:
            
            
            sub_sum = max(val, val + sub_sum)
            if sub_sum > max_sum:
                max_sum = sub_sum
                
            
        return max_sum
