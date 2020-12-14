class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        if num == 1 or num == 4: return True
        
        while num >= 4:
            
            if num % 4: return False
            
            num //= 4
            
            if num == 4: return True
        
        return False
