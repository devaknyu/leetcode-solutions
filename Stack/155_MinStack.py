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
      
# Example usage
if __name__ == "__main__":
    minStack = MinStack()
    
    operations = [
        ("push", -2),
        ("push", 0),
        ("push", -3),
        ("getMin", None),
        ("pop", None),
        ("top", None),
        ("getMin", None),
    ]
    
    for operation, value in operations:
        if operation == "push":
            minStack.push(value)
            print(f"push({value})")
        elif operation == "pop":
            minStack.pop()
            print("pop()")
        elif operation == "top":
            result = minStack.top()
            print(f"top() = {result}")
        elif operation == "getMin":
            result = minStack.getMin()
            print(f"getMin() = {result}")
    
    print(f"\nFinal stack: {minStack.stack}")
    print(f"Final min stack: {minStack.minstack}")