class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []
        self.stack_top = -1


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minstack.append(val)
        self.minstack.sort(reverse=True)
        self.stack_top += 1


    def pop(self) -> None:
        if self.stack_top == -1:
            raise Exception("stack is empty")
        else:
            num = self.stack.pop()
            idx = self.minstack.index(num)
            self.minstack.pop(idx)
            self.stack_top -= 1


    def top(self) -> int:
        if self.stack_top == -1:
            raise Exception("stack is empty")
        else:
            return self.stack[self.stack_top]


    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# obj.getMin()
# obj.pop()
# obj.top()
# obj.getMin()