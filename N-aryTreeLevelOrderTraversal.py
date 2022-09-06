"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        answer = []
        queue = deque([root])
        while queue:
            curLevelVal = []
            for i in range(len(queue)):
                temp = queue.popleft()
                curLevelVal.append(temp.val)
                for each in temp.children:
                    queue.append(each)
            answer.append(curLevelVal)
        return answer
            