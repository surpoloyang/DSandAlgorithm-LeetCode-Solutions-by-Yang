# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newHead = ListNode(0, head)
        fast, slow = head, newHead
        while n:
            fast = fast.next
            n -= 1
        while fast:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return newHead.next
            