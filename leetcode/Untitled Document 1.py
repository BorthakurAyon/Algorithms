class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        self.matrix = matrix
        self.longestpath = []
         
        m, n = len(matrix), len(matrix[0])
        self.visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.visited[i][j] = True
                self.dfs(i, j, m, n, [])
                
        return len(self.longestpath)
    
    def dfs(self, i, j, m, n, path):
        
        
        if len(path) and not path[-1] < self.matrix[i][j]:
            if len(self.longestpath) < len(path):
                self.longestpath = path
            return
        
        path.append(self.matrix[i][j])
        
        print(path)
        
        
        if i - 1 > -1 and not self.visited[i-1][j]:
            self.visited[i-1][j] = True
            self.dfs(i-1, j, m, n, path)
            self.visited[i-1][j] = False
            
        if i + 1 < n and not self.visited[i+1][j]:
            self.visited[i+1][j] = True
            self.dfs(i+1, j, m, n, path)
            self.visited[i+1][j] = False
            
        if j + 1 < n and not self.visited[i][j+1]:
            self.visited[i][j+1] = True
            self.dfs(i, j+1, m, n, path)
            self.visited[i][j+1] = False
            
        if j - 1 > -1 and not self.visited[i][j - 1]:
            self.visited[i][j-1] = True
            self.dfs(i, j-1, m, n, path)
            self.visited[i][j-1] = False
            
            
        return 
            
