# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        slow, fast = head, head
        while cnt:
            fast = fast.next
            cnt -= 1
        while fast:
            slow, fast = slow.next, fast.next
        return slow
