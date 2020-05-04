"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    
    prev = []
      
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        q = []
        if n == 0: return 0
        if len(self.prev):
            item = ''
            for _ in range(min(n, len(self.prev))):
                item += self.prev.pop(0)
            
            q += item
        while len(q) < n:
            tmp = [""] * 4
            tmp.sort()
            count = read4(tmp)
            if count:
                q += tmp[0:n]
                self.prev += tmp[n:count]
            else:
                break
        length = min(n, len(q))
        buf[0:length] = q[0:length]
        del q
        return length
                     
            
        
