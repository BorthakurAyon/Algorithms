from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = -1
        item_map = defaultdict(int)
        for item in s:
            item_map[item] += 1
        for idx, item in enumerate(s):
            if item_map[item] == 1:
                ans = idx
                return ans
            
        return ans
