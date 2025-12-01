"""
LeetCode 155: Min Stack
https://leetcode.com/problems/min-stack/

Approach:
- Design a stack that supports push, pop, top, and retrieving the minimum element in constant time
- Use two stacks: one for all values, one for tracking current minimum
- Each element in minStack represents the minimum at that point in the main stack

Technique: Dual Stack with Minimum Tracking
1. Main stack: stores all pushed values
2. Min stack: stores current minimum value at each state
3. When pushing: min stack gets min(current value, previous min)
4. When popping: both stacks pop together to maintain synchronization
5. All operations O(1) time complexity

Time Complexity: O(1) for all operations
Space Complexity: O(n) for the two stacks
"""

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