class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        
    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))

        popped = self.queue1.pop(0)

        while self.queue2:
            self.queue1.append(self.queue2.pop(0))

        return popped

    def top(self) -> int:
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))
        
        popping = self.queue1.pop(0)

        self.queue2.append(popping)

        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        
        return popping

    def empty(self) -> bool:
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()