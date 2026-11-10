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