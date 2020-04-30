from collections import defaultdict

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j_map = defaultdict(bool)
        stone_cnt = 0
        for item in J:
            j_map[item] = True
        for item in S:
            if j_map[item]:
                stone_cnt += 1
        
        return stone_cnt
        
