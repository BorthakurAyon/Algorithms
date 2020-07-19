class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        
        n = len(digits)
        val = 0
        while n:
            val = digits[n-1] + 1
            if val < 10:
                digits[n-1] += 1
                return digits
            else:
                digits[n-1] = val % 10
                n -= 1
            
        digits.insert(0, 1)
        return digits
