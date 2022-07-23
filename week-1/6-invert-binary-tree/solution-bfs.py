# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return None
        
        queue = collections.deque([root])
        
        while queue:
            cur_node = queue.popleft()
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
            if cur_node.left:
                queue.append(cur_node.left)
            
            if cur_node.right:
                queue.append(cur_node.right)
        
        return root
        
        