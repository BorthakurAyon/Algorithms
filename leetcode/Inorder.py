# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        
        output = []
        
        stack = collections.deque([])
        
        _left = root
        
        while _left is not None:
            
            stack.append(_left)
            _left = _left.left
            
            
        while len(stack):
            
            node = stack.pop()
            output.append(node.val)
            node = node.right
            while node is not None:
                stack.append(node)
                node = node.left
                
        return output
