# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        def dfs(node, curSum, curList):
            curSum += node.val
            curList.append(node.val)
            if not node.left and not node.right:
                if curSum == targetSum:
                    answer.append(curList.copy())
            if node.left:
                dfs(node.left, curSum, curList)
            if node.right:
                dfs(node.right, curSum, curList)
            curSum -= node.val
            curList.pop()
        if root:
            dfs(root, 0, [])
        return answer