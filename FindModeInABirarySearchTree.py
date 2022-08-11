# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        answer = []
        def dfs(node):
            if not node: return
            counter[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        maxFreq = max(counter.values())
        for each in counter:
            if counter[each] == maxFreq:
                answer.append(each)
        return answer
        