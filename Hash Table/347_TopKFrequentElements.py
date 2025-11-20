"""
LeetCode 347: Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Approach:
- Find k most frequent elements using bucket sort
- Count frequencies, then group numbers by frequency in buckets
- Extract top k from highest frequency buckets

Technique: Bucket Sort with Frequency Counting
1. Count frequency of each number using hash map
2. Create buckets where index represents frequency
3. Place numbers in buckets according to their frequency
4. Iterate buckets from highest to lowest frequency to get top k

Time Complexity: O(n) for counting + O(n) for bucket processing = O(n)
Space Complexity: O(n) for frequency map and buckets
"""
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        
        # Count frequencies
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # Group numbers by frequency
        for num, freq_count in count.items():
            freq[freq_count].append(num)
        
        res = []
        # Extract top k from highest frequency
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([1,1,1,2,2,3], 2),     # → [1,2]
        ([1], 1),                # → [1]
        ([4,1,-1,2,-1,2,3], 2), # → [-1,2]
    ]
    
    for nums, k in test_cases:
        print(f"nums={nums}, k={k} → {sol.topKFrequent(nums, k)}")