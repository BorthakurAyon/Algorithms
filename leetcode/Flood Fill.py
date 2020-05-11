class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        self.image = image
        
        m, n  = len(image), len(image[0])
        self.visited = [[False for _ in range(n)] for _ in range(m)]
        
        self.dfs(sr, sc, m, n, oldColor, newColor)
        
        return self.image
        
    def dfs(self, i, j, m, n, oldColor, newColor):
        
        if i > m - 1 or i < 0 or j > n - 1 or j < 0 or self.visited[i][j]:
            return
        
        if self.image[i][j] == oldColor:
            self.image[i][j] = newColor
        else:
            return
            
        self.visited[i][j] = True
            
        self.dfs(i  + 1, j, m, n, oldColor, newColor)
        self.dfs(i  - 1, j, m, n, oldColor, newColor)
        self.dfs(i, j - 1, m, n, oldColor, newColor)    
        self.dfs(i, j + 1, m, n, oldColor, newColor)    
