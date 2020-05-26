class Solution:
    def __init__(self):
        
        self.ans = 0
        
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        m, n  = len(matrix), len(matrix[0])
        self.matrix = matrix
        
        
        for i in range(m):
            for j in range(n):
                if self.matrix[i][j]:
                    self.ans += 1
                    self.dfs(m, n, i, j, 1)
        
        
        return self.ans
    
    def dfs(self, m, n, i, j, spread):
        
        if i + spread >= m or j + spread >= n: return
        
        for idx in range(spread + 1):
            if not self.matrix[i + idx][j + spread]: return
            if idx < spread and not self.matrix[i + spread][j + idx]: return
        
        
        self.ans += 1
        
        
        self.dfs(m, n, i, j, spread+1)
        
        return
