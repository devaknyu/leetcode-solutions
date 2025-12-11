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
