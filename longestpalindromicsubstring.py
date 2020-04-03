class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # DP approach
        '''
        n = len(s)
        if not n: return ''
        if n==1: return s
        pair_dict = {}
        for step in range(n):
            for alpha in range(n):
                distance = alpha + step
                if distance >= n: continue
                if distance - alpha >= 2:
                    pair_dict[(alpha, distance)] = pair_dict[(alpha + 1, distance - 1)] and s[alpha] == s[distance]
                else:
                    pair_dict[(alpha, distance)] = s[alpha] == s[distance]
                    
                    
        start, end = max([p for p in pair_dict if pair_dict[p]], key=lambda x:x[1]-x[0])
                    
        return s[start:end+1]
        '''
        
        # Mirror approach
        
        n = len(s)
        if not n: return ''
        if n==1: return s
        curr_pali = ''
        for i in range(n):
            k = i
            for j in [i, i + 1]:
                k = i
                l = j
                while k>= 0 and l<n:
                    
                    if s[k] != s[l]: break
                    k -= 1
                    l += 1
                tmp_pali = s[k+1:l]
                if len(tmp_pali) >len(curr_pali):
                    curr_pali = tmp_pali
                    
        return curr_pali
                
                
