class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        
        dist = []
        
        for idx, item in enumerate(ratings):
            dist.append(1)

            if idx and ratings[idx] > ratings[idx-1]:
                dist[idx]  = dist[idx - 1] + 1
            elif idx + 1 < n and ratings[idx] > ratings[idx+1]:
                dist[idx] += 1
                
        for idx in range(n-1, -1, -1):
                
            if idx and ratings[idx] < ratings[idx-1] and dist[idx] >= dist[idx-1]:
                dist[idx - 1] = dist[idx] + 1
                
        
        return sum(dist)
