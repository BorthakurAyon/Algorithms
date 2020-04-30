class Solution:
    def nextClosestTime(self, time: str) -> str:
        time = list(time)
        time_list = []
        min_val = 10
        for item in time:
            if item != ':':
                time_list.append(item)
                if int(item) < min_val:
                    min_val = int(item)
        
        time_list = sorted(time_list)
                
            
        for item in time_list:
            if int(item) > int(time[-1]):
                time[-1] = item
                return ''.join(time)
        for item in time_list:
            if int(item) > int(time[-2]) and int(item) <= 5:
                time[-2] = item
                time[-1] = str(min_val)
                return ''.join(time)
        for item in time_list:
            if int(item) > int(time[1]):
                if int(time[0]) < 2:
                    time[1] = item
                    time[-2] = str(min_val)
                    time[-1] = str(min_val)
                    return ''.join(time)
                elif int(item) <= 3:
                    time[1] = item
                    time[-2] = str(min_val)
                    time[-1] = str(min_val)
                    return ''.join(time)
        for item in time_list:
            if int(item) > int(time[0]) and int(item) <= 2:
                    time[0] = item
                    time[1] = str(min_val)
                    time[-2] = str(min_val)
                    time[-1] = str(min_val)
                    return ''.join(time)
                
        return 2 * str(min_val) + ':' + 2 * str(min_val)
