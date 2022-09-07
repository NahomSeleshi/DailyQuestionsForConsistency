# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.answer = []
        def dfs(node):
            if not node:
                return 
            self.answer.append("(")
            self.answer.append(str(node.val))
            if node.left: dfs(node.left)
            if node.right:
                if not node.left: self.answer.append("()")
                dfs(node.right)
            self.answer.append(")")
        dfs(root)
        return "".join(self.answer[1:len(self.answer)-1])