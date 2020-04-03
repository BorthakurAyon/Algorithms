class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = []
        if not bool(strs): return ''
        elif len(strs) == 1: return ''.join(strs)

        for idx in range(len(strs[0])):
            val = strs[0][idx]
            for item_idx, item in enumerate(strs[1:]):
                if len(item) < idx + 1:
                    return ''.join(longest_prefix)
                elif item[idx] != val:
                    return ''.join(longest_prefix)
                elif item_idx == len(strs) - 2:
                    longest_prefix.append(val)
                    
        return ''.join(longest_prefix)
