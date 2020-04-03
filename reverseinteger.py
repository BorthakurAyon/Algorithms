class Solution:
    def reverse(self, x: int) -> int:
        new_num = 0
        sign_new_num = x/max(abs(x), 1)
        x = abs(x)
        while x:
            new_num *= 10
            new_num += (x % 10)
            x //= 10
        
        if -2**31 <= new_num <= 2**31 - 1:
            return int(sign_new_num * new_num)
        else: return 0
