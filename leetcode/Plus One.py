class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0
        for idx, val in enumerate(digits[::-1]):
            if not idx:
                add = 1 
            else:
                add = 0 
            digits[n - idx - 1] += add + carry
            if digits[n - idx - 1] < 10:
                return digits
            else:
                carry = digits[n - idx - 1] // 10
                digits[n - idx - 1] %= 10
        if carry:
            return [carry] + digits
