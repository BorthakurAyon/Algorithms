class MyCalendarTwo:

    def __init__(self):
        self.calender = []
        self.overlap = []
        

    def book(self, start: int, end: int) -> bool:
        
        for i, j in self.overlap:
            if start < j and end > i:
                return False
        for i, j in self.calender:
            if start < j and end > i:
                self.overlap.append((max(start, i), min(end, j)))
        self.calender.append((start, end))
        return True
            
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
