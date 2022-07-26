# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findAncestors(node, ancestors, target, level):
            if not node: return False
            if node.val == target.val:
                ancestors.append([level, node.val])
                return True
            
            foundTargetLeft = findAncestors(node.left, ancestors, target, level + 1)
            if not foundTargetLeft:
                foundTargetRight = findAncestors(node.right, ancestors, target, level + 1)
            if foundTargetLeft or foundTargetRight:
                ancestors.append([level, node.val])
                return True
            return False
        pAncestors = []
        qAncestors = []
        findAncestors(root, pAncestors, p, 0)
        findAncestors(root, qAncestors, q, 0)
        
        pPointer, qPointer = 0,0
        while pAncestors[pPointer][1] != qAncestors[qPointer][1]:
            if pAncestors[pPointer][0] < qAncestors[qPointer][0]:
                qPointer += 1
            elif pAncestors[pPointer][0] > qAncestors[qPointer][0]:
                pPointer += 1
            else:
                if pAncestors[pPointer][1] != qAncestors[qPointer][1]:
                    pPointer += 1
                    qPointer += 1
        return TreeNode(pAncestors[pPointer][1])
                 
                 
