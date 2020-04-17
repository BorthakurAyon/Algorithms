class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        
        self.all_word_squares = []
        self.prefixToWordMap = self.getprefixTowordmap(words)
        for word in words:
            n = len(word)
            self.genwordsquares(1, n, [word])
            
        return self.all_word_squares
    
    def genwordsquares(self, step, n, results):
        
        
        if step >= n: 
            # print(step, n , results)
            self.all_word_squares.append(results[:])
            return
        
        prefixforthisstep  = ''
        for i in range(len(results)):
            prefixforthisstep += results[i][step]
        # print(step, n, results, prefixforthisstep)
        if bool(self.prefixToWordMap.get(prefixforthisstep)):
            for item in self.prefixToWordMap[prefixforthisstep]:
                results.append(item)
                self.genwordsquares(step + 1, n, results)
                results.pop()
            
        else:
            return
        
        return
    
    def getprefixTowordmap(self, words):
        prefword = {}
        
        for word in words:
            for i in range(len(word)):
                prefword.setdefault(word[:i], set()).add(word)
        
        return prefword
