"""
LeetCode 355: Design Twitter
https://leetcode.com/problems/design-twitter/

Problem Description:
- Design a simplified Twitter system that supports:
  1. Posting tweets.
  2. Following and unfollowing users.
  3. Retrieving the 10 most recent tweets in a user's news feed.
- Each tweet is associated with a unique tweetId.
- Tweets must be returned in reverse chronological order.

Approach:
- Assign each tweet a timestamp using a global counter.
- Store tweets per user as (timestamp, tweetId).
- Maintain a follow map to track follow relationships.
- Use a Min Heap to efficiently merge tweets from multiple users
  when generating the news feed.

Key Observations:
- Only the 10 most recent tweets are needed.
- Each user’s tweets are already sorted by time.
- This problem reduces to merging multiple sorted lists.
- A heap allows efficient k-way merge.

Technique: Heap + Hash Maps (K-Way Merge)
1. Use a counter to timestamp tweets.
2. Store each user's tweets in a list.
3. Track follow relationships using a set.
4. When generating the feed:
   - Add the most recent tweet of each followed user to a heap.
   - Pop the most recent tweet and push the next older tweet
     from the same user.
5. Stop once 10 tweets are collected.

Time Complexity:
- postTweet: O(1)
- follow / unfollow: O(1)
- getNewsFeed: O(F log F)
  where F is the number of followed users (including self)

Space Complexity:
- O(U + T)
  where U is the number of users and T is the number of tweets
"""


from typing import List
from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)   # userId -> list of (timestamp, tweetId)
        self.followMap = defaultdict(set)   # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1  # ensures newer tweets have higher priority

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # User follows themselves
        self.followMap[userId].add(userId)

        # Initialize heap with most recent tweet from each followee
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])

        heapq.heapify(minHeap)

        # Extract up to 10 most recent tweets
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            # Push next older tweet from same user
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

if __name__ == "__main__":
    twitter = Twitter()

    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))  # Expected: [5]

    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))  # Expected: [6, 5]

    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))  # Expected: [5]
