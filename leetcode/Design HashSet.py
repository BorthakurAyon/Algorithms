class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set_table = []
        

    def add(self, key: int) -> None:
        
        if not self.contains(key):
            self.set_table.append(key)

    def remove(self, key: int) -> None:
        try:
            self.set_table.remove(key)
        except:
            pass

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.set_table


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
