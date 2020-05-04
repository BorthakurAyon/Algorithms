class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S, T = list(S), list(T)
        ns, nt = len(S), len(T)
        s, t = [], []
        
        for i in range(ns):
            
            if S[i] != '#':
                s.append(S[i])
            else:
                if len(s):
                    s.pop()
                    
        for i in range(nt):
                
            if T[i] != '#':
                t.append(T[i])
                
            else:
                if len(t):
                    t.pop()
                    
            
        return s == t
