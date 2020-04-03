class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        len = n
        
        return self.finditems(len, n)
    
    def finditems(self, len, n):
        
        if n == 0: return ['']
        elif n == 1: return ['0', '1', '8']
        
        # [0, 1, 6, 8, 9]
        
        middles = self.finditems(len, n-2)
        results = []
        for middle in middles:
            results.append('1' + middle + '1')
            results.append('8' + middle + '8')
            results.append('6' + middle + '9')
            results.append('9' + middle + '6')
            if n < len:
                results.append('0' + middle + '0')
        
        return results
        
