class Solution:
    def validIPAddress(self, IP: str) -> str:
        
        if IP.count(".") == 3 and all(self.ipv4(s) for s in IP.split(".")):
            return "IPv4"
        elif IP.count(":") == 7 and all(self.ipv6(s) for s in IP.split(":")):
            return "IPv6"
        else:
            return "Neither"
    
    
    def ipv4(self, s):
        
        try:
            return str(int(s)) == s and 0 <= int(s) <= 255
        except:
            return False
        
             
    def ipv6(self, s):
        
        if len(s) > 4: return False
        
        try:
            return int(s, 16) >= 0 and s[0] != '-'
        except:
            return False
        
