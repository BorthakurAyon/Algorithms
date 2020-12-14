n = len(arr)
       
        if n < 3:
            return False
        
        if arr[1] - arr[0] <= 0:
            return False
        
        last = arr[0]
        i = 1
        
        while i < n and arr[i] > last:
            last = arr[i]
            i += 1
            
        if i == n or arr[i] == last:
            return False
        
        last = arr[i]
        i += 1
        
        while i < n and arr[i] < last:
            last = arr[i]
            i += 1
            
        if i == n:
            return True
        
        else:
            return False
