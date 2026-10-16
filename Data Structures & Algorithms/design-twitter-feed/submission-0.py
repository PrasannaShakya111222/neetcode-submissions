from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        heap = []
        for uid in users:
            tweets = self.tweets[uid]
            if tweets:
                idx = len(tweets) - 1
                time, tweetId = tweets[idx]
                heapq.heappush(
                    heap, (-time, tweetId, uid, idx)
                )
        result = []

        while heap and len(result) < 10:
            _, tweetId, uid, idx = heapq.heappop(heap)
            result.append(tweetId)
            idx -= 1
            if idx >= 0:
                time, nextTweetId = self.tweets[uid][idx]
                heapq.heappush(
                    heap, (-time, nextTweetId, uid, idx)
                )
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)