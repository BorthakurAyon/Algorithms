from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.G = defaultdict(dict)
        for s, e in zip(equations, values):
            self.G[s[0]][s[1]] = e
            self.G[s[1]][s[0]] = 1/e
            self.G[s[0]][s[0]] = 1
            self.G[s[1]][s[1]] = 1
              
        return [self.dfs(s[0], s[1], set()) for s in queries]
                
    def dfs(self, s, e, path):
        if s not in self.G or e not in self.G:
            return -1
        if e in self.G[s]:
            return self.G[s][e]
        
        for item in self.G[s]:
            if item not in path:
                path.add(item)
                val = self.dfs(item, e, path)
                if val != -1:
                    return val * self.G[s][item]
                path.remove(item)
        return -1        
