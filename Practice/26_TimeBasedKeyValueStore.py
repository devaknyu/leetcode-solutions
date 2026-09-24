"""
LeetCode 981: Time Based Key-Value Store
https://leetcode.com/problems/time-based-key-value-store/

Approach:
- Design time-based key-value store supporting set and get operations
- set(key, value, timestamp): store value with timestamp
- get(key, timestamp): get most recent value for key with timestamp <= given timestamp
- If no such timestamp, return empty string

Technique: Hash Map with Binary Search
1. Dictionary where key maps to list of [value, timestamp] pairs
2. Timestamps are strictly increasing (as per problem constraints)
3. Use binary search to find appropriate timestamp in sorted list

Time Complexity:
- set: O(1) amortized (append to list)
- get: O(log n) for binary search
Space Complexity: O(n) for storing all key-value pairs
"""

class TimeMap:

    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        l, r = 0, len(values) - 1

        # Binary search for timestamp <= given timestamp
        while l <= r:
            m = (r + l) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]  # Update result with latest valid value
                l = m + 1          # Search right for potentially newer valid value
            else:
                r = m - 1          # Search left for older value
        return res

# Example usage
if __name__ == "__main__":
    timeMap = TimeMap()
    
    # Example operations
    operations = [
        ("set", "foo", "bar", 1),
        ("get", "foo", 1, "bar"),
        ("get", "foo", 3, "bar"),
        ("set", "foo", "bar2", 4),
        ("get", "foo", 4, "bar2"),
        ("get", "foo", 5, "bar2"),
    ]
    
    for op in operations:
        if op[0] == "set":
            timeMap.set(op[1], op[2], op[3])
            print(f"set({op[1]}, '{op[2]}', {op[3]})")
        elif op[0] == "get":
            result = timeMap.get(op[1], op[2])
            expected = op[3]
            status = "✓" if result == expected else "✗"
            print(f"get({op[1]}, {op[2]}) = '{result}' (Expected: '{expected}') {status}")
    
    print(f"\nInternal store structure: {timeMap.store}")