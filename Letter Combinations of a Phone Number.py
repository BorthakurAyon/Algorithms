class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        self.letters = {}
        self.dig2letter = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        n = len(digits)
        if n:
            self.findletters(0, digits, [], n)
        return self.letters.keys()
    
    
    def findletters(self, step, digits, cur_letter, n):
        
        if len(cur_letter) == n:
            self.letters["".join(cur_letter)] = True
            
        if step > n - 1:
            return
        
        for alph in self.dig2letter[digits[step]]:
            cur_letter.append(alph)
            
            self.findletters(step + 1, digits, cur_letter, n) 
            cur_letter.pop()
        
        return
        
        
