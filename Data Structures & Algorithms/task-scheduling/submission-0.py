class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = sum(
            1 for count in freq.values()
            if count == max_freq)
        intervals = (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), intervals)