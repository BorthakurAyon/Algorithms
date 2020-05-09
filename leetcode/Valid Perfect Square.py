class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        prev_ans, ans = -1, 0
        while prev_ans != ans:
            prev_ans = ans     
            ans = int(max(1, (left+right)/2))
            if ans ** 2 == num:
                return True
            elif ans ** 2 < num:
                left = ans
            elif ans ** 2 > num:
                right = ans    
        
        return False
            
