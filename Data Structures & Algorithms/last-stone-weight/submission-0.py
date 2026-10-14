class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Convert to max heap using -ve weights
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = -heapq.heappop(stones)  # Heaviest
            y = -heapq.heappop(stones)  # 2nd heaviest
            if x != y:
                heapq.heappush(stones, -(x - y))
        return -stones[0] if stones else 0