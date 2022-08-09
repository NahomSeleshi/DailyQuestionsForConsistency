# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        def dfs(node, direction):
            if not node:
                return
            if not node.left and not node.right and direction == "L":
                self.answer += node.val
                return
            dfs(node.left, "L")
            dfs(node.right, "R")
        dfs(root.left,"L")
        dfs(root.right,"R")
        return self.answer