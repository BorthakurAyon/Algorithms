"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        pointer = head
        
        while pointer and not pointer.child:
            pointer = pointer.next
            
        if pointer:
            
            child_tail  = pointer.child
            while child_tail.next:
                child_tail = child_tail.next
                
            rest_head  = self.flatten(pointer.next)
            if rest_head:
                child_tail.next = rest_head
                rest_head.prev = child_tail
                
            child_head = self.flatten(pointer.child)
            pointer.next = child_head
            child_head.prev = pointer
            pointer.child = None
            
        return head
        
