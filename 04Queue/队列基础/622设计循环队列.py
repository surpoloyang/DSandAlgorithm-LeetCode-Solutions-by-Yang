class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k + 1
        self.queue = [None for _ in range(self.size)]
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[(self.front + 1) % self.size]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()