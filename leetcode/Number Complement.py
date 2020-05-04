class Solution:
    def findComplement(self, num: int) -> int:
        complement = ''
        while num:
            val = (num % 2)
            if val:
               complement += '0'
            else:
                complement += '1'
            num //= 2
        return int(complement[::-1], 2)
    
