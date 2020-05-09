# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        self.dx, self.px = -1, None
        self.dy, self.py = -2, None
        
        def preorder(r, par, d):
            
            if not r: return 
            
            if r.val == x:
                self.dx, self.px = d, par
            if r.val == y:
                self.dy, self.py = d, par
            
            preorder(r.left, r, d+1)
            preorder(r.right, r, d+1)
            
        
        preorder(root, None, 0)
        return self.dx == self.dy and self.px != self.py
