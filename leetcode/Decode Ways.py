class Solution:
    def numDecodings(self, s: str) -> int:
        
        ans = []
        n = len(s)
        
        if not n: return 0
        
        if not int(s[0]): return 0
        
        if n == 1: return 1
        
        for idx, val in enumerate(s):
            
            if not idx:
                ans.append(1)
                
            elif not int(val) and not int(s[idx - 1]):
                return 0
                
            elif (int(s[idx - 1: idx + 1]) <= 26) and int(s[max(0, idx - 1)]) and int(s[min(n-1, idx + 1)]) and int(val):
                
                if idx < 2:
                    ans.append(2)
                else:
                    ans.append(ans[-1] + ans[-2])
            
            else:
                ans.append(ans[-1])
                
        return ans[-1]
