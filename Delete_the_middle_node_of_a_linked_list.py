# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        slow, fast = head, head.next
        while fast:
            fast = fast.next
            if not fast or fast.next == None:
                slow.next = slow.next.next
                break
            else:
                slow = slow.next
            fast = fast.next
        return head