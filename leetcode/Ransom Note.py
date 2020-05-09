from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        mag_map = defaultdict(int)
        for item in magazine:
            mag_map[item] += 1
            
        for item in ransomNote:
            if mag_map[item]:
                mag_map[item] -= 1
            else:
                return False
        
        return True
