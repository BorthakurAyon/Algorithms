lass Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        if not n: return 1
        
        x0 = x
        
        
        def pow(x):
            
            return x*x0
        
        for _ in range(abs(n) - 1):
            
            x = pow(x)
            
        if n > 0:
            return x
        else:
            return 1/x
        '''
        
        def pow(x, y):
            
            res = 1
            
            while y > 0:
                
                if y & 1: res *= x
                
                x *= x 
                y >>= 1
                
            return res
        
        return pow(x, n) if n > 0 else 1./pow(x, -n)
        
