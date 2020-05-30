class Solution:
    def countBits(self, num: int) -> List[int]:
        
        ans = [0] * (num + 1)
        
        offset = 0
        
        for i in range(1, num + 1):
            
            
            if not i & (i - 1):
                ans[i] = 1
                offset = 0
            else:
                
                offset += 1
                ans[i] = 1 + ans[offset]
                
        return ans
