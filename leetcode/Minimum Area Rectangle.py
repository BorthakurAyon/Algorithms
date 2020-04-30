class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        S = set(map(tuple, points))
        ans = float('inf')
        
        for i, p1 in enumerate(points):
            for j in range(i):
                p2 = points[j]
                if (p1[0] != p2[0]) and (p1[1] != p2[1]) and (p1[0], p2[1]) in S and (p2[0], p1[1]) in S:
                    ans = min(ans, abs(p1[0]-p2[0]) * abs(p2[1]-p1[1]))
                    
        return ans if ans < float('inf') else 0
