class MinStack:

    def __init__(self):
        self.my_min_stack = []
        
    def push(self, val: int) -> None:
        cur_min = self.getMin()
        if cur_min == None or x < cur_min:
            cur_min = x
        self.my_min_stack.append((x, cur_min))

    def pop(self) -> None:
        self.my_min_stack.pop()
    def top(self) -> int:
        return self.my_min_stack[-1][0]

    def getMin(self) -> int:
        if len(self.my_min_stack) == 0:
            return None
        else:
            return self.my_min_stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()