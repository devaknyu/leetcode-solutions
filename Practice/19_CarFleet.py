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