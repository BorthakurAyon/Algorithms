from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        diag_distance = []
        dist_map = defaultdict(list)
        ans = []
        
        for idx, (x, y) in enumerate(points):
            diag_distance.append(x**2 + y**2)
            dist_map[diag_distance[idx]].append(idx)
            
        diag_distance = sorted(diag_distance)
        
        for i in range(K):
            
            while dist_map[diag_distance[i]]:
                
                idx  = dist_map[diag_distance[i]].pop()
            
                ans.append(points[idx])
            
            
        return ans
