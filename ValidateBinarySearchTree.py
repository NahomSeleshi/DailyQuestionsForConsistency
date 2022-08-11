# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, leftRange, rightRange):
            if not node:
                return True
            if not (leftRange < node.val < rightRange):
                return False
            return dfs(node.left, leftRange, node.val) and dfs(node.right, node.val, rightRange)
        
        return dfs(root, -inf, inf)