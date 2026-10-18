class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0] * 1001
        # Record passenger pickups & drop-offs
        for num, start, end in trips:
            passengers[start] += num
            passengers[end] -= num
        # Track passengers currently in car
        current = 0
        for change in passengers:
            current += change
            if current > capacity:
                return False
        return True