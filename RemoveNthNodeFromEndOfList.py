# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLength = 1
        temp = head
        while temp.next != None:
            listLength += 1
            temp = temp.next
        if n == listLength:
            return head.next
        curNode = 1
        temp2 = head
        while curNode < listLength-n:
            curNode += 1
            temp2 = temp2.next
        temp2.next = temp2.next.next
        
        return head
        