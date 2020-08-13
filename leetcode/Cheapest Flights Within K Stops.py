from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        
        ans = [float("inf")]
        graph = defaultdict(dict)
        for u, v ,e in flights:
            graph[u][v] = e
            
        visited = [0] * n
            
        self.dfs(graph, src, dst, K + 1, 0, visited, ans)
        
        return -1 if ans[0] == float("inf") else ans[0]
    

    def dfs(self, graph, src, dst, k, cost, visited, ans):
        
        if src == dst and ans[0] > cost:
            ans[0] = cost
            return 
        
        if k == 0: return 
        
        for v, e in graph[src].items():
            
            if visited[v]: continue
            if cost + e > ans[0]: continue
            visited[v] = 1
            self.dfs(graph, v, dst, k - 1, cost + e, visited, ans)
            visited[v] = 0
        
