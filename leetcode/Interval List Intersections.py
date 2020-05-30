class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        ans  = []
        
        for (x1, y1) in A:
            
            for (x2, y2) in B:
            
                if max(x1, x2) <= min(y1, y2):

                    ans.append((max(x1, x2), min(y1, y2)))
                
        return ans
