# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        status = True
        version = int(n/2)
        left = 0
        right = n
        cnt = 0
        while cnt < n + 1: 
            status = isBadVersion(version)
            if not status:
                left = version
                version = left + int(max(1, (right - left)/2))
                
            elif status:
                right = version
                if version  - 1 >= 0 and not isBadVersion(version - 1):
                    return version
                version = int(max(1, (right + left)/2))
            cnt += 1
            
            if n == 1 and not status:
                return 1
            
            
