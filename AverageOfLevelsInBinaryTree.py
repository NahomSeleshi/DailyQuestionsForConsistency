# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([])
        queue.append(root)
        answer = []
        while queue:
            curElements = []
            for i in range(len(queue)):
                curElement = queue.popleft()
                curElements.append(curElement.val)
                if curElement.left:
                    queue.append(curElement.left)
                if curElement.right:
                    queue.append(curElement.right)
            answer.append(sum(curElements)/len(curElements))
        return answer