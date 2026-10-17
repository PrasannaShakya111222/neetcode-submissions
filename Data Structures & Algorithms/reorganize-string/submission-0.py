class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        # If any character appears too frequently, impossible
        if max(freq.values()) > (len(s) + 1) // 2:
            return ""
        # Max heap using negative frequencies
        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)
        result = []
        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)
            # Restore previously used character if it has remaining copies
            if 'prev' in locals() and prev[0] < 0:
                heapq.heappush(heap, prev)
            # Store current character for next iteration
            prev = (count + 1, char)
        return ''.join(result)