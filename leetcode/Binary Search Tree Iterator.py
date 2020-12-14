from collections import deque  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        
        
        self.node_lifo = deque()
        
        while root is not None:
            self.node_lifo.append(root)
            root = root.left
        

    def next(self) -> int:
        
        # if len(self.node_lifo):
        
        current_node = self.node_lifo.pop()

        if current_node.right is not None:
            self.node_lifo.append(current_node.right)
            left_root = current_node.right.left
            while left_root is not None:
                self.node_lifo.append(left_root)
                left_root = left_root.left


        return current_node.val
        

    def hasNext(self) -> bool:
        
        if len(self.node_lifo):
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
