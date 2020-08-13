class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        if n == 1: return 1
        
        row = 1
        
        while n > 0:
            
            n -= row
            row += 1
        
        
        if not n: return row - 1
        else: return row - 2
