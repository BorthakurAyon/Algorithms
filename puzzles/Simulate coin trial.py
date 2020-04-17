"""
https://www.dataquest.io/blog/basic-statistics-in-python-probability/
"""
import random

class Cointrial(object):
        
    def count_heads(self):
        
        if random.random() <= 0.5:
            self.num_heads += 1
            
    def simulation(self, n):
    
        self.num_heads = 0
        self.num_trails = 0
        
        for _ in range(n):
            
            self.num_trails += 1
            self.count_heads()
            
        print(self.num_heads/self.num_trails)
        

if __name__ == '__main__':
    
    ins = Cointrial()
    ins.simulation(400)
