class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        _items = ""
        for _s in s:
            
            if _s.isalnum():
                _items += _s.lower()
               
        return _items == _items[::-1]
