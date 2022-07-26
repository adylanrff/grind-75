# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def iterate_tree(node, level):
            tree_map[level].append(node.val)
            max_level = level
            if node.left:
                max_level = max(max_level, iterate_tree(node.left, level+1))
            if node.right:
                max_level = max(max_level, iterate_tree(node.right, level+1))
            return max_level

        tree_map = defaultdict(list)

        if root is None:
            return []

        max_level = iterate_tree(root, 0)

        result = []
        for i in range(max_level+1):
            result.append(tree_map[i])

        return result
