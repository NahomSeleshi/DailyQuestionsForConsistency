# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Here, we are sure that the target value is in the cloned tree too because it is a copy of the original tree. 
# So, we are going to use a breadth first search algorithm to find the requested target. 
# We will initialize our queue with the root of the cloned tree and strart our traversal. 
# When we find it, we will return that node.

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = deque([cloned])
        while queue:
            n = len(queue)
            for i in range(n):
                temp = queue.popleft()
                if temp.val == target.val:
                    return temp
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                
