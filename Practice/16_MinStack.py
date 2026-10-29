class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        # Current min is min(val, previous min) or val if first element
        current_min = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(current_min)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]