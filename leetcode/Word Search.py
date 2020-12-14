class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        m, n = len(board), len(board[0])
        
        self.visited = [[False for _ in range(n)] for _ in range(m)]
        
        l = len(word)
        
        for i in range(m):
            for j in range(n):
                
                if word[0] == board[i][j]:
                    
                    ans = self.dfs(board, i, j, m, n, word, l , 1)
                    
                    if ans:
                        return ans
                    
        return False
    
    def dfs(self, board, i, j, m, n, word, l , depth):
        
        
        if i > m - 1 or i < 0 or j > n - 1 or j < 0:
            return False
        
        if self.visited[i][j]:
            return False
        
        self.visited[i][j] = True
        
        if word[depth - 1] != board[i][j]:
            self.visited[i][j] = False
            return False
        
        
        if depth == l and word[depth - 1] == board[i][j]:
            return True
        
        
        if self.dfs(board, i + 1, j, m, n, word, l , depth + 1):
            return True
        elif self.dfs(board, i - 1, j, m, n, word, l , depth + 1):
            return True
        elif self.dfs(board, i, j - 1, m, n, word, l , depth + 1):
            return True
        elif self.dfs(board, i, j + 1, m, n, word, l , depth + 1):
            return True
        
        self.visited[i][j] = False
        
        return False
