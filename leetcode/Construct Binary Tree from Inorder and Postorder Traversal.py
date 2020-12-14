# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        n = len(inorder)
        if n == 0:
            return None
        elif n == 1:
            return TreeNode(postorder[-1])
        else:
            root = TreeNode(postorder[-1])
            mid_inorder = inorder.index(postorder[-1])
            root.left = self.buildTree(inorder[:mid_inorder], postorder[:mid_inorder])
            root.right = self.buildTree(inorder[mid_inorder+1:], postorder[mid_inorder:-1])
            return root
