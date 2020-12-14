from collections import defaultdict
import math

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        
        ans = 0
        
        zero_time = []
        
        for idx, _val in enumerate(time):
            
            _val = _val % 60
            
            if not _val:
                zero_time.append(0)

            else:
                time[idx] = _val
                
        if len(zero_time) > 1:
            ans += math.comb(len(zero_time), 2)
            
        
        time = sorted(time)
    
        time_cnt = defaultdict(int)
        
        uniq_time = []
        
        for val in time:
            
            if val:
            
                time_cnt[val] += 1

                if (time_cnt[val] == 1) and (val != 30):
                    uniq_time.append(val)
        del time
        
        if time_cnt[30] > 1:
            ans += math.comb(time_cnt[30], 2)
        
        i = 0
        j = len(uniq_time) - 1
        
        while i < j:
            
            _sum = uniq_time[i] + uniq_time[j]
            
            if _sum == 60:
                ans += (1 * time_cnt[uniq_time[i]] * time_cnt[uniq_time[j]])
                i += 1
                j -= 1
            elif _sum > 60:
                j -= 1
            elif _sum < 60:            
                i += 1
        
        return ans
        
