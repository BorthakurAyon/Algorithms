from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        n = len(secret)
        sec_map = defaultdict(bool)
        guess_map = defaultdict(bool)
        cow_idx = []
        
        for i in range(n):
            sec_map[secret[i]] += 1
            guess_map[guess[i]] += 1
        
        for i in range(n):
            if secret[i] == guess[i]: 
                bulls += 1
                sec_map[secret[i]] -= 1
                guess_map[guess[i]] -= 1
            else:
                cow_idx.append(i)
        
        for i in cow_idx:
            if sec_map[guess[i]] > 0:
                cows += 1
                sec_map[guess[i]] -= 1
        
        return str(bulls) + 'A' + str(cows) + 'B'
