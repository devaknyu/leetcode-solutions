from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create pairs of (position, speed) and sort by position descending
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        # Process cars from closest to target to farthest
        for p, s in sorted(pair)[::-1]:
            # Time to reach target
            time = (target - p) / s
            stack.append(time)
            
            # If current car catches up to car in front (time <= previous time)
            # They become same fleet, so pop the faster car from stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]),  # → 3
        (10, [3], [3]),                           # → 1
        (100, [0, 2, 4], [4, 2, 1]),              # → 1
    ]
    
    for target, position, speed in test_cases:
        print(f"Target: {target}, Position: {position}, Speed: {speed}")
        result = sol.carFleet(target, position, speed)
        print(f"Number of fleets: {result}\n")