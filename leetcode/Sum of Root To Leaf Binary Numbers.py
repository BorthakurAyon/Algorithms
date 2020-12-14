import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        
        heap = collections.deque([(root, 0)]) 
        
        total = 0
        
        while len(heap):
            
            node, val = heap.pop()
            
            
            if node.val:
                val = (val << 1) | 1
            else:
                val = val << 1
            
            if node.left is None and node.right is None:
                
                total += val
                
                
            if node.left is not None:
                
                heap.append((node.left, val))
                
            if node.right is not None:
                
                heap.append((node.right, val))
                
                
        return total
            
