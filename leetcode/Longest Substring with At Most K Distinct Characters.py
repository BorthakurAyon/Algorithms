from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        n = len(s)
        
        if not s or not k:
            return 0
        
        left, right = 0, 0
        
        max_len = 1
        
        item_map = {}
        
        while right < n:
            
            item_map[s[right]] = right
            right += 1
            
            if len(item_map) == k + 1:
                idx = min(item_map.values())
                del item_map[s[idx]]
                left = idx + 1
                
            max_len = max(max_len, right - left)

            
        return max_len
