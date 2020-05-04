class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_dict = {}
        t_dict = {}
        
        for idx, value in enumerate(s):
            s_dict[value] = s_dict.get(value, []) + [idx]
        for idx, value in enumerate(t):
            t_dict[value] = t_dict.get(value, []) +[idx]
            
        if sorted(s_dict.values()) == sorted(t_dict.values()):
            return True
        else:
            return False
