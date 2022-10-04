# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node, curSum):
            if not node.left and not node.right:
                if curSum + node.val == targetSum:
                    return True
            left, right = False, False       
            if node.left:
                left = dfs(node.left, curSum + node.val)
            if node.right:
                right = dfs(node.right, curSum + node.val)
            return left or right
        return dfs(root, 0)
