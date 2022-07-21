# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        answer = []
        while head:
            answer.append(head.val)
            head = head.next
        left, right = left-1, right-1
                
        while left < right:
            answer[left], answer[right] = answer[right], answer[left]
            left += 1
            right -= 1
        temp = ListNode(0)
        final = temp
        for each in answer:
            temp1 = ListNode(each)
            temp.next = temp1
            temp = temp.next
        return final.next
