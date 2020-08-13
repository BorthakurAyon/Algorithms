class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        self.perimeter = 0
        
        m, n = len(grid), len(grid[0])
        
        self.visited = [[False for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    self.dfs(grid, i, j, m , n)
                    return self.perimeter
        
        return 0
    
    def dfs(self, grid, i, j, m , n):
        
        
        
        if i > m - 1 or i < 0 or j > n - 1 or j < 0:
            self.perimeter += 1
            return
        
        if not grid[i][j]: 
            self.perimeter += 1
            return
        
        
        if self.visited[i][j]: return
    
        
        self.visited[i][j] = True
        
        
        self.dfs(grid, i + 1, j , m, n)
        self.dfs(grid, i - 1, j , m, n)
        self.dfs(grid, i, j + 1 , m, n)
        self.dfs(grid, i, j - 1, m, n)
        
            
        return 
            
