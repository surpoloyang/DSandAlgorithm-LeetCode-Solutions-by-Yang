# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy_head = ListNode(-1)
        dummy_head.next = head
        sorted_list = head
        cur = head.next

        while cur:
            # 已排序区间尾元素小于cur，所以cur右移一位，sorted_list也向右拓展一个
            if sorted_list.val <= cur.val:
                sorted_list = sorted_list.next
            else:
                pre = dummy_head
                # 找到pre.val <= cur.val & pre.next.val > cur.val
                while pre.next.val <= cur.val:
                    pre = pre.next
                # 将cur插入到pre和pre.next之间
                sorted_list.next = cur.next
                cur.next = pre.next
                pre.next = cur
            cur = sorted_list.next

        return dummy_head.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.insertionSort(head)