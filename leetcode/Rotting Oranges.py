class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        self.ans = 0
        
        m, n = len(grid), len(grid[0])
        
        self.visited = [False for _ in range(n)] * m
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
