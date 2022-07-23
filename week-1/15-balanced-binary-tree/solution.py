# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        right_height = self.node_height(root.right, 1)
        left_height = self.node_height(root.left, 1)
        if abs(right_height - left_height) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
     
    def node_height(self, root, level):
        if root == None:
            return level
        
        return max(self.node_height(root.left, level+1), self.node_height(root.right, level+1))