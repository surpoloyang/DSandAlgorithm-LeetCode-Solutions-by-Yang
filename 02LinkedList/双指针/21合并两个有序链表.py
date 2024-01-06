# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newlist = ListNode()
        left_3 = newlist
        while  list1 and list2:
            if list1.val <= list2.val:
                left_3.next = list1
                list1 = list1.next
            else:
                left_3.next = list2
                list2 = list2.next
            left_3 = left_3.next
        left_3.next = list2 if not list1 else list1
        return newlist.next
                
                
            