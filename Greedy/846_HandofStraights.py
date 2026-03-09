"""
LeetCode 846: Hand of Straights
https://leetcode.com/problems/hand-of-straights/

Problem Description:
- You are given an array `hand` representing cards.
- Each card has an integer value.
- You must rearrange the cards into groups where:
    1) Each group has size `groupSize`
    2) Cards in each group are consecutive numbers

Goal:
- Return **True** if the cards can be rearranged into valid groups.
- Otherwise return **False**.

Examples:
hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
→ True

Explanation:
We can rearrange into groups:
[1,2,3], [2,3,4], [6,7,8]

hand = [1,2,3,4,5], groupSize = 4
→ False

Explanation:
We cannot form groups of 4 consecutive cards.

hand = [1,2,3,4], groupSize = 2
→ True

Possible grouping:
[1,2], [3,4]

Approach (Greedy + Min Heap):

Key Idea:
- Always start forming groups from the **smallest available card**.
- If we start with the smallest number `x`, we must also have:
      x+1, x+2, ..., x+groupSize-1

Data Structures:
- `count` → dictionary counting occurrences of each card
- `minH` → min heap of card values to always get the smallest card

Step-by-step logic:

1) First check:
      len(hand) % groupSize == 0
   If not, grouping is impossible.

2) Count occurrences of each card.

3) Push all unique card values into a **min heap**.

4) While the heap is not empty:

   Let `first` be the smallest card.

5) Try to build a group:
      first, first+1, ..., first+groupSize-1

6) For each number `i` in this range:
   - If `i` is not in `count` → return False
   - Decrease its count.

7) If a card's count becomes zero:
   - It must be the **top of the heap**
   - Pop it from the heap.

8) Continue until all cards are used.

Example:
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3

Counts:
1:1
2:2
3:2
4:1
6:1
7:1
8:1

Heap → [1,2,3,4,6,7,8]

Process:

Start at 1:
[1,2,3]

Start at 2:
[2,3,4]

Start at 6:
[6,7,8]

All groups formed → True.

Example 2:
hand = [1,2,3,4,5], groupSize = 4

Need groups of 4 but have 5 cards → impossible → False.

Time Complexity: O(n log n)
- Heap operations for unique card values.

Space Complexity: O(n)
- Hash map and heap store card values.
"""

from typing import List
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False

                count[i] -= 1

                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)

        return True

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))  # Expected: True
    print(sol.isNStraightHand([1,2,3,4,5], 4))          # Expected: False
    print(sol.isNStraightHand([1,2,3,4], 2))            # Expected: True