class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        angle_hourhand_12 = hour * (360/12) + (minutes/60) * (360/12)
         
        angle_minutehand_12 = minutes * (360/60)
        
        return min(360 - abs(angle_hourhand_12 - angle_minutehand_12), abs(angle_hourhand_12 - angle_minutehand_12))
