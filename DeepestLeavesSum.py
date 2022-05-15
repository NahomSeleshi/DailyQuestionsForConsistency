# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepestLeavesSum = 0
        queue = deque([root])
        while queue:
            deepestLeavesSum = 0
            n = len(queue)
            for i in range(n):
                temp = queue.popleft()
                deepestLeavesSum += temp.val
                if temp.left: queue.append(temp.left)
                if temp.right: queue.append(temp.right)
        
        return deepestLeavesSum
        
        
