class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        ans = 0
        
        if not len(s):
            return ans
        
        for item in s[::-1]:
            
            if item == ' ' and ans:
                return ans
            elif item != ' ':
                ans += 1
                
        return ans
