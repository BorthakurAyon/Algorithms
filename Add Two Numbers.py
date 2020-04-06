# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
            self.val = x
            self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        result = dummy
        carry = 0
        
        
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = val // 10, val % 10
            result.next = ListNode(val)
            result = result.next
            
        if carry == 1:
            result.next = ListNode(1)
            
        return dummy.next
        
