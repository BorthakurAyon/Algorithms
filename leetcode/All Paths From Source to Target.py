class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        N = len(graph)
        self.ans = []
        if not len(graph[0]): return []
        
        self.full_path = []
        
        for _item in graph[0]:
            path = [0]
            self.visited = [0] * N
            path.append(_item)
            self.dfs(path, N, graph)
            
        return self.ans
    
    def dfs(self, path, N, graph):
        
        if path[-1] == N-1:
            self.full_path += path
            self.ans.append(self.full_path)
            self.full_path = []
        
        self.visited[path[-1]] = 1
        if len(graph[path[-1]]):
            for _item in graph[path[-1]]:
                if not self.visited[_item]:
                    path.append(_item)
                    self.dfs(path, N, graph)
                    
                    path.pop(-1)
                    
                    
        self.visited[path[-1]] = 0
        
        return
