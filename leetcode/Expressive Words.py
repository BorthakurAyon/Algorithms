from collections import defaultdict

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        s_dict = defaultdict(int)
        output = 0
        
        for item in S:
            s_dict[item] += 1
        for word in words:
            w_dict = defaultdict(int)
            str2match = ''
            for item in word:
                if s_dict[item]:
                    w_dict[item] += 1
                    
                else:
                    break
            for item in w_dict.keys():
                if s_dict[item]:
                    if s_dict[item] > w_dict[item] and s_dict[item] >= 3:
                        str2match += s_dict[item] * item
                    elif s_dict[item] == w_dict[item]:
                        str2match += w_dict[item] * item
                    
                else:
                    break 
            if str2match == S:
                output += 1
                
        return output
