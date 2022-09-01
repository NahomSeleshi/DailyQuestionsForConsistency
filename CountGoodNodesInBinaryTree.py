# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 1
        def dfs(curMax, node):
            if not node:
                return 
            if node.val >= curMax:
                self.goodNodes += 1
            curMax = max(curMax, node.val)
            dfs(curMax, node.left)
            dfs(curMax, node.right)
        dfs(root.val, root.left)
        dfs(root.val, root.right)
        return self.goodNodes