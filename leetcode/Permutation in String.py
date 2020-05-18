from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        ds1 = Counter(s1)
        n, m = len(s1), len(s2)
        ds2 = Counter(s2[0:n-1])
        
        for start in range(m - n + 1):
            end = start + n - 1
            ds2[s2[end]] = ds2.get(s2[end], 0) + 1
            if ds1 == ds2: return True
            
            ds2[s2[start]] -= 1
            if not ds2[s2[start]]:
                del ds2[s2[start]]
                
        return False
