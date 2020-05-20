'''
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ans = []
        
        p_map = defaultdict(int)
        for item in p:
            p_map[item] += 1
            
        n, m = len(s), len(p)
        idx, cnt = 0, 0
        cnt_map = defaultdict(int)
        
        while idx < n:

            if p_map[s[idx]]:
                cnt_map[s[idx]] += 1
                cnt += 1
                
            if cnt_map == p_map:
                ans.append(idx - m + 1)
                cnt_map = defaultdict(int)
                cnt = 0
            elif cnt >= m:
                cnt = 1
                cnt_map = defaultdict(int)
                cnt_map[s[idx]] += 1

            idx += 1
            
            print(cnt, cnt_map)
                   
                
        return ans
'''
    
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        d1 = Counter(p)
        n, m = len(s), len(p)
        d2 = Counter(s[:m-1])
        
        for start in range(n - m + 1):
            end = start + m - 1
            d2[s[end]] = d2.get(s[end], 0) + 1
            if d1 == d2:
                res.append(start)
                
            d2[s[start]] -= 1
            if not d2[s[start]]:
                del d2[s[start]]
                
        return res
        
        
                
