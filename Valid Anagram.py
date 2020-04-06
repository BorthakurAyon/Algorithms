from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = defaultdict(bool)
        s_cnt, t_cnt = 0, 0 
        for item in s:
            s_dict[item] += 1 
            s_cnt += 1
            
            
        for item in t:
            if not s_dict[item]:
                return False
            else:
                s_dict[item] -= 1
            t_cnt += 1
            
        if s_cnt == t_cnt:
            return True
