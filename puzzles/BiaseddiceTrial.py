import random

class Dicetrial(object):
            
    def simulation(self, n):
    
        self.count = 0
        
        for _ in range(n):
            
            
            '''
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            '''
            # for biased use random.choice with curated list
            prob_list = []
            for i in range(1, 7):
                for _ in range(i):
                    prob_list.append(i)
            print(prob_list)
            dice1 = random.choice(prob_list)
            
            score = dice1
            
            if score % 6 == 0:
                self.count += 1 
            
        print(self.count/n)
        

if __name__ == '__main__':
    
    ins = Dicetrial()
    ins.simulation(10000)
        
        
        
