# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p = head
        tail = None
        # Outer loop runs for the number of nodes in the linked list - 1
        while p.next:
            cur = head
            while cur and cur.next != tail:
                if cur.val > cur.next.val:
                    # Swap the values of the two nodes
                    cur.val, cur.next.val = cur.next.val, cur.val
                cur = cur.next
            # Move the tail pointer one step forward, the tail pointer and its right side are the sorted part of the linked list
            p = p.next
            tail = cur
            
        return head
