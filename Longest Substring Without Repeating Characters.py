class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        for idx0, val0 in enumerate(s[:]):
            l = 0
            itemsPresent = dict()
            itemsPresent[str(val0)] = 1
            l += 1
            for idx1, val1 in enumerate(s[idx0+1:]):
                if str(val1) not in itemsPresent:
                    itemsPresent[str(val1)] = 1
                    l += 1
                else:
                    break
            if l > max_l:
                max_l = l
                
        return max_l
