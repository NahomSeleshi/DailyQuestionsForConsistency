# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        forward, backward = [], []
        while head:
            forward.append(str(head.val))
            head = head.next
        for i in range(len(forward)-1, -1, -1):
            backward.append(forward[i])
        forward, backward = "".join(forward), "".join(backward)
        return forward == backward