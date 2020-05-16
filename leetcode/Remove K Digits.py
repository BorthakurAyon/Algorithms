class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        
        if num == k:
            return '0'
        
        stack = []    
        for n in num:
            while stack and k and int(stack[-1]) > int(n):
                stack.pop()
                k -= 1
            stack.append(n)
        while k:
            stack.pop()
            k -= 1
        if not stack:
            return '0'
        return str(int("".join(stack)))

