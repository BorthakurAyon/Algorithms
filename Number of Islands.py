class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not len(grid):
            return 0
        
        m, n = len(grid), len(grid[0])
        self.visited = [[False for _ in range(n)] for _ in range(m)]
        self.nislands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not self.visited[i][j]:
                    self.dfs(i, j, grid, m, n)
                    self.nislands += 1
        return self.nislands
    
    def dfs(self, i, j, grid, m, n):
        
        
        if i >= m or j >= n or i < 0 or j < 0:
            return
        
        
        if self.visited[i][j]:
            return
        
        
        if grid[i][j] == '0':
            return
        
        else: 
        
            self.visited[i][j] = True
            r = self.dfs(i+1, j, grid, m, n)
            l = self.dfs(i-1, j, grid, m, n)     
            t = self.dfs(i, j-1, grid, m, n) 
            b = self.dfs(i, j+1, grid, m, n)
        
