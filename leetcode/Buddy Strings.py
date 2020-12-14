class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if len(A) != len(B): return False
        if A == B:
            
            item_set = set()
            for idx, val in enumerate(A):
                if val in item_set:
                    return True
                else:
                    item_set.add(val)
        
        diff_cnt = 0
        
        for idx, val in enumerate(A):
            
            if val != B[idx] and not diff_cnt:
                
                x = B[idx]
                y = val
                diff_cnt += 1
                
            elif val != B[idx] and diff_cnt:
                
                diff_cnt += 1
                
                if not ((val == x) and (B[idx] == y)):
                    
                    return False
                
        if diff_cnt == 2:
            return True
