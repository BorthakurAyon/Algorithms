class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        
        ans = ''
        
        m, n = len(a), len(b)
        
        if m >= n:
            extra_chr = a[0:m-n]
        else:
            extra_chr = b[0:n-m]
        
        carry = 0
        
        for idx in range(min(m, n)):
            
            ans += str((int(a[-1-idx]) + int(b[-1-idx]) + carry) % 2)
            carry = (int(a[-1-idx]) + int(b[-1-idx]) + carry) // 2
            
        for idx in range(len(extra_chr)):
            
            ans += str((int(extra_chr[-1-idx]) + carry) % 2)
            carry = (int(extra_chr[-1-idx]) + carry) // 2
        if carry:
            ans += str(carry)
            
        return ans[::-1]
