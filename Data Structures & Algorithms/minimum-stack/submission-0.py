class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            current_min=min(val,self.minStack[-1])
            self.minStack.append(current_min)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minStack[-1]