# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if root:
            BFSTraversal = deque([root]) 
        else: 
            return []
        while BFSTraversal:
            size = len(BFSTraversal)
            currentMaximum = BFSTraversal[0].val
            for value in range(size):
                node = BFSTraversal.popleft()
                if node.val > currentMaximum:
                    currentMaximum = node.val
                if node.left:
                    BFSTraversal.append(node.left)
                if node.right:
                    BFSTraversal.append(node.right)
            answer.append(currentMaximum)
        return answer
            
        
