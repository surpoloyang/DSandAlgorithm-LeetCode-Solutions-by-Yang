class MyLinkedList:

    def __init__(self):
        self.head = None
    
    def getLength(self):
        cur = self.head
        _length = 0
        while cur:
            _length += 1
            cur = cur.next
        return _length

    def get(self, index: int) -> int:
        cur = self.head
        cnt = 0
        while cur:
            if cnt == index:
                # print(cur.val)
                return cur.val
            cnt += 1
            cur = cur.next
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node

    def addAtTail(self, val: int) -> None:
        if self.getLength() < 1:
            self.addAtHead(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        node = Node(val)
        cur.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.getLength():
            self.addAtTail(val)
            return
        cur = self.head
        add_idx = 0
        length = self.getLength()
        node = Node(val)
        while cur and add_idx < index - 1:
            add_idx += 1
            cur = cur.next

        if cur and cur.next:
            node.next = cur.next
            cur.next = node
        elif cur and not cur.next:
            cur.next = node



    def deleteAtIndex(self, index: int) -> None:
        del_idx = 0
        cur = self.head
        length = self.getLength()
        if 0 < index < length - 1:
            while cur.next and del_idx < index - 1:
                del_idx += 1
                cur = cur.next
            cur.next = cur.next.next
        elif index == 0:
            self.head = cur.next
        elif index == length - 1:
            while cur.next.next:
                cur = cur.next
            cur.next = None

        


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
