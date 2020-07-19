# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
         
        if root == None:
            return []
        
        res = []            
        nodes = [root]
        while nodes:
            res.append([node.val for node in nodes])
            next_nodes = []
            for node in nodes:
                if node.left:
                	next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            nodes = next_nodes
        
        return res[::-1]
        
    '''
        
        self.traversal = []
        
        if not root: return []
        
        self.traverse(root)
        self.traversal.append([root.val])
        
        return self.traversal
    
    def traverse(self, root):
        
        if not root: return
        
        self.traverse(root.left)
        self.traverse(root.right)
        
        if root.left and root.right:
            self.traversal.append([root.left.val, root.right.val])
        elif root.left:
            self.traversal.append([root.left.val])
        elif root.right:
            self.traversal.append([root.right.val])
        
        
        return 
        
    '''
