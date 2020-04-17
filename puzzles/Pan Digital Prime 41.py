"""
Project Euler 41
"""
from itertools import permutations
from functools import reduce

class Pandigital(object):
    
    def __init__(self):
        self.getprime()
    
    def getprime(self):
        
        for p in permutations(range(7, 0, -1)):
            n = reduce(lambda b, a : 10 * b + a, p)
            if self.isprime(n):
                print(n)
                break
            
    def isprime(self, n):
        
        if not n % 2 or not n % 3:
            return False
        for i in range(5, int(0.5 * n) +1, 6):
            if not n % i or not n % (i + 2):
                return False
                
        return True
            

if __name__ == '__main__':
    
    ins = Pandigital()
