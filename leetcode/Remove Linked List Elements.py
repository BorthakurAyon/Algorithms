# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        
        '''
        new_head = ListNode()
        
        while head:
            new_head.val = head.val
            new_head.next = head.next
            
            if val == head.next.val:
                
                head = head.next
                new_head.next = head.next
            
            head = head.next
        
        return new_head
        '''
        
        if not head:
            return head
        
        head.next = self.removeElements(head.next, val)
        return head if head.val != val else head.next
