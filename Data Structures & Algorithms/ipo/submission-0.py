class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Sort projects by required capital
        projects = sorted(zip(capital, profits))
        max_heap = []
        i = 0
        n = len(projects)
        for _ in range(k):
            # Add all projects currently affordable
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            # No available project remains
            if not max_heap:
                break
            # Select available project with max profit
            w += -heapq.heappop(max_heap)
        return w