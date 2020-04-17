class TrieNode(object):
    
    def __init__(self):
        self.isend = False
        self.children = {}
        
class Trie(object):
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isend = True
        

class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        self.results = {}
        m, n  = len(board), len(board[0])
        self.visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.findwordsrec(board, trie.root, i, j, m, n, [])
        
        return self.results.keys()
    
    def findwordsrec(self, board, trie, i, j, m, n, cur_word):
        
        if i < 0 or i > m - 1 or j < 0 or j > n - 1 or self.visited[i][j]:
            return
        
        if board[i][j] not in trie.children:
            return
        
        cur_word.append(board[i][j])
        next_node = trie.children[board[i][j]]
        
        if next_node.isend:
            self.results["".join(cur_word)] = True
            
        self.visited[i][j] = True
        self.findwordsrec(board, next_node, i+1, j, m, n, cur_word)
        self.findwordsrec(board, next_node, i-1, j, m, n, cur_word)
        self.findwordsrec(board, next_node, i, j-1, m, n, cur_word)
        self.findwordsrec(board, next_node, i, j+1, m, n, cur_word)
        cur_word.pop()
        self.visited[i][j] = False
