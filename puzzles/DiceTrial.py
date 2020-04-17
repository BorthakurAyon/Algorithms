import random

class Dicetrial(object):
            
    def simulation(self, n):
    
        self.count = 0
        
        for _ in range(n):
            
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            
            score = dice1 + dice2
            
            if score % 2 == 0 or score > 7:
                self.count += 1 
            
        print(self.count/n)
        

if __name__ == '__main__':
    
    ins = Dicetrial()
    ins.simulation(10000)
        
        
        
